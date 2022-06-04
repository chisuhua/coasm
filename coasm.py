from enum import Enum
from collections import OrderedDict
from collections import namedtuple
from jinja2 import Template
from ctypes import *
import pdb

MAX_SREG_NUM = 255
MAX_RESERVED_SREG_NUM = 4
MAX_USER_SREG_NUM = 220
MAX_VREG_NUM = 512
MAX_DREG_NUM = 255
MAX_TCC_NUM = 32
SREG_TCC = 106

def utilReplace(str):
    str = str.replace('_', "'_'")
    str = str.replace('3', "'3'")
    str = str.replace('2', "'2'")
    str = str.replace('6', "'6'")
    str = str.replace('4', "'4'")
    str = str.replace('0', "'0'")
    str = str.replace('1', "'1'")
    str = str.replace('8', "'8'")
    return str



#SpecialRegAlias = {"vcc":SREG_VCC}

class Scope:
    def getScopeName(self):
        pass

    def getEnclosingScope(self):
        pass

    def define(self, sym):
        pass

    def resolve(self, name):         pass

class MemSpace:
    MaxGlobalSize = 1000
    MaxSharedSize = 1000
    class KindEnum(Enum):
        INVALID = 0
        GLOBAL = 1
        SHARED = 2
    def __init__(self, string):
        self.kind = MemSpace.KindEnum.INVALID
        if string.startswith("."):
            string = string[1:]
        if string == "global":
            self.kind = MemSpace.KindEnum.GLOBAL
            self.name = "global"
        elif string == "shared":
            self.kind = MemSpace.KindEnum.SHARED
            self.name = "shared"
        else:
            assert("dont't know the space {}".format(string))

    def getMaxSize(self):
        if self.name == "global":
            return MemSpace.MaxGlobalSize
        elif self.name == "shared":
            return MemSpace.MaxSharedSize


class DataType:
    class TypeEnum(Enum):
        DT_INT8   = 0
        DT_UINT8  = 1
        DT_INT16  = 2
        DT_UINT16 = 3
        DT_INT32  = 4
        DT_UINT32 = 5
        DT_FP16   = 6
        DT_BF16   = 7
        DT_TF32   = 8
        DT_FP32   = 9
        DT_B16    = 10
        DT_B32    = 11
        DT_I16x2  = 12
        DT_U16x2  = 13
        DT_B16x2  = 14
        DT_FP16x2 = 15
        DT_BF16x2 = 16
        DT_INT64  = 17
        DT_UINT64 = 18
        DT_B64    = 19
        DT_MAX    = 99
    class TypeKind(Enum):
        INT = 0
        FLOAT = 0

    Dtype = namedtuple('Dtype', ['dtype_enum', 'size', 'dtype_kind', 'signed'])
    dtype= {}
    dtype["i8"] = Dtype(TypeEnum.DT_INT8, 1, TypeKind.INT, True)
    dtype["u8"] = Dtype(TypeEnum.DT_UINT8, 1, TypeKind.INT, False)
    dtype["i16"] = Dtype(TypeEnum.DT_INT16, 2, TypeKind.INT, True)
    dtype["u16"] = Dtype(TypeEnum.DT_UINT16, 2, TypeKind.INT, False)
    dtype["i32"] = Dtype(TypeEnum.DT_INT32, 4, TypeKind.INT, True)
    dtype["u32"] = Dtype(TypeEnum.DT_UINT32, 4, TypeKind.INT, False)
    dtype["i64"] = Dtype(TypeEnum.DT_INT64, 8, TypeKind.INT, True)
    dtype["u64"] = Dtype(TypeEnum.DT_UINT64, 8, TypeKind.INT, False)
    dtype["f16"] = Dtype(TypeEnum.DT_FP16, 2, TypeKind.FLOAT, None)
    dtype["bf16"] = Dtype(TypeEnum.DT_BF16, 2, TypeKind.FLOAT, None)
    dtype["f32"] = Dtype(TypeEnum.DT_FP32, 4, TypeKind.FLOAT, None)
    dtype["tf32"] = Dtype(TypeEnum.DT_TF32, 4, TypeKind.FLOAT, None)
    dtype["b16"] = Dtype(TypeEnum.DT_B16, 2, TypeKind.INT, None)
    dtype["b32"] = Dtype(TypeEnum.DT_B32, 4, TypeKind.INT, None)
    dtype["b64"] = Dtype(TypeEnum.DT_B64, 8, TypeKind.INT, None)
    dtype["i16x2"] = Dtype(TypeEnum.DT_I16x2, 4, TypeKind.INT, True)
    dtype["u16x2"] = Dtype(TypeEnum.DT_U16x2, 4, TypeKind.INT, False)
    dtype["b16x2"] = Dtype(TypeEnum.DT_B16x2, 4, TypeKind.INT, None)
    dtype["fp16x2"] = Dtype(TypeEnum.DT_FP16x2, 4, TypeKind.FLOAT, None)
    dtype["bf16x2"] = Dtype(TypeEnum.DT_BF16x2, 4, TypeKind.FLOAT, None)
    dtype["ptr"] = Dtype(TypeEnum.DT_UINT64, 8, TypeKind.INT, None)
    def __init__(self, string):
        self.is_ptr = False
        self.data_type = None
        if string.endswith("*"):
            string = string[:-1]
            self.is_ptr = True
        if string.startswith("."):
            string = string[1:]
        if string in DataType.dtype:
            self.data_type = DataType.dtype[string]
        else:
            assert("Invalid Datatype " + string)

    def getSize(self):
        return self.data_type.size

    def isSignedInt(self):
        if self.data_type.dtype_kind is DataType.TypeKind.INT and self.data_type.signed is True:
            return True
        return False

    def isUnSignedInt(self):
        if self.data_type.dtype_kind is DataType.TypeKind.INT and self.data_type.signed is False:
            return True
        return False

    def isInt(self):
        if self.data_type.dtype_kind is DataType.TypeKind.INT:
            return True

    def isFloat(self):
        if self.data_type.dtype_kind is DataType.TypeKind.FLOAT:
            return True

    def isPointer(self):
          return self.is_ptr

class Symbol:
    class TypeEnum(Enum):
        INVALID   = 0
        LABEL = 1
        KERNEL = 2
        FUNC = 3
        VAR = 4
        REG = 5

    class RegEnum(Enum):
        REG_DST = 0
        REG_SRC0 = 1
        REG_SRC1 = 2
        REG_SRC2 = 3
        REG_SRC3 = 4

    def __init__(self, name='', stype=TypeEnum.INVALID):
        self.name = name
        self.type = stype
        self.scope = None

    def __str__(self):
        if self.type != Symbol.TypeEnum.INVALID:
            return '<'+self.name+':'+self.type.name+'>'
        else:
            return self.name


class BaseScope(Scope):
    def __init__(self, scope: Scope):
        self.enclosingScope = scope
        self.symbols = {}

    def resolve(self, name):
        s = self.symbols.get(name)
        if s is not None:
            return s
        if self.enclosingScope is not None:
            return self.enclosingScope.resolve(name)
        return None
    def define(self, sym: Symbol):
          self.symbols[sym.name] = sym

    def getEnclosingScope(self):
        return self.enclosingScope

    def __str__(self):
        buf = self.getScopeName() + ' : ' + list(self.symbols.keys()).__str__()
        return buf

class GlobalScope(BaseScope):
    def __init__(self, scope):
        super().__init__(scope)

    def getScopeName(self):
        return 'globals'


class LocalScope(BaseScope):
    def __init__(self, parent):
        super().__init__(parent)

    def getScopeName(self):
        return 'locals'


class FunctionSymbol(Symbol, Scope):
    def __init__(self, name='', stype=Symbol.TypeEnum.KERNEL, scope=None):
        super().__init__(name, stype)
        self.enclosingScope = scope
        self.arguments = {}

    def resolve(self, name):
        s = self.arguments.get(name)
        if s is not None:
            return s
        if self.enclosingScope is not None:
            return self.enclosingScope.resolve(name)
        return None

    def define(self, sym: Symbol):
        self.arguments[sym.name] = sym
        sym.scope = self

    def getEnclosingScope(self):
        return self.enclosingScope

    def getScopeName(self):
        return self.name

    def __str__(self):
        buf = "function "
        buf += super().__str__()
        buf += " : "
        for par in self.arguments.values():
            buf += par.__str__() + ';'
        return buf


class VariableSymbol(Symbol):
    class RelocType(Enum):
        Normal         = 0
        RelBranch      = 1
        SavePC         = 2
        PCRel32        = 3
        PCRel32Lo      = 4
        PCRel32Hi      = 5
        Rel32Lo        = 6
        Rel32Hi        = 7

    def __init__(self, name):
        super().__init__(name, Symbol.TypeEnum.VAR)
        func_name = ""

