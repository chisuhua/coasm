#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ts=4 sw=4 sts=4 expandtab

import sys
from collections import OrderedDict
from string import Template

from antlr4 import *
from antlr4.InputStream import InputStream
from coasm import *
import yaml

from grammar.CoasmLexer import CoasmLexer
from grammar.CoasmParser import CoasmParser
from grammar.CoasmListener import CoasmListener

import struct

def get_type(tokenType):
    if tokenType == CoasmParser.K_FLOAT:
        return Symbol.TypeEnum.FLOAT
    elif tokenType == CoasmParser.K_INT:
        return Symbol.TypeEnum.INT
    elif tokenType == CoasmParser.K_VOID:
        return Symbol.TypeEnum.VOID
    elif tokenType == CoasmParser.LABEL:
        return Symbol.TypeEnum.LABEL
    else:
        return Symbol.TypeEnum.INVALID

def error(token, msg):
    print('[Error] line %d:%d %s' % (token.line, token.column, msg))

def info(token, msg):
    print('[Info] line %d:%d %s' % (token.line, token.column, msg))

class Var(VariableSymbol):
    def __init__(self, name, dtype: DataType, mspace: MemSpace):
        super().__init__(name)
        self.size = None
        self.data_type = dtype
        self.mem_space = mspace
        self.data = []

    def isPointer(self):
        return self.data_type.isPointer()

class KernelArg(ArgSymbol):
    def __init__(self, name):
        super().__init__(name)
        self.data_type = None
        self.mem_type = None

def getArrayElements(token):
    num_elements = 1
    if token is not None:
        text = token.getText()
        if text[0] == '-':
            error(token, "array length can't be negaive")
        num_elements = int(text)
    return num_elements

