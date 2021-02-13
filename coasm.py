from enum import Enum
from collections import OrderedDict
from collections import namedtuple
from jinja2 import Template
import pdb

MAX_SREG_NUM = 255
MAX_USER_SREG_NUM = 220
MAX_VREG_NUM = 255

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


class SpecialREG(Enum):
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
    def __init__(self, reg_str):
        self.is_neg = False
        self.reg_name = None
        self.idx = None
        self.end_idx = None
        start_pos = 0
        print("INFO: reg str:" + reg_str)
        if reg_str[0] == '-' or reg_str[0] == '!':
            self.is_neg = True
            start_pos = 1
        reg_str = reg_str[start_pos:]
        super().__init__(reg_str)
        idx_pos = reg_str.find("[")
        if idx_pos > 0:
            colon_pos = reg_str.find(":")
            end_idx_pos = reg_str.find("]")
            self.reg_name = reg_str[0:idx_pos]
            self.idx = int(reg_str[idx_pos+1:colon_pos])
            self.end_idx = int(reg_str[colon_pos+1:end_idx_pos])
        else:
            # here we assume reg name is s|v or s|vreg
            if reg_str[1].isdigit():
                idx_pos = 1
            elif reg_str[4].isdigit():
                idx_pos = 4
            else:
                assert("Invalid Reg str")
            self.reg_name = reg_str[0:idx_pos]
            self.idx = int(reg_str[idx_pos:])
            self.end_idx = self.idx
        if reg_str[0] == "s":
            self.rtype = Reg.RegType.Scalar
        elif reg_str[0] == "v":
            self.rtype = Reg.RegType.Vector
        else:
            assert("invalid reg name")

        self.alias = None
        self.reloc_type = VariableSymbol.RelocType.Normal

    def __str__(self):
        if self.end_idx is not None:
            return "{}[{}:{}]".format( "sreg" if self.rtype is Reg.RegType.Scalar else "vreg", self.idx, self.end_idx)
        else:
            return "{}{}".format( "sreg" if self.rtype is Reg.RegType.Scalar else "vreg", self.idx)

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

class InstrField:
    class TypeEnum(Enum):
        UINT = 0
        INT = 1
        STRUCT = 2
        UNION = 3

    def __init__(self, name="", type=TypeEnum.UINT):
        self.name = name
        self.msb = 0
        self.lsb = 0
        self.type =  TypeEnum.UINT
        self.child = []

class VisitType(Enum):
    GRAMMAR_INSTR_FMT = 1
    GRAMMAR_INSTR_DEF = 2
    GEN_INSTR_FMT_DEF = 3
    GEN_INSTR_FMT_FIELD = 4
    GEN_INSTR_OP_ENUM_DEF = 5
    GEN_INSTR_DEF = 6


