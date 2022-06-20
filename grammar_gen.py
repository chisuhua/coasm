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
    for instr_name, fmt in fmt_list:
        exec("instr = {}()".format(instr_name))
        f.write("DEFFMT({},{},{})\n".format(fmt, '"'+str(fmt)+'"', hex(Instr.fmt_enc[fmt].value)))
        instr.genInstrOpcodeDef(f, fmt);
        f.write("DEFEND({})\n\n".format(fmt))

tpl = env.get_template("coasm.h.tpl")
optype_list = ""
for n, v in OpType._member_map_.items():
    optype_list += ",\n{} = {}".format(n, v.value)

atomic_list = ""
for n, v in AtomicOpType._member_map_.items():
    atomic_list += ",\n{} = {}".format(n, v.value)

datatype_list = ""
for n, v in DataType.TypeEnum._member_map_.items():
    datatype_list += ",\n{} = {}".format(n, v.value)

cacheop_list = ""
for n, v in CacheOpType._member_map_.items():
    cacheop_list += ",\n{} = {}".format(n, v.value)

mspace_list = ""
for n, v in MemSpace.KindEnum._member_map_.items():
    if mspace_list != "":
        mspace_list += ","
    mspace_list += "\n{} = {}".format(n, v.value)

memop_list = ""
for n, v in MemOpType._member_map_.items():
    if memop_list != "":
        memop_list += ","
    memop_list += "\n{} = {}".format(n, v.value)

pipeline_list = ""
for n, v in OpPipeline._member_map_.items():
    if pipeline_list != "":
        pipeline_list += ","
    pipeline_list += "\n{} = {}".format(n, v.value)


tpl_out = tpl.render(OpTypeList=optype_list, OpAtomicList=atomic_list, DataTypeList=datatype_list, CacheOpList=cacheop_list, MSpaceList=mspace_list, MemopList=memop_list, PipelineList=pipeline_list)
with open(os.path.join(path, "coasm.h"), 'w') as f:
    f.writelines(tpl_out)