class Kernel(KernelSymbol):
    def __init__(self, name=''):
        super().__init__(name)
        self.args = {}
        self.mode = 0
        self.stack = 0
        self.alias_reg = {}
        self.id_stype = {}
        self.input_user_sreg_num = 0
        self.control = {}
        self.control['grid_dim_x_en'] = 0
        self.control['grid_dim_y_en'] = 0
        self.control['grid_dim_z_en'] = 0
        self.control['block_dim_en'] = 0
        self.control['block_idx_x_en'] = 0
        self.control['block_idx_y_en'] = 0
        self.control['block_idx_z_en'] = 0
        self.control['start_thread_idx_en'] = 0
        self.control['user_sreg_num'] = 0
        self.control['vload_in_order'] = 0
        self.control['vstore_in_order'] = 0
        self.control['sload_in_order'] = 0
        self.control['sstore_in_order'] = 0
        self.control['priority'] = 0
        self.mode = {}
        self.mode['fp_rndmode'] = 0
        self.mode['i_rndmode'] = 0
        self.mode['fp_denorm'] = 0
        self.mode['saturation'] = 0
        self.mode['exception_en'] = 0
        self.mode['relu'] = 0
        self.mode['trap_en'] = 0
        self.mode['debug_en'] = 0
        self.resource = {}
        self.resource['vreg_number'] = 0
        self.resource['sreg_number'] = 0
        self.resource['smem_size'] = 0
        self.resource['stack_size'] = 0

    def addArg(self, arg: KernelArg):
        self.args[arg.name] = arg

    def addAliasReg(self, alias_name, reg: Reg):
        self.alias_reg[alias_name] = reg

    def addAliasReg(self, alias_name, reg_type, reg_idx, size):
        if reg_type is Reg.RegType.Scalar:
            self.alias_reg[alias_name] = Reg("sreg[{}:{}]".format(reg_idx, reg_idx + size))
        elif reg_type is Reg.RegType.Vector:
            self.alias_reg[alias_name] = Reg("vreg[{}:{}]".format(reg_idx, reg_idx + size))

    def getArgs(self, arg: KernelArg):
        return self.args

    def updateArgs(self):
        sreg_num = 6
        for arg_name, arg in self.args.items():
            if arg.kind in [ArgSymbol.Kind.SREG_VALUE, ArgSymbol.Kind.SREG_PTR]:
                arg_sreg_num = arg.offset + arg.size
                sreg_num = arg_sreg_num
        input_user_sreg_num = self.control["user_sreg_num"]
        if input_user_sreg_num != 0:
            if input_user_sreg_num != sreg_num:
                printf("[Warn] kernel {} set user_sreg_num to {}", self.cur_kernel.name, input_user_sreg_num)
        else:
            self.control["user_sreg_num"] = sreg_num

    def addKernelOption(self, name, value):
        if name.find("workitem_id") > 0:
            name = "start_thread_idx_en"
            self.addControl(name, value)
        # FIXME
        elif name == "block_dim_x_en" or name == "block_dim_y_en" or name == "block_dim_z_en":
            name = "block_dim_en"
            self.addControl(name, value)
        elif name.find("next_free_vgpr") > 0:
            if (value >= 0 and value <= 256):
                print("[Error] kernel control vreg_num value is not valid")
            name = "user_vreg"
            self.addResource(name, value)
        elif name.find("next_free_sgpr") > 0:
            if (value >= 0 and value <= 256):
                print("[Error] kernel control sreg_num value is not valid")
            name = "user_sreg"
            self.addResource(name, value)
        elif name.find("group_segment_fixed_size") > 0:
            if (value >= 0 and value <= 4096):
                print("[Error] kernel control smem_size value is not valid")
            name = "smem_size"
            self.addResource(name, value)
        elif name.find("float_round_mode") > 0:
            if not (value >= 0 and value <= 4):
                print("[Error] kernel control fp_rndmode value is not valid")
            self.addMode(name, value)
        elif name.find("float_denorm") > 0:
            if not (value >= 0 and value <= 3):
                print("[Error] kernel control fp_denorm value is not valid")
            self.addMode(name, value)
        elif name == "saturation" and not (value >= 0 and value <= 7):
            print("[Error] kernel control saturation value is not valid")
            self.addMode(name, value)
        elif name.find("excepion") > 0:
            if not (value >= 0 and value <= 256):
                print("[Error] kernel control excepion_en value is not valid")
            self.addMode(name, value)


    def addControl(self, name, value):
        if name not in self.control:
            print("[Error] invalide kernel option " + name)
        self.control[name] = value
        if name == "user_sreg_num" and not (value >= 0 and value <= 63):
            print("[Error] kernel control sreg_num value is not valid")
        elif name == "priority" and not (value >= 0 and value <= 3):
            print("[Error] kernel control priority value is not valid")

    def addResource(self, name, value):
        if name not in self.resource:
            print("[Error] invalide kernel option for resource " + name)
        self.resource[name] = value

    def addMode(self, name, value):
        if name not in self.mode:
            print("[Error] invalide kernel option for mode " + name)
        self.mode[name] = value

class Function(FunctionSymbol):
    def __init__(self, name='', scope=None):
        super().__init__(name, Symbol.TypeEnum.FUNC, scope)
        #self.graph = Graph()
        self.name = name
        self.labels = {}
        self.instrs = OrderedDict()
        self.visible = True

    def addLabel(self, label: LabelSymbol):
        self.labels[label.name] = label

    def updateLabel(self, label: LabelSymbol, instr: Instr):
        self.labels[label.name].addInstr(instr)

    def addInstr(self, instr: Instr):
        self.instrs[instr] = []

    def setVisible(self, flag):
        self.visible = flag

def parseNumber(token, dtype = DataType("i32")):
    valid = False
    num = None
    token_str = CoasmParser.symbolicNames[token.type]
    if token_str == "DIGIT":
        num_string = token.text
        if dtype.isInt():
            num = int(num_string)
            valid = True
        elif dtype.isFloat():
            num = struct.unpack('!f', bytes.fromhex(num_string))[0]
            valid = True
        else:
            num = int(num_string)
            valid = True
    elif token_str == "FP_NUMBER":
        num_string = token.text
        num = float(num_string)
        valid = True
    elif token_str == "HEX_NUMBER":
        num_string = token.text
        num = int(num_string, 16)
        valid = True
    return [num, valid]

