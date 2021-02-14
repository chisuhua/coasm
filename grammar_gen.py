#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ts=4 sw=4 sts=4 expandtab
import sys
import os
import jinja2
from coasm import *

path = os.path.dirname(os.path.abspath(__file__))

env = jinja2.Environment(loader=jinja2.FileSystemLoader(path))

tpl = env.get_template("grammar/Coasm.g4.tpl")

Instr = Instr()

# genrate Coasm.g4
#render_dict = {}
instr_fmt_list = Instr.getGrammarInstrFmtList()
instr_class_list = Instr.getGrammarInstrClassList()
instr_def_list = Instr.getGrammarInstrDefList()

#print(instr_def_list)

tpl_out = tpl.render(InstrFmtList=instr_fmt_list, instr_class_list=instr_class_list, instr_def_list=instr_def_list)
with open(os.path.join(path, "grammar/Coasm.g4"), 'w') as f:
    f.writelines(tpl_out)
    f.close()


# genrate opcodes_fmt.def
with open("opcodes_fmt.def", 'w') as f:
    Instr.visitClass(VisitType.GEN_INSTR_FMT_FIELD, f);

fmt_list = []
Instr.visitClass(VisitType.GET_INSTR_FMT_LIST, fmt_list)
with open("opcodes.def", 'w') as f:
    for fmt in fmt_list:
        Instr = exec("Instr{}()".format(fmt))
        fmt_name = Instr.getFmtName()
        f.write("DEFFMT({},{},{})".format(fmt_name, "", Instr.fmt_enc[fmt_name].value))
        Instr.genInstrOpcodeDef(f);
        f.write("DEFEND({})".format(fmt_name))