class Reg(VariableSymbol):
    class RegType(Enum):
        Scalar         = 0
        Vector         = 1
        Data           = 2
        #Param          = 3  # Param
        TCC            = 4  # thread condition code
        #BUILTIN_SREG   = 5  # builtin register
        #BUILTIN_VREG   = 6  # builtin register
    def __init__(self, reg_str, operand_type=None):
        self.operand_type = operand_type
        self.is_neg = False
        self.reg_name = None
        self.idx = None
        self.end_idx = None
        self.lie = None     # for Data register and lane id to reg_idx
        start_pos = 0
        print("INFO: reg str:" + reg_str)
        if len(reg_str) == 0:
            assert("Reg is null str")
        if reg_str == '':
            pdb.set_trace()
        if reg_str[0] == '-' or reg_str[0] == '!':
            self.is_neg = True
            start_pos = 1
        reg_str = reg_str[start_pos:]
        super().__init__(reg_str)
        #pdb.set_trace()
        #if reg_str.find("param_") >= 0:
        #    self.rtype = Reg.RegType.Param
        #elif reg_str.find("builtin_sreg") >= 0:
        #    self.rtype = Reg.RegType.BUILTIN_SREG
        #elif reg_str.find("builtin_vreg") >= 0:
        #    self.rtype = Reg.RegType.BUILTIN_VREG
        if reg_str[0] == "s":
            self.rtype = Reg.RegType.Scalar
        elif reg_str[0] == "v":
            self.rtype = Reg.RegType.Vector
        elif reg_str[0] == "d":
            self.rtype = Reg.RegType.Data
        elif reg_str[0] == "l":
            self.rtype = Reg.RegType.Data
            self.lie = True
        elif reg_str[0:3] == "tcc":
            self.rtype = Reg.RegType.TCC
        else:
            assert("invalid reg name")
        idx_pos = reg_str.find("[")
        if idx_pos > 0:
            colon_pos = reg_str.find(":")
            end_idx_pos = reg_str.find("]")
            self.reg_name = reg_str[0:idx_pos]
            self.idx = int(reg_str[idx_pos+1:colon_pos])
            self.end_idx = int(reg_str[colon_pos+1:end_idx_pos])
        elif self.rtype == Reg.RegType.Scalar or \
                self.rtype == Reg.RegType.Vector or \
                self.rtype == Reg.RegType.Data or self.rtype == Reg.RegType.TCC:
            # here we assume reg name is s|v|d or s|v|dreg
            # or like t0/tcc0
            if reg_str[1].isdigit():
                idx_pos = 1
            elif reg_str[3].isdigit():
                idx_pos = 3
            elif reg_str[4].isdigit():
                idx_pos = 4
            else:
                assert("Invalid Reg str")
            self.reg_name = reg_str[0:idx_pos]
            self.idx = int(reg_str[idx_pos:])
            self.end_idx = self.idx
        else:
            self.reg_name = reg_str
            self.idx = 0
        self.alias = None
        self.reloc_type = VariableSymbol.RelocType.Normal

    def __str__(self):
        if self.end_idx is not None and self.end_idx != self.idx:
            return "{}[{}:{}]".format( "s" if self.rtype is Reg.RegType.Scalar \
                                  else "v" if self.rtype is Reg.RegType.Vector \
                                  else "l" if self.rtype is Reg.RegType.Data and self.lie \
                                  else "tcc" if self.rtype is Reg.RegType.TCC \
                                  else "d",
                    self.idx, self.end_idx)
        else:
            return "{}{}".format( "s" if self.rtype is Reg.RegType.Scalar \
                             else "v" if self.rtype is Reg.RegType.Vector \
                             else "l" if self.rtype is Reg.RegType.Data and self.lie \
                             else "tcc" if self.rtype is Reg.RegType.TCC \
                             else "d",
                    self.idx)

class SpecialREG:
    class Kind(Enum):
        SREG_VCC = 0xdf
        SREG_TREG0  = 0xe0
        SREG_TREG15 = 0xef
        HWREG_EMSK  = 0xf0
        HWREG_SCC   = 0xf1
        HWREG_X0    = 0xf2
        HWREG_MODE  = 0xf3
        HWREG_STATUS = 0xf4
        HWREG_VCB   = 0xf5
        LTID        = 0xfe
        ISREG       = 0xff
        IVREG       = 0xff
        BUILTIN_THREAD = 0
        BUILTIN_BLOCK  = 1
        BUILTIN_KERNEL = 2
        
    #special_reg['m0'] = SpecialReg("RegisterM0", Reg('s124'))
    #special_reg['vcc'] = SpecialReg("RegisterVcc", Reg('s106'))
    #special_reg['vccz'] = SpecialReg("RegisterVcc", Reg('s251'))
    #special_reg['exec'] = SpecialReg("RegisterVcc", Reg('s126'))
    #special_reg['execz'] = SpecialReg("RegisterVcc", Reg('s252'))
    #special_reg['scc'] = SpecialReg("RegisterVcc", Reg('s253'))
    # the reg_size is 4B as unit
    BuiltinReg = namedtuple('BuiltinReg', ['name', 'is_builtin', 'kind', 'reg_size', 'ctrl_bit'])
    builtin_reg = []
    builtin_reg.append(BuiltinReg("param_global_base", True, Kind.BUILTIN_KERNEL, 2, 0))
    builtin_reg.append(BuiltinReg("grid_dim_x", True, Kind.BUILTIN_KERNEL, 1, 4))
    builtin_reg.append(BuiltinReg("grid_dim_y", True, Kind.BUILTIN_KERNEL, 1,5))
    builtin_reg.append(BuiltinReg("grid_dim_z", True, Kind.BUILTIN_KERNEL, 1,6))
    builtin_reg.append(BuiltinReg("block_dim_x", True, Kind.BUILTIN_KERNEL, 1,7))
    builtin_reg.append(BuiltinReg("block_dim_y", True, Kind.BUILTIN_KERNEL, 1,8))
    builtin_reg.append(BuiltinReg("block_dim_z", True, Kind.BUILTIN_KERNEL, 1,9))
    builtin_reg.append(BuiltinReg("block_idx_x", True, Kind.BUILTIN_BLOCK, 1,12))
    builtin_reg.append(BuiltinReg("block_idx_y", True, Kind.BUILTIN_BLOCK, 1,13))
    builtin_reg.append(BuiltinReg("block_idx_z", True, Kind.BUILTIN_BLOCK, 1,14))
    builtin_reg.append(BuiltinReg("thread_idx_x", True, Kind.BUILTIN_THREAD, 1,16))
    builtin_reg.append(BuiltinReg("thread_idx_y", True, Kind.BUILTIN_THREAD, 1,17))
    builtin_reg.append(BuiltinReg("thread_idx_z", True, Kind.BUILTIN_THREAD, 1,18))
    @classmethod
    def get_builtin_reg(cls, name):
        for reg in cls.builtin_reg:
            if reg.is_builtin and name == reg.name:
                return reg
        assert("can't find the builtin reg {} ".format(name))

class UnresolvedReg:
    class Kind(Enum):
        ci = 0
        co = 1
        param = 2
        pred = 3
        tcc = 4
        builtin = 5
    def __init__(self, operand_type, name):
        self.type = operand_type
        self.name = name
    @classmethod
    def get_kind(cls, operand_type):
        assert(isinstance(operand_type, str))
        if operand_type == "ci":
            return Kind.ci
        elif operand_type == "co":
            return Kind.co
        elif operand_type == "param":
            return Kind.param
        elif operand_type == "pred":
            return Kind.pred
        elif operand_type == "tcc":
            return Kind.tcc
        elif operand_type == "builtin":
            return Kind.builtin
        else:
            assert("unknown opernad type {}".format(operand_type))


class LabelSymbol(Symbol):
    def __init__(self, name):
        super().__init__(name, Symbol.TypeEnum.LABEL)
        self.instr = None

    def addInstr(self, instr):
        self.instr = instr

class KernelSymbol(Symbol):
    def __init__(self, name):
        super().__init__(name, Symbol.TypeEnum.KERNEL)

class ArgSymbol(Symbol):
    class Kind(Enum):
        GLOBAL_PTR      = 0
        GLOBAL_VALUE    = 1
        SREG_PTR        = 2
        SREG_VALUE      = 3
        HIDDEN_GM_BASE  = 4  # base ptr for global data
        HIDDEN_KM_BASE  = 5  # base ptr for kernel args in global memory
        HIDDEN_PM_BASE  = 6  # base ptr for stack
        HIDDEN_PM_SIZE  = 7  # stack size per thread in bytes
        INVALID_ARG_VALUE_KIND = 0xff

    def __init__(self, name):
        super().__init__(name)
        self.offset = 0
        self.size = 0
        self.kind = ArgSymbol.Kind.SREG_VALUE

#class InstrField:
#    class TypeEnum(Enum):
#        UINT = 0
#        INT = 1
#        STRUCT = 2
#        UNION = 3
#
#    def __init__(self, name="", type=TypeEnum.UINT):
#        self.name = name
#        self.msb = 0
#        self.lsb = 0
#        self.type =  TypeEnum.UINT
#        self.child = []

class VisitType(Enum):
    GRAMMAR_INSTR_FMT = 1
    GRAMMAR_INSTR_DEF = 2
    GET_INSTR_FMT_LIST = 3
    GEN_INSTR_FMT_FIELD = 4
    GEN_INSTR_OPCODE_DEF = 5
    GEN_INSTR_OP_ENUM_DEF = 6
    GEN_INSTR_DEF = 7