class DefPhase(CoasmListener):
    def __init__(self):
        self.globals = None
        self.currentScope = None
        self.scopes = {}
        self.id_stype = {}
        self.kernels = {}
        self.functions = {}
        self.variables = {}
        self.cur_function = None
        #self.cur_function = Function("default", self.currentScope)
        #self.functions["default"] = self.cur_function
        self.cur_section = None
        self.cur_kernel = None
        self.cur_label = []
        self.cur_var = None
        self.cur_instr = None
        self.memsize = {}
        self.memsize["global"] = 0
        self.memsize["shared"] = 0
        self.data = []
        self.unresolved_instr = {}

    def enterProg(self, ctx):
        self.globals = GlobalScope(None)
        self.currentScope = self.globals

    def exitProg(self, ctx):
        self.globals = GlobalScope(None)
        info(ctx.start, "Exit Prog")

    def enterLabel(self, ctx):
        label_id = ctx.ident().getText()
        info(ctx.start, "Find label {}".format(label_id))
        if label_id in self.id_stype:
            stype = self.id_stype[label_id]
            if stype is Symbol.TypeEnum.INVALID:
                error(cxt.ident().getSymbol(), "no such variable :" + name)
        self.id_stype[label_id] = Symbol.TypeEnum.LABEL
        label = LabelSymbol(label_id)
        self.cur_label.append(label)
        if label_id in self.functions:
            self.cur_function = self.functions[label_id]
        else:
            pass
        self.cur_function.addLabel(label)

    def enterIdent(self, ctx):
        ident = ctx.getText()
        if self.cur_instr is not None:
            if ident in self.id_stype:
                stype = self.id_stype[ident]
                if stype is Symbol.TypeEnum.REG:
                    # ODO
                    self.cur_instr.addReg(reg_alias[ident])
                else:
                    self.cur_instr.addOperand(ident)
            else:
                self.id_stype[ident] = None

    def enterKernel_directive(self, ctx:CoasmParser.Kernel_directiveContext):
        info(ctx.start, "Kernel directive")
        if ctx.START_KERNEL() is not None:
            self.cur_section = ctx.START_KERNEL().getText()
            name = ctx.ident().getText()
            self.cur_kernel = Kernel(name)
            self.kernels[name] = self.cur_kernel
            if name not in self.functions:
                self.functions[name] = Function(name, self.currentScope)
            else:
                self.functions[name].setVisible(True)
            self.memsize['global'] = 0
        #elif ctx.KERNEL_ARG() is not None:
        #    self.cur_section = ctx.KERNEL_ARG().getText()
        #elif ctx.KERNEL_INFO() is not None:
        #    self.cur_section = ctx.KERNEL_INFO().getText()
        elif ctx.END_KERNEL() is not None:
            self.cur_section = ctx.END_KERNEL().getText()
            self.memsize['global'] = 0

            kname = self.cur_kernel.name
            if self.cur_kernel is not None:
                self.cur_kernel.updateArgs()
                offset = self.cur_kernel.control["user_sreg_num"]
                if "grid_dim_x_en" in self.cur_kernel.control.keys():
                    self.cur_kernel.addAliasReg("gridDim.x", Reg.RegType.Scalar, offset, 1)
                    self.id_stype["gridDim.x@"+kname] = Symbol.TypeEnum.REG
                    offset += 1
                if "grid_dim_y_en" in self.cur_kernel.control.keys():
                    self.cur_kernel.addAliasReg("gridDim.y", Reg.RegType.Scalar, offset, 1)
                    self.id_stype["gridDim.y@"+kname] = Symbol.TypeEnum.REG
                    offset += 1
                if "grid_dim_z_en" in self.cur_kernel.control.keys():
                    self.cur_kernel.addAliasReg("gridDim.z", Reg.RegType.Scalar, offset, 1)
                    self.id_stype["gridDim.z@"+kname] = Symbol.TypeEnum.REG
                    offset += 1
                    offset = (offset + 1) & (~1)
                if "block_dim_en" in self.cur_kernel.control.keys():
                    self.cur_kernel.addAliasReg("blockDim", Reg.RegType.Scalar, offset, 1)
                    self.id_stype["blockDim@"+kname] = Symbol.TypeEnum.REG
                    offset += 1
                if "start_thread_idx_en" in self.cur_kernel.control.keys():
                    self.cur_kernel.addAliasReg("threadId", Reg.RegType.Scalar, offset, 1)
                    self.id_stype["threadId@"+kname] = Symbol.TypeEnum.REG
                    offset += 1
                if "block_idx_x_en" in self.cur_kernel.control.keys():
                    self.cur_kernel.addAliasReg("threadblockId.x", Reg.RegType.Scalar, offset, 1)
                    self.id_stype["threadblockId.x@"+kname] = Symbol.TypeEnum.REG
                    offset += 1
                if "block_idx_y_en" in self.cur_kernel.control.keys():
                    self.cur_kernel.addAliasReg("threadblockId.y", Reg.RegType.Scalar, offset, 1)
                    self.id_stype["threadblockId.y@"+kname] = Symbol.TypeEnum.REG
                    offset += 1
                if "block_idx_z_en" in self.cur_kernel.control.keys():
                    self.cur_kernel.addAliasReg("threadblockId.z", Reg.RegType.Scalar, offset, 1)
                    self.id_stype["threadblockId.z@"+kname] = Symbol.TypeEnum.REG
                    offset += 1
            else:
                error(ctx.END_KERNEL(), "invalid kernel directive\n")
            self.cur_kernel = None

    def enterKernel_option_item(self, ctx:CoasmParser.Kernel_option_itemContext):
        info(ctx.start, "Kernel Option item")
        if self.cur_kernel is None:
            error(ctx.getText(), "cur kernel is None")
        option_key = ""
        if ctx.KERNEL_OPTION_KEY() is not None:
            option_key = ctx.KERNEL_OPTION_KEY().getText()
            #key = option_key.split(".kernel_control.")[1]
            key = option_key.replace(".kernel_control.", "")
            self.cur_kernel.addKernelOption(key, int(ctx.DIGIT().getText()))

    def enterDecl_directive(self, ctx:CoasmParser.Decl_directiveContext):
        info(ctx.start, "enter type Decl")
        if ctx.DECL_FUNC() is not None:
            func_id = ctx.ident().getText()
            if func_id not in self.functions:
                self.functions[func_id] = Function(func_id, self.currentScope)
        self.cur_function = None
        self.cur_label = []


    def enterInst_directive(self, ctx:CoasmParser.Inst_directiveContext):
        assert(self.cur_kernel is not None)
        #assert(self.cur_section == ".text")
        self.cur_instr = Instr()
        start = ctx.start.start
        stop = ctx.stop.stop
        self.cur_instr.str_instr = input_stream.getText(start, stop)

        if ctx.HEX_NUMBER() is not None:
            hex_inst = int(ctx.HEX_NUMBER().getText(), 16)
            #self.cur_instr.setEncodedInst(hex_inst)
            #self.cur_instr.pos = self.instrs.length()
            pass

    def enterAlign_directive(self, ctx:CoasmParser.Align_directiveContext):
        pass


    def enterReg_directive(self, ctx:CoasmParser.Reg_directiveContext):
        if self.cur_section != ".kernel_arg" or self.cur_kernel is None:
            error(ctx.start, "ERROR: must in .kernel_arg")
        if ctx.register_().sreg() is None:
            error(ctx.start, "ERROR: must use sreg as kernel arg")
        ident = ctx.ident().getText()
        reg_name = ident + "@" + self.cur_kernel.name;
        if ident in self.id_stype:
            error(ctx.ident(), "ERROR, dupliatate name" + ident)

        if reg_name in self.id_stype:
            if self.id_stype[reg_name] != Symbol.TypeEnum.INVALID:
                error(ctx.ident(), "ERROR, duplicate name" + reg_name)
        dtype = DataType(ctx.DATA_TYPE().getText())
        num_elements = 1
        if ctx.DIGIT() is not None:
            text = ctx.DIGIT().getText()
            if text[0] == '-':
                error(ctx.DIGIT(), "ERROR: array length can't be negative")
            num_elements = int(text);
        if (dtype.getSize() % 4) > 0:
            num_elements *= dtype.getSize()/4 + 1
        else:
            num_elements *= dtype.getSize()/4

        self.id_stype[reg_name] = Symbol.TypeEnum.REG
        reg = Reg(ctx.register_().getText())
        self.cur_kernel.addAliasReg(reg_name, reg)
        num_regs = reg.end_idx - reg.idx + 1

        if num_regs != num_elements:
            error(ctx.register_(), "ERROR: number of register unmatched")

        arg = KernelArg()
        arg.offset = reg.idx
        arg.size = num_regs
        if dtype.isPointer():
            arg.kind = ArgSymbol.Kind.SREG_PTR
        else:
            arg.kind = ArgSymbol.Kind.SREG_VALUE
        arg.data_type = dtype

        if ident.find(".") :
            # TODO
            pass
        self.cur_kernel.addArg(arg)

    def enterMem_directive(self, ctx:CoasmParser.Mem_directiveContext):
        ident = ctx.ident().getText()
        if ident in self.id_stype and (self.id_stype[ident] is not Symbol.TypeEnum.INVALID):
            error(ctx.ident(), "ERROR: dumplcate name" + ident)
        if self.cur_kernel is not None:
            ident = ident + "@" + self.cur_kernel.name
        self.id_stype[ident] = Symbol.TypeEnum.VAR

        mspace = MemSpace(ctx.MEM_SPACE().getText())
        if mspace.kind == MemSpace.KindEnum.INVALID:
            error(ctx.start, "ERROR: unknow memory space" + ident)

        dtype = DataType(ctx.DATA_TYPE().getText())
        self.cur_var = Var(ident, dtype, mspace)
        num_elements = getArrayElements(ctx.DIGIT())
        num_inits = 0
        if ctx.data_expr_list() is not None:
            num_inits = len(ctx.data_expr_list().number())
        if num_elements < num_inits:
            error(ctx.data_expr_list(), "ERROR: number of initial is not match with array length")
        elif num_elements > num_inits:
            if self.cur_section == ".data":
                printf("INFO: global data without initial value will be filled with zero")
        element_size = dtype.getSize()
        self.cur_var.size = element_size * num_elements
        cur_mem_size =self.memsize[mspace.name];
        if (cur_mem_size + self.cur_var.size) > mspace.getMaxSize():
            error(ctx, "ERROR: execed memory space size")
        self.cur_var.offset = cur_mem_size

    def exitMem_directive(self, ctx:CoasmParser.Mem_directiveContext):
        cur_var = self.cur_var
        if self.cur_kernel is not None:
            if self.cur_section != ".kernel_arg":
                error(ctx.ident(), "ERROR: should be defined in .kernel_arg")
            ident = ctx.ident().getText()
            arg = KernelArg(ident)
            arg.offset = cur_var.offset
            arg.size = cur_var.size
            if cur_var.name.startswith("."):
                error(ctx.ident(), "ERROR: hidden kernel arg at global mem space is not suppoted")
            if cur_var.isPointer():
                arg.kind = ArgSymbol.Kind.GLOBAL_PTR
                arg.data_type = cur_var.data_type
            else:
                arg.kind = ArgSymbol.Kind.GLOBAL_VALUE
                arg.data_type = cur_var.data_type
            self.cur_kernel.addArg(arg)
        self.variables[cur_var.name] = cur_var
        self.memsize[cur_var.mem_space.name] = cur_var.offset + cur_var.size;
    def enterData_offset(self, ctx:CoasmParser.Data_offsetContext):
        cur_var = self.cur_var
        user_offset = 0
        if ctx.DIGIT() is not None:
            digit = ctx.DIGIT().getText()
            if digit[0] == '-':
                error(ctx.DIGIT(), "ERROR: offset can't be negative")
            user_offset = int(digit)
        elif ctx.HEX_NUMBER() is not None:
            digit = ctx.HEX_NUMBER().getText()
            user_offset = int(digit, 16)
        if cur_var.offset > user_offset:
            error(ctx, "ERROR: cant allocate {} at {} before current offset {}".format(cur_var.name, user_offset, cur_var.offset))
        cur_var.offset = user_offset

    def exitData_offset(self, ctx:CoasmParser.Data_offsetContext):
        cur_var = self.cur_var
        if (cur_var.offset + cur_var.size) > MemSpace.getMaxSize(cur_var.mem_space):
            error(ctx, "ERROR: cant allocate {} since memory full".format(cur_var.name))


    def enterNumber(self, ctx:CoasmParser.NumberContext):
        # parse number for Mem_directive
        if self.cur_var is not None:
            num, valid = parseNumber(ctx.start, self.cur_var.data_type)
            if valid is False:
                error(ctx.start, "ERROR: parse number failed")
            self.cur_var.data = num
        # parse number for Instr
        elif self.cur_instr is not None:
            num, valid = parseNumber(ctx.start, DataType('i32'))
            self.cur_instr.addOperand(num)

    def exitSreg(self, ctx:CoasmParser.SregContext):
        reg = Reg(ctx.getText())
        self.cur_instr.addReg(reg)
        pass
    def exitVreg(self, ctx:CoasmParser.VregContext):
        reg = Reg(ctx.getText())
        self.cur_instr.addReg(reg)
        pass

    def enterSize_directive(self, ctx:CoasmParser.Size_directiveContext):
        pass

    def enterSection_directive(self, ctx:CoasmParser.Section_directiveContext):
        self.cur_section = ctx.section_name().getText().lower()
        if self.cur_section == ".section.rodata" or self.cur_section == ".section.bss" or self.cur_section == ".section.data":
            self.cur_section = ".data"

    def enterLink_directive(self, ctx:CoasmParser.Link_directiveContext):
        if ctx.VISIBLE() is not None:
            ident = ctx.ident().getText()
            if ident in self.functions:
                self.functions[ident].setVisible(True)

    def parseInstrOp(self, op_str):
        op_flag = {}
        if op_str.find("E32") > 0:
            op_flag["E32"] = 1
            op_str = op_str.replace("_E32", "")
        if op_str.find("MEM") > 0 or op_str.find("TSM") > 0:
            if op_str.find("_RTN") != -1:
                op_flag["RTN"] = 1
                op_str = op_str.replace("_RTN", "")
            if op_str.find("_RDC"):
                op_flag["RDC"] = 1
                op_str = op_str.replace("_RDC", "")
            if op_str.find("_KP") != -1:
                if op_str.find("TSM") and not op_str.find("VMEM"):
                    error(ctx, "TSM operation must have caceh policy")
                pos = op_str.index("_KP") + 3
                if op_str[pos] == '1':
                    op_flag["KP0"] = 1
                elif op_str[pos] == '2':
                    op_flag["KP0"] = 2
                elif op_str[pos] == '2':
                    if op.find("_ST"):
                        error(etx, "ERROR: store should not have KP2 cache policy")
                    op_flag["KP1"] = 1
                elif op_str[pos] == '3':
                    op_flag["KP0"] = 1
                    op_flag["KP1"] = 1
                elif op_str[pos] == '4':
                    op_flag["KP2"] = 1
                elif op_str[pos] == '5':
                    op_flag["KP0"] = 1
                    op_flag["KP2"] = 1
                op_str = op_str.replace("_KP" + op_str[pos], "")
            if op_str.find("_GA"):
                op_flag["GA"] = 1
                op_str = op_str.replace("_GA", "")
        #if op_str.find("MEM") || op_str.find("TSM"):
        return op_str, op_flag

    def enterInstruction(self, ctx:CoasmParser.Inst_directiveContext):
        assert(self.cur_kernel is None)
        #assert(self.cur_section == ".text")
        token = ctx.start
        instr_fmt = CoasmParser.symbolicNames[token.type]
        op_str = token.text.upper().replace('.', '_')
        instr_op, instr_flag = self.parseInstrOp(op_str)
        info(token, "enter Instrucion" + instr_fmt + ", op " + instr_op)
        exec("self.cur_instr = Instr{}(instr_op)".format(instr_fmt))
        cur_instr = self.cur_instr
        for k,v in instr_flag.items():
            cur_instr.setFlag(k)

    def exitInstruction(self, ctx:CoasmParser.InstructionContext):
        if self.cur_instr is None:
            error(ctx, "ERROR: invalid intruction")
        if self.cur_function is not None:
            print("instr: Line={}, opcode={}".format(self.cur_instr.name, self.cur_instr))
            #self.instrs.append(self.cur_instr)
            if len(self.cur_label) > 0:
                for label in self.cur_label:
                    self.cur_function.updateLabel(label, self.cur_instr)
                self.cur_label = []
            self.cur_function.addInstr(self.cur_instr);
            self.cur_instr.name = self.cur_function.name
            self.cur_instr = None

    def exitAlu_expr_list(self, ctx:CoasmParser.Alu_expr_listContext):
        cur_instr = self.cur_instr
        if cur_instr is None:
           error(ctx, "ERROR: cur_instr is None")
        dtype = cur_instr.getInputDataType()
        info(ctx.start, "exitAlu_expr_list")

        if len(ctx.alu_expr()) > 0:
            if len(ctx.alu_expr()) == 1:
                str_expr = ctx.getText()
                str_expr_k = ""
                if self.cur_function is not None:
                    str_expr_k = str_expr + "@" + self.cur_function.name
                if (str_expr not in self.id_stype or self.id_stype[str_expr] != Symbol.TypeEnum.REG) and \
                        (str_expr_k not in self.id_stype or self.id_stype[str_expr_k] != Symbol.TypeEnum.REG):
                    self.unresolved_instr[cur_instr] = ctx
                    cur_instr.setImm(0)
            else:
                error(ctx, "Unsupported expr list")
        elif ctx.register_() is not None:
            pass
        else:
            num, valid = parseNumber(ctx.start)
            cur_instr.addOperand(num)

    def exitLop_imm(self, ctx:CoasmParser.Lop_immContext):
        num, valid = parseNumber(ctx.start)
        cur_instr.setLopImm(num);


