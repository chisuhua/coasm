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

number: DIGIT | HEX_NUMBER | FP_NUMBER;

// generic_reg: register_ | ident;
generic_reg: register_ ;


register_: sreg | vreg | dreg | lreg;

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

instruction: instrvalu | instrsalu | instrsmem | instrvmem | instrdmem ;

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


instrvalu:
		VALU_VOP2 vreg ',' vreg ',' generic_reg_or_number (',' special_operand)*
         | VALU_VOP1 vreg ',' (generic_reg_or_number | builtin_operand)
         | VALU_VOPC sreg_or_tcc ',' vreg ',' generic_reg
         | VALU_VOP3A vreg ',' generic_reg ',' generic_reg ',' generic_reg
         | VALU_VOP3B vreg ',' generic_reg_or_number ',' vreg (',' special_operand)* ;

instrsalu:
		SALU_SOP1 sreg_or_tcc ',' sreg_or_tcc
         | SALU_SOP2 sreg ',' sreg ',' sreg
         | SALU_SOPK sreg ',' number
         | SALU_SOPC sreg ',' sreg
         | SALU_SOPP ( (sreg_or_tcc ',')? branch_target | number | wait_expr (',' wait_expr)*)?;

instrsmem:
		SMEM_SLS (sreg | ident) ',' sreg ',' (sreg | number) ('%' mspace_all)? ;

instrvmem:
		VMEM_VMUBUF vreg ',' vreg ',' sreg ',' sreg
         | VMEM_VLS vreg ',' (vreg | dreg | vmem_special_operand) ',' (vreg | dreg | number) ('%' mspace_all)?;

instrdmem:
		DMEM_DLS (vreg | ident | mem_expr_list) ',' mem_expr_list;



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

MSPACE: 'mspace';

comment: COMMENT;
line_comment: LINE_COMMENT;


VALU_VOP2:
		(V '_' C N D M A S K '_' B '3' '2'
         | V '_' A D D '_' F '3' '2'
         | V '_' S U B '_' F '3' '2'
         | V '_' S U B R E V '_' F '3' '2'
         | V '_' M U L '_' F '3' '2'
         | V '_' M U L '_' I '3' '2' '_' I '2' '4'
         | V '_' M U L L O '_' I '3' '2' '_' I '3' '2'
         | V '_' M U L '_' I '6' '4' '_' I '3' '2'
         | V '_' M I N '_' F '3' '2'
         | V '_' M A X '_' F '3' '2'
         | V '_' M I N '_' I '3' '2'
         | V '_' M A X '_' I '3' '2'
         | V '_' M I N '_' U '3' '2'
         | V '_' M A X '_' U '3' '2'
         | V '_' L S H R R E V '_' B '3' '2'
         | V '_' A S H R R E V '_' I '3' '2'
         | V '_' L S H L '_' B '3' '2'
         | V '_' L S H L R E V '_' B '3' '2'
         | V '_' A N D '_' B '3' '2'
         | V '_' O R '_' B '3' '2'
         | V '_' X O R '_' B '3' '2'
         | V '_' B F M '_' B '3' '2'
         | V '_' M A C '_' F '3' '2'
         | V '_' A D D '_' I '3' '2'
         | V '_' A D D '_' I '6' '4'
         | V '_' S U B '_' I '3' '2'
         | V '_' S U B R E V '_' I '3' '2'
         | V '_' A D D '_' U '3' '2'
         | V '_' A D D C O '_' U '3' '2'
         | V '_' S U B '_' U '3' '2'
         | V '_' S U B R E V '_' U '3' '2'
         | V '_' L S H L '_' B '6' '4'
         | V '_' A S H R '_' I '6' '4'
         | V '_' A D D '_' F '6' '4') E32?;