class Instr:
    FmtEnc = namedtuple('FmtEnc', ['bit_start', 'width', 'value'])
    fmt_enc = {}
    fmt_enc["VOP2"] = FmtEnc(31, 1,  0b0)
    fmt_enc["VOP1"] = FmtEnc(31, 7, 0b1000001)
    fmt_enc["VOPC"] = FmtEnc(31, 7, 0b1000000)
    fmt_enc["VOP3A"] =FmtEnc(31, 6, 0b100001)
    fmt_enc["SOP1"] = FmtEnc(31, 9, 0b100001)
    fmt_enc["SOP2"] = FmtEnc(31, 2, 0b11)
    fmt_enc["SOPK"] = FmtEnc(31, 4, 0b1001)
    fmt_enc["SOPC"] = FmtEnc(31, 9, 0b1001)
    fmt_enc["SOPP"] = FmtEnc(31, 9, 0b1001)
    fmt_enc["SMRD"] = FmtEnc(31, 5, 0b10001)
    fmt_enc["DS"] =   FmtEnc(31, 6, 0b101000)
    fmt_enc["MUBUF"] =FmtEnc(31, 6, 0b101001)
    fmt_enc["FLAT"] = FmtEnc(31, 6, 0b101010)

    def __init__(self, name=''):
        #super().__init__(name)
        self.opcode = None
        #self.has_imm = False
        self.imm = None
        self.lop_imm = None
        self.stride_imm = 0
        self.branch_cond = 0
        self.pos = 0
        self.flags = {}
        self.encoded_inst = 0
        self.is_encoded = False
        self.fmt_dst = 0
        self.fmt_src = 0
        self.stride_pos = 0
        self.regs = []
        self.operands = []
        self.dst_reg = None
        self.name = name       # in fact it is line number
        self.instr_str = None
        self.func_name = None
        if hasattr(self, "field"):
            for n,v in self.field.items():
                setattr(self, n, 0)
        print("[instr create info] create instr with op {}".format(name))
        if name == "":
            print("Warn:create instr without correct op enum")
        else:
            self.enc = fmt_enc[self.getFmtName()].value
            self.op = self.OpcodeEnum[name.upper()].value


    def addOperand(self, operand):
        if (isinstance(operand, int)):
            self.setImm(operand)
        self.operands.append(operand)

    def addReg(self, reg: Reg):
        if self.dst_reg is None:
            self.dst_reg = reg
        self.regs.append(reg)
        self.addOperand(reg)

    def setImm(self, imm):
        self.imm = imm

    def setLopImm(self, lop_imm):
        self.lop_imm = lop_imm

    def setStrideImm(self, stride_imm):
        self.stride_imm = stride_imm

    def setFlag(self, *name):
        for n in name:
            self.flags[n] = True

    def getFmtName(self):
        _, fmt = self.__class__.__name__.split('_')
        return fmt

    def getInstrDefName(self):
        instr_def = self.__class__.__name__.replace('Instr', "")
        #print("GetInstrDef" + instr_def)
        return instr_def

    def getCppFmtDef(self):
        instr_encode = "\nBytes" + self.getFmtName() + " " + self.getFmtName() + ";"
        return instr_encode

    def getCppFieldEncode(self):
        instr_encode = "\nstruct Bytes" + self.getFmtName() +  " {\n" + \
        "\n".join(["uint32_t {} : {};".format(n, v) for n,v in self.field.items()]) + "};"
        return instr_encode

    def getCppInstrAsm(self):
        bit_count = 0
        instr = "bytes." + self.getFmtName() + "= {"
        value = []
        for n,v in self.field.items():
            bit_count += v
            value.append(str(getattr(self, n)))
        instr += ','.join(value)
        instr += "};"
        instr += "code.push_back(bytes.word[0]);"
        if bit_count > 32:
            instr += "code.push_back(bytes.word[1]);"
        return instr

    def getFlag(self, name):
        if name in flags:
            return self.flags[name];
        else:
            return False

    def getInputDataType(self):
        pass

    def genInstrAsm(self, f):
        f.write("{}\n".format(self.getCppInstrAsm()))

    def getOpcodeEnumList(self):
        opcode_list = OrderedDict()
        for op in self.OpcodeEnum:
            opcode_list[op.name] = hex(op.value)
        return opcode_list

    def genInstrDef(self, visit_type, f):
        if visit_type == VisitType.GEN_INSTR_FMT_DEF:
            f.write(self.getCppFmtDef())
        elif visit_type == VisitType.GEN_INSTR_FMT_FIELD:
            f.write(self.getCppFieldEncode())
        elif visit_type == VisitType.GEN_INSTR_OP_ENUM_DEF:
            opcode_list = self.getOpcodeEnumList()
            for n, v in opcode_list:
                f.write("{} = {}".format(n, v))
        elif visit_type == VisitType.GEN_INSTR_DEF:
            pass

    def __str__(self):
        if self.instr_str is not None:
            return self.instr_str
        instr_str = self.name + " "
        #if self.dst_reg is not None:
        #    instr_str += self.dst_reg.__str__()
        for operand in self.operands:
            #if isinstance(operand, Reg):
            instr_str += " " + format(operand.__str__())
        return instr_str

    @classmethod
    def getInstrFmtList(cls):
        return " | ".join([subcls.__name__.lower() for subcls in __class__.__subclasses__()])

    @classmethod
    def getInstrClassList(cls):
        instr_class = []
        for subcls in __class__.__subclasses__():
            print("InInstrClass: {} visit {}".format(cls.__name__, subcls.__name__))
            subcls.visitSubClass(VisitType.GRAMMAR_INSTR_FMT, instr_class)
        return instr_class

    @classmethod
    def getInstrDefList(cls):
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
            sub = subcls()
            if cls.__name__ == subcls.__name__:
                continue
            print("InSubClass visit_type {}: {} visit {}".format(visit_type, cls.__name__, subcls.__name__))
            if visit_type == VisitType.GRAMMAR_INSTR_DEF:
                tmp.append(sub.genGrammarInstrDef(f))
            elif visit_type == VisitType.GRAMMAR_INSTR_FMT:
                tmp.append(sub.genGrammarInstrClass())
            else:
                sub.genInstrDef(visit_type, f)
        if visit_type == VisitType.GRAMMAR_INSTR_FMT:
            f.append({"name": cls.__name__.lower(), "value": "\n         | ".join(tmp)})


    def genGrammarInstrDef(self, f):
        tmp = [utilReplace(" ".join(list(op.name))) for op in self.OpcodeEnum]
        op_list = "(" + "\n         | ".join(tmp) + ") E32?"
        f.append({"name": self.getInstrDefName(), "value": op_list})
        return