CommonEnc = namedtuple('CommonEnc', ['width', 'value'])
common_enc = {}
common_enc["ext1_enc"] = CommonEnc(4, 0x7)
common_enc["dsrc0_l"] = CommonEnc(2, 0x3)
common_enc["dsrc0_d"] = CommonEnc(2, 0x2)
common_enc["dsrc0_s"] = CommonEnc(2, 0x1)
common_enc["dsrc0_v"] = CommonEnc(2, 0x0)
common_enc["max_src0_32e"] = CommonEnc(6, 64)
common_enc["max_vsrc1_32e"] = CommonEnc(6, 64)
common_enc["max_vdst_32e"] = CommonEnc(6, 64)
common_enc["max_vdata_32e"] = CommonEnc(6, 64)
common_enc["max_vaddr_32e"] = CommonEnc(6, 64)
common_enc["max_vls_offset_32e"] = CommonEnc(7, 128)
common_enc["max_tcc_32e"] = CommonEnc(2, 3)
common_enc["max_simm12"] = CommonEnc(12, (1 << 12) -1)
common_enc["min_simm12"] = CommonEnc(12, 1 - ((1 << 13) -1))
common_enc["max_barcount"] = CommonEnc(4, 8)
#common_enc["bar_op"] = CommonEnc(2, 3)


# to compatiable RISCV isa encoding, we avoid using RISCV enc field:
#   32bit 11
#   48bit 111110
#   64bit 1111110
# and use similar rd/rs field,  and extend rd/rs field in next 32bit
# but below is just temperaly to ,and will adjust after merge riscv encoding

# EXT enc is a way to add more 32bit to next instruction.
#    the EXT 32bit 's decoding is depend on next instruction enc
# the Instr is created with enterInstruction in assembler.py , which pas op name as arg
class OpType(Enum):
    IALU_OP = 0
    IALU_LONG_OP = 1
    FALU_OP = 2
    SFP_OP = 3
    TENSOR_OP = 4
    INTP_OP = 5
    ALU_SFU_OP = 6
    TENSOR_LOAD_OP = 7
    TENSOR_STORE_OP = 8
    LOAD_OP = 9
    STORE_OP = 10
    BRANCH_OP = 11
    BARRIER_OP = 12
    MEMORY_BARRIER_OP  = 13
    WAITCNT_OP  = 14
    CALL_OP = 15
    RET_OP = 16
    EXIT_OP = 17

# add default optype, dst_reg
def decode_OpType(op):
    if (len(op) == 2):
        op_name = op[0]
        if op_name.find("_F32") > 0:
            op = (*op, OpType.FALU_OP, 0)
        elif op_name.find("_F64") > 0:
            op = (*op, OpType.FALU_OP, 0)
        elif op_name.find("_LOAD") > 0:
            op = (*op, OpType.LOAD_OP, 0)
        elif op_name.find("_STORE") > 0:
            op = (*op, OpType.STORE_OP, 0)
        elif op_name.find("BRANCH") > 0:
            op = (*op, OpType.BRANCH_OP, 0)
        else:
            op = (*op, OpType.IALU_OP, 0)
    elif (len(op) == 3):
            op = (*op, 0)
    return op

OpEncode = namedtuple('OpEncode', ['name', 'value', 'optype', 'dst_reg'])
class Instr(LittleEndianStructure):
    _pack_ = 1
    FmtEnc = namedtuple('FmtEnc', ['bit_start', 'width', 'value'])
    fmt_enc = {}
    fmt_enc["VOP2"] = FmtEnc(31, 2, 0b00)
    fmt_enc["EXT1"] = FmtEnc(31, 3, 0b010)
    fmt_enc["EXT"] =  FmtEnc(31, 4, 0b0111)
    fmt_enc["SOP2"] = FmtEnc(31, 4, 0b0110)
    fmt_enc["SOPK"] = FmtEnc(31, 4, 0b1001)
    fmt_enc["SLS"] =  FmtEnc(31, 4, 0b1011)
    fmt_enc["VSMRD"] =FmtEnc(31, 5, 0b100010)
    fmt_enc["DLS"] =  FmtEnc(31, 6, 0b100000)
    fmt_enc["VLS"] =  FmtEnc(31, 6, 0b100001)
    fmt_enc["VMUBUF"]=FmtEnc(31, 6, 0b100011)
    fmt_enc["VOP3A"] =FmtEnc(31, 6, 0b101001)
    fmt_enc["VOP3B"] =FmtEnc(31, 6, 0b101011)
    fmt_enc["VOP1"] = FmtEnc(31, 7, 0b1010001)
    fmt_enc["VOPC"] = FmtEnc(31, 7, 0b1010000)
    fmt_enc["SOPC"] = FmtEnc(31, 9, 0b101010000)
    fmt_enc["SOPP"] = FmtEnc(31, 9, 0b101010001)
    fmt_enc["SOP1"] = FmtEnc(31, 9, 0b101010010)

    def __init__(self, name=''):
        #super().__init__(name)
        self.opcode = None
        #self.has_imm = False
        #self.imm = None
        self.lop_imm = None
        self.stride_imm = 0
        self.branch_cond = 0
        self.code_pos = 0
        self.flags = {}
        self.encoded_inst = 0
        self.is_encoded = False
        self.fmt_dst = 0
        self.fmt_src = 0
        self.stride_pos = 0
        self.regs = []
        self.operands = []
        #self.special_operands = {} #ci/co/param/tcc/builtin/pred is keys, value is Reg or regstr
        self.unresolved = False # unresolved operand is raw str
        self.dst_reg = None
        self.name = name       # in fact it is line number
        self.instr_str = None
        self.func_name = None
        self.instr_size = sizeof(self)
        self.mspace = None
        #if hasattr(self, "field"):
        #    for n,v in self.field.items():
        #        setattr(self, n, 0)
        print("[instr create info] create instr with op {}".format(name))
        if name == "":
            assert("Warn:create instr without correct op enum")
        else:
            self.setupOpTable()
            self.enc = Instr.fmt_enc[self.getFmtName()].value
            self.op = self.optable[name.upper()].value
            if self.optable[name.upper()].dst_reg is not None:
                self.dst_reg = self.optable[name.upper()].dst_reg
            assert(self.enc == Instr.fmt_enc[self.getFmtName()].value)
            assert(self.op == self.optable[name.upper()].value)

    def setupOpTable(self):
        self.optable = {}
        for op in self._optable_:
            op = decode_OpType(op)
            self.optable[op[0]] = OpEncode(*op)


    def addOperand(self, operand):
        if (isinstance(operand, int)):
            self.setImm(operand)
        elif (isinstance(operand, str)):
            self.unresolved = True
        self.operands.append(operand)

    def addUnresolvedOperand(self, operand_type, reg_str):
        assert(isinstance(reg_str, str))
        self.operands.append(UnresolvedReg(operand_type, reg_str))
        self.unresolved = True

    def addReg(self, reg: Reg):
        #if self.dst_reg is None:
        #    self.dst_reg = reg
        self.regs.append(reg)
        self.addOperand(reg)

    # for vcc etc.
    def addSpecialOperand(self, operand_type, reg_str):
        #pdb.set_trace()
        #if reg_str in SpecialREG.special_reg.keys():
        #    #self.regs.append(SpecialREG.special_reg[reg_str].reg)
        #    self.special_operands[operand_type] = SpecialREG.special_reg[reg_str].reg
        #else:
        #    self.special_operands[operand_type] = Reg(reg_str)
        self.addUnresolvedOperand(operand_type, reg_str)
        #return self.special_operands[operand_type]

    def setImm(self, imm):
        self.imm = imm

    def setLopImm(self, lop_imm):
        self.lop_imm = lop_imm

    def setStrideImm(self, stride_imm):
        self.stride_imm = stride_imm

    def setFlag(self, *name):
        for n in name:
            self.flags[n] = True

    def setMspace(self, mspace):
        self.mspace = mspace

    def getFmtName(self):
        _, fmt = self.__class__.__name__.split('_')
        return fmt

    def getInstrDefName(self):
        instr_def = self.__class__.__name__.replace('Instr', "")
        #print("GetInstrDef" + instr_def)
        return instr_def

    def getInstrFmtList(self):
        #return [fmtcls.__name__.lower() for fmtcls [k() for k in __class__.__subclasses__()]]
        _, fmt = self.__class__.__name__.split('_')
        instr = self.__class__.__name__
        return instr, fmt

    def getCppFieldEncode(self):
        instr_encode = "\nstruct Bytes" + self.getFmtName() +  " {\n"
        instr_encode += "\n".join(["    uint32_t {} : {};".format(n[0], n[-1]) for n in self._fields_ if n[0][0:3] != 'ext'])
        ext_  = [n for n in self._fields_ if n[0][0:3] == 'ext']
        if len(ext_) > 0:
            instr_encode += "\n\tunion {\n"
            instr_encode += "\tstruct Ext {\n"
            instr_encode += "\n".join(["\t    uint32_t {} : {};".format(n[0], n[-1]) for n in ext_])
            instr_encode += "\n\t} e0_;\n"
            for ext_fields in dir(self):
                if ext_fields.find('_fields_e') >= 0:
                    #pdb.set_trace()
                    instr_encode += "\n\tstruct Bytes" + self.getFmtName() +  "_{}".format(ext_fields[8:]) + " {\n"
                    exec("self.tmp_ext_field = self.{}._fields_".format(ext_fields))
                    instr_encode += "\n".join(["\t    uint32_t {} : {};".format(n[0], n[-1]) for n in self.tmp_ext_field]) + "\n\t}" + " {};".format(ext_fields[8:])
            instr_encode += "\n\t} ext;\n"
        instr_encode += "\n};"
        instr_encode += "\nvoid print" + self.getFmtName() + "(Bytes" + self.getFmtName() + " bytes) {\n" + \
                "printf(\"decoding: " + ",".join(["{} %x ".format(n[0]) for n in self._fields_ if n[0][0:3] != 'ext']) + "\\n\", " + \
                ",".join(["bytes.{}".format(n[0]) for n in self._fields_ if n[0][0:3] != 'ext']) + ");\n"
        if len(ext_) > 0:
            ext = 1
            for ext_fields in dir(self):
                if ext_fields.find('_fields_e') >= 0:
                    exec("self.tmp_ext_field = self.{}._fields_".format(ext_fields))
                    instr_encode += "printf(\"ext_field{}: ".format(ext) + ",".join(["{} %x ".format(n[0]) for n in self.tmp_ext_field]) + "\\n\", " + \
                    ",".join(["bytes.ext.e{}_.{}".format(ext, n[0]) for n in self.tmp_ext_field]) + ");\n"
                    ext += 1
        instr_encode += "\n};"
        return instr_encode

    def getFlag(self, name):
        if name in flags:
            return self.flags[name];
        else:
            return False

    def getInputDataType(self):
        pass

    def genInstrAsm(self):
        return string_at(addressof(self), self.getInstrSize())

    def getInstrSize(self):
        return self.instr_size

    def getOpcodeEnumList(self):
        opcode_list = OrderedDict()
        for op in self._optable_:
            op = decode_OpType(op)
            name = op[0]
            value = op[1]
            optype = "opu_op_t::{}".format(op[2].name)
            opcode_list[name] = [hex(value), optype]
        return opcode_list

    def genInstrOpcodeDef(self, f, fmt):
        opcode_list = self.getOpcodeEnumList()
        for n, v in opcode_list.items():
            #TODO fix instr_size with E32 flag
            f.write("DEFINST({},{}, {}, {}, {})\n".format(n, fmt, v[0], v[1], 0))
        f.write("DEFINSTEND({})\n".format(fmt))
        for n, v in opcode_list.items():
            #TODO fix instr_size with E32 flag
            f.write("DEFINST2({})\n".format(n))


    def genInstrDef(self, visit_type, f):
        if visit_type == VisitType.GEN_INSTR_FMT_FIELD:
            f.write(self.getCppFieldEncode())
        elif visit_type == VisitType.GET_INSTR_FMT_LIST:
            return self.getInstrFmtList()
        elif visit_type == VisitType.GEN_INSTR_OP_ENUM_DEF:
            opcode_list = self.getOpcodeEnumList()
            for n, v in opcode_list:
                f.write("{} = {}".format(n, v[0]))

    def __str__(self):
        if self.instr_str is not None:
            return self.instr_str
        instr_str = self.name.lower() + " "
        #if self.dst_reg is not None:
        #    instr_str += self.dst_reg.__str__()
        for operand in self.operands:
            #if isinstance(operand, Reg):
            instr_str += " " + format(operand.__str__())
        return instr_str

    @classmethod
    def getGrammarInstrFmtList(cls):
        return " | ".join([subcls.__name__.lower() for subcls in __class__.__subclasses__()])

    @classmethod
    def getGrammarInstrClassList(cls):
        instr_class = []
        for subcls in __class__.__subclasses__():
            print("InInstrClass: {} visit {}".format(cls.__name__, subcls.__name__))
            subcls.visitSubClass(VisitType.GRAMMAR_INSTR_FMT, instr_class)
        return instr_class

    @classmethod
    def getGrammarInstrDefList(cls):
        instr_def = []
        for subcls in __class__.__subclasses__():
            print("InInstrDef: {} visit {}".format(cls.__name__, subcls.__name__))
            subcls.visitSubClass(VisitType.GRAMMAR_INSTR_DEF, instr_def)
        return instr_def


    @classmethod
    def visitClass(cls, visit_type, f):
        for subcls in __class__.__subclasses__():
            print("in visitClass visit_type {}: {} visit {}".format(visit_type, cls.__name__, subcls.__name__))
            subcls.visitSubClass(visit_type, f)

    @classmethod
    def visitSubClass(cls, visit_type, f):
        tmp = []
        for subcls in cls.__subclasses__():
            subobj = subcls()
            if cls.__name__ == subcls.__name__:
                continue
            print("InSubClass visit_type {}: {} visit {}".format(visit_type, cls.__name__, subcls.__name__))
            if visit_type == VisitType.GRAMMAR_INSTR_DEF:
                tmp.append(subobj.genGrammarInstrDef(f))
            elif visit_type == VisitType.GRAMMAR_INSTR_FMT:
                tmp.append(subobj.genGrammarInstrClass())
            else:
                tmp.append(subobj.genInstrDef(visit_type, f))
        if visit_type == VisitType.GRAMMAR_INSTR_FMT:
            f.append({"name": cls.__name__.lower(), "value": "\n         | ".join(tmp)})
        elif visit_type == VisitType.GET_INSTR_FMT_LIST:
            f += tmp


    def genGrammarInstrDef(self, f):
        tmp = [utilReplace(" ".join(op[0])) for op in self._optable_]
        op_list = "(" + "\n         | ".join(tmp) + ") E32?"
        f.append({"name": self.getInstrDefName(), "value": op_list})
        return