VALU_VOP1:
		(V '_' M O V '_' B '3' '2'
         | V '_' R E A D F I R S T L A N E '_' B '3' '2'
         | V '_' C V T '_' I '3' '2' '_' F '6' '4'
         | V '_' C V T '_' F '6' '4' '_' I '3' '2'
         | V '_' C V T '_' F '3' '2' '_' I '3' '2'
         | V '_' C V T '_' F '3' '2' '_' U '3' '2'
         | V '_' C V T '_' U '3' '2' '_' F '3' '2'
         | V '_' C V T '_' I '3' '2' '_' F '3' '2'
         | V '_' C V T '_' F '3' '2' '_' F '6' '4'
         | V '_' C V T '_' F '6' '4' '_' F '3' '2'
         | V '_' C V T '_' F '6' '4' '_' U '3' '2'
         | V '_' C V T A '_' S H A R E D '_' T O '_' F L A T
         | V '_' C V T A '_' F L A T '_' T O '_' G L O B A L
         | V '_' T R U N C '_' F '3' '2'
         | V '_' F L O O R '_' F '3' '2'
         | V '_' L O G '_' F '3' '2'
         | V '_' R C P '_' F '3' '2'
         | V '_' R S Q '_' F '3' '2'
         | V '_' R C P '_' F '6' '4'
         | V '_' R S Q '_' F '6' '4'
         | V '_' S Q R T '_' F '3' '2'
         | V '_' S I N '_' F '3' '2'
         | V '_' C O S '_' F '3' '2'
         | V '_' N O T '_' B '3' '2'
         | V '_' F F B H '_' U '3' '2'
         | V '_' F R A C T '_' F '6' '4'
         | V '_' M O V R E L D '_' B '3' '2'
         | V '_' M O V R E L S '_' B '3' '2'
         | V '_' S E X T '_' I '6' '4' '_' I '3' '2'
         | V '_' S E X T '_' I '3' '2' '_' I '8'
         | V '_' S E X T '_' I '3' '2' '_' I '1' '6'
         | V '_' Z E X T '_' B '3' '2' '_' B '1' '6'
         | V '_' Z E X T '_' B '3' '2' '_' B '8'
         | V '_' Z E X T '_' B '6' '4' '_' B '3' '2'
         | V '_' C H O P '_' B '1' '6' '_' B '3' '2') E32?;

VALU_VOPC:
		(V '_' C M P '_' L T '_' F '3' '2'
         | V '_' C M P '_' G T '_' F '3' '2'
         | V '_' C M P '_' G E '_' F '3' '2'
         | V '_' C M P '_' N G T '_' F '3' '2'
         | V '_' C M P '_' N E Q '_' F '3' '2'
         | V '_' C M P '_' L T '_' I '3' '2'
         | V '_' C M P '_' E Q '_' I '3' '2'
         | V '_' C M P '_' L E '_' I '3' '2'
         | V '_' C M P '_' G T '_' I '3' '2'
         | V '_' C M P '_' N E '_' I '3' '2'
         | V '_' C M P '_' G E '_' I '3' '2'
         | V '_' C M P '_' L T '_' U '3' '2'
         | V '_' C M P '_' E Q '_' U '3' '2'
         | V '_' C M P '_' L E '_' U '3' '2'
         | V '_' C M P '_' G T '_' U '3' '2'
         | V '_' C M P '_' N E '_' U '3' '2'
         | V '_' C M P '_' G E '_' U '3' '2') E32?;