#------------------------------
class InstrValu(Instr):
    def __init__(self, name=''):
        super().__init__(name)

    #@classmethod
    #def visitSubClass(cls, visit_type, f):
    #    for subcls in __class__.__subclasses__():
    #        sub = subcls()
    #        print("{} visit {}".format(cls.__name__, subcls.__name__))
    #        if visit_type == VisitType.GRAMMAR_INSTR_FMT:
    #            sub.genInstrDef(visit_type, f)
    #        elif visit_type == VisitType.GEN_INSTR_DEF:
    #            sub.genInstrDef(visit_type, f)


class InstrSalu(Instr):
    def __init__(self, name=''):
        super().__init__(name)

    #@classmethod
    #def visitSubClass(cls, visit_type, f):
    #    for subcls in __class__.__subclasses__():
    #        print("{} visit {}".format(cls.__name__, subcls.__name__))
    #        sub = subcls()
    #        sub.genInstrDef(visit_type, f)

class InstrSmem(Instr):
    def __init__(self, name=''):
        super().__init__(name)

    #@classmethod
    #def visitSubClass(cls, visit_type, f):
    #    for subcls in __class__.__subclasses__():
    #        sub = subcls()
    #        print("{} visit {}".format(cls.__name__, subcls.__name__))
    #        sub.genInstrDef(visit_type, f)


class InstrVmem(Instr):
    def __init__(self, name=''):
        super().__init__(name)

    #@classmethod
    #def visitSubClass(cls, visit_type, f):
    #    for subcls in __class__.__subclasses__():
    #        sub = subcls()
    #        print("{} visit {}".format(cls.__name__, subcls.__name__))
    #        sub.genInstrDef(visit_type, f)

class InstrDmem(Instr):
    def __init__(self, name=''):
        super().__init__(name)

    #@classmethod
    #def visitSubClass(cls, visit_type, f):
    #    for subcls in __class__.__subclasses__():
    #        sub = subcls()
    #        print("{} visit {}".format(cls.__name__, subcls.__name__))
    #        sub.genInstrDef(visit_type, f)