#------------------------------
class InstrValu(Instr):
    def __init__(self, name=''):
        super().__init__(name)

    def encode_vdst(self, operand, ext_field_reg):
        assert(isinstance(operand, Reg))
        self.vdst = operand.idx & ((1 << (common_enc["max_vdst_32e"].width + 1)) - 1)
        ext_bits = operand.idx >> common_enc["max_vdst_32e"].width
        if ext_bits > 0:
            #if self.vdst == 63:
            #    pdb.set_trace()
            ext_field_reg.vdst = ext_bits
            self.ext_enc = common_enc["ext1_enc"].value
        else:
            ext_field_reg.vdst = 0

    def encode_src0(self, operand, ext_field_reg):
        if (isinstance(operand, int)):
            self.imm_ = 1
            self.src0 = operand & ((1 << (common_enc["max_src0_32e"].width + 1)) - 1)
            self.dsrc0_ = (operand >> 6) & 0x3
            ext_bits = operand >> (common_enc["max_src0_32e"].width + 2)
            if ext_bits > 0:
                self.ext_enc = common_enc["ext1_enc"].value
                self.ext1.imm = ext_bits
            else:
                self.ext1.imm = 0
            return
        assert(isinstance(operand, Reg))
        if (operand.rtype == Reg.RegType.Data):
            if operand.lie is True:
                self.dsrc0_ = common_enc["dsrc0_l"].value
            else:
                self.dsrc0_ = common_enc["dsrc0_d"].value
        elif (operand.rtype == Reg.RegType.Scalar):
            self.dsrc0_ = common_enc["dsrc0_s"].value
        else:
            self.dsrc0_ = common_enc["dsrc0_v"].value
        self.src0 = operand.idx
        ext_bits = operand.idx >> common_enc["max_src0_32e"].width
        if ext_bits > 0:
            self.ext_enc = common_enc["ext1_enc"].value
            ext_field_reg.src0 = ext_bits
        else:
            ext_field_reg.src0 = 0

    def encode_vsrc1(self, operand, ext_field_reg):
        assert(isinstance(operand, Reg))
        self.vsrc1 = operand.idx
        ext_bits = operand.idx >> common_enc["max_vsrc1_32e"].width
        if ext_bits > 0:
            self.ext_enc = common_enc["ext1_enc"].value
            ext_field_reg.vsrc1 = ext_bits
        else:
            ext_field_reg.vsrc1 = 0


class InstrSalu(Instr):
    def __init__(self, name=''):
        super().__init__(name)

class InstrSmem(Instr):
    def __init__(self, name=''):
        super().__init__(name)

class InstrVmem(Instr):
    def __init__(self, name=''):
        super().__init__(name)

    def encode_vdata(self, operand, ext_field_reg):
        assert(isinstance(operand, Reg))
        self.vdata = operand.idx & ((1 << (common_enc["max_vdata_32e"].width + 1)) - 1)
        ext_bits = operand.idx >> common_enc["max_vdata_32e"].width
        if ext_bits > 0:
            ext_field_reg.vdata = ext_bits
            self.ext_enc = common_enc["ext1_enc"].value
        else:
            ext_field_reg.vdata = 0

    def encode_vaddr(self, operand, ext_field_reg):
        assert(isinstance(operand, Reg))
        if (operand.rtype == Reg.RegType.Scalar):
            self.ssrc0_ = 1
        else:
            self.ssrc0_ = 0
        self.vaddr = operand.idx & ((1 << (common_enc["max_vaddr_32e"].width + 1)) - 1)
        ext_bits = operand.idx >> common_enc["max_vaddr_32e"].width
        if ext_bits > 0:
            self.ext_enc = common_enc["ext1_enc"].value
            ext_field_reg.vaddr = ext_bits
        else:
            ext_field_reg.vaddr = 0

    def encode_vls_offset(self, operand, ext_field_reg):
        assert (isinstance(operand, int))
        self.offset = operand & ((1 << (common_enc["max_vls_offset_32e"].width + 1)) - 1)
        ext_bits = operand >> common_enc["max_vls_offset_32e"].width
        if ext_bits > 0:
            self.ext_enc = common_enc["ext1_enc"].value
            ext_field_reg.imm = ext_bits
        else:
            ext_field_reg.imm = 0




class InstrDmem(Instr):
    def __init__(self, name=''):
        super().__init__(name)

