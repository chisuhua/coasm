# Generated from grammar/Coasm.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CoasmParser import CoasmParser
else:
    from CoasmParser import CoasmParser

# This class defines a complete listener for a parse tree produced by CoasmParser.
class CoasmListener(ParseTreeListener):

    # Enter a parse tree produced by CoasmParser#prog.
    def enterProg(self, ctx:CoasmParser.ProgContext):
        pass

    # Exit a parse tree produced by CoasmParser#prog.
    def exitProg(self, ctx:CoasmParser.ProgContext):
        pass


    # Enter a parse tree produced by CoasmParser#line.
    def enterLine(self, ctx:CoasmParser.LineContext):
        pass

    # Exit a parse tree produced by CoasmParser#line.
    def exitLine(self, ctx:CoasmParser.LineContext):
        pass


    # Enter a parse tree produced by CoasmParser#label.
    def enterLabel(self, ctx:CoasmParser.LabelContext):
        pass

    # Exit a parse tree produced by CoasmParser#label.
    def exitLabel(self, ctx:CoasmParser.LabelContext):
        pass


    # Enter a parse tree produced by CoasmParser#internal_id.
    def enterInternal_id(self, ctx:CoasmParser.Internal_idContext):
        pass

    # Exit a parse tree produced by CoasmParser#internal_id.
    def exitInternal_id(self, ctx:CoasmParser.Internal_idContext):
        pass


    # Enter a parse tree produced by CoasmParser#directive.
    def enterDirective(self, ctx:CoasmParser.DirectiveContext):
        pass

    # Exit a parse tree produced by CoasmParser#directive.
    def exitDirective(self, ctx:CoasmParser.DirectiveContext):
        pass


    # Enter a parse tree produced by CoasmParser#asm_directive.
    def enterAsm_directive(self, ctx:CoasmParser.Asm_directiveContext):
        pass

    # Exit a parse tree produced by CoasmParser#asm_directive.
    def exitAsm_directive(self, ctx:CoasmParser.Asm_directiveContext):
        pass


    # Enter a parse tree produced by CoasmParser#kernel_directive.
    def enterKernel_directive(self, ctx:CoasmParser.Kernel_directiveContext):
        pass

    # Exit a parse tree produced by CoasmParser#kernel_directive.
    def exitKernel_directive(self, ctx:CoasmParser.Kernel_directiveContext):
        pass


    # Enter a parse tree produced by CoasmParser#kernel_option_item.
    def enterKernel_option_item(self, ctx:CoasmParser.Kernel_option_itemContext):
        pass

    # Exit a parse tree produced by CoasmParser#kernel_option_item.
    def exitKernel_option_item(self, ctx:CoasmParser.Kernel_option_itemContext):
        pass


    # Enter a parse tree produced by CoasmParser#decl_directive.
    def enterDecl_directive(self, ctx:CoasmParser.Decl_directiveContext):
        pass

    # Exit a parse tree produced by CoasmParser#decl_directive.
    def exitDecl_directive(self, ctx:CoasmParser.Decl_directiveContext):
        pass


    # Enter a parse tree produced by CoasmParser#inst_directive.
    def enterInst_directive(self, ctx:CoasmParser.Inst_directiveContext):
        pass

    # Exit a parse tree produced by CoasmParser#inst_directive.
    def exitInst_directive(self, ctx:CoasmParser.Inst_directiveContext):
        pass


    # Enter a parse tree produced by CoasmParser#align_directive.
    def enterAlign_directive(self, ctx:CoasmParser.Align_directiveContext):
        pass

    # Exit a parse tree produced by CoasmParser#align_directive.
    def exitAlign_directive(self, ctx:CoasmParser.Align_directiveContext):
        pass


    # Enter a parse tree produced by CoasmParser#size_directive.
    def enterSize_directive(self, ctx:CoasmParser.Size_directiveContext):
        pass

    # Exit a parse tree produced by CoasmParser#size_directive.
    def exitSize_directive(self, ctx:CoasmParser.Size_directiveContext):
        pass


    # Enter a parse tree produced by CoasmParser#ident_directive.
    def enterIdent_directive(self, ctx:CoasmParser.Ident_directiveContext):
        pass

    # Exit a parse tree produced by CoasmParser#ident_directive.
    def exitIdent_directive(self, ctx:CoasmParser.Ident_directiveContext):
        pass


    # Enter a parse tree produced by CoasmParser#alias_directive.
    def enterAlias_directive(self, ctx:CoasmParser.Alias_directiveContext):
        pass

    # Exit a parse tree produced by CoasmParser#alias_directive.
    def exitAlias_directive(self, ctx:CoasmParser.Alias_directiveContext):
        pass


    # Enter a parse tree produced by CoasmParser#mem_directive.
    def enterMem_directive(self, ctx:CoasmParser.Mem_directiveContext):
        pass

    # Exit a parse tree produced by CoasmParser#mem_directive.
    def exitMem_directive(self, ctx:CoasmParser.Mem_directiveContext):
        pass


    # Enter a parse tree produced by CoasmParser#extend_mem_directive.
    def enterExtend_mem_directive(self, ctx:CoasmParser.Extend_mem_directiveContext):
        pass

    # Exit a parse tree produced by CoasmParser#extend_mem_directive.
    def exitExtend_mem_directive(self, ctx:CoasmParser.Extend_mem_directiveContext):
        pass


    # Enter a parse tree produced by CoasmParser#reg_directive.
    def enterReg_directive(self, ctx:CoasmParser.Reg_directiveContext):
        pass

    # Exit a parse tree produced by CoasmParser#reg_directive.
    def exitReg_directive(self, ctx:CoasmParser.Reg_directiveContext):
        pass


    # Enter a parse tree produced by CoasmParser#data_expr_list.
    def enterData_expr_list(self, ctx:CoasmParser.Data_expr_listContext):
        pass

    # Exit a parse tree produced by CoasmParser#data_expr_list.
    def exitData_expr_list(self, ctx:CoasmParser.Data_expr_listContext):
        pass


    # Enter a parse tree produced by CoasmParser#data_offset.
    def enterData_offset(self, ctx:CoasmParser.Data_offsetContext):
        pass

    # Exit a parse tree produced by CoasmParser#data_offset.
    def exitData_offset(self, ctx:CoasmParser.Data_offsetContext):
        pass


    # Enter a parse tree produced by CoasmParser#number.
    def enterNumber(self, ctx:CoasmParser.NumberContext):
        pass

    # Exit a parse tree produced by CoasmParser#number.
    def exitNumber(self, ctx:CoasmParser.NumberContext):
        pass


    # Enter a parse tree produced by CoasmParser#generic_reg.
    def enterGeneric_reg(self, ctx:CoasmParser.Generic_regContext):
        pass

    # Exit a parse tree produced by CoasmParser#generic_reg.
    def exitGeneric_reg(self, ctx:CoasmParser.Generic_regContext):
        pass


    # Enter a parse tree produced by CoasmParser#register_.
    def enterRegister_(self, ctx:CoasmParser.Register_Context):
        pass

    # Exit a parse tree produced by CoasmParser#register_.
    def exitRegister_(self, ctx:CoasmParser.Register_Context):
        pass


    # Enter a parse tree produced by CoasmParser#sreg.
    def enterSreg(self, ctx:CoasmParser.SregContext):
        pass

    # Exit a parse tree produced by CoasmParser#sreg.
    def exitSreg(self, ctx:CoasmParser.SregContext):
        pass


    # Enter a parse tree produced by CoasmParser#vreg.
    def enterVreg(self, ctx:CoasmParser.VregContext):
        pass

    # Exit a parse tree produced by CoasmParser#vreg.
    def exitVreg(self, ctx:CoasmParser.VregContext):
        pass


    # Enter a parse tree produced by CoasmParser#dreg.
    def enterDreg(self, ctx:CoasmParser.DregContext):
        pass

    # Exit a parse tree produced by CoasmParser#dreg.
    def exitDreg(self, ctx:CoasmParser.DregContext):
        pass


    # Enter a parse tree produced by CoasmParser#lreg.
    def enterLreg(self, ctx:CoasmParser.LregContext):
        pass

    # Exit a parse tree produced by CoasmParser#lreg.
    def exitLreg(self, ctx:CoasmParser.LregContext):
        pass


    # Enter a parse tree produced by CoasmParser#vreg_or_number.
    def enterVreg_or_number(self, ctx:CoasmParser.Vreg_or_numberContext):
        pass

    # Exit a parse tree produced by CoasmParser#vreg_or_number.
    def exitVreg_or_number(self, ctx:CoasmParser.Vreg_or_numberContext):
        pass


    # Enter a parse tree produced by CoasmParser#generic_reg_or_number.
    def enterGeneric_reg_or_number(self, ctx:CoasmParser.Generic_reg_or_numberContext):
        pass

    # Exit a parse tree produced by CoasmParser#generic_reg_or_number.
    def exitGeneric_reg_or_number(self, ctx:CoasmParser.Generic_reg_or_numberContext):
        pass


    # Enter a parse tree produced by CoasmParser#mspace_all.
    def enterMspace_all(self, ctx:CoasmParser.Mspace_allContext):
        pass

    # Exit a parse tree produced by CoasmParser#mspace_all.
    def exitMspace_all(self, ctx:CoasmParser.Mspace_allContext):
        pass


    # Enter a parse tree produced by CoasmParser#mspace_global.
    def enterMspace_global(self, ctx:CoasmParser.Mspace_globalContext):
        pass

    # Exit a parse tree produced by CoasmParser#mspace_global.
    def exitMspace_global(self, ctx:CoasmParser.Mspace_globalContext):
        pass


    # Enter a parse tree produced by CoasmParser#mspace_shared.
    def enterMspace_shared(self, ctx:CoasmParser.Mspace_sharedContext):
        pass

    # Exit a parse tree produced by CoasmParser#mspace_shared.
    def exitMspace_shared(self, ctx:CoasmParser.Mspace_sharedContext):
        pass


    # Enter a parse tree produced by CoasmParser#mspace_flat.
    def enterMspace_flat(self, ctx:CoasmParser.Mspace_flatContext):
        pass

    # Exit a parse tree produced by CoasmParser#mspace_flat.
    def exitMspace_flat(self, ctx:CoasmParser.Mspace_flatContext):
        pass


    # Enter a parse tree produced by CoasmParser#flat_.
    def enterFlat_(self, ctx:CoasmParser.Flat_Context):
        pass

    # Exit a parse tree produced by CoasmParser#flat_.
    def exitFlat_(self, ctx:CoasmParser.Flat_Context):
        pass


    # Enter a parse tree produced by CoasmParser#private_.
    def enterPrivate_(self, ctx:CoasmParser.Private_Context):
        pass

    # Exit a parse tree produced by CoasmParser#private_.
    def exitPrivate_(self, ctx:CoasmParser.Private_Context):
        pass


    # Enter a parse tree produced by CoasmParser#const_.
    def enterConst_(self, ctx:CoasmParser.Const_Context):
        pass

    # Exit a parse tree produced by CoasmParser#const_.
    def exitConst_(self, ctx:CoasmParser.Const_Context):
        pass


    # Enter a parse tree produced by CoasmParser#param_.
    def enterParam_(self, ctx:CoasmParser.Param_Context):
        pass

    # Exit a parse tree produced by CoasmParser#param_.
    def exitParam_(self, ctx:CoasmParser.Param_Context):
        pass


    # Enter a parse tree produced by CoasmParser#global_.
    def enterGlobal_(self, ctx:CoasmParser.Global_Context):
        pass

    # Exit a parse tree produced by CoasmParser#global_.
    def exitGlobal_(self, ctx:CoasmParser.Global_Context):
        pass


    # Enter a parse tree produced by CoasmParser#shared_.
    def enterShared_(self, ctx:CoasmParser.Shared_Context):
        pass

    # Exit a parse tree produced by CoasmParser#shared_.
    def exitShared_(self, ctx:CoasmParser.Shared_Context):
        pass


    # Enter a parse tree produced by CoasmParser#float_mode.
    def enterFloat_mode(self, ctx:CoasmParser.Float_modeContext):
        pass

    # Exit a parse tree produced by CoasmParser#float_mode.
    def exitFloat_mode(self, ctx:CoasmParser.Float_modeContext):
        pass


    # Enter a parse tree produced by CoasmParser#special_operand.
    def enterSpecial_operand(self, ctx:CoasmParser.Special_operandContext):
        pass

    # Exit a parse tree produced by CoasmParser#special_operand.
    def exitSpecial_operand(self, ctx:CoasmParser.Special_operandContext):
        pass


    # Enter a parse tree produced by CoasmParser#sreg_or_tcc.
    def enterSreg_or_tcc(self, ctx:CoasmParser.Sreg_or_tccContext):
        pass

    # Exit a parse tree produced by CoasmParser#sreg_or_tcc.
    def exitSreg_or_tcc(self, ctx:CoasmParser.Sreg_or_tccContext):
        pass


    # Enter a parse tree produced by CoasmParser#special_cc_reg.
    def enterSpecial_cc_reg(self, ctx:CoasmParser.Special_cc_regContext):
        pass

    # Exit a parse tree produced by CoasmParser#special_cc_reg.
    def exitSpecial_cc_reg(self, ctx:CoasmParser.Special_cc_regContext):
        pass


    # Enter a parse tree produced by CoasmParser#vmem_special_operand.
    def enterVmem_special_operand(self, ctx:CoasmParser.Vmem_special_operandContext):
        pass

    # Exit a parse tree produced by CoasmParser#vmem_special_operand.
    def exitVmem_special_operand(self, ctx:CoasmParser.Vmem_special_operandContext):
        pass


    # Enter a parse tree produced by CoasmParser#branch_target.
    def enterBranch_target(self, ctx:CoasmParser.Branch_targetContext):
        pass

    # Exit a parse tree produced by CoasmParser#branch_target.
    def exitBranch_target(self, ctx:CoasmParser.Branch_targetContext):
        pass


    # Enter a parse tree produced by CoasmParser#builtin_operand.
    def enterBuiltin_operand(self, ctx:CoasmParser.Builtin_operandContext):
        pass

    # Exit a parse tree produced by CoasmParser#builtin_operand.
    def exitBuiltin_operand(self, ctx:CoasmParser.Builtin_operandContext):
        pass


    # Enter a parse tree produced by CoasmParser#tcc.
    def enterTcc(self, ctx:CoasmParser.TccContext):
        pass

    # Exit a parse tree produced by CoasmParser#tcc.
    def exitTcc(self, ctx:CoasmParser.TccContext):
        pass


    # Enter a parse tree produced by CoasmParser#section_directive.
    def enterSection_directive(self, ctx:CoasmParser.Section_directiveContext):
        pass

    # Exit a parse tree produced by CoasmParser#section_directive.
    def exitSection_directive(self, ctx:CoasmParser.Section_directiveContext):
        pass


    # Enter a parse tree produced by CoasmParser#section_name.
    def enterSection_name(self, ctx:CoasmParser.Section_nameContext):
        pass

    # Exit a parse tree produced by CoasmParser#section_name.
    def exitSection_name(self, ctx:CoasmParser.Section_nameContext):
        pass


    # Enter a parse tree produced by CoasmParser#section_modifier.
    def enterSection_modifier(self, ctx:CoasmParser.Section_modifierContext):
        pass

    # Exit a parse tree produced by CoasmParser#section_modifier.
    def exitSection_modifier(self, ctx:CoasmParser.Section_modifierContext):
        pass


    # Enter a parse tree produced by CoasmParser#link_directive.
    def enterLink_directive(self, ctx:CoasmParser.Link_directiveContext):
        pass

    # Exit a parse tree produced by CoasmParser#link_directive.
    def exitLink_directive(self, ctx:CoasmParser.Link_directiveContext):
        pass


    # Enter a parse tree produced by CoasmParser#instruction.
    def enterInstruction(self, ctx:CoasmParser.InstructionContext):
        pass

    # Exit a parse tree produced by CoasmParser#instruction.
    def exitInstruction(self, ctx:CoasmParser.InstructionContext):
        pass


    # Enter a parse tree produced by CoasmParser#alu_expr_list.
    def enterAlu_expr_list(self, ctx:CoasmParser.Alu_expr_listContext):
        pass

    # Exit a parse tree produced by CoasmParser#alu_expr_list.
    def exitAlu_expr_list(self, ctx:CoasmParser.Alu_expr_listContext):
        pass


    # Enter a parse tree produced by CoasmParser#alu_expr.
    def enterAlu_expr(self, ctx:CoasmParser.Alu_exprContext):
        pass

    # Exit a parse tree produced by CoasmParser#alu_expr.
    def exitAlu_expr(self, ctx:CoasmParser.Alu_exprContext):
        pass


    # Enter a parse tree produced by CoasmParser#alu_multiply_expr.
    def enterAlu_multiply_expr(self, ctx:CoasmParser.Alu_multiply_exprContext):
        pass

    # Exit a parse tree produced by CoasmParser#alu_multiply_expr.
    def exitAlu_multiply_expr(self, ctx:CoasmParser.Alu_multiply_exprContext):
        pass


    # Enter a parse tree produced by CoasmParser#alu_argument.
    def enterAlu_argument(self, ctx:CoasmParser.Alu_argumentContext):
        pass

    # Exit a parse tree produced by CoasmParser#alu_argument.
    def exitAlu_argument(self, ctx:CoasmParser.Alu_argumentContext):
        pass


    # Enter a parse tree produced by CoasmParser#lop_imm.
    def enterLop_imm(self, ctx:CoasmParser.Lop_immContext):
        pass

    # Exit a parse tree produced by CoasmParser#lop_imm.
    def exitLop_imm(self, ctx:CoasmParser.Lop_immContext):
        pass


    # Enter a parse tree produced by CoasmParser#instrvalu.
    def enterInstrvalu(self, ctx:CoasmParser.InstrvaluContext):
        pass

    # Exit a parse tree produced by CoasmParser#instrvalu.
    def exitInstrvalu(self, ctx:CoasmParser.InstrvaluContext):
        pass


    # Enter a parse tree produced by CoasmParser#instrsalu.
    def enterInstrsalu(self, ctx:CoasmParser.InstrsaluContext):
        pass

    # Exit a parse tree produced by CoasmParser#instrsalu.
    def exitInstrsalu(self, ctx:CoasmParser.InstrsaluContext):
        pass


    # Enter a parse tree produced by CoasmParser#instrsmem.
    def enterInstrsmem(self, ctx:CoasmParser.InstrsmemContext):
        pass

    # Exit a parse tree produced by CoasmParser#instrsmem.
    def exitInstrsmem(self, ctx:CoasmParser.InstrsmemContext):
        pass


    # Enter a parse tree produced by CoasmParser#instrvmem.
    def enterInstrvmem(self, ctx:CoasmParser.InstrvmemContext):
        pass

    # Exit a parse tree produced by CoasmParser#instrvmem.
    def exitInstrvmem(self, ctx:CoasmParser.InstrvmemContext):
        pass


    # Enter a parse tree produced by CoasmParser#instrdmem.
    def enterInstrdmem(self, ctx:CoasmParser.InstrdmemContext):
        pass

    # Exit a parse tree produced by CoasmParser#instrdmem.
    def exitInstrdmem(self, ctx:CoasmParser.InstrdmemContext):
        pass


    # Enter a parse tree produced by CoasmParser#mem_expr_list.
    def enterMem_expr_list(self, ctx:CoasmParser.Mem_expr_listContext):
        pass

    # Exit a parse tree produced by CoasmParser#mem_expr_list.
    def exitMem_expr_list(self, ctx:CoasmParser.Mem_expr_listContext):
        pass


    # Enter a parse tree produced by CoasmParser#mem_expr.
    def enterMem_expr(self, ctx:CoasmParser.Mem_exprContext):
        pass

    # Exit a parse tree produced by CoasmParser#mem_expr.
    def exitMem_expr(self, ctx:CoasmParser.Mem_exprContext):
        pass


    # Enter a parse tree produced by CoasmParser#mem_off.
    def enterMem_off(self, ctx:CoasmParser.Mem_offContext):
        pass

    # Exit a parse tree produced by CoasmParser#mem_off.
    def exitMem_off(self, ctx:CoasmParser.Mem_offContext):
        pass


    # Enter a parse tree produced by CoasmParser#mem_idx_expr.
    def enterMem_idx_expr(self, ctx:CoasmParser.Mem_idx_exprContext):
        pass

    # Exit a parse tree produced by CoasmParser#mem_idx_expr.
    def exitMem_idx_expr(self, ctx:CoasmParser.Mem_idx_exprContext):
        pass


    # Enter a parse tree produced by CoasmParser#mem_idx.
    def enterMem_idx(self, ctx:CoasmParser.Mem_idxContext):
        pass

    # Exit a parse tree produced by CoasmParser#mem_idx.
    def exitMem_idx(self, ctx:CoasmParser.Mem_idxContext):
        pass


    # Enter a parse tree produced by CoasmParser#mem_stride.
    def enterMem_stride(self, ctx:CoasmParser.Mem_strideContext):
        pass

    # Exit a parse tree produced by CoasmParser#mem_stride.
    def exitMem_stride(self, ctx:CoasmParser.Mem_strideContext):
        pass


    # Enter a parse tree produced by CoasmParser#mem_base.
    def enterMem_base(self, ctx:CoasmParser.Mem_baseContext):
        pass

    # Exit a parse tree produced by CoasmParser#mem_base.
    def exitMem_base(self, ctx:CoasmParser.Mem_baseContext):
        pass


    # Enter a parse tree produced by CoasmParser#comment.
    def enterComment(self, ctx:CoasmParser.CommentContext):
        pass

    # Exit a parse tree produced by CoasmParser#comment.
    def exitComment(self, ctx:CoasmParser.CommentContext):
        pass


    # Enter a parse tree produced by CoasmParser#line_comment.
    def enterLine_comment(self, ctx:CoasmParser.Line_commentContext):
        pass

    # Exit a parse tree produced by CoasmParser#line_comment.
    def exitLine_comment(self, ctx:CoasmParser.Line_commentContext):
        pass


    # Enter a parse tree produced by CoasmParser#wait_expr.
    def enterWait_expr(self, ctx:CoasmParser.Wait_exprContext):
        pass

    # Exit a parse tree produced by CoasmParser#wait_expr.
    def exitWait_expr(self, ctx:CoasmParser.Wait_exprContext):
        pass


    # Enter a parse tree produced by CoasmParser#ident.
    def enterIdent(self, ctx:CoasmParser.IdentContext):
        pass

    # Exit a parse tree produced by CoasmParser#ident.
    def exitIdent(self, ctx:CoasmParser.IdentContext):
        pass



del CoasmParser