#------------------------------
class InstrVALU_VOP2(InstrValu):
    def __init__(self, name=''):
        self.field = OrderedDict()
        self.field["src0"]  = 9
        self.field["vsrc1"] = 8
        self.field["vdst"]  = 8
        self.field["op"]    = 6
        self.field["enc"]        = 1
        self.field["lit_const"]  = 32
        super().__init__(name)

    class OpcodeEnum(Enum):
        V_CNDMASK_B32              = 0x0
        V_ADD_F32                  = 0x1
        V_AND_F32                  = 0x2
        V_SUB_F32                  = 0x3
        V_SUBREV_F32               = 0x4
        V_MUL_F32                  = 0x5
        V_MUL_I32_I24              = 0x6
        V_MIN_F32                  = 0x7
        V_MAX_F32                  = 0x8
        V_MIN_I32                  = 0x9
        V_MAX_I32                  = 0x10
        V_MIN_U32                  = 0x11
        V_MAX_U32                  = 0x12
        V_LSHRREV_B32              = 0x13
        V_ASHRREV_I32              = 0x14
        V_LSHL_B32                 = 0x15
        V_LSHLREV_B32              = 0x16
        V_AND_B32                  = 0x17
        V_OR_B32                   = 0x18
        V_XOR_B32                  = 0x19
        V_BFM_B32                  = 0x20
        V_MAC_F32                  = 0x21
        V_MADMK_F32                = 0x22
        V_ADD_I32                  = 0x23
        V_SUB_I32                  = 0x24
        V_SUBREV_I32               = 0x25
        V_CVT_PKRZ_F16_F32         = 0x26

    def genGrammarInstrClass(self):
        return self.getInstrDefName() + " generic_reg (',' generic_reg)? ',' alu_expr_list ('#' lop_imm)?"



class InstrVALU_VOP1(InstrValu):
    def __init__(self, name=''):
        self.field = OrderedDict()
        self.field["src0"]  = 9
        self.field["op"]    = 8
        self.field["vdst"]  = 8
        self.field["enc"]         = 7
        self.field["lit_const"]   = 32
        super().__init__(name)

    class OpcodeEnum(Enum):
        V_NOP                         = 0x1
        V_MOV_B32                     = 0x2
        V_READFIRSTLANE_B32           = 0x3
        V_CVT_I32_F64                 = 0x4
        V_CVT_F64_I32                 = 0x5
        V_CVT_F32_U32                 = 0x6
        V_CVT_U32_F32                 = 0x7
        V_CVT_I32_F32                 = 0x8
        V_CVT_F32_F64                 = 0x9
        V_CVT_F64_F32                 = 0xa
        V_CVT_F64_U32                 = 0xb
        V_TRUNC_F32                   = 0xc
        V_FLOOR_F32                   = 0xd
        V_LOG_F32                     = 0xe
        V_RCP_F32                     = 0xf
        V_RSQ_F32                     = 0x10
        V_RCP_F64                   = 0x11
        V_RSQ_F64                   = 0x12
        V_SQRT_F32                  = 0x13
        V_SIN_F32                   = 0x14
        V_COS_F32                   = 0x15
        V_NOT_B32                   = 0x16
        V_FFBH_U32                  = 0x17
        V_FRACT_F64                 = 0x18
        V_MOVRELD_B32                 = 0x19
        V_MOVRELS_B32                 = 0x1a

    def genGrammarInstrClass(self):
        return self.getInstrDefName() + " generic_reg ',' alu_expr_list"


class InstrVALU_VOPC(InstrValu):
    def __init__(self, name=''):
        self.field = OrderedDict()
        self.field["src0"]  = 9
        self.field["vsrc1"]  = 8
        self.field["op"]    = 8
        self.field["enc"]         = 7
        self.field["lit_const"]   = 32
        super().__init__(name)

    class OpcodeEnum(Enum):
        V_CMP_LT_F32                = 0x1
        V_CMP_GT_F32                = 0x2
        V_CMP_GE_F32                = 0x3
        V_CMP_NGT_F32               = 0x4
        V_CMP_NEQ_F32               = 0x5
        V_CMP_LT_F62                = 0x6
        V_CMP_EQ_F62                = 0x7
        V_CMP_LE_F62                = 0x8
        V_CMP_GT_F62                = 0xa
        V_CMP_NGE_F62               = 0xb
        V_CMP_NEQ_F62               = 0xc
        V_CMP_NLT_F62               = 0xd
        V_CMP_LT_I32                = 0xe
        V_CMP_EQ_I32                = 0xf
        V_CMP_LE_I32                = 0x10
        V_CMP_GT_I32                = 0x11
        V_CMP_NE_I32                = 0x12
        V_CMP_GE_I32                = 0x13
        V_CMP_CLASS_F64             = 0x14
        V_CMP_LT_U32                = 0x15
        V_CMP_EQ_U32                = 0x16
        V_CMP_LE_U32                = 0x17
        V_CMP_GT_U32                = 0x18
        V_CMP_NE_U32                = 0x19
        V_CMP_GE_U32                = 0x1a

    def genGrammarInstrClass(self):
        return self.getInstrDefName() + " generic_reg ',' alu_expr_list"