#------------------------------
class InstrVALU_VOP2(InstrValu):
    _fields_ = [
                ("pred", c_uint, 2),
                ("imm_", c_uint, 1),  # imm_ indicate dsrc0_src0 is imm
                ("src0", c_uint, 6),
                ("dsrc0_", c_uint, 2),  # '10, dreg '11 it is lreg,  '00 is vector, '01 is Scalar
                ("vsrc1", c_uint, 6),
                ("vdst", c_uint, 6),
                ("op", c_uint, 7),
                ("enc", c_uint, 2),
                ('ext',     c_uint, 28),
                ('ext_enc', c_uint, 4)]

    class _fields_e1_(LittleEndianStructure):
        _pack_ = 1
        _fields_ = [
                ("imm", c_uint, 22),
                ("src0", c_uint, 2),
                ("vsrc1", c_uint, 2),
                ("vdst", c_uint, 2),
                ('ext_enc', c_uint, 4)
                ]

    def __init__(self, name=''):
        self.ext1 = self._fields_e1_()
        super().__init__(name)


    _optable_ = [
                ('V_CNDMASK_B32',  0x0),
                ('V_ADD_F32',  0x1),
                ('V_SUB_F32',  0x2),
                ('V_SUBREV_F32', 0x3),
                ('V_MUL_F32',   0x4),
                ('V_MUL_I32_I24', 0x5),
                ('V_MULLO_I32_I24', 0xe),
                ('V_MULLO_I32', 0x6),
                ('V_MULHI_I32', 0x7),
                ('V_MULLO_U32', 0x8),
                ('V_MULHI_U32', 0x9),
                ('V_MUL_I64_I32', 0x2d),
                ('V_MIN_F32', 0xa),
                ('V_MAX_F32', 0xb),
                ('V_MIN_I32', 0xc),
                ('V_MAX_I32', 0xd),
                ('V_MIN_U32', 0x11),
                ('V_MAX_U32', 0x12),
                ('V_LSHRREV_B32', 0x13),
                ('V_ASHRREV_I32', 0x14),
                ('V_LSHL_B32', 0x15),
                ('V_LSHLREV_B32', 0x16),
                ('V_AND_B32', 0x17),
                ('V_OR_B32', 0x18),
                ('V_XOR_B32', 0x19),
                ('V_BFM_B32', 0x20),
                ('V_MAC_F32', 0x21),
                #('V_MADMK_F32', 0x22),  move to 3 op
                ('V_ADD_I32', 0x22),
                ('V_ADD_I64', 0x23),
                ('V_SUB_I32', 0x24),
                ('V_SUBREV_I32', 0x25),
                ('V_ADD_U32', 0x26),
                ('V_ADDCO_U32', 0x27),
                ('V_SUB_U32', 0x28),
                ('V_SUBREV_U32', 0x29),
                ('V_LSHL_B64', 0x2a),
                ('V_ASHR_I64', 0x2b),
                ('V_ADD_F64', 0x2c)
            ]

    def genGrammarInstrClass(self):
        #return self.getInstrDefName() + " vreg ',' generic_reg_or_number ',' vreg (',' special_operand)*"
        return self.getInstrDefName() + " vreg ',' vreg ',' generic_reg_or_number (',' special_operand)* ('%' float_mode (',' float_mode)*)? "

    def addOperand(self, operand):
        super().addOperand(operand)
        if isinstance(operand, str):
            self.unresolved = True
            return
        self.updateOperand(len(self.operands))

    def updateOperand(self, operand_num):
        operand = self.operands[operand_num-1]
        if operand_num == 1:
            self.encode_vdst(operand, self.ext1)
        elif operand_num == 2:
            self.encode_vsrc1(operand, self.ext1)
        elif operand_num == 3:
            self.encode_src0(operand, self.ext1)



    def addSpecialOperand(self, operand_type, reg_str):
        assert(operand_type == UnresolvedReg.Kind.ci and reg_str[0:3] == "tcc")
        #super().addSpecialOperand(operand_type, reg_str)
        #reg = super().addSpecialOperand(operand_type, reg_str)
        self.regs.append(Reg(reg_str, operand_type))
        if (self.op == self.OpcodeEnum.V_ADD_U32.value):
            self.op = self.OpcodeEnum.V_ADDCO_U32.value

    def getInstrSize(self):
        if self.ext_enc == common_enc["ext1_enc"].value:
            self.ext = self.ext1.vdst << 26 | self.ext1.vsrc1 << 24 | self.ext1.src0 << 22 | self.ext1.imm
            return 8
        elif self.ext_enc != 0x0:
            pdb.set_trace()
            return 8
        else:
            return 4

# dreg use implicit M0 to knoe stride addr between lane
class InstrVALU_VOP1(InstrValu):
    _fields_ = [
                ("pred", c_uint, 2),
                ("imm_", c_uint, 1),  # imm_ indicate dsrc0_src0 is imm
                ("src0", c_uint, 6),
                ("dsrc0_", c_uint, 2),  # '10, dreg '11 it is lreg,  '00 is vector, '01 is Scalar
                ("op", c_uint, 8),
                ("vdst", c_uint, 6),
                ("enc", c_uint, 7),
                ('ext',     c_uint, 28),
                ('ext_enc', c_uint, 4)]

    _optable_ = [
                ('V_MOV_B32', 0x1),
                ('V_READFIRSTLANE_B32', 0x2),
                ('V_CVT_I32_F64', 0x3),
                ('V_CVT_F64_I32', 0x4),
                ('V_CVT_F32_I32', 0x5),
                ('V_CVT_F32_U32', 0x6),
                ('V_CVT_U32_F32', 0x7),
                ('V_CVT_I32_F32', 0x8),
                ('V_CVT_F32_F64', 0x9),
                ('V_CVT_F64_F32', 0xa),
                ('V_CVT_F64_U32', 0xb),
                ('V_CVTA_SHARED_TO_FLAT', 0x25),
                ('V_CVTA_FLAT_TO_GLOBAL', 0x27),
                ('V_TRUNC_F32', 0xc),
                ('V_FLOOR_F32', 0xd),
                ('V_LOG_F32', 0xe),
                ('V_RCP_F32', 0xf),
                ('V_RSQ_F32', 0x10),
                ('V_RCP_F64', 0x11),
                ('V_RSQ_F64', 0x12),
                ('V_SQRT_F32', 0x13),
                ('V_SIN_F32', 0x14),
                ('V_COS_F32', 0x15),
                ('V_NOT_B32', 0x16),
                ('V_FFBH_U32', 0x17),
                ('V_FRACT_F64', 0x18),
                ('V_MOVRELD_B32', 0x19),
                ('V_MOVRELS_B32', 0x1a),
                ('V_SEXT_I64_I32', 0x1b),
                ('V_SEXT_I32_I8', 0x1c),
                ('V_SEXT_I32_I16', 0x1d),
                ('V_ZEXT_B32_B16', 0x1e),
                ('V_ZEXT_B32_B8', 0x1f),
                ('V_ZEXT_B64_B32', 0x20),
                ('V_CHOP_B16_B32', 0x22)
                ]

    class _fields_e1_(LittleEndianStructure):
        _pack_ = 1
        _fields_ = [
                ("imm", c_uint, 26),
                ("vdst", c_uint, 2),
                ('ext_enc', c_uint, 4)
                ]

    class _fields_e2_(LittleEndianStructure):
        _pack_ = 1
        _fields_ = [
                ("unused", c_uint, 24),
                ("src0", c_uint, 2),
                ("vdst", c_uint, 2),
                ('ext_enc', c_uint, 4)
                ]


    def __init__(self, name=''):
        self.ext1 = self._fields_e1_()
        self.ext2 = self._fields_e2_()
        super().__init__(name)

    def genGrammarInstrClass(self):
        #return self.getInstrDefName() + " vreg ',' generic_reg"
        return self.getInstrDefName() + " vreg ',' (generic_reg_or_number | builtin_operand)"

    def addOperand(self, operand):
        super().addOperand(operand)
        if isinstance(operand, str):
            self.unresolved = True
            return
        self.updateOperand(len(self.operands))


    def updateOperand(self, operand_num):
        operand = self.operands[operand_num - 1]
        if operand_num == 1:
            self.encode_vdst(operand, self.ext2)
        elif operand_num == 2:
            self.encode_src0(operand, self.ext2)

    def addBuiltinOperand(self, reg_str):
        super().addSpecialOperand(UnresolvedReg.Kind.builtin, reg_str)
        #reg = super().addSpecialOperand("builtin", reg_str)
        #self.addOperand(reg)

    def getInstrSize(self):
        if self.ext_enc == common_enc["ext1_enc"].value:
            #pdb.set_trace()
            self.ext = self.ext1.vdst << 26 | self.ext1.imm
            self.ext |= self.ext2.vdst << 26;
            self.ext |= self.ext2.src0 << 24;
            return 8
        elif self.ext_enc != 0x0:
            pdb.set_trace()
            return 8
        else:
            return 4

