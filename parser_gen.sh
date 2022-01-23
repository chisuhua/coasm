#!/bin/bash
# -*- coding: utf-8 -*-

THIS_SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export CLASSPATH=$THIS_SCRIPT_DIR/../py3antlr4book/antlr.jar

antlr4py3="java org.antlr.v4.Tool -Dlanguage=Python3"

python grammar_gen.py
$antlr4py3 grammar/Coasm.g4