class InstrVALU_VOP3A(InstrValu):
    def __init__(self, name=''):
        self.field = OrderedDict()
        self.field["vdst"]      = 8
        self.field["abs"]       = 3
        self.field["clamp"]     = 1
        self.field["reserved"]  = 5
        self.field["op"]        = 9
        self.field["enc"]       = 6
        self.field["src0"]      = 9
        self.field["src1"]      = 9
        self.field["src2"]      = 9
        self.field["omod"]      = 2
        self.field["neg"]       = 3
        super().__init__(name)

    class OpcodeEnum(Enum):
        V_CNDMASK_B32_VOP3A     = 0x1
        V_ADD_F32_VOP3A         = 0x2
        V_SUBREV_F32_VOP3A      = 0x3
        V_MUL_F32_VOP3A         = 0x4
        V_MUL_I32_I24_VOP3A     = 0x5
        V_MAX_F32_VOP3A         = 0x6
        V_MAD_F32               = 0x7
        V_MAD_U32_U24           = 0x8
        V_BFE_U32               = 0x9
        V_BFE_I32               = 0xa
        V_BFI_B32               = 0xb
        V_FMA_F32               = 0xc
        V_FMA_F64               = 0xd
        V_ALIGNBIT_B32          = 0xe
        V_MAX3_I32              = 0xf
        V_DIV_FIXUP_F64         = 0x10
        V_LSHL_B64              = 0x11
        V_ASHR_I64              = 0x12
        V_MIN_F64               = 0x13
        V_MAX_F64               = 0x14
        V_MUL_LO_U32            = 0x15
        V_MUL_HI_U32            = 0x16
        V_MUL_LO_I32            = 0x17

    def genGrammarInstrClass(self):
        return self.getInstrDefName() + " generic_reg ',' generic_reg ',' generic_reg ',' alu_expr_list ('#' lop_imm)?"

 #------------------------------
class InstrSALU_SOP1(InstrSalu):
    def __init__(self, name=''):
        self.field = OrderedDict()
        self.field["ssrc0"] = 8
        self.field["op"] = 8
        self.field["sdst"] = 7
        self.field["enc"] = 9
        self.field["lit_const"] = 32
        super().__init__(name)

    class OpcodeEnum(Enum):
        S_MOV_B32                = 0x3
        S_MOV_B64                = 0x4
        S_NOT_B32                = 0x7
        S_WQM_B64                = 0x11
        S_SWAPPC_B64             = 0x12
        S_AND_SAVEEXEC_B64       = 0x13

    def genGrammarInstrClass(self):
        return self.getInstrDefName() + " generic_reg ',' alu_expr_list ('#' lop_imm)"


class InstrSALU_SOP2(InstrSalu):
    def __init__(self, name=''):
        self.field = OrderedDict()
        self.field["ssrc0"] = 8
        self.field["ssrc1"] = 8
        self.field["sdst"] = 7
        self.field["op"] = 7
        self.field["enc"] = 2
        self.field["lit_const"] = 32
        super().__init__(name)

    class OpcodeEnum(Enum):
        S_ADD_U32                = 0x1
        S_ADD_I32                = 0x2
        S_SUB_I32                = 0x3
        S_MIN_U32                = 0x4
        S_MAX_I32                = 0x5
        S_MAX_U32                = 0x6
        S_CSELECT_B32            = 0x7
        S_AND_B32                = 0x8
        S_AND_B64                = 0x10
        S_OR_B32                = 0x11
        S_OR_B64                = 0x12
        S_XOR_B64                = 0x13
        S_ANDN2_B64                = 0x14
        S_NAND_B64                = 0x15
        S_LSHL_B32                = 0x16
        S_LSHR_B32                = 0x17
        S_ASHR_I32                = 0x18
        S_MUL_I32                = 0x19
        S_BFE_I32                = 0x1a

    def genGrammarInstrClass(self):
        return self.getInstrDefName() + " generic_reg ',' generic_reg ',' alu_expr_list ('#' lop_imm)?"