#TODO add VOPCK
class InstrVALU_VOPC(InstrValu):
    _fields_ = [
                ("pred", c_uint, 2),
                ("imm_", c_uint, 1),
                ("src0", c_uint, 6),
                ("dsrc0_", c_uint, 2),
                ("vsrc1", c_uint, 6),
                ("tcc", c_uint, 2),
                ("op", c_uint, 6),
                ("enc", c_uint, 7),
                ('ext',     c_uint, 28),
                ('ext_enc', c_uint, 4)]

    class _fields_e1_(LittleEndianStructure):
        _pack_ = 1
        _fields_ = [
                ("imm", c_uint, 22),
                ("src0", c_uint, 2),
                ("vsrc1", c_uint, 2),
                ("tcc", c_uint, 2),
                ('ext_enc', c_uint, 4)
                ]

    def __init__(self, name=''):
        self.ext1 = self._fields_e1_()
        super().__init__(name)


    _optable_ = [
                ('V_CMP_LT_F32', 0x1),
                ('V_CMP_GT_F32', 0x2),
                ('V_CMP_GE_F32', 0x3),
                ('V_CMP_NGT_F32', 0x4),
                ('V_CMP_NEQ_F32', 0x5),
                #('#V_CMP_LT_F64', 0x6),
                #('#V_CMP_EQ_F64', 0x7),
                #('#V_CMP_LE_F64', 0x8),
                #('#V_CMP_GT_F64', 0xa),
                #('#V_CMP_NGE_F64', 0xb),
                #('#V_CMP_NEQ_F64', 0xc),
                #('#V_CMP_NLT_F64', 0xd),
                ('V_CMP_LT_I32', 0xe),
                ('V_CMP_EQ_I32', 0xf),
                ('V_CMP_LE_I32', 0x10),
                ('V_CMP_GT_I32', 0x11),
                ('V_CMP_NE_I32', 0x12),
                ('V_CMP_GE_I32', 0x13),
                #('#V_CMP_CLASS_F64', 0x14),
                ('V_CMP_LT_U32', 0x15),
                ('V_CMP_EQ_U32', 0x16),
                ('V_CMP_LE_U32', 0x17),
                ('V_CMP_GT_U32', 0x18),
                ('V_CMP_NE_U32', 0x19),
                ('V_CMP_GE_U32', 0x1a)
                ]

    def genGrammarInstrClass(self):
        return self.getInstrDefName() + " sreg_or_tcc ',' vreg ',' generic_reg_or_number"

    def addOperand(self, operand):
        super().addOperand(operand)
        #if isinstance(operand, str):
        #    self.unresolved = True
        #    return
        #self.updateOperand(len(self.operands))

    def updateOperand(self, operand_num):
        operand = self.operands[operand_num - 1]
        if operand_num == 1:
            assert(isinstance(operand, Reg))
            self.tcc = operand.idx & ((1 << (common_enc["max_tcc_32e"].width + 1)) - 1)
            ext_bits = operand.idx >> common_enc["max_tcc_32e"].width
            if ext_bits > 0:
                self.ext_enc = common_enc["ext1_enc"].value
                self.ext1.tcc = ext_bits
            else:
                self.ext1.tcc = 0
        elif operand_num == 2:
            self.encode_vsrc1(operand, self.ext1)
        elif operand_num == 3:
            self.encode_src0(operand, self.ext1)


    #def addSpecialCCReg(self, reg_str):
    #    #pdb.set_trace()
    #    reg = Reg(reg_str)
    #    self.addReg(reg)
    #    #self.updateOperand(len(self.operands))
    #    #super().addSpecialOperand(UnresolvedReg.Kind.tcc, reg_str)
    #    #reg = super().addSpecialOperand("tcc", reg_str)
    #    #self.addOperand(reg)
    #    #if (self.op == self.OpcodeEnum.V_ADD_U32.value):
    #    #    self.op = self.OpcodeEnum.V_ADDCO_U32.value

    def getInstrSize(self):
        if self.ext_enc == common_enc["ext1_enc"].value:
            self.ext = self.ext1.tcc << 26 | self.ext1.vsrc1 << 24 | self.ext1.src0 << 22 | self.ext1.imm
            return 8
        elif self.ext_enc != 0x0:
            pdb.set_trace()
        else:
            return 4

class InstrVALU_VOP3A(InstrValu):
    _fields_ = [("vdst", c_uint, 8),
                ("abs", c_uint, 3),
                ("clamp", c_uint, 1),
                ("reserved", c_uint, 5),
                ("op", c_uint, 9),
                ("enc", c_uint, 6),
                ("src0", c_uint, 9),
                ("src1", c_uint, 9),
                ("src2", c_uint, 9),
                ("omod", c_uint, 2),
                ("neg", c_uint, 3)]

    _optable_ = [
                ('V_CNDMASK_B32_VOP3A', 0x1),
                ('V_ADD_F32_VOP3A', 0x2),
                ('V_SUBREV_F32_VOP3A', 0x3),
                ('V_MUL_F32_VOP3A', 0x4),
                ('V_MUL_I32_I24_VOP3A', 0x5),
                ('V_MAX_F32_VOP3A', 0x6),
                ('V_MAD_F32', 0x7),
                ('V_MAD_U32_U24', 0x8),
                ('V_MADLO_I32_I32', 0x40),
                ('V_BFE_U32', 0x9),
                ('V_BFE_I32', 0xa),
                ('V_BFI_B32', 0xb),
                ('V_FMA_F32', 0xc),
                ('V_FMA_F64', 0xd),
                ('V_ALIGNBIT_B32', 0xe),
                ('V_CSEL_B32', 0xf),
                ('V_CSEL_B64', 0x10),
                ('V_MAX3_I32', 0x12),
                #('#V_DIV_FIXUP_F64', 0x10),
                #('#V_DIV_FMAS_F64', 0x10),
                ('V_MIN_F64', 0x13),
                ('V_MAX_F64', 0x14),
                ('V_FRACT_F32_VOP3A', 0x18),
                ('V_CMP_LT_F32_VOP3A', 0x19),
                ('V_CMP_EQ_F32_VOP3A', 0x1a),
                ('V_CMP_GT_F32_VOP3A', 0x1b),
                ('V_CMP_NLE_F32_VOP3A', 0x1c),
                ('V_CMP_NEQ_F32_VOP3A', 0x1d),
                ('V_CMP_NLT_F32_VOP3A', 0x1e),
                ('V_CMP_LT_I32_VOP3A', 0x1f),
                ('V_CMP_EQ_I32_VOP3A', 0x20),
                ('V_CMP_LE_I32_VOP3A', 0x21),
                ('V_CMP_GT_I32_VOP3A', 0x22),
                ('V_CMP_GE_I32_VOP3A', 0x23),
                ('V_CMP_NE_I32_VOP3A', 0x24),
                ('V_CMPX_EQ_I32_VOP3A', 0x25),
                ('V_CMP_OP16_F64_VOP3A', 0x26),
                ('V_CMP_CLASS_F64_VOP3A', 0x27),
                ('V_CMP_LT_U32_VOP3A', 0x28),
                ('V_CMP_LE_U32_VOP3A', 0x29),
                ('V_CMP_GT_U32_VOP3A', 0x2a),
                ('V_CMP_LG_U32_VOP3A', 0x2b),
                ('V_CMP_GE_U32_VOP3A', 0x2c),
                ('V_CMP_LT_U64_VOP3A', 0x2d),
                ('V_LSHR_B64', 0x30),
                ('V_MUL_F64', 0x32),
                ('V_LDEXP_F64', 0x33),
                ('V_CMP_LE_F32_VOP3A', 0x38),
                #('#V_MED3_I32_VOP3A', 0x39),
                ('V_MED3_I32', 0x3a)
                ]
    def __init__(self, name=''):
        super().__init__(name)

    def genGrammarInstrClass(self):
        return self.getInstrDefName() + " vreg ',' generic_reg ',' generic_reg ',' generic_reg ('%' float_mode (',' float_mode)*)? "

    def addOperand(self, operand):
        super().addOperand(operand)
        if isinstance(operand, str):
            self.unresolved = True
            return
        self.updateOperand(len(self.operands))

    def updateOperand(self, operand_num):
        operand = self.operands[operand_num - 1]
        if operand_num == 1:
            assert(isinstance(operand, Reg))
            self.sdst = operand.idx
        elif operand_num == 2:
            assert(isinstance(operand, Reg))
            self.src0 = operand.idx
            if (operand.rtype == Reg.RegType.Vector):
                self.src0 += 0x100
        elif operand_num == 3:
            assert(isinstance(operand, Reg))
            self.src1 = operand.idx
            if (operand.rtype == Reg.RegType.Vector):
                self.src1 += 0x100
        elif operand_num == 4:
            assert(isinstance(operand, Reg))
            self.src1 = operand.idx
            if (operand.rtype == Reg.RegType.Vector):
                self.src1 += 0x100

    def getInstrSize(self):
        if self.src0 == 0xFF:
            return self.instr_size
        else:
            return 4

class InstrVALU_VOP3B(InstrValu):
    _fields_ = [("vdst", c_uint, 8),
                ("sdst", c_uint, 7),
                ("src0", c_uint, 9),
                ("op", c_uint, 2),
                ("enc", c_uint, 6),
                ("vsrc1", c_uint, 8),
                ("ssrc2", c_uint, 8),
                ("lit_const", c_uint, 16)]

    _optable_ = [
                ('V_ADDC_U32', 0x1)
                ]

    def __init__(self, name=''):
        super().__init__(name)

    def genGrammarInstrClass(self):
        return self.getInstrDefName() + " vreg ',' generic_reg_or_number ',' vreg (',' special_operand)* "

    def addOperand(self, operand):
        super().addOperand(operand)
        if isinstance(operand, str):
            self.unresolved = True
            return
        self.updateOperand(len(self.operands))

    def updateOperand(self, operand_num):
        operand = self.operands[operand_num - 1]
        if operand_num == 1:
            assert(isinstance(operand, Reg))
            self.vdst = operand.idx
        elif operand_num == 2:
            if isinstance(operand, int):
                self.lit_const = operand
                self.src0 = 0xFF
                return
            assert(isinstance(operand, Reg))
            self.src0 = operand.idx
            if (operand.rtype == Reg.RegType.Vector):
                self.src0 += 0x100
        elif operand_num == 3:
            assert(isinstance(operand, Reg))
            assert(operand.rtype == Reg.RegType.Vector)
            self.vsrc1 = operand.idx

    def addSpecialOperand(self, operand_type, reg_str):
        super().addSpecialOperand(operand_type, reg_str)
        #reg = super().addSpecialOperand(operand_type, reg_str)
        if (operand_type == UnresolvedReg.Kind.co):
            self.sdst = reg.idx
        elif (operand_type == UnresolvedReg.Kind.ci):
            self.ssrc2 = reg.idx


    def getInstrSize(self):
        return self.instr_size

 #------------------------------
