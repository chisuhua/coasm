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
#render_dict = {}
instr_fmt_list = Instr.getInstrFmtList()
instr_class_list = Instr.getInstrClassList()
instr_def_list = Instr.getInstrDefList()

#print(instr_def_list)

tpl_out = tpl.render(InstrFmtList=instr_fmt_list, instr_class_list=instr_class_list, instr_def_list=instr_def_list)
with open(os.path.join(path, "grammar/Coasm.g4"), 'w') as f:
    f.writelines(tpl_out)
    f.close()