#ODO setup global data array here
class RefPhase(CoasmListener):
    def __init__(self, glbs, scopes, id_stype, kernels, functions, variables, memsize, unresolved_instr):
        self.globals = glbs
        self.scopes = scopes
        self.id_stype = id_stype
        self.kernels = kernels
        self.functions = functions
        self.variables = variables
        self.memsize = memsize
        self.unresolved_instr = unresolved_instr
        self.currentScope = None

    def enterProg(self, ctx):
        self.currentScope = self.globals

    def exitProg(self, ctx:CoasmParser.ProgContext):
        print(self.globals)
        info(ctx.start, "Exit Prog")
        for func_name, func in self.functions.items():
            print("[Scan function] {}".format(func_name))
            for instr in func.instrs:
                print("[Scan instr] {} {}".format(instr.name, instr))
                reg = None
                for operand in instr.operands:
                    if isinstance(operand, Reg):
                        reg = operand
                    elif not isinstance(operand, int):
                        if operand in self.id_stype:
                            stype = self.id_stype[operand]
                            if stype is Symbol.TypeEnum.REG:
                                pass
                            elif stype is Symbol.TypeEnum.VAR:
                                pass
                            elif stype is Symbol.TypeEnum.LABEL:
                                pass
                            elif operand.find("@pcrel32") or operand.find("@rel32"):
                                pass
                            else:
                                error(ctx, "ERROR: unresolved id" + operand)
                        else:
                            error(ctx, "ERROR: unresolved id" + operand)
            # instr.verify
            for instr in func.instrs:
                pass
        # update kernel resource
        for kernel_name, kernel in self.kernels.items():
            if kernel_name not in self.functions:
                print("ERROR: kernel " + kernel_name + " is not in funtions")
            func = self.functions[kernel_name]
            print("process kernel_name {}".format(kernel_name))
            sreg_usage = {}
            vreg_usage = {}
            max_sreg = -1
            max_vreg = -1
            for instr in func.instrs:
                for reg in instr.regs:
                    print("process reg {}, reg.idx={}, reg.end_idx={}".format(reg, reg.idx, reg.end_idx))
                    for idx in range(reg.idx, reg.end_idx):
                        if reg.rtype is Reg.RegType.Scalar:
                            sreg_usage[idx] = True
                            if idx <= MAX_USER_SREG_NUM and idx > max_sreg:
                                max_sreg = idx
                        else:
                            vreg_usage[idx] = True
                            if idx <= MAX_VREG_NUM and idx > max_vreg:
                                max_vreg = idx
            input_sreg_num = kernel.resource["sreg_number"]
            sreg_num = max_sreg + 1 + 1   # add vcc
            sreg_num = (sreg_num + 7 ) / 8    # align to 8
            if kernel.mode["trap_en"]:
                sreg_num += 16
            if input_sreg_num == 0:
                kernel.resource["sreg_number"] = sreg_num
            elif input_sreg_num != sreg_num:
                print("WARN: kernel {} set sreg_number to {}, recommended value = {}".format(kernel_name, input_sreg_num, sreg_num))
            input_vreg_num = kernel.resource["vreg_number"]
            vreg_num = max_vreg + 1    # add vcc
            vreg_num = (vreg_num + 1) / 2
            if input_vreg_num == 0:
                kernel.resource["vreg_number"] = vreg_num
            elif input_vreg_num != vreg_num:
                print("WARN: kernel {} set vreg_number to {}, recommended value = {}".format(kernel_name, input_vreg_num, vreg_num))
            input_smem_size = kernel.resource["smem_size"]
            smem_size = (self.memsize["shared"] + 127) / 128
            if input_smem_size == 0:
                kernel.resource["smem_size"] = smem_size
            elif input_smem_size != smem_size:
                print("WARN: kernel {} set smem_size to {}, recommended value = {}".format(kernel_name, input_smem_size, smem_size))
            info(ctx.start, "Exit Prog End")
        for instr in self.unresolved_instr:
            print("instr {} is unresolved".format(self.unresolved_instr))

        with open("gen_def.h", 'w') as f:
            Instr.visitClass(VisitType.GEN_INSTR_FMT_FIELD, f);

        with open("gen_asm.c", 'w') as f:
            #Instr.visitSubClass("opcode_enum")
            f.write("""
#include <iostream>
#include <fstream>
#include <vector>
#include <stdint.h>
#include "gen_def.h"
using namespace std;
std::vector<uint32_t> code;

union Bytes {
    uint8_t bytes[8];
    uint32_t word[2];
""")
            Instr.visitClass(VisitType.GEN_INSTR_FMT_DEF, f);
            f.write("""
};

Bytes bytes;
int main() {
""")
            for func_name, func in self.functions.items():
                for instr in func.instrs:
                    instr.genInstrAsm(f)
            f.write("""
    ofstream outFile("_asm.hex", ios::out | ios::binary);
    for (uint32_t i ; i < code.size(); i++) {
        if (i % 8 == 0) printf("\\ndata:");
        printf("8%8x ", code[i]);
        outFile.write((char*)&code[i], sizeof(uint32_t));
    }
    printf("\\n");
    outFile.close();
    return 0;
}
""")