class InstrSALU_SOP1(InstrSalu):
    _fields_ = [("ssrc0", c_uint, 8),
                ("op", c_uint, 7),
                ("sdst", c_uint, 8),
                ("enc", c_uint, 9),
                ('ext',     c_uint, 28),
                ('ext_enc', c_uint, 4)]

    _optable_ = [
                ('S_MOV_B32', 0x3),
                ('S_MOV_B64', 0x4),
                ('S_NOT_B32', 0x7),
                ('S_WQM_B64', 0x11),
                ('S_SWAPPC_B64', 0x12),
                ('S_AND_SAVEEXEC_B64', 0x13)
                ]

    def __init__(self, name=''):
        super().__init__(name)


    def genGrammarInstrClass(self):
        return self.getInstrDefName() + " sreg_or_tcc ',' sreg_or_tcc"

    def addOperand(self, operand):
        super().addOperand(operand)
        if isinstance(operand, str):
            self.unresolved = True
            return
        self.updateOperand(len(self.operands))

    def updateOperand(self, operand_num):
        operand = self.operands[operand_num - 1]
        if operand_num == 1:
            assert(isinstance(operand, Reg))
            if (operand.rtype == Reg.RegType.TCC):
                self.sdst = operand.idx + SREG_TCC
            else:
                self.sdst = operand.idx
        elif operand_num == 2:
            assert(isinstance(operand, Reg))
            if (operand.rtype == Reg.RegType.TCC):
                self.ssrc0 = operand.idx + SREG_TCC
            else:
                self.ssrc0 = operand.idx

    def getInstrSize(self):
        if self.ext_enc != 0x0:
            return 8
        else:
            return 4



class InstrSALU_SOP2(InstrSalu):
    _fields_ = [
                ("ssrc0", c_uint, 7),
                ("ssrc1", c_uint, 7),
                ("sdst", c_uint, 7),
                ("op", c_uint, 7),
                ("enc", c_uint, 4)]

    def __init__(self, name=''):
        super().__init__(name)

    _optable_ = [
                ('S_ADD_U32', 0x1),
                ('S_ADD_I32', 0x2),
                ('S_SUB_I32', 0x3),
                ('S_MIN_U32', 0x4),
                ('S_MAX_I32', 0x5),
                ('S_MAX_U32', 0x6),
                ('S_CSELECT_B32', 0x7),
                ('S_AND_B32', 0x8),
                ('S_AND_B64', 0x10),
                ('S_OR_B32', 0x11),
                ('S_OR_B64', 0x12),
                ('S_XOR_B64', 0x13),
                ('S_ANDN2_B64', 0x14),
                ('S_NAND_B64', 0x15),
                ('S_LSHL_B32', 0x16),
                ('S_LSHR_B32', 0x17),
                ('S_ASHR_I32', 0x18),
                ('S_MUL_I32', 0x19),
                ('S_BFE_I32', 0x1a)
                ]

    def genGrammarInstrClass(self):
        #return self.getInstrDefName() + " sreg ',' sreg ',' alu_expr_list ('#' lop_imm)?"
        return self.getInstrDefName() + " sreg ',' sreg ',' sreg"

    def addOperand(self, operand):
        super().addOperand(operand)
        if isinstance(operand, str):
            self.unresolved = True
            return
        self.updateOperand(len(self.operands))

    def updateOperand(self, operand_num):
        operand = self.operands[operand_num - 1]
        if operand_num == 1:
            assert(isinstance(operand, Reg))
            self.sdst = operand.idx
        elif operand_num == 2:
            assert(isinstance(operand, Reg))
            self.ssrc0 = operand.idx
        elif operand_num == 3:
            assert(isinstance(operand, Reg))
            self.ssrc1 = operand.idx

    def getInstrSize(self):
        if self.ssrc0 == 0xFF or self.ssrc1 == 0xFF:
            return self.instr_size
        else:
            return 4

class InstrSALU_SOPK(InstrSalu):
    _fields_ = [("simm16", c_uint, 16),
                ("sdst", c_uint, 7),
                ("op", c_uint, 5),
                ("enc", c_uint, 4)]

    _optable_ = [
                ('S_MOVK_I32', 0x1),
                ('S_CMPK_LE_U32', 0x2),
                ('S_ADDK_I32', 0x3),
                ('S_MULK_I32', 0x4)
                ]

    def __init__(self, name=''):
        super().__init__(name)


    def genGrammarInstrClass(self):
        return self.getInstrDefName() + " sreg ',' number"

    def addOperand(self, operand):
        super().addOperand(operand)
        if isinstance(operand, str):
            self.unresolved = True
            return
        self.updateOperand(len(self.operands))

    def updateOperand(self, operand_num):
        operand = self.operands[operand_num - 1]
        if operand_num == 1:
            assert(isinstance(operand, Reg))
            self.sdst = operand.idx
        elif operand_num == 2:
            assert(isinstance(operand, int))
            self.simm16 = operand


class InstrSALU_SOPC(InstrSalu):
    _fields_ = [("ssrc0", c_uint, 8),
                ("ssrc1", c_uint, 8),
                ("op", c_uint, 7),
                ("enc", c_uint, 9),
                ("lit_const", c_uint, 32)]

    _optable_ = [
                ('S_CMP_EQ_I32', 0x1),
                ('S_CMP_GT_I32', 0x2),
                ('S_CMP_GE_I32', 0x3),
                ('S_CMP_LT_I32', 0x4),
                ('S_CMP_LE_I32', 0x5),
                ('S_CMP_GT_U32', 0x6),
                ('S_CMP_GE_U32', 0x7),
                ('S_CMP_LE_U32', 0x8)
                ]

    def __init__(self, name=''):
        super().__init__(name)

    def genGrammarInstrClass(self):
        return self.getInstrDefName() + " sreg ',' sreg"

    def addOperand(self, operand):
        super().addOperand(operand)
        if isinstance(operand, str):
            self.unresolved = True
            return
        self.updateOperand(len(self.operands))

    def updateOperand(self, operand_num):
        operand = self.operands[operand_num - 1]
        if operand_num == 1:
            assert(isinstance(operand, Reg))
            self.ssrc0 = operand.idx
        elif operand_num == 2:
            assert(isinstance(operand, Reg))
            self.ssrc1 = operand.idx

    def getInstrSize(self):
        if self.ssrc0 == 0xFF or self.ssrc1 == 0xFF:
            return self.instr_size
        else:
            return 4

class InstrSALU_SOPP(InstrSalu):
    _fields_ = [
                ("pred", c_uint, 3),
                ("simm12", c_uint, 12),
                ("tcc", c_uint, 3),
                ("op", c_uint, 5),
                ("enc", c_uint, 9),
                ('ext',     c_uint, 28),
                ('ext_enc', c_uint, 4)]

    _optable_ = [
                ('T_CBRANCH_TCCZ', 0x0, OpType.BRANCH_OP, None),
                ('T_CBRANCH_TCCNZ', 0x1, OpType.BRANCH_OP, None),
                #('S_CBRANCH_SCC0', 0x3),
                #('S_CBRANCH_SCC1', 0x4),
                ('S_CBRANCH_SCCZ', 0x2, OpType.BRANCH_OP, None),
                ('S_CBRANCH_SCCNZ', 0x3, OpType.BRANCH_OP, None),
                ('T_CBRANCH_EXECZ', 0x4, OpType.BRANCH_OP, None),
                ('T_CBRANCH_EXECNZ', 0x5, OpType.BRANCH_OP, None),
                ('S_BRANCH', 0x8, OpType.BRANCH_OP, None),
                ('S_BARRIER', 0x9, OpType.BARRIER_OP, None),
                ('S_WAITCNT', 0xa, OpType.WAITCNT_OP, None),
                ('BAR_SYNC', 0xd, OpType.BARRIER_OP, None),
                ('S_PHI', 0xb, OpType.BRANCH_OP, None),
                ('T_EXIT', 0xc, OpType.EXIT_OP, None),
                ('T_NOP', 0xe)
                ]

    def __init__(self, name=''):
        super().__init__(name)

    def getInstrSize(self):
        if self.ext_enc != 0x0:
            return 8
        else:
            return 4

    def isBranchOp(self):
        return self.op <= self.optable['S_BRANCH'].value

    def isCBranchOp(self):
        return self.op <= self.optable['T_CBRANCH_EXECNZ'].value

    def isBarOp(self):
        return self.op == self.optable['BAR_SYNC'].value

    def updateOperand(self, operand_num):
        #pdb.set_trace()
        operand = self.operands[operand_num - 1]
        if operand_num == 1:
            if self.isBarOp():
                assert(isinstance(operand, int))
                # setup  bar_id
                self.tcc = operand
                return
            elif self.isCBranchOp():
                assert(isinstance(operand, Reg))
                assert(operand.rtype == Reg.RegType.TCC)
                self.tcc = operand.idx
            elif self.isBranchOp():
                assert(isinstance(operand, int))
                self.simm12 = operand
                if self.simm12 > common_enc["max_simm12"].value or self.simm12 < common_enc["min_simm12"].value:
                    # branch out of range
                    pdb.set_trace()
            else:
                # TODO extend tcc for s_branch target
                pdb.set_trace()
        elif operand_num == 2:
            if not isinstance(operand, int):
                pdb.set_trace()
            assert(isinstance(operand, int))
            # setup  bar_count
            if self.isBranchOp():
                self.simm12 = operand
                if self.simm12 > common_enc["max_simm12"].value or self.simm12 < common_enc["min_simm12"].value:
                    pdb.set_trace()
            elif self.isBarOp():
                if self.simm12 > common_enc["max_barcount"].value:
                    # branch out of range
                    pdb.set_trace()
                self.simm12 = operand

    def genGrammarInstrClass(self):
        #return self.getInstrDefName() + " ( (sreg_or_tcc ',')? branch_target | number | wait_expr (',' wait_expr)*)?"
        return self.getInstrDefName() + " (sreg_or_tcc ',')? (branch_target | number | wait_expr (',' wait_expr)*)?"