VALU_VOP3A:
		(V '_' C N D M A S K '_' B '3' '2' '_' V O P '3' A
         | V '_' A D D '_' F '3' '2' '_' V O P '3' A
         | V '_' S U B R E V '_' F '3' '2' '_' V O P '3' A
         | V '_' M U L '_' F '3' '2' '_' V O P '3' A
         | V '_' M U L '_' I '3' '2' '_' I '2' '4' '_' V O P '3' A
         | V '_' M A X '_' F '3' '2' '_' V O P '3' A
         | V '_' M A D '_' F '3' '2'
         | V '_' M A D '_' U '3' '2' '_' U '2' '4'
         | V '_' M A D L O '_' I '3' '2' '_' I '3' '2'
         | V '_' B F E '_' U '3' '2'
         | V '_' B F E '_' I '3' '2'
         | V '_' B F I '_' B '3' '2'
         | V '_' F M A '_' F '3' '2'
         | V '_' F M A '_' F '6' '4'
         | V '_' A L I G N B I T '_' B '3' '2'
         | V '_' M A X '3' '_' I '3' '2'
         | V '_' M I N '_' F '6' '4'
         | V '_' M A X '_' F '6' '4'
         | V '_' M U L '_' L O '_' U '3' '2'
         | V '_' M U L '_' H I '_' U '3' '2'
         | V '_' M U L '_' L O '_' I '3' '2'
         | V '_' F R A C T '_' F '3' '2' '_' V O P '3' A
         | V '_' C M P '_' L T '_' F '3' '2' '_' V O P '3' A
         | V '_' C M P '_' E Q '_' F '3' '2' '_' V O P '3' A
         | V '_' C M P '_' G T '_' F '3' '2' '_' V O P '3' A
         | V '_' C M P '_' N L E '_' F '3' '2' '_' V O P '3' A
         | V '_' C M P '_' N E Q '_' F '3' '2' '_' V O P '3' A
         | V '_' C M P '_' N L T '_' F '3' '2' '_' V O P '3' A
         | V '_' C M P '_' L T '_' I '3' '2' '_' V O P '3' A
         | V '_' C M P '_' E Q '_' I '3' '2' '_' V O P '3' A
         | V '_' C M P '_' L E '_' I '3' '2' '_' V O P '3' A
         | V '_' C M P '_' G T '_' I '3' '2' '_' V O P '3' A
         | V '_' C M P '_' G E '_' I '3' '2' '_' V O P '3' A
         | V '_' C M P '_' N E '_' I '3' '2' '_' V O P '3' A
         | V '_' C M P X '_' E Q '_' I '3' '2' '_' V O P '3' A
         | V '_' C M P '_' O P '1' '6' '_' F '6' '4' '_' V O P '3' A
         | V '_' C M P '_' C L A S S '_' F '6' '4' '_' V O P '3' A
         | V '_' C M P '_' L T '_' U '3' '2' '_' V O P '3' A
         | V '_' C M P '_' L E '_' U '3' '2' '_' V O P '3' A
         | V '_' C M P '_' G T '_' U '3' '2' '_' V O P '3' A
         | V '_' C M P '_' L G '_' U '3' '2' '_' V O P '3' A
         | V '_' C M P '_' G E '_' U '3' '2' '_' V O P '3' A
         | V '_' C M P '_' L T '_' U '6' '4' '_' V O P '3' A
         | V '_' L S H R '_' B '6' '4'
         | V '_' M U L '_' F '6' '4'
         | V '_' L D E X P '_' F '6' '4'
         | V '_' C M P '_' L E '_' F '3' '2' '_' V O P '3' A
         | V '_' M E D '3' '_' I '3' '2') E32?;

VALU_VOP3B:
		(V '_' A D D C '_' U '3' '2') E32?;

SALU_SOP1:
		(S '_' M O V '_' B '3' '2'
         | S '_' M O V '_' B '6' '4'
         | S '_' N O T '_' B '3' '2'
         | S '_' W Q M '_' B '6' '4'
         | S '_' S W A P P C '_' B '6' '4'
         | S '_' A N D '_' S A V E E X E C '_' B '6' '4') E32?;