is_kernel_option = False;
is_kernel_meta = False;

if __name__ == '__main__':
    asm_input = []
    metas = []
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    for line in lines:
        if ".kernel " in line:
            is_kernel_option = True
        elif ".end_kernel"  in line:
            is_kernel_option = False
        elif "---"  in line:
            is_kernel_meta = True
        elif "..."  in line:
            is_kernel_meta = False
        if is_kernel_option == True and line.find(".kernel ") == -1:
            line = line.replace(".", ".kernel_option.")
        if is_kernel_meta == True:
            metas.append(line)
        else:
            asm_input.append(line)

    kernel_meta = yaml.load("".join(metas))
    print(kernel_meta)
    input_stream = InputStream("".join(asm_input))

    lexer = CoasmLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CoasmParser(token_stream)
    tree = parser.prog()

    lisp_tree_str = tree.toStringTree(recog=parser)
    print(lisp_tree_str)

    walker = ParseTreeWalker()

    # definition phase, collect data
    print('*** Scan Definitions ***')
    def_phase = DefPhase()
    walker.walk(def_phase, tree)

    # reference phase, check error
    print('*** Ref Phase ***')
    #ref_phase = RefPhase(def_phase.globals, def_phase.scopes)
    ref_phase = RefPhase(def_phase.globals, def_phase.scopes, \
            def_phase.id_stype, \
            def_phase.kernels,  \
            def_phase.functions, \
            def_phase.variables, \
            def_phase.memsize, \
            def_phase.unresolved_instr)
    walker.walk(ref_phase, tree)


