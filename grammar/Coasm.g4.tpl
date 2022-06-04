grammar Coasm;

prog: (line)*;

line: (directive | label | label? instruction) line_comment?;

label: ident ':';

internal_id: TID | PC;

directive:
         asm_directive
         | mem_directive
         | extend_mem_directive
         | reg_directive
         | section_directive
         | link_directive;

asm_directive:
         kernel_directive
         | decl_directive
         | inst_directive
         | align_directive
         | size_directive
         | ident_directive
         | alias_directive;

kernel_directive:
         START_KERNEL ident
         | kernel_option_item
         | END_KERNEL;

kernel_option_item:
         KERNEL_OPTION_KEY DIGIT
         ;


KERNEL_OPTION_KEY: '.' K ( E R N E L '_' O P T I O N)? '.' NAME;

decl_directive: TYPE ident ',' (DECL_FUNC | DECL_OBJECT);

inst_directive: INST HEX_NUMBER;

align_directive: P2ALIGN number (',' number)*;

size_directive: SIZE ident ',' alu_expr;

ident_directive: IDENT;

alias_directive: ALIAS ident('[' DIGIT ']')? register_;

mem_directive: MEM_SPACE DATA_TYPE ident('[' DIGIT ']')? data_expr_list? data_offset?;

extend_mem_directive:
         DATA_DIRECTIVE number
         | MEM_SPACE ident ',' number ',' number;

reg_directive: REG DATA_TYPE ident('[' DIGIT ']')? register_;

data_expr_list: number (',' number)*;

data_offset: '(' (DIGIT | HEX_NUMBER) ')';

number: ( HEX_NUMBER | FP_NUMBER | DIGIT);

// generic_reg: register_ | ident;
generic_reg: register_ ;


register_: sreg_or_tcc | vreg | dreg | lreg;

sreg: ('-' | '!')? (SREG | SREG_INDEX);

vreg: ('-' | '!')? (VREG | VREG_INDEX);

dreg: ('-' | '!')? (DREG | DREG_INDEX);

lreg: ('-' | '!')? (LREG | LREG_INDEX);

vreg_or_number: vreg | number;

generic_reg_or_number: generic_reg | number;

mspace_all: MSPACE ':' (flat_ | private_ | const_ | param_ | global_ | shared_);
mspace_global: MSPACE ':' global_;
mspace_shared: MSPACE ':' shared_;
mspace_flat: MSPACE ':' flat_;

flat_: FLAT;
private_: PRIVATE;
const_: CONST;
param_: PARAM;
global_: GLOBAL_;
shared_: SHARED_;

float_mode : ROUND_MODE | SAT_MODE;
ROUND_MODE: RM ':' ( RN | RZ);
SAT_MODE: SAT ':' ( SAT01 );

special_operand : ident ':' sreg_or_tcc;
sreg_or_tcc: sreg | tcc;

// use in VOPC
special_cc_reg: sreg | tcc;

vmem_special_operand : ident;

branch_target : ident;

builtin_operand : ident;

tcc:  TCC;

section_directive: section_name (',' section_modifier)*;

section_name: (PREDEF_SECTION | SECTION) PREDEF_SECTION? ('"'? '.' NAME '"'?)?;

section_modifier: ('#' | '@' | '"')? (NAME | DIGIT) '"'?;

link_directive: EXTERN ident | VISIBLE ident;

instruction: {{InstrFmtList}} ;

alu_expr_list
         : register_
         | alu_expr (',' alu_expr)*
         | FP_NUMBER
         | HEX_NUMBER
         ;

alu_expr
         : alu_multiply_expr (SIGN alu_multiply_expr)*
         ;

alu_multiply_expr
         : alu_argument (MSIGN alu_argument)*
         ;

alu_argument
         : DIGIT | ident | internal_id
         | '(' alu_expr ')'
         ;

lop_imm
         : DIGIT | HEX_NUMBER
         ;

{% for instr_class in instr_class_list %}
{{instr_class.name}}:
		{{instr_class.value}};
{% endfor %}


mem_expr_list: '[' mem_expr (SIGN mem_expr)* ']';

mem_expr: mem_off | mem_idx_expr;

mem_off: DIGIT | HEX_NUMBER | ident | sreg | vreg;

mem_idx_expr: mem_idx MSIGN mem_stride;

mem_idx: vreg | ident | TID | ('(' (vreg | ident) SIGN TID ')');

mem_stride: DIGIT | HEX_NUMBER;

mem_base: register_ | ident;

fragment ATM_OP:
     A T M '.' (
       A D D
     | S U B
         | M I N
         | M A X
         | A N D
         | O R
         | X O R
         | I N C
         | D E C
         | S W A P
         | C A S ) ATM_MOD?;

      fragment LDST_OP: ( L D | S T ) ('.' T S M)? LDST_MOD* ('.' B U L K)?;

fragment MODIFIER: ATM_MOD | LDST_MOD;

fragment ATM_MOD: '.' (R D C | R T N);

fragment LDST_MOD: '.' (K P ('0' .. '5') | G A);

fragment E32: '_' E '3' '2';

ALIAS: '.' A L I A S;
REG: '.' R E G;

TID: '%' T I D;
PC: '%' P C;

LREG: L (R E G)? DIGIT;

LREG_INDEX: L (R E G)? '[' DIGIT ':' DIGIT ']';