SALU_SOP2:
		(S '_' A D D '_' U '3' '2'
         | S '_' A D D '_' I '3' '2'
         | S '_' S U B '_' I '3' '2'
         | S '_' M I N '_' U '3' '2'
         | S '_' M A X '_' I '3' '2'
         | S '_' M A X '_' U '3' '2'
         | S '_' C S E L E C T '_' B '3' '2'
         | S '_' A N D '_' B '3' '2'
         | S '_' A N D '_' B '6' '4'
         | S '_' O R '_' B '3' '2'
         | S '_' O R '_' B '6' '4'
         | S '_' X O R '_' B '6' '4'
         | S '_' A N D N '2' '_' B '6' '4'
         | S '_' N A N D '_' B '6' '4'
         | S '_' L S H L '_' B '3' '2'
         | S '_' L S H R '_' B '3' '2'
         | S '_' A S H R '_' I '3' '2'
         | S '_' M U L '_' I '3' '2'
         | S '_' B F E '_' I '3' '2') E32?;

SALU_SOPK:
		(S '_' M O V K '_' I '3' '2'
         | S '_' C M P K '_' L E '_' U '3' '2'
         | S '_' A D D K '_' I '3' '2'
         | S '_' M U L K '_' I '3' '2') E32?;

SALU_SOPC:
		(S '_' C M P '_' E Q '_' I '3' '2'
         | S '_' C M P '_' G T '_' I '3' '2'
         | S '_' C M P '_' G E '_' I '3' '2'
         | S '_' C M P '_' L T '_' I '3' '2'
         | S '_' C M P '_' L E '_' I '3' '2'
         | S '_' C M P '_' G T '_' U '3' '2'
         | S '_' C M P '_' G E '_' U '3' '2'
         | S '_' C M P '_' L E '_' U '3' '2') E32?;

SALU_SOPP:
		(T '_' C B R A N C H '_' T C C Z
         | T '_' C B R A N C H '_' T C C N Z
         | S '_' C B R A N C H '_' S C C Z
         | S '_' C B R A N C H '_' S C C N Z
         | T '_' C B R A N C H '_' E X E C Z
         | T '_' C B R A N C H '_' E X E C N Z
         | S '_' B R A N C H
         | S '_' B A R R I E R
         | S '_' W A I T C N T
         | B A R '_' S Y N C
         | S '_' P H I
         | T '_' E X I T
         | T '_' N O P) E32?;

SMEM_SLS:
		(S '_' L O A D '_' D W O R D
         | S '_' L O A D '_' D W O R D X '2'
         | S '_' L O A D '_' D W O R D X '4'
         | S '_' L O A D '_' D W O R D X '8'
         | S '_' L O A D '_' D W O R D X '1' '6') E32?;

VMEM_VMUBUF:
		(V '_' B U F F E R '_' L O A D '_' S B Y T E
         | V '_' B U F F E R '_' L O A D '_' D W O R D
         | V '_' B U F F E R '_' S T O R E '_' S B Y T E
         | V '_' B U F F E R '_' S T O R E '_' D W O R D
         | V '_' B U F F E R '_' A T O M I C '_' A D D) E32?;

VMEM_VLS:
		(V '_' L O A D '_' U '8'
         | V '_' L O A D '_' U '1' '6'
         | V '_' L O A D '_' U '3' '2'
         | V '_' L O A D '_' U '6' '4'
         | V '_' L O A D '_' U '3' '2' X '4'
         | V '_' S T O R E '_' U '8'
         | V '_' S T O R E '_' U '1' '6'
         | V '_' S T O R E '_' U '3' '2'
         | V '_' S T O R E '_' U '6' '4') E32?;

DMEM_DLS:
		(D '_' A D D '_' U '3' '2'
         | D '_' I N C '_' U '3' '2'
         | D '_' W R I T E '_' B '3' '2'
         | D '_' W R I T E '2' '_' B '3' '2'
         | D '_' W R I T E '_' B '8'
         | D '_' W R I T E '_' B '1' '6'
         | D '_' R E A D '_' B '3' '2'
         | D '_' R E A D '2' '_' B '3' '2'
         | D '_' R E A D '_' I '8'
         | D '_' R E A D '_' U '8'
         | D '_' R E A D '_' I '1' '6'
         | D '_' R E A D '_' U '1' '6') E32?;


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