class InstrSMEM_SLS(InstrSmem):
    _fields_ = [("offset", c_uint, 8),
                ("imm", c_uint, 1),
                ("sbase", c_uint, 6),
                ("sdst", c_uint, 7),
                ("op", c_uint, 5),
                ("enc", c_uint, 5)]

    _optable_ = [
                ('S_LOAD_DWORD', 0x0),
                ('S_LOAD_DWORDX2', 0x1),
                ('S_LOAD_DWORDX4', 0x2),
                ('S_LOAD_DWORDX8', 0x3),
                ('S_LOAD_DWORDX16', 0x4)
                #('#S_BUFFER_LOAD_DWORD', 0x5),
                #('#S_BUFFER_LOAD_DWORDX2', 0x6),
                #('#S_BUFFER_LOAD_DWORDX4', 0x7),
                #('#S_BUFFER_LOAD_DWORDX8', 0x8),
                #('#S_BUFFER_LOAD_DWORDX16', 0x9)
                ]

    def __init__(self, name=''):
        super().__init__(name)


    def genGrammarInstrClass(self):
        return self.getInstrDefName() + " (sreg | ident) ',' sreg ',' (sreg | number) ('%' mspace_all)? "

    def addOperand(self, operand):
        super().addOperand(operand)
        if isinstance(operand, str):
            self.unresolved = True
            return
        self.updateOperand(len(self.operands))

    def updateOperand(self, operand_num):
        operand = self.operands[operand_num - 1]
        if operand_num == 1:
            assert(isinstance(operand, Reg))
            self.sdst = operand.idx
        elif operand_num == 2:
            assert(isinstance(operand, Reg))
            self.sbase = operand.idx
        elif operand_num == 3:
            if (isinstance(operand, Reg)):
                self.offset = operand.idx
                self.imm = 0
            else:
                self.offset = operand
                self.imm = 1

class InstrDMEM_DLS(InstrDmem):
    _fields_ = [("offset0", c_uint, 8),
                ("offset1", c_uint, 8),
                ("reserved", c_uint, 1),
                ("gds", c_uint, 1),
                ("op", c_uint, 8),
                ("enc", c_uint, 6),
                ("addr", c_uint, 8),
                ("data0", c_uint, 8),
                ("data1", c_uint, 8),
                ("vdst", c_uint, 8)]

    _optable_ = [
                ('D_ADD_U32', 0x1),
                ('D_INC_U32', 0x2),
                ('D_WRITE_B32', 0x3),
                ('D_WRITE2_B32', 0x4),
                ('D_WRITE_B8', 0x5),
                ('D_WRITE_B16', 0x6),
                ('D_READ_B32', 0x7),
                ('D_READ2_B32', 0x8),
                ('D_READ_I8', 0x9),
                ('D_READ_U8', 0xa),
                ('D_READ_I16', 0xb),
                ('D_READ_U16', 0xc)
                ]

    def __init__(self, name=''):
        super().__init__(name)

    def genGrammarInstrClass(self):
        return self.getInstrDefName() + " (vreg | ident | mem_expr_list) ',' mem_expr_list"

class InstrVMEM_VMUBUF(InstrVmem):
    _fields_ = [("offset", c_uint, 12),
                ("offen",  c_uint, 1),
                ("idxen",  c_uint, 1),
                ("glc",    c_uint, 1),
                ("addr64", c_uint, 1),
                ("lds",    c_uint, 1),
                ("reserved0", c_uint, 1),
                ("op",     c_uint, 7),
                ("reserved1", c_uint, 1),
                ("enc",    c_uint, 6),
                ("vaddr", c_uint, 8),
                ("vdata", c_uint, 8),
                ("srsrc", c_uint, 5),
                ("reserved2", c_uint, 1),
                ("slc",   c_uint, 1),
                ("tfe",   c_uint, 1),
                ("soffset", c_uint, 8)]

    _optable_ = [
                ('V_BUFFER_LOAD_SBYTE', 0x1),
                ('V_BUFFER_LOAD_DWORD', 0x2),
                ('V_BUFFER_STORE_SBYTE', 0x3),
                ('V_BUFFER_STORE_DWORD', 0x4),
                ('V_BUFFER_ATOMIC_ADD', 0x5)
                ]

    def __init__(self, name=''):
       super().__init__(name)

    def genGrammarInstrClass(self):
        return self.getInstrDefName() + " vreg ',' vreg ',' sreg ',' sreg"

class InstrVMEM_VLS(InstrVmem):
    _fields_ = [
                ("offset", c_uint, 7),
                ("vaddr", c_uint, 6),
                ("ssrc0_", c_uint, 1),
                ("vdata", c_uint, 6),
                ("slc",   c_uint, 1),
                ("op",    c_uint, 5),
                ("enc",   c_uint, 6),
                ('ext',     c_uint, 28),
                ('ext_enc', c_uint, 4)]

    class _fields_e1_(LittleEndianStructure):
        _pack_ = 1
        _fields_ = [("imm", c_uint, 28),
                ('ext_enc', c_uint, 4)
                ]

    class _fields_e2_(LittleEndianStructure):
        _pack_ = 1
        _fields_ = [
                ("imm", c_uint, 24),
                ("vaddr", c_uint, 2),
                ("vdata", c_uint, 2),
                ('ext_enc', c_uint, 4)
                ]

    def __init__(self, name=''):
        self.ext1 = self._fields_e1_()
        self.ext2 = self._fields_e2_()
        super().__init__(name)


    _optable_ = [
                ('V_LOAD_U8',  0x0),
                ('V_LOAD_U16',  0x1),
                ('V_LOAD_U32',  0x2),
                ('V_LOAD_U64',0x3),
                ('V_LOAD_U32X4',0x4),
                ('V_STORE_U8', 0x5, OpType.STORE_OP, None),
                ('V_STORE_U16', 0x6, OpType.STORE_OP, None),
                ('V_STORE_U32', 0x7, OpType.STORE_OP, None),
                ('V_STORE_U64', 0x8, OpType.STORE_OP, None)
                #('#FLAT_LOAD_SBYTE', 0x1),
                #('#FLAT_STORE_SBYTE', 0x3),
                #('#FLAT_ATOMIC_ADD', 0x5),
            ]

    def getInstrSize(self):
        if self.ext_enc == common_enc["ext1_enc"].value:
            self.ext = self.ext2.imm
            self.ext |= self.ext2.vaddr << 24
            self.ext |= self.ext2.vdata << 26
            return 8
        elif self.ext_enc != 0x0:
            pdb.set_trace()
        else:
            return 4

    def genGrammarInstrClass(self):
        return self.getInstrDefName() + " vreg ',' (vreg | dreg | vmem_special_operand) (',' number)? ('%' mspace_all)?"

    def isStoreOp(self):
        return self.op >= self.optable['V_STORE_DWORD'].value

    def updateOperand(self, operand_num):
        operand = self.operands[operand_num - 1]
        if operand_num == 1:
            assert(isinstance(operand, Reg))
            self.encode_vdata(operand, self.ext2)
        elif operand_num == 2:
            assert(isinstance(operand, Reg))
            if operand.rtype == Reg.RegType.Scalar:
                self.ssrc0_ = 1
            self.encode_vaddr(operand, self.ext2)
        elif operand_num == 3:
            #if (isinstance(operand, Reg)):
            #    self.offset = operand.idx
            #    self.imm = 0
            #else:
            #    self.offset = operand
            #    self.imm = 1
            assert (isinstance(operand, int))
            self.encode_vls_offset(operand, self.ext2)
            #self.offset = operand


    def addOperand(self, operand):
        super().addOperand(operand)
        if isinstance(operand, str):
            self.unresolved = True
            return
        self.updateOperand(len(self.operands))

    def addSpecialOperand(self, reg_str):
        #pdb.set_trace()
        super().addSpecialOperand(UnresolvedReg.Kind.param, reg_str)