DREG: D (R E G)? DIGIT;

DREG_INDEX: D (R E G)? '[' DIGIT ':' DIGIT ']';

VREG: V (R E G)? DIGIT;

VREG_INDEX: V (R E G)? '[' DIGIT ':' DIGIT ']';

SREG: S (R E G)? DIGIT;

SREG_INDEX: S (R E G)? '[' DIGIT ':' DIGIT ']';

TCC: T (C C)? DIGIT;

FLAT: F L A T;

PRIVATE: P R I V A T E;

CONST: C O N S T;

PARAM: P A R A M;

GLOBAL_: G L O B A L;

SHARED_: S H A R E D;

RM: R M;
RN: R N;
RZ: R Z;
SAT: S A T;
SAT01: S A T '0' '1';

MSPACE: 'mspace';

comment: COMMENT;
line_comment: LINE_COMMENT;

{% for instr in instr_def_list %}
{{instr.name}}:
		{{instr.value}};
{% endfor %}

wait_expr: WAIT_TYPE ('(' DIGIT ')')?;

WAIT_TYPE:
         ((S M E M | V M E M | T S M) '_' (L D)? (S T)? ('_' T S M)?)
         | (V L D | V S T | S L D | S S T | T S M | V T S M) C N T
         | (C O M M I T OP_SP G R O U P);

fragment BR_COND: A O | A Z | N Z;

COMMENT:   '/*' .*? '*/' -> skip;

LINE_COMMENT: (';' | '//') ~ [\r\n]* -> skip;

// ID  : IDNAME;

ident : NAME;

fragment IDNAME: (H_PREFIX | L_PREFIX)? [_a-zA-Z] [a-zA-Z0-9._@-]*;

NAME: (H_PREFIX | L_PREFIX)? [_a-zA-Z] [a-zA-Z0-9._@-]*;

fragment H_PREFIX: '.' H (I D D E N)? '.';

fragment L_PREFIX: '.' L F U N C;

MEM_SPACE: '.' (SHARED | GLOBAL);

DATA_DIRECTIVE: '.' (ZERO | BYTE | SHORT | LONG | QUAD);

START_KERNEL: '.' KERNEL;

END_KERNEL: '.' E N D '_' KERNEL;


fragment CMP_FMT: '.' (O | U)? ( E Q | L T | G T | L E | G E | N E | (F P OP_SP C L A S S));

DATA_TYPE:
         '.' (
                 ((I | U | B) ('32' | '24' | '64'))
                 | ((F | (T F)) '32')
                 | ((I | U | B | F | (B F)) '16' (X '2')?)
                 | ((I | U | B) '8' (X '2')?)
                 | (B '32' X ('2' | '4' | '8' | '16'))
         ) ('*')?;

DIGIT: ('-')?('0' .. '9')+;

HEX_NUMBER: ('0' X) [0-9a-fA-F]+;

SIGN: '+' | '-';

MSIGN: '*' | '/';

WS: [ \t\r\n\u000C]+ -> skip;

TODO: T O D O;

fragment SHARED: S H A R E D;

fragment GLOBAL: G L O B A L;

fragment ZERO: Z E R O;

fragment BYTE: B Y T E;

fragment SHORT: S H O R T;

fragment LONG: L O N G;

fragment QUAD: Q U A D;

TYPE: '.' T Y P E;

INST: '.' I N S T;

P2ALIGN: '.' P '2' A L I G N (W | L)?;

SIZE: '.' S I Z E;

FUNC_END: '.' L F U N C '_' E N D ('0' .. '9')+;

IDENT: '.ident' ~ [\r\n]* -> skip;

DECL_FUNC: '@function';

DECL_OBJECT: '@object';

FP_NUMBER: ('-')?(('0' .. '9')+ '.' ('0' .. '9')* Exponent?
         | '.' ('0' .. '9')+ Exponent?
         | ('0' .. '9')+ Exponent);

EXTERN: '.' E X T E R N;

VISIBLE: '.' (V I S I B L E | G L O B L | W E A K);

PREDEF_SECTION: '.' B S S | '.' (R O)? D A T A | '.' T E X T;

SECTION: '.' S E C T I O N;

fragment OP_SP: ('.' | '_');

fragment KERNEL: K E R N E L;

fragment Exponent: ('e' | 'E') ('+' | '-')? ('0' .. '9')+;

fragment A: ('a' | 'A');

fragment B: ('b' | 'B');

fragment C: ('c' | 'C');

fragment D: ('d' | 'D');

fragment E: ('e' | 'E');

fragment F: ('f' | 'F');

fragment G: ('g' | 'G');

fragment H: ('h' | 'H');

fragment I: ('i' | 'I');

fragment J: ('j' | 'J');

fragment K: ('k' | 'K');

fragment L: ('l' | 'L');

fragment M: ('m' | 'M');

fragment N: ('n' | 'N');

fragment O: ('o' | 'O');

fragment P: ('p' | 'P');

fragment Q: ('q' | 'Q');

fragment R: ('r' | 'R');

fragment S: ('s' | 'S');

fragment T: ('t' | 'T');

fragment U: ('u' | 'U');

fragment V: ('v' | 'V');

fragment W: ('w' | 'W');

fragment X: ('x' | 'X');

fragment Y: ('y' | 'Y');

fragment Z: ('z' | 'Z');