class InstrSALU_SOPK(InstrSalu):
    def __init__(self, name=''):
        self.field = OrderedDict()
        self.field["simm16"] = 16
        self.field["sdst"] = 7
        self.field["op"] = 5
        self.field["enc"] = 4
        super().__init__(name)

    class OpcodeEnum(Enum):
        S_MOVK_I32                = 0x1
        S_CMPK_LE_U32             = 0x2
        S_ADDK_I32                = 0x3
        S_MULK_I32                = 0x4

    def genGrammarInstrClass(self):
        return self.getInstrDefName() + " generic_reg ',' number"

class InstrSALU_SOPC(InstrSalu):
    def __init__(self, name=''):
        self.field = OrderedDict()
        self.field["ssrc0"] = 8
        self.field["ssrc1"] = 8
        self.field["op"] = 7
        self.field["enc"] = 9
        self.field["li_const"] = 32
        super().__init__(name)

    class OpcodeEnum(Enum):
        S_CMP_EQ_I32                = 0x1
        S_CMP_GT_I32                = 0x2
        S_CMP_GE_I32                = 0x3
        S_CMP_LT_I32                = 0x4
        S_CMP_LE_I32                = 0x5
        S_CMP_GT_U32                = 0x6
        S_CMP_GE_U32                = 0x7
        S_CMP_LE_U32                = 0x8

    def genGrammarInstrClass(self):
        return self.getInstrDefName() + " generic_reg ',' generic_reg"

class InstrSALU_SOPP(InstrSalu):
    def __init__(self, name=''):
        self.field = OrderedDict()
        self.field["simm16"] = 16
        self.field["op"] = 7
        self.field["enc"] = 9
        super().__init__(name)

    class OpcodeEnum(Enum):
        S_EXIT                  = 0x1
        S_BRANCH                = 0x2
        S_CBRANCH_SCC0          = 0x3
        S_CBRANCH_SCC1          = 0x4
        S_CBRANCH_VCCZ          = 0x5
        S_CBRANCH_VCCNZ         = 0x6
        S_CBRANCH_EXECZ         = 0x7
        S_CBRANCH_EXECNZ        = 0x8
        S_BARRIER               = 0x9
        S_WAITCNT               = 0xa
        S_PHI                   = 0xb

    def genGrammarInstrClass(self):
        return self.getInstrDefName() + " (number | wait_expr (',' wait_expr)*)?"

class InstrSMEM_SMRD(InstrSmem):
    def __init__(self, name=''):
        self.field = OrderedDict()
        self.field["offset"] = 8
        self.field["imm"]    = 1
        self.field["sbase"]  = 6
        self.field["sdst"]   = 7
        self.field["op"]  = 5
        self.field["enc"]  = 5
        super().__init__(name)

    class OpcodeEnum(Enum):
        S_LOAD_DWORDX2                = 0x1
        S_LOAD_DWORDX4                = 0x2
        S_LOAD_DWORDX8                = 0x3
        S_LOAD_DWORDX16               = 0x4
        S_BUFFER_LOAD_DWORD           = 0x5
        S_BUFFER_LOAD_DWORDX2         = 0x6
        S_BUFFER_LOAD_DWORDX4         = 0x7
        S_BUFFER_LOAD_DWORDX8         = 0x8
        S_BUFFER_LOAD_DWORDX16        = 0x9

    def genGrammarInstrClass(self):
        return self.getInstrDefName() + " (sreg | ident) ',' sreg ',' (sreg | number)"

    def addOperand(self, operand):
        super().addOperand(operand)
        if len(self.operands) == 1:
            assert(isinstance(operand, Reg))
            self.sdst = operand.idx
        elif len(self.operands) == 2:
            assert(isinstance(operand, Reg))
            self.sbase = operand.idx
        elif len(self.operands) == 3:
            if (isinstance(operand, Reg)):
                self.offset = operand.idx
                self.imm = 0
            else:
                self.offset = operand
                self.imm = 1

class InstrDMEM_DS(InstrDmem):
    def __init__(self, name=''):
        self.field = OrderedDict()
        self.field["offset0"] = 8
        self.field["offset1"] = 8
        self.field["reserved"] = 1
        self.field["gds"]    = 1
        self.field["op"]    = 8
        self.field["enc"]   = 6
        self.field["addr"]  = 8
        self.field["data0"]  = 8
        self.field["data1"]  = 8
        self.field["vdst"]  = 8
        super().__init__(name)

    class OpcodeEnum(Enum):
        DS_ADD_U32                = 0x1
        DS_INC_U32                = 0x2
        DS_WRITE_B32              = 0x3
        DS_WRITE2_B32             = 0x4
        DS_WRITE_B8               = 0x5
        DS_WRITE_B16              = 0x6
        DS_READ_B32               = 0x7
        DS_READ2_B32              = 0x8
        DS_READ_I8                = 0x9
        DS_READ_U8                = 0xa
        DS_READ_I16               = 0xb
        DS_READ_U16               = 0xc

    def genGrammarInstrClass(self):
        return self.getInstrDefName() + " (vreg | ident | mem_expr_list) ',' mem_expr_list"

class InstrVMEM_MUBUF(InstrVmem):
    def __init__(self, name=''):
        self.field = OrderedDict()
        self.field["offset"]     = 12
        self.field["offen"]      = 1
        self.field["idxen"]      = 1
        self.field["glc"]        = 1
        self.field["addr64"]     = 1
        self.field["lds"]        = 1
        self.field["reserved0"]  = 1
        self.field["op"]         = 7
        self.field["reserved1"]  = 1
        self.field["enc"]        = 6
        self.field["vaddr"]      = 8
        self.field["vdata"]      = 8
        self.field["srsrc"]      = 5
        self.field["reserved2"]  = 1
        self.field["slc"]        = 1
        self.field["tfe"]        = 1
        self.field["soffet"]     = 8
        super().__init__(name)

    class OpcodeEnum(Enum):
        BUFFER_LOAD_SBYTE                = 0x1
        BUFFER_LOAD_DWORD                = 0x2
        BUFFER_STORE_SBYTE               = 0x3
        BUFFER_STORE_DWORD               = 0x4
        BUFFER_ATOMIC_ADD                = 0x5


    def genGrammarInstrClass(self):
        return self.getInstrDefName() + " vreg ',' vreg ',' sreg ',' sreg"

class InstrVMEM_FLAT(InstrVmem):
    def __init__(self, name=''):
        self.field = OrderedDict()
        self.field["offset"]     = 12
        self.field["offen"]      = 1
        self.field["idxen"]      = 1
        self.field["glc"]        = 1
        self.field["addr64"]     = 1
        self.field["lds"]        = 1
        self.field["reserved0"]  = 1
        self.field["op"]         = 7
        self.field["reserved1"]  = 1
        self.field["enc"]        = 6
        self.field["vaddr"]      = 8
        self.field["vdata"]      = 8
        self.field["srsrc"]      = 5
        self.field["reserved2"]  = 1
        self.field["slc"]        = 1
        self.field["tfe"]        = 1
        self.field["soffet"]     = 8
        super().__init__(name)

    class OpcodeEnum(Enum):
        FLAT_LOAD_SBYTE                = 0x1
        FLAT_LOAD_DWORD                = 0x2
        FLAT_STORE_SBYTE               = 0x3
        FLAT_STORE_DWORD               = 0x4
        FLAT_ATOMIC_ADD                = 0x5


    def genGrammarInstrClass(self):
        return self.getInstrDefName() + " vreg ',' vreg"


