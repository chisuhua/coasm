# Generated from grammar/Coasm.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3M")
        buf.write("\u027b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\3\2\7\2\u008e\n\2\f\2\16\2\u0091\13\2\3")
        buf.write("\3\3\3\3\3\5\3\u0096\n\3\3\3\5\3\u0099\n\3\3\3\5\3\u009c")
        buf.write("\n\3\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00a9")
        buf.write("\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00b2\n\7\3\b\3\b")
        buf.write("\3\b\3\b\5\b\u00b8\n\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\7\f\u00c9\n\f\f\f\16\f")
        buf.write("\u00cc\13\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\3\17\5\17\u00da\n\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\5\20\u00e4\n\20\3\20\5\20\u00e7\n\20\3")
        buf.write("\20\5\20\u00ea\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\5\21\u00f5\n\21\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\5\22\u00fd\n\22\3\22\3\22\3\23\3\23\3\23\7\23\u0104")
        buf.write("\n\23\f\23\16\23\u0107\13\23\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\26\3\26\5\26\u0111\n\26\3\27\3\27\3\27\5\27\u0116")
        buf.write("\n\27\3\30\5\30\u0119\n\30\3\30\3\30\3\31\5\31\u011e\n")
        buf.write("\31\3\31\3\31\3\32\5\32\u0123\n\32\3\32\3\32\3\33\3\33")
        buf.write("\5\33\u0129\n\33\3\34\3\34\5\34\u012d\n\34\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\5\35\u0137\n\35\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3\"\3")
        buf.write("\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3\'\3\'\3(\3(\5(\u0157")
        buf.write("\n(\3)\3)\5)\u015b\n)\3*\3*\3+\3+\3,\3,\3-\3-\3-\7-\u0166")
        buf.write("\n-\f-\16-\u0169\13-\3.\3.\5.\u016d\n.\3.\5.\u0170\n.")
        buf.write("\3.\3.\3.\5.\u0175\n.\5.\u0177\n.\3/\5/\u017a\n/\3/\3")
        buf.write("/\5/\u017e\n/\3\60\3\60\3\60\3\60\5\60\u0184\n\60\3\61")
        buf.write("\3\61\3\61\3\61\3\61\5\61\u018b\n\61\3\62\3\62\3\62\3")
        buf.write("\62\7\62\u0191\n\62\f\62\16\62\u0194\13\62\3\62\3\62\5")
        buf.write("\62\u0198\n\62\3\63\3\63\3\63\7\63\u019d\n\63\f\63\16")
        buf.write("\63\u01a0\13\63\3\64\3\64\3\64\7\64\u01a5\n\64\f\64\16")
        buf.write("\64\u01a8\13\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65")
        buf.write("\u01b1\n\65\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67\3")
        buf.write("\67\3\67\7\67\u01bd\n\67\f\67\16\67\u01c0\13\67\3\67\3")
        buf.write("\67\3\67\3\67\3\67\5\67\u01c7\n\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\7\67\u01e0\n")
        buf.write("\67\f\67\16\67\u01e3\13\67\5\67\u01e5\n\67\38\38\38\3")
        buf.write("8\38\38\38\38\38\38\38\38\38\38\38\38\38\38\38\38\38\3")
        buf.write("8\38\38\38\38\38\78\u0202\n8\f8\168\u0205\138\58\u0207")
        buf.write("\n8\58\u0209\n8\39\39\39\59\u020e\n9\39\39\39\39\39\5")
        buf.write("9\u0215\n9\39\39\59\u0219\n9\3:\3:\3:\3:\3:\3:\3:\3:\3")
        buf.write(":\3:\3:\3:\3:\3:\3:\5:\u022a\n:\3:\3:\3:\3:\5:\u0230\n")
        buf.write(":\3:\3:\5:\u0234\n:\5:\u0236\n:\3;\3;\3;\3;\5;\u023c\n")
        buf.write(";\3;\3;\3;\3<\3<\3<\3<\7<\u0245\n<\f<\16<\u0248\13<\3")
        buf.write("<\3<\3=\3=\5=\u024e\n=\3>\3>\3>\3>\3>\5>\u0255\n>\3?\3")
        buf.write("?\3?\3?\3@\3@\3@\3@\3@\3@\5@\u0261\n@\3@\3@\3@\3@\5@\u0267")
        buf.write("\n@\3A\3A\3B\3B\5B\u026d\nB\3C\3C\3D\3D\3E\3E\3E\3E\5")
        buf.write("E\u0277\nE\3F\3F\3F\2\2G\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b")
        buf.write("dfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a\2\r")
        buf.write("\3\2\23\24\3\2FG\3\2:;\4\2:;HH\3\2\t\n\3\2\31\32\3\2\27")
        buf.write("\30\3\2\25\26\3\2KL\4\2\13\13\r\16\4\2\64\64::\2\u0298")
        buf.write("\2\u008f\3\2\2\2\4\u0098\3\2\2\2\6\u009d\3\2\2\2\b\u00a0")
        buf.write("\3\2\2\2\n\u00a8\3\2\2\2\f\u00b1\3\2\2\2\16\u00b7\3\2")
        buf.write("\2\2\20\u00b9\3\2\2\2\22\u00bc\3\2\2\2\24\u00c1\3\2\2")
        buf.write("\2\26\u00c4\3\2\2\2\30\u00cd\3\2\2\2\32\u00d2\3\2\2\2")
        buf.write("\34\u00d4\3\2\2\2\36\u00dd\3\2\2\2 \u00f4\3\2\2\2\"\u00f6")
        buf.write("\3\2\2\2$\u0100\3\2\2\2&\u0108\3\2\2\2(\u010c\3\2\2\2")
        buf.write("*\u0110\3\2\2\2,\u0115\3\2\2\2.\u0118\3\2\2\2\60\u011d")
        buf.write("\3\2\2\2\62\u0122\3\2\2\2\64\u0128\3\2\2\2\66\u012c\3")
        buf.write("\2\2\28\u012e\3\2\2\2:\u0138\3\2\2\2<\u013c\3\2\2\2>\u0140")
        buf.write("\3\2\2\2@\u0144\3\2\2\2B\u0146\3\2\2\2D\u0148\3\2\2\2")
        buf.write("F\u014a\3\2\2\2H\u014c\3\2\2\2J\u014e\3\2\2\2L\u0150\3")
        buf.write("\2\2\2N\u0156\3\2\2\2P\u015a\3\2\2\2R\u015c\3\2\2\2T\u015e")
        buf.write("\3\2\2\2V\u0160\3\2\2\2X\u0162\3\2\2\2Z\u016a\3\2\2\2")
        buf.write("\\\u0179\3\2\2\2^\u0183\3\2\2\2`\u018a\3\2\2\2b\u0197")
        buf.write("\3\2\2\2d\u0199\3\2\2\2f\u01a1\3\2\2\2h\u01b0\3\2\2\2")
        buf.write("j\u01b2\3\2\2\2l\u01e4\3\2\2\2n\u0208\3\2\2\2p\u020a\3")
        buf.write("\2\2\2r\u0235\3\2\2\2t\u0237\3\2\2\2v\u0240\3\2\2\2x\u024d")
        buf.write("\3\2\2\2z\u0254\3\2\2\2|\u0256\3\2\2\2~\u0266\3\2\2\2")
        buf.write("\u0080\u0268\3\2\2\2\u0082\u026c\3\2\2\2\u0084\u026e\3")
        buf.write("\2\2\2\u0086\u0270\3\2\2\2\u0088\u0272\3\2\2\2\u008a\u0278")
        buf.write("\3\2\2\2\u008c\u008e\5\4\3\2\u008d\u008c\3\2\2\2\u008e")
        buf.write("\u0091\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2")
        buf.write("\u0090\3\3\2\2\2\u0091\u008f\3\2\2\2\u0092\u0099\5\n\6")
        buf.write("\2\u0093\u0099\5\6\4\2\u0094\u0096\5\6\4\2\u0095\u0094")
        buf.write("\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0097\3\2\2\2\u0097")
        buf.write("\u0099\5`\61\2\u0098\u0092\3\2\2\2\u0098\u0093\3\2\2\2")
        buf.write("\u0098\u0095\3\2\2\2\u0099\u009b\3\2\2\2\u009a\u009c\5")
        buf.write("\u0086D\2\u009b\u009a\3\2\2\2\u009b\u009c\3\2\2\2\u009c")
        buf.write("\5\3\2\2\2\u009d\u009e\5\u008aF\2\u009e\u009f\7\3\2\2")
        buf.write("\u009f\7\3\2\2\2\u00a0\u00a1\t\2\2\2\u00a1\t\3\2\2\2\u00a2")
        buf.write("\u00a9\5\f\7\2\u00a3\u00a9\5\36\20\2\u00a4\u00a9\5 \21")
        buf.write("\2\u00a5\u00a9\5\"\22\2\u00a6\u00a9\5X-\2\u00a7\u00a9")
        buf.write("\5^\60\2\u00a8\u00a2\3\2\2\2\u00a8\u00a3\3\2\2\2\u00a8")
        buf.write("\u00a4\3\2\2\2\u00a8\u00a5\3\2\2\2\u00a8\u00a6\3\2\2\2")
        buf.write("\u00a8\u00a7\3\2\2\2\u00a9\13\3\2\2\2\u00aa\u00b2\5\16")
        buf.write("\b\2\u00ab\u00b2\5\22\n\2\u00ac\u00b2\5\24\13\2\u00ad")
        buf.write("\u00b2\5\26\f\2\u00ae\u00b2\5\30\r\2\u00af\u00b2\5\32")
        buf.write("\16\2\u00b0\u00b2\5\34\17\2\u00b1\u00aa\3\2\2\2\u00b1")
        buf.write("\u00ab\3\2\2\2\u00b1\u00ac\3\2\2\2\u00b1\u00ad\3\2\2\2")
        buf.write("\u00b1\u00ae\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b0\3")
        buf.write("\2\2\2\u00b2\r\3\2\2\2\u00b3\u00b4\7\67\2\2\u00b4\u00b8")
        buf.write("\5\u008aF\2\u00b5\u00b8\5\20\t\2\u00b6\u00b8\78\2\2\u00b7")
        buf.write("\u00b3\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b6\3\2\2\2")
        buf.write("\u00b8\17\3\2\2\2\u00b9\u00ba\7\20\2\2\u00ba\u00bb\7:")
        buf.write("\2\2\u00bb\21\3\2\2\2\u00bc\u00bd\7@\2\2\u00bd\u00be\5")
        buf.write("\u008aF\2\u00be\u00bf\7\4\2\2\u00bf\u00c0\t\3\2\2\u00c0")
        buf.write("\23\3\2\2\2\u00c1\u00c2\7A\2\2\u00c2\u00c3\7;\2\2\u00c3")
        buf.write("\25\3\2\2\2\u00c4\u00c5\7B\2\2\u00c5\u00ca\5(\25\2\u00c6")
        buf.write("\u00c7\7\4\2\2\u00c7\u00c9\5(\25\2\u00c8\u00c6\3\2\2\2")
        buf.write("\u00c9\u00cc\3\2\2\2\u00ca\u00c8\3\2\2\2\u00ca\u00cb\3")
        buf.write("\2\2\2\u00cb\27\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cd\u00ce")
        buf.write("\7C\2\2\u00ce\u00cf\5\u008aF\2\u00cf\u00d0\7\4\2\2\u00d0")
        buf.write("\u00d1\5d\63\2\u00d1\31\3\2\2\2\u00d2\u00d3\7E\2\2\u00d3")
        buf.write("\33\3\2\2\2\u00d4\u00d5\7\21\2\2\u00d5\u00d9\5\u008aF")
        buf.write("\2\u00d6\u00d7\7\5\2\2\u00d7\u00d8\7:\2\2\u00d8\u00da")
        buf.write("\7\6\2\2\u00d9\u00d6\3\2\2\2\u00d9\u00da\3\2\2\2\u00da")
        buf.write("\u00db\3\2\2\2\u00db\u00dc\5,\27\2\u00dc\35\3\2\2\2\u00dd")
        buf.write("\u00de\7\65\2\2\u00de\u00df\79\2\2\u00df\u00e3\5\u008a")
        buf.write("F\2\u00e0\u00e1\7\5\2\2\u00e1\u00e2\7:\2\2\u00e2\u00e4")
        buf.write("\7\6\2\2\u00e3\u00e0\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4")
        buf.write("\u00e6\3\2\2\2\u00e5\u00e7\5$\23\2\u00e6\u00e5\3\2\2\2")
        buf.write("\u00e6\u00e7\3\2\2\2\u00e7\u00e9\3\2\2\2\u00e8\u00ea\5")
        buf.write("&\24\2\u00e9\u00e8\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\37")
        buf.write("\3\2\2\2\u00eb\u00ec\7\66\2\2\u00ec\u00f5\5(\25\2\u00ed")
        buf.write("\u00ee\7\65\2\2\u00ee\u00ef\5\u008aF\2\u00ef\u00f0\7\4")
        buf.write("\2\2\u00f0\u00f1\5(\25\2\u00f1\u00f2\7\4\2\2\u00f2\u00f3")
        buf.write("\5(\25\2\u00f3\u00f5\3\2\2\2\u00f4\u00eb\3\2\2\2\u00f4")
        buf.write("\u00ed\3\2\2\2\u00f5!\3\2\2\2\u00f6\u00f7\7\22\2\2\u00f7")
        buf.write("\u00f8\79\2\2\u00f8\u00fc\5\u008aF\2\u00f9\u00fa\7\5\2")
        buf.write("\2\u00fa\u00fb\7:\2\2\u00fb\u00fd\7\6\2\2\u00fc\u00f9")
        buf.write("\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe")
        buf.write("\u00ff\5,\27\2\u00ff#\3\2\2\2\u0100\u0105\5(\25\2\u0101")
        buf.write("\u0102\7\4\2\2\u0102\u0104\5(\25\2\u0103\u0101\3\2\2\2")
        buf.write("\u0104\u0107\3\2\2\2\u0105\u0103\3\2\2\2\u0105\u0106\3")
        buf.write("\2\2\2\u0106%\3\2\2\2\u0107\u0105\3\2\2\2\u0108\u0109")
        buf.write("\7\7\2\2\u0109\u010a\t\4\2\2\u010a\u010b\7\b\2\2\u010b")
        buf.write("\'\3\2\2\2\u010c\u010d\t\5\2\2\u010d)\3\2\2\2\u010e\u0111")
        buf.write("\5,\27\2\u010f\u0111\5\u008aF\2\u0110\u010e\3\2\2\2\u0110")
        buf.write("\u010f\3\2\2\2\u0111+\3\2\2\2\u0112\u0116\5.\30\2\u0113")
        buf.write("\u0116\5\60\31\2\u0114\u0116\5\62\32\2\u0115\u0112\3\2")
        buf.write("\2\2\u0115\u0113\3\2\2\2\u0115\u0114\3\2\2\2\u0116-\3")
        buf.write("\2\2\2\u0117\u0119\t\6\2\2\u0118\u0117\3\2\2\2\u0118\u0119")
        buf.write("\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u011b\t\7\2\2\u011b")
        buf.write("/\3\2\2\2\u011c\u011e\t\6\2\2\u011d\u011c\3\2\2\2\u011d")
        buf.write("\u011e\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0120\t\b\2\2")
        buf.write("\u0120\61\3\2\2\2\u0121\u0123\t\6\2\2\u0122\u0121\3\2")
        buf.write("\2\2\u0122\u0123\3\2\2\2\u0123\u0124\3\2\2\2\u0124\u0125")
        buf.write("\t\t\2\2\u0125\63\3\2\2\2\u0126\u0129\5\60\31\2\u0127")
        buf.write("\u0129\5(\25\2\u0128\u0126\3\2\2\2\u0128\u0127\3\2\2\2")
        buf.write("\u0129\65\3\2\2\2\u012a\u012d\5*\26\2\u012b\u012d\5(\25")
        buf.write("\2\u012c\u012a\3\2\2\2\u012c\u012b\3\2\2\2\u012d\67\3")
        buf.write("\2\2\2\u012e\u012f\7\"\2\2\u012f\u0136\7\3\2\2\u0130\u0137")
        buf.write("\5@!\2\u0131\u0137\5B\"\2\u0132\u0137\5D#\2\u0133\u0137")
        buf.write("\5F$\2\u0134\u0137\5H%\2\u0135\u0137\5J&\2\u0136\u0130")
        buf.write("\3\2\2\2\u0136\u0131\3\2\2\2\u0136\u0132\3\2\2\2\u0136")
        buf.write("\u0133\3\2\2\2\u0136\u0134\3\2\2\2\u0136\u0135\3\2\2\2")
        buf.write("\u01379\3\2\2\2\u0138\u0139\7\"\2\2\u0139\u013a\7\3\2")
        buf.write("\2\u013a\u013b\5H%\2\u013b;\3\2\2\2\u013c\u013d\7\"\2")
        buf.write("\2\u013d\u013e\7\3\2\2\u013e\u013f\5J&\2\u013f=\3\2\2")
        buf.write("\2\u0140\u0141\7\"\2\2\u0141\u0142\7\3\2\2\u0142\u0143")
        buf.write("\5@!\2\u0143?\3\2\2\2\u0144\u0145\7\34\2\2\u0145A\3\2")
        buf.write("\2\2\u0146\u0147\7\35\2\2\u0147C\3\2\2\2\u0148\u0149\7")
        buf.write("\36\2\2\u0149E\3\2\2\2\u014a\u014b\7\37\2\2\u014bG\3\2")
        buf.write("\2\2\u014c\u014d\7 \2\2\u014dI\3\2\2\2\u014e\u014f\7!")
        buf.write("\2\2\u014fK\3\2\2\2\u0150\u0151\5\u008aF\2\u0151\u0152")
        buf.write("\7\3\2\2\u0152\u0153\5N(\2\u0153M\3\2\2\2\u0154\u0157")
        buf.write("\5.\30\2\u0155\u0157\5V,\2\u0156\u0154\3\2\2\2\u0156\u0155")
        buf.write("\3\2\2\2\u0157O\3\2\2\2\u0158\u015b\5.\30\2\u0159\u015b")
        buf.write("\5V,\2\u015a\u0158\3\2\2\2\u015a\u0159\3\2\2\2\u015bQ")
        buf.write("\3\2\2\2\u015c\u015d\5\u008aF\2\u015dS\3\2\2\2\u015e\u015f")
        buf.write("\5\u008aF\2\u015fU\3\2\2\2\u0160\u0161\7\33\2\2\u0161")
        buf.write("W\3\2\2\2\u0162\u0167\5Z.\2\u0163\u0164\7\4\2\2\u0164")
        buf.write("\u0166\5\\/\2\u0165\u0163\3\2\2\2\u0166\u0169\3\2\2\2")
        buf.write("\u0167\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168Y\3\2\2")
        buf.write("\2\u0169\u0167\3\2\2\2\u016a\u016c\t\n\2\2\u016b\u016d")
        buf.write("\7K\2\2\u016c\u016b\3\2\2\2\u016c\u016d\3\2\2\2\u016d")
        buf.write("\u0176\3\2\2\2\u016e\u0170\7\13\2\2\u016f\u016e\3\2\2")
        buf.write("\2\u016f\u0170\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u0172")
        buf.write("\7\f\2\2\u0172\u0174\7\64\2\2\u0173\u0175\7\13\2\2\u0174")
        buf.write("\u0173\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0177\3\2\2\2")
        buf.write("\u0176\u016f\3\2\2\2\u0176\u0177\3\2\2\2\u0177[\3\2\2")
        buf.write("\2\u0178\u017a\t\13\2\2\u0179\u0178\3\2\2\2\u0179\u017a")
        buf.write("\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017d\t\f\2\2\u017c")
        buf.write("\u017e\7\13\2\2\u017d\u017c\3\2\2\2\u017d\u017e\3\2\2")
        buf.write("\2\u017e]\3\2\2\2\u017f\u0180\7I\2\2\u0180\u0184\5\u008a")
        buf.write("F\2\u0181\u0182\7J\2\2\u0182\u0184\5\u008aF\2\u0183\u017f")
        buf.write("\3\2\2\2\u0183\u0181\3\2\2\2\u0184_\3\2\2\2\u0185\u018b")
        buf.write("\5l\67\2\u0186\u018b\5n8\2\u0187\u018b\5p9\2\u0188\u018b")
        buf.write("\5r:\2\u0189\u018b\5t;\2\u018a\u0185\3\2\2\2\u018a\u0186")
        buf.write("\3\2\2\2\u018a\u0187\3\2\2\2\u018a\u0188\3\2\2\2\u018a")
        buf.write("\u0189\3\2\2\2\u018ba\3\2\2\2\u018c\u0198\5,\27\2\u018d")
        buf.write("\u0192\5d\63\2\u018e\u018f\7\4\2\2\u018f\u0191\5d\63\2")
        buf.write("\u0190\u018e\3\2\2\2\u0191\u0194\3\2\2\2\u0192\u0190\3")
        buf.write("\2\2\2\u0192\u0193\3\2\2\2\u0193\u0198\3\2\2\2\u0194\u0192")
        buf.write("\3\2\2\2\u0195\u0198\7H\2\2\u0196\u0198\7;\2\2\u0197\u018c")
        buf.write("\3\2\2\2\u0197\u018d\3\2\2\2\u0197\u0195\3\2\2\2\u0197")
        buf.write("\u0196\3\2\2\2\u0198c\3\2\2\2\u0199\u019e\5f\64\2\u019a")
        buf.write("\u019b\7<\2\2\u019b\u019d\5f\64\2\u019c\u019a\3\2\2\2")
        buf.write("\u019d\u01a0\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019f\3")
        buf.write("\2\2\2\u019fe\3\2\2\2\u01a0\u019e\3\2\2\2\u01a1\u01a6")
        buf.write("\5h\65\2\u01a2\u01a3\7=\2\2\u01a3\u01a5\5h\65\2\u01a4")
        buf.write("\u01a2\3\2\2\2\u01a5\u01a8\3\2\2\2\u01a6\u01a4\3\2\2\2")
        buf.write("\u01a6\u01a7\3\2\2\2\u01a7g\3\2\2\2\u01a8\u01a6\3\2\2")
        buf.write("\2\u01a9\u01b1\7:\2\2\u01aa\u01b1\5\u008aF\2\u01ab\u01b1")
        buf.write("\5\b\5\2\u01ac\u01ad\7\7\2\2\u01ad\u01ae\5d\63\2\u01ae")
        buf.write("\u01af\7\b\2\2\u01af\u01b1\3\2\2\2\u01b0\u01a9\3\2\2\2")
        buf.write("\u01b0\u01aa\3\2\2\2\u01b0\u01ab\3\2\2\2\u01b0\u01ac\3")
        buf.write("\2\2\2\u01b1i\3\2\2\2\u01b2\u01b3\t\4\2\2\u01b3k\3\2\2")
        buf.write("\2\u01b4\u01b5\7#\2\2\u01b5\u01b6\5\60\31\2\u01b6\u01b7")
        buf.write("\7\4\2\2\u01b7\u01b8\5\66\34\2\u01b8\u01b9\7\4\2\2\u01b9")
        buf.write("\u01be\5\60\31\2\u01ba\u01bb\7\4\2\2\u01bb\u01bd\5L\'")
        buf.write("\2\u01bc\u01ba\3\2\2\2\u01bd\u01c0\3\2\2\2\u01be\u01bc")
        buf.write("\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01e5\3\2\2\2\u01c0")
        buf.write("\u01be\3\2\2\2\u01c1\u01c2\7$\2\2\u01c2\u01c3\5\60\31")
        buf.write("\2\u01c3\u01c6\7\4\2\2\u01c4\u01c7\5,\27\2\u01c5\u01c7")
        buf.write("\5T+\2\u01c6\u01c4\3\2\2\2\u01c6\u01c5\3\2\2\2\u01c7\u01e5")
        buf.write("\3\2\2\2\u01c8\u01c9\7M\2\2\u01c9\u01ca\7\4\2\2\u01ca")
        buf.write("\u01cb\5\60\31\2\u01cb\u01cc\7\4\2\2\u01cc\u01cd\5*\26")
        buf.write("\2\u01cd\u01e5\3\2\2\2\u01ce\u01cf\7&\2\2\u01cf\u01d0")
        buf.write("\5\60\31\2\u01d0\u01d1\7\4\2\2\u01d1\u01d2\5*\26\2\u01d2")
        buf.write("\u01d3\7\4\2\2\u01d3\u01d4\5*\26\2\u01d4\u01d5\7\4\2\2")
        buf.write("\u01d5\u01d6\5*\26\2\u01d6\u01e5\3\2\2\2\u01d7\u01d8\7")
        buf.write("\'\2\2\u01d8\u01d9\5\60\31\2\u01d9\u01da\7\4\2\2\u01da")
        buf.write("\u01db\5\66\34\2\u01db\u01dc\7\4\2\2\u01dc\u01e1\5\60")
        buf.write("\31\2\u01dd\u01de\7\4\2\2\u01de\u01e0\5L\'\2\u01df\u01dd")
        buf.write("\3\2\2\2\u01e0\u01e3\3\2\2\2\u01e1\u01df\3\2\2\2\u01e1")
        buf.write("\u01e2\3\2\2\2\u01e2\u01e5\3\2\2\2\u01e3\u01e1\3\2\2\2")
        buf.write("\u01e4\u01b4\3\2\2\2\u01e4\u01c1\3\2\2\2\u01e4\u01c8\3")
        buf.write("\2\2\2\u01e4\u01ce\3\2\2\2\u01e4\u01d7\3\2\2\2\u01e5m")
        buf.write("\3\2\2\2\u01e6\u01e7\7(\2\2\u01e7\u01e8\5.\30\2\u01e8")
        buf.write("\u01e9\7\4\2\2\u01e9\u01ea\5.\30\2\u01ea\u0209\3\2\2\2")
        buf.write("\u01eb\u01ec\7)\2\2\u01ec\u01ed\5.\30\2\u01ed\u01ee\7")
        buf.write("\4\2\2\u01ee\u01ef\5.\30\2\u01ef\u01f0\7\4\2\2\u01f0\u01f1")
        buf.write("\5.\30\2\u01f1\u0209\3\2\2\2\u01f2\u01f3\7*\2\2\u01f3")
        buf.write("\u01f4\5.\30\2\u01f4\u01f5\7\4\2\2\u01f5\u01f6\5(\25\2")
        buf.write("\u01f6\u0209\3\2\2\2\u01f7\u01f8\7+\2\2\u01f8\u01f9\5")
        buf.write(".\30\2\u01f9\u01fa\7\4\2\2\u01fa\u01fb\5.\30\2\u01fb\u0209")
        buf.write("\3\2\2\2\u01fc\u0206\7,\2\2\u01fd\u0207\5(\25\2\u01fe")
        buf.write("\u0203\5\u0088E\2\u01ff\u0200\7\4\2\2\u0200\u0202\5\u0088")
        buf.write("E\2\u0201\u01ff\3\2\2\2\u0202\u0205\3\2\2\2\u0203\u0201")
        buf.write("\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u0207\3\2\2\2\u0205")
        buf.write("\u0203\3\2\2\2\u0206\u01fd\3\2\2\2\u0206\u01fe\3\2\2\2")
        buf.write("\u0206\u0207\3\2\2\2\u0207\u0209\3\2\2\2\u0208\u01e6\3")
        buf.write("\2\2\2\u0208\u01eb\3\2\2\2\u0208\u01f2\3\2\2\2\u0208\u01f7")
        buf.write("\3\2\2\2\u0208\u01fc\3\2\2\2\u0209o\3\2\2\2\u020a\u020d")
        buf.write("\7-\2\2\u020b\u020e\5.\30\2\u020c\u020e\5\u008aF\2\u020d")
        buf.write("\u020b\3\2\2\2\u020d\u020c\3\2\2\2\u020e\u020f\3\2\2\2")
        buf.write("\u020f\u0210\7\4\2\2\u0210\u0211\5.\30\2\u0211\u0214\7")
        buf.write("\4\2\2\u0212\u0215\5.\30\2\u0213\u0215\5(\25\2\u0214\u0212")
        buf.write("\3\2\2\2\u0214\u0213\3\2\2\2\u0215\u0218\3\2\2\2\u0216")
        buf.write("\u0217\7\17\2\2\u0217\u0219\58\35\2\u0218\u0216\3\2\2")
        buf.write("\2\u0218\u0219\3\2\2\2\u0219q\3\2\2\2\u021a\u021b\7.\2")
        buf.write("\2\u021b\u021c\5\60\31\2\u021c\u021d\7\4\2\2\u021d\u021e")
        buf.write("\5\60\31\2\u021e\u021f\7\4\2\2\u021f\u0220\5.\30\2\u0220")
        buf.write("\u0221\7\4\2\2\u0221\u0222\5.\30\2\u0222\u0236\3\2\2\2")
        buf.write("\u0223\u0224\7/\2\2\u0224\u0225\5\60\31\2\u0225\u0229")
        buf.write("\7\4\2\2\u0226\u022a\5\60\31\2\u0227\u022a\5\62\32\2\u0228")
        buf.write("\u022a\5R*\2\u0229\u0226\3\2\2\2\u0229\u0227\3\2\2\2\u0229")
        buf.write("\u0228\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u022f\7\4\2\2")
        buf.write("\u022c\u0230\5\60\31\2\u022d\u0230\5\62\32\2\u022e\u0230")
        buf.write("\5(\25\2\u022f\u022c\3\2\2\2\u022f\u022d\3\2\2\2\u022f")
        buf.write("\u022e\3\2\2\2\u0230\u0233\3\2\2\2\u0231\u0232\7\17\2")
        buf.write("\2\u0232\u0234\58\35\2\u0233\u0231\3\2\2\2\u0233\u0234")
        buf.write("\3\2\2\2\u0234\u0236\3\2\2\2\u0235\u021a\3\2\2\2\u0235")
        buf.write("\u0223\3\2\2\2\u0236s\3\2\2\2\u0237\u023b\7\60\2\2\u0238")
        buf.write("\u023c\5\60\31\2\u0239\u023c\5\u008aF\2\u023a\u023c\5")
        buf.write("v<\2\u023b\u0238\3\2\2\2\u023b\u0239\3\2\2\2\u023b\u023a")
        buf.write("\3\2\2\2\u023c\u023d\3\2\2\2\u023d\u023e\7\4\2\2\u023e")
        buf.write("\u023f\5v<\2\u023fu\3\2\2\2\u0240\u0241\7\5\2\2\u0241")
        buf.write("\u0246\5x=\2\u0242\u0243\7<\2\2\u0243\u0245\5x=\2\u0244")
        buf.write("\u0242\3\2\2\2\u0245\u0248\3\2\2\2\u0246\u0244\3\2\2\2")
        buf.write("\u0246\u0247\3\2\2\2\u0247\u0249\3\2\2\2\u0248\u0246\3")
        buf.write("\2\2\2\u0249\u024a\7\6\2\2\u024aw\3\2\2\2\u024b\u024e")
        buf.write("\5z>\2\u024c\u024e\5|?\2\u024d\u024b\3\2\2\2\u024d\u024c")
        buf.write("\3\2\2\2\u024ey\3\2\2\2\u024f\u0255\7:\2\2\u0250\u0255")
        buf.write("\7;\2\2\u0251\u0255\5\u008aF\2\u0252\u0255\5.\30\2\u0253")
        buf.write("\u0255\5\60\31\2\u0254\u024f\3\2\2\2\u0254\u0250\3\2\2")
        buf.write("\2\u0254\u0251\3\2\2\2\u0254\u0252\3\2\2\2\u0254\u0253")
        buf.write("\3\2\2\2\u0255{\3\2\2\2\u0256\u0257\5~@\2\u0257\u0258")
        buf.write("\7=\2\2\u0258\u0259\5\u0080A\2\u0259}\3\2\2\2\u025a\u0267")
        buf.write("\5\60\31\2\u025b\u0267\5\u008aF\2\u025c\u0267\7\23\2\2")
        buf.write("\u025d\u0260\7\7\2\2\u025e\u0261\5\60\31\2\u025f\u0261")
        buf.write("\5\u008aF\2\u0260\u025e\3\2\2\2\u0260\u025f\3\2\2\2\u0261")
        buf.write("\u0262\3\2\2\2\u0262\u0263\7<\2\2\u0263\u0264\7\23\2\2")
        buf.write("\u0264\u0265\7\b\2\2\u0265\u0267\3\2\2\2\u0266\u025a\3")
        buf.write("\2\2\2\u0266\u025b\3\2\2\2\u0266\u025c\3\2\2\2\u0266\u025d")
        buf.write("\3\2\2\2\u0267\177\3\2\2\2\u0268\u0269\t\4\2\2\u0269\u0081")
        buf.write("\3\2\2\2\u026a\u026d\5,\27\2\u026b\u026d\5\u008aF\2\u026c")
        buf.write("\u026a\3\2\2\2\u026c\u026b\3\2\2\2\u026d\u0083\3\2\2\2")
        buf.write("\u026e\u026f\7\62\2\2\u026f\u0085\3\2\2\2\u0270\u0271")
        buf.write("\7\63\2\2\u0271\u0087\3\2\2\2\u0272\u0276\7\61\2\2\u0273")
        buf.write("\u0274\7\7\2\2\u0274\u0275\7:\2\2\u0275\u0277\7\b\2\2")
        buf.write("\u0276\u0273\3\2\2\2\u0276\u0277\3\2\2\2\u0277\u0089\3")
        buf.write("\2\2\2\u0278\u0279\7\64\2\2\u0279\u008b\3\2\2\2?\u008f")
        buf.write("\u0095\u0098\u009b\u00a8\u00b1\u00b7\u00ca\u00d9\u00e3")
        buf.write("\u00e6\u00e9\u00f4\u00fc\u0105\u0110\u0115\u0118\u011d")
        buf.write("\u0122\u0128\u012c\u0136\u0156\u015a\u0167\u016c\u016f")
        buf.write("\u0174\u0176\u0179\u017d\u0183\u018a\u0192\u0197\u019e")
        buf.write("\u01a6\u01b0\u01be\u01c6\u01e1\u01e4\u0203\u0206\u0208")
        buf.write("\u020d\u0214\u0218\u0229\u022f\u0233\u0235\u023b\u0246")
        buf.write("\u024d\u0254\u0260\u0266\u026c\u0276")
        return buf.getvalue()


class CoasmParser ( Parser ):

    grammarFileName = "Coasm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "','", "'['", "']'", "'('", "')'", 
                     "'-'", "'!'", "'\"'", "'.'", "'#'", "'@'", "'%'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'mspace'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'@function'", "'@object'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "KERNEL_OPTION_KEY", "ALIAS", 
                      "REG", "TID", "PC", "DREG", "DREG_INDEX", "VREG", 
                      "VREG_INDEX", "SREG", "SREG_INDEX", "TCC", "FLAT", 
                      "PRIVATE", "CONST", "PARAM", "GLOBAL_", "SHARED_", 
                      "MSPACE", "VALU_VOP2", "VALU_VOP1", "VALU_VOPC", "VALU_VOP3A", 
                      "VALU_VOP3B", "SALU_SOP1", "SALU_SOP2", "SALU_SOPK", 
                      "SALU_SOPC", "SALU_SOPP", "SMEM_SLS", "VMEM_VMUBUF", 
                      "VMEM_VLS", "DMEM_DLS", "WAIT_TYPE", "COMMENT", "LINE_COMMENT", 
                      "NAME", "MEM_SPACE", "DATA_DIRECTIVE", "START_KERNEL", 
                      "END_KERNEL", "DATA_TYPE", "DIGIT", "HEX_NUMBER", 
                      "SIGN", "MSIGN", "WS", "TODO", "TYPE", "INST", "P2ALIGN", 
                      "SIZE", "FUNC_END", "IDENT", "DECL_FUNC", "DECL_OBJECT", 
                      "FP_NUMBER", "EXTERN", "VISIBLE", "PREDEF_SECTION", 
                      "SECTION", "VALU_VOPCspecial_cc_reg" ]

    RULE_prog = 0
    RULE_line = 1
    RULE_label = 2
    RULE_internal_id = 3
    RULE_directive = 4
    RULE_asm_directive = 5
    RULE_kernel_directive = 6
    RULE_kernel_option_item = 7
    RULE_decl_directive = 8
    RULE_inst_directive = 9
    RULE_align_directive = 10
    RULE_size_directive = 11
    RULE_ident_directive = 12
    RULE_alias_directive = 13
    RULE_mem_directive = 14
    RULE_extend_mem_directive = 15
    RULE_reg_directive = 16
    RULE_data_expr_list = 17
    RULE_data_offset = 18
    RULE_number = 19
    RULE_generic_reg = 20
    RULE_register_ = 21
    RULE_sreg = 22
    RULE_vreg = 23
    RULE_dreg = 24
    RULE_vreg_or_number = 25
    RULE_generic_reg_or_number = 26
    RULE_mspace_all = 27
    RULE_mspace_global = 28
    RULE_mspace_shared = 29
    RULE_mspace_flat = 30
    RULE_flat_ = 31
    RULE_private_ = 32
    RULE_const_ = 33
    RULE_param_ = 34
    RULE_global_ = 35
    RULE_shared_ = 36
    RULE_special_operand = 37
    RULE_special_reg = 38
    RULE_special_cc_reg = 39
    RULE_vmem_special_operand = 40
    RULE_builtin_operand = 41
    RULE_tcc = 42
    RULE_section_directive = 43
    RULE_section_name = 44
    RULE_section_modifier = 45
    RULE_link_directive = 46
    RULE_instruction = 47
    RULE_alu_expr_list = 48
    RULE_alu_expr = 49
    RULE_alu_multiply_expr = 50
    RULE_alu_argument = 51
    RULE_lop_imm = 52
    RULE_instrvalu = 53
    RULE_instrsalu = 54
    RULE_instrsmem = 55
    RULE_instrvmem = 56
    RULE_instrdmem = 57
    RULE_mem_expr_list = 58
    RULE_mem_expr = 59
    RULE_mem_off = 60
    RULE_mem_idx_expr = 61
    RULE_mem_idx = 62
    RULE_mem_stride = 63
    RULE_mem_base = 64
    RULE_comment = 65
    RULE_line_comment = 66
    RULE_wait_expr = 67
    RULE_ident = 68

    ruleNames =  [ "prog", "line", "label", "internal_id", "directive", 
                   "asm_directive", "kernel_directive", "kernel_option_item", 
                   "decl_directive", "inst_directive", "align_directive", 
                   "size_directive", "ident_directive", "alias_directive", 
                   "mem_directive", "extend_mem_directive", "reg_directive", 
                   "data_expr_list", "data_offset", "number", "generic_reg", 
                   "register_", "sreg", "vreg", "dreg", "vreg_or_number", 
                   "generic_reg_or_number", "mspace_all", "mspace_global", 
                   "mspace_shared", "mspace_flat", "flat_", "private_", 
                   "const_", "param_", "global_", "shared_", "special_operand", 
                   "special_reg", "special_cc_reg", "vmem_special_operand", 
                   "builtin_operand", "tcc", "section_directive", "section_name", 
                   "section_modifier", "link_directive", "instruction", 
                   "alu_expr_list", "alu_expr", "alu_multiply_expr", "alu_argument", 
                   "lop_imm", "instrvalu", "instrsalu", "instrsmem", "instrvmem", 
                   "instrdmem", "mem_expr_list", "mem_expr", "mem_off", 
                   "mem_idx_expr", "mem_idx", "mem_stride", "mem_base", 
                   "comment", "line_comment", "wait_expr", "ident" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    KERNEL_OPTION_KEY=14
    ALIAS=15
    REG=16
    TID=17
    PC=18
    DREG=19
    DREG_INDEX=20
    VREG=21
    VREG_INDEX=22
    SREG=23
    SREG_INDEX=24
    TCC=25
    FLAT=26
    PRIVATE=27
    CONST=28
    PARAM=29
    GLOBAL_=30
    SHARED_=31
    MSPACE=32
    VALU_VOP2=33
    VALU_VOP1=34
    VALU_VOPC=35
    VALU_VOP3A=36
    VALU_VOP3B=37
    SALU_SOP1=38
    SALU_SOP2=39
    SALU_SOPK=40
    SALU_SOPC=41
    SALU_SOPP=42
    SMEM_SLS=43
    VMEM_VMUBUF=44
    VMEM_VLS=45
    DMEM_DLS=46
    WAIT_TYPE=47
    COMMENT=48
    LINE_COMMENT=49
    NAME=50
    MEM_SPACE=51
    DATA_DIRECTIVE=52
    START_KERNEL=53
    END_KERNEL=54
    DATA_TYPE=55
    DIGIT=56
    HEX_NUMBER=57
    SIGN=58
    MSIGN=59
    WS=60
    TODO=61
    TYPE=62
    INST=63
    P2ALIGN=64
    SIZE=65
    FUNC_END=66
    IDENT=67
    DECL_FUNC=68
    DECL_OBJECT=69
    FP_NUMBER=70
    EXTERN=71
    VISIBLE=72
    PREDEF_SECTION=73
    SECTION=74
    VALU_VOPCspecial_cc_reg=75

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoasmParser.LineContext)
            else:
                return self.getTypedRuleContext(CoasmParser.LineContext,i)


        def getRuleIndex(self):
            return CoasmParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = CoasmParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 14)) & ~0x3f) == 0 and ((1 << (_la - 14)) & ((1 << (CoasmParser.KERNEL_OPTION_KEY - 14)) | (1 << (CoasmParser.ALIAS - 14)) | (1 << (CoasmParser.REG - 14)) | (1 << (CoasmParser.VALU_VOP2 - 14)) | (1 << (CoasmParser.VALU_VOP1 - 14)) | (1 << (CoasmParser.VALU_VOP3A - 14)) | (1 << (CoasmParser.VALU_VOP3B - 14)) | (1 << (CoasmParser.SALU_SOP1 - 14)) | (1 << (CoasmParser.SALU_SOP2 - 14)) | (1 << (CoasmParser.SALU_SOPK - 14)) | (1 << (CoasmParser.SALU_SOPC - 14)) | (1 << (CoasmParser.SALU_SOPP - 14)) | (1 << (CoasmParser.SMEM_SLS - 14)) | (1 << (CoasmParser.VMEM_VMUBUF - 14)) | (1 << (CoasmParser.VMEM_VLS - 14)) | (1 << (CoasmParser.DMEM_DLS - 14)) | (1 << (CoasmParser.NAME - 14)) | (1 << (CoasmParser.MEM_SPACE - 14)) | (1 << (CoasmParser.DATA_DIRECTIVE - 14)) | (1 << (CoasmParser.START_KERNEL - 14)) | (1 << (CoasmParser.END_KERNEL - 14)) | (1 << (CoasmParser.TYPE - 14)) | (1 << (CoasmParser.INST - 14)) | (1 << (CoasmParser.P2ALIGN - 14)) | (1 << (CoasmParser.SIZE - 14)) | (1 << (CoasmParser.IDENT - 14)) | (1 << (CoasmParser.EXTERN - 14)) | (1 << (CoasmParser.VISIBLE - 14)) | (1 << (CoasmParser.PREDEF_SECTION - 14)) | (1 << (CoasmParser.SECTION - 14)) | (1 << (CoasmParser.VALU_VOPCspecial_cc_reg - 14)))) != 0):
                self.state = 138
                self.line()
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def directive(self):
            return self.getTypedRuleContext(CoasmParser.DirectiveContext,0)


        def label(self):
            return self.getTypedRuleContext(CoasmParser.LabelContext,0)


        def instruction(self):
            return self.getTypedRuleContext(CoasmParser.InstructionContext,0)


        def line_comment(self):
            return self.getTypedRuleContext(CoasmParser.Line_commentContext,0)


        def getRuleIndex(self):
            return CoasmParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)




    def line(self):

        localctx = CoasmParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 144
                self.directive()
                pass

            elif la_ == 2:
                self.state = 145
                self.label()
                pass

            elif la_ == 3:
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CoasmParser.NAME:
                    self.state = 146
                    self.label()


                self.state = 149
                self.instruction()
                pass


            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CoasmParser.LINE_COMMENT:
                self.state = 152
                self.line_comment()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(CoasmParser.IdentContext,0)


        def getRuleIndex(self):
            return CoasmParser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)




    def label(self):

        localctx = CoasmParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.ident()
            self.state = 156
            self.match(CoasmParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Internal_idContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TID(self):
            return self.getToken(CoasmParser.TID, 0)

        def PC(self):
            return self.getToken(CoasmParser.PC, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_internal_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInternal_id" ):
                listener.enterInternal_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInternal_id" ):
                listener.exitInternal_id(self)




    def internal_id(self):

        localctx = CoasmParser.Internal_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_internal_id)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            _la = self._input.LA(1)
            if not(_la==CoasmParser.TID or _la==CoasmParser.PC):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DirectiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asm_directive(self):
            return self.getTypedRuleContext(CoasmParser.Asm_directiveContext,0)


        def mem_directive(self):
            return self.getTypedRuleContext(CoasmParser.Mem_directiveContext,0)


        def extend_mem_directive(self):
            return self.getTypedRuleContext(CoasmParser.Extend_mem_directiveContext,0)


        def reg_directive(self):
            return self.getTypedRuleContext(CoasmParser.Reg_directiveContext,0)


        def section_directive(self):
            return self.getTypedRuleContext(CoasmParser.Section_directiveContext,0)


        def link_directive(self):
            return self.getTypedRuleContext(CoasmParser.Link_directiveContext,0)


        def getRuleIndex(self):
            return CoasmParser.RULE_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirective" ):
                listener.enterDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirective" ):
                listener.exitDirective(self)




    def directive(self):

        localctx = CoasmParser.DirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_directive)
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.asm_directive()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.mem_directive()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 162
                self.extend_mem_directive()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 163
                self.reg_directive()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 164
                self.section_directive()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 165
                self.link_directive()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Asm_directiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kernel_directive(self):
            return self.getTypedRuleContext(CoasmParser.Kernel_directiveContext,0)


        def decl_directive(self):
            return self.getTypedRuleContext(CoasmParser.Decl_directiveContext,0)


        def inst_directive(self):
            return self.getTypedRuleContext(CoasmParser.Inst_directiveContext,0)


        def align_directive(self):
            return self.getTypedRuleContext(CoasmParser.Align_directiveContext,0)


        def size_directive(self):
            return self.getTypedRuleContext(CoasmParser.Size_directiveContext,0)


        def ident_directive(self):
            return self.getTypedRuleContext(CoasmParser.Ident_directiveContext,0)


        def alias_directive(self):
            return self.getTypedRuleContext(CoasmParser.Alias_directiveContext,0)


        def getRuleIndex(self):
            return CoasmParser.RULE_asm_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsm_directive" ):
                listener.enterAsm_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsm_directive" ):
                listener.exitAsm_directive(self)




    def asm_directive(self):

        localctx = CoasmParser.Asm_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_asm_directive)
        try:
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CoasmParser.KERNEL_OPTION_KEY, CoasmParser.START_KERNEL, CoasmParser.END_KERNEL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.kernel_directive()
                pass
            elif token in [CoasmParser.TYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.decl_directive()
                pass
            elif token in [CoasmParser.INST]:
                self.enterOuterAlt(localctx, 3)
                self.state = 170
                self.inst_directive()
                pass
            elif token in [CoasmParser.P2ALIGN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 171
                self.align_directive()
                pass
            elif token in [CoasmParser.SIZE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 172
                self.size_directive()
                pass
            elif token in [CoasmParser.IDENT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 173
                self.ident_directive()
                pass
            elif token in [CoasmParser.ALIAS]:
                self.enterOuterAlt(localctx, 7)
                self.state = 174
                self.alias_directive()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Kernel_directiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def START_KERNEL(self):
            return self.getToken(CoasmParser.START_KERNEL, 0)

        def ident(self):
            return self.getTypedRuleContext(CoasmParser.IdentContext,0)


        def kernel_option_item(self):
            return self.getTypedRuleContext(CoasmParser.Kernel_option_itemContext,0)


        def END_KERNEL(self):
            return self.getToken(CoasmParser.END_KERNEL, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_kernel_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKernel_directive" ):
                listener.enterKernel_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKernel_directive" ):
                listener.exitKernel_directive(self)




    def kernel_directive(self):

        localctx = CoasmParser.Kernel_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_kernel_directive)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CoasmParser.START_KERNEL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.match(CoasmParser.START_KERNEL)
                self.state = 178
                self.ident()
                pass
            elif token in [CoasmParser.KERNEL_OPTION_KEY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.kernel_option_item()
                pass
            elif token in [CoasmParser.END_KERNEL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 180
                self.match(CoasmParser.END_KERNEL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Kernel_option_itemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KERNEL_OPTION_KEY(self):
            return self.getToken(CoasmParser.KERNEL_OPTION_KEY, 0)

        def DIGIT(self):
            return self.getToken(CoasmParser.DIGIT, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_kernel_option_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKernel_option_item" ):
                listener.enterKernel_option_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKernel_option_item" ):
                listener.exitKernel_option_item(self)




    def kernel_option_item(self):

        localctx = CoasmParser.Kernel_option_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_kernel_option_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(CoasmParser.KERNEL_OPTION_KEY)
            self.state = 184
            self.match(CoasmParser.DIGIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_directiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(CoasmParser.TYPE, 0)

        def ident(self):
            return self.getTypedRuleContext(CoasmParser.IdentContext,0)


        def DECL_FUNC(self):
            return self.getToken(CoasmParser.DECL_FUNC, 0)

        def DECL_OBJECT(self):
            return self.getToken(CoasmParser.DECL_OBJECT, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_decl_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl_directive" ):
                listener.enterDecl_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl_directive" ):
                listener.exitDecl_directive(self)




    def decl_directive(self):

        localctx = CoasmParser.Decl_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_decl_directive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(CoasmParser.TYPE)
            self.state = 187
            self.ident()
            self.state = 188
            self.match(CoasmParser.T__1)
            self.state = 189
            _la = self._input.LA(1)
            if not(_la==CoasmParser.DECL_FUNC or _la==CoasmParser.DECL_OBJECT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inst_directiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INST(self):
            return self.getToken(CoasmParser.INST, 0)

        def HEX_NUMBER(self):
            return self.getToken(CoasmParser.HEX_NUMBER, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_inst_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInst_directive" ):
                listener.enterInst_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInst_directive" ):
                listener.exitInst_directive(self)




    def inst_directive(self):

        localctx = CoasmParser.Inst_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_inst_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(CoasmParser.INST)
            self.state = 192
            self.match(CoasmParser.HEX_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Align_directiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def P2ALIGN(self):
            return self.getToken(CoasmParser.P2ALIGN, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoasmParser.NumberContext)
            else:
                return self.getTypedRuleContext(CoasmParser.NumberContext,i)


        def getRuleIndex(self):
            return CoasmParser.RULE_align_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlign_directive" ):
                listener.enterAlign_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlign_directive" ):
                listener.exitAlign_directive(self)




    def align_directive(self):

        localctx = CoasmParser.Align_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_align_directive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(CoasmParser.P2ALIGN)
            self.state = 195
            self.number()
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CoasmParser.T__1:
                self.state = 196
                self.match(CoasmParser.T__1)
                self.state = 197
                self.number()
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Size_directiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIZE(self):
            return self.getToken(CoasmParser.SIZE, 0)

        def ident(self):
            return self.getTypedRuleContext(CoasmParser.IdentContext,0)


        def alu_expr(self):
            return self.getTypedRuleContext(CoasmParser.Alu_exprContext,0)


        def getRuleIndex(self):
            return CoasmParser.RULE_size_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSize_directive" ):
                listener.enterSize_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSize_directive" ):
                listener.exitSize_directive(self)




    def size_directive(self):

        localctx = CoasmParser.Size_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_size_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(CoasmParser.SIZE)
            self.state = 204
            self.ident()
            self.state = 205
            self.match(CoasmParser.T__1)
            self.state = 206
            self.alu_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ident_directiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(CoasmParser.IDENT, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_ident_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdent_directive" ):
                listener.enterIdent_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdent_directive" ):
                listener.exitIdent_directive(self)




    def ident_directive(self):

        localctx = CoasmParser.Ident_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ident_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(CoasmParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Alias_directiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALIAS(self):
            return self.getToken(CoasmParser.ALIAS, 0)

        def ident(self):
            return self.getTypedRuleContext(CoasmParser.IdentContext,0)


        def register_(self):
            return self.getTypedRuleContext(CoasmParser.Register_Context,0)


        def DIGIT(self):
            return self.getToken(CoasmParser.DIGIT, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_alias_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlias_directive" ):
                listener.enterAlias_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlias_directive" ):
                listener.exitAlias_directive(self)




    def alias_directive(self):

        localctx = CoasmParser.Alias_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_alias_directive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(CoasmParser.ALIAS)
            self.state = 211
            self.ident()
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CoasmParser.T__2:
                self.state = 212
                self.match(CoasmParser.T__2)
                self.state = 213
                self.match(CoasmParser.DIGIT)
                self.state = 214
                self.match(CoasmParser.T__3)


            self.state = 217
            self.register_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mem_directiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MEM_SPACE(self):
            return self.getToken(CoasmParser.MEM_SPACE, 0)

        def DATA_TYPE(self):
            return self.getToken(CoasmParser.DATA_TYPE, 0)

        def ident(self):
            return self.getTypedRuleContext(CoasmParser.IdentContext,0)


        def DIGIT(self):
            return self.getToken(CoasmParser.DIGIT, 0)

        def data_expr_list(self):
            return self.getTypedRuleContext(CoasmParser.Data_expr_listContext,0)


        def data_offset(self):
            return self.getTypedRuleContext(CoasmParser.Data_offsetContext,0)


        def getRuleIndex(self):
            return CoasmParser.RULE_mem_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMem_directive" ):
                listener.enterMem_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMem_directive" ):
                listener.exitMem_directive(self)




    def mem_directive(self):

        localctx = CoasmParser.Mem_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_mem_directive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(CoasmParser.MEM_SPACE)
            self.state = 220
            self.match(CoasmParser.DATA_TYPE)
            self.state = 221
            self.ident()
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CoasmParser.T__2:
                self.state = 222
                self.match(CoasmParser.T__2)
                self.state = 223
                self.match(CoasmParser.DIGIT)
                self.state = 224
                self.match(CoasmParser.T__3)


            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 56)) & ~0x3f) == 0 and ((1 << (_la - 56)) & ((1 << (CoasmParser.DIGIT - 56)) | (1 << (CoasmParser.HEX_NUMBER - 56)) | (1 << (CoasmParser.FP_NUMBER - 56)))) != 0):
                self.state = 227
                self.data_expr_list()


            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CoasmParser.T__4:
                self.state = 230
                self.data_offset()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Extend_mem_directiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATA_DIRECTIVE(self):
            return self.getToken(CoasmParser.DATA_DIRECTIVE, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoasmParser.NumberContext)
            else:
                return self.getTypedRuleContext(CoasmParser.NumberContext,i)


        def MEM_SPACE(self):
            return self.getToken(CoasmParser.MEM_SPACE, 0)

        def ident(self):
            return self.getTypedRuleContext(CoasmParser.IdentContext,0)


        def getRuleIndex(self):
            return CoasmParser.RULE_extend_mem_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtend_mem_directive" ):
                listener.enterExtend_mem_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtend_mem_directive" ):
                listener.exitExtend_mem_directive(self)




    def extend_mem_directive(self):

        localctx = CoasmParser.Extend_mem_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_extend_mem_directive)
        try:
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CoasmParser.DATA_DIRECTIVE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.match(CoasmParser.DATA_DIRECTIVE)
                self.state = 234
                self.number()
                pass
            elif token in [CoasmParser.MEM_SPACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.match(CoasmParser.MEM_SPACE)
                self.state = 236
                self.ident()
                self.state = 237
                self.match(CoasmParser.T__1)
                self.state = 238
                self.number()
                self.state = 239
                self.match(CoasmParser.T__1)
                self.state = 240
                self.number()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Reg_directiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REG(self):
            return self.getToken(CoasmParser.REG, 0)

        def DATA_TYPE(self):
            return self.getToken(CoasmParser.DATA_TYPE, 0)

        def ident(self):
            return self.getTypedRuleContext(CoasmParser.IdentContext,0)


        def register_(self):
            return self.getTypedRuleContext(CoasmParser.Register_Context,0)


        def DIGIT(self):
            return self.getToken(CoasmParser.DIGIT, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_reg_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReg_directive" ):
                listener.enterReg_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReg_directive" ):
                listener.exitReg_directive(self)




    def reg_directive(self):

        localctx = CoasmParser.Reg_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_reg_directive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(CoasmParser.REG)
            self.state = 245
            self.match(CoasmParser.DATA_TYPE)
            self.state = 246
            self.ident()
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CoasmParser.T__2:
                self.state = 247
                self.match(CoasmParser.T__2)
                self.state = 248
                self.match(CoasmParser.DIGIT)
                self.state = 249
                self.match(CoasmParser.T__3)


            self.state = 252
            self.register_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_expr_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoasmParser.NumberContext)
            else:
                return self.getTypedRuleContext(CoasmParser.NumberContext,i)


        def getRuleIndex(self):
            return CoasmParser.RULE_data_expr_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData_expr_list" ):
                listener.enterData_expr_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData_expr_list" ):
                listener.exitData_expr_list(self)




    def data_expr_list(self):

        localctx = CoasmParser.Data_expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_data_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.number()
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CoasmParser.T__1:
                self.state = 255
                self.match(CoasmParser.T__1)
                self.state = 256
                self.number()
                self.state = 261
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_offsetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self):
            return self.getToken(CoasmParser.DIGIT, 0)

        def HEX_NUMBER(self):
            return self.getToken(CoasmParser.HEX_NUMBER, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_data_offset

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData_offset" ):
                listener.enterData_offset(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData_offset" ):
                listener.exitData_offset(self)




    def data_offset(self):

        localctx = CoasmParser.Data_offsetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_data_offset)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(CoasmParser.T__4)
            self.state = 263
            _la = self._input.LA(1)
            if not(_la==CoasmParser.DIGIT or _la==CoasmParser.HEX_NUMBER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 264
            self.match(CoasmParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self):
            return self.getToken(CoasmParser.DIGIT, 0)

        def HEX_NUMBER(self):
            return self.getToken(CoasmParser.HEX_NUMBER, 0)

        def FP_NUMBER(self):
            return self.getToken(CoasmParser.FP_NUMBER, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = CoasmParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            _la = self._input.LA(1)
            if not(((((_la - 56)) & ~0x3f) == 0 and ((1 << (_la - 56)) & ((1 << (CoasmParser.DIGIT - 56)) | (1 << (CoasmParser.HEX_NUMBER - 56)) | (1 << (CoasmParser.FP_NUMBER - 56)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Generic_regContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def register_(self):
            return self.getTypedRuleContext(CoasmParser.Register_Context,0)


        def ident(self):
            return self.getTypedRuleContext(CoasmParser.IdentContext,0)


        def getRuleIndex(self):
            return CoasmParser.RULE_generic_reg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeneric_reg" ):
                listener.enterGeneric_reg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeneric_reg" ):
                listener.exitGeneric_reg(self)




    def generic_reg(self):

        localctx = CoasmParser.Generic_regContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_generic_reg)
        try:
            self.state = 270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CoasmParser.T__6, CoasmParser.T__7, CoasmParser.DREG, CoasmParser.DREG_INDEX, CoasmParser.VREG, CoasmParser.VREG_INDEX, CoasmParser.SREG, CoasmParser.SREG_INDEX]:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.register_()
                pass
            elif token in [CoasmParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.ident()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Register_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sreg(self):
            return self.getTypedRuleContext(CoasmParser.SregContext,0)


        def vreg(self):
            return self.getTypedRuleContext(CoasmParser.VregContext,0)


        def dreg(self):
            return self.getTypedRuleContext(CoasmParser.DregContext,0)


        def getRuleIndex(self):
            return CoasmParser.RULE_register_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegister_" ):
                listener.enterRegister_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegister_" ):
                listener.exitRegister_(self)




    def register_(self):

        localctx = CoasmParser.Register_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_register_)
        try:
            self.state = 275
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.sreg()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.vreg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 274
                self.dreg()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SregContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SREG(self):
            return self.getToken(CoasmParser.SREG, 0)

        def SREG_INDEX(self):
            return self.getToken(CoasmParser.SREG_INDEX, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_sreg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSreg" ):
                listener.enterSreg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSreg" ):
                listener.exitSreg(self)




    def sreg(self):

        localctx = CoasmParser.SregContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_sreg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CoasmParser.T__6 or _la==CoasmParser.T__7:
                self.state = 277
                _la = self._input.LA(1)
                if not(_la==CoasmParser.T__6 or _la==CoasmParser.T__7):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 280
            _la = self._input.LA(1)
            if not(_la==CoasmParser.SREG or _la==CoasmParser.SREG_INDEX):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VregContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VREG(self):
            return self.getToken(CoasmParser.VREG, 0)

        def VREG_INDEX(self):
            return self.getToken(CoasmParser.VREG_INDEX, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_vreg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVreg" ):
                listener.enterVreg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVreg" ):
                listener.exitVreg(self)




    def vreg(self):

        localctx = CoasmParser.VregContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_vreg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CoasmParser.T__6 or _la==CoasmParser.T__7:
                self.state = 282
                _la = self._input.LA(1)
                if not(_la==CoasmParser.T__6 or _la==CoasmParser.T__7):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 285
            _la = self._input.LA(1)
            if not(_la==CoasmParser.VREG or _la==CoasmParser.VREG_INDEX):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DregContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DREG(self):
            return self.getToken(CoasmParser.DREG, 0)

        def DREG_INDEX(self):
            return self.getToken(CoasmParser.DREG_INDEX, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_dreg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDreg" ):
                listener.enterDreg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDreg" ):
                listener.exitDreg(self)




    def dreg(self):

        localctx = CoasmParser.DregContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_dreg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CoasmParser.T__6 or _la==CoasmParser.T__7:
                self.state = 287
                _la = self._input.LA(1)
                if not(_la==CoasmParser.T__6 or _la==CoasmParser.T__7):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 290
            _la = self._input.LA(1)
            if not(_la==CoasmParser.DREG or _la==CoasmParser.DREG_INDEX):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vreg_or_numberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vreg(self):
            return self.getTypedRuleContext(CoasmParser.VregContext,0)


        def number(self):
            return self.getTypedRuleContext(CoasmParser.NumberContext,0)


        def getRuleIndex(self):
            return CoasmParser.RULE_vreg_or_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVreg_or_number" ):
                listener.enterVreg_or_number(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVreg_or_number" ):
                listener.exitVreg_or_number(self)




    def vreg_or_number(self):

        localctx = CoasmParser.Vreg_or_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_vreg_or_number)
        try:
            self.state = 294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CoasmParser.T__6, CoasmParser.T__7, CoasmParser.VREG, CoasmParser.VREG_INDEX]:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.vreg()
                pass
            elif token in [CoasmParser.DIGIT, CoasmParser.HEX_NUMBER, CoasmParser.FP_NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.number()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Generic_reg_or_numberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def generic_reg(self):
            return self.getTypedRuleContext(CoasmParser.Generic_regContext,0)


        def number(self):
            return self.getTypedRuleContext(CoasmParser.NumberContext,0)


        def getRuleIndex(self):
            return CoasmParser.RULE_generic_reg_or_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeneric_reg_or_number" ):
                listener.enterGeneric_reg_or_number(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeneric_reg_or_number" ):
                listener.exitGeneric_reg_or_number(self)




    def generic_reg_or_number(self):

        localctx = CoasmParser.Generic_reg_or_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_generic_reg_or_number)
        try:
            self.state = 298
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CoasmParser.T__6, CoasmParser.T__7, CoasmParser.DREG, CoasmParser.DREG_INDEX, CoasmParser.VREG, CoasmParser.VREG_INDEX, CoasmParser.SREG, CoasmParser.SREG_INDEX, CoasmParser.NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.generic_reg()
                pass
            elif token in [CoasmParser.DIGIT, CoasmParser.HEX_NUMBER, CoasmParser.FP_NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.number()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mspace_allContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MSPACE(self):
            return self.getToken(CoasmParser.MSPACE, 0)

        def flat_(self):
            return self.getTypedRuleContext(CoasmParser.Flat_Context,0)


        def private_(self):
            return self.getTypedRuleContext(CoasmParser.Private_Context,0)


        def const_(self):
            return self.getTypedRuleContext(CoasmParser.Const_Context,0)


        def param_(self):
            return self.getTypedRuleContext(CoasmParser.Param_Context,0)


        def global_(self):
            return self.getTypedRuleContext(CoasmParser.Global_Context,0)


        def shared_(self):
            return self.getTypedRuleContext(CoasmParser.Shared_Context,0)


        def getRuleIndex(self):
            return CoasmParser.RULE_mspace_all

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMspace_all" ):
                listener.enterMspace_all(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMspace_all" ):
                listener.exitMspace_all(self)




    def mspace_all(self):

        localctx = CoasmParser.Mspace_allContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_mspace_all)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(CoasmParser.MSPACE)
            self.state = 301
            self.match(CoasmParser.T__0)
            self.state = 308
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CoasmParser.FLAT]:
                self.state = 302
                self.flat_()
                pass
            elif token in [CoasmParser.PRIVATE]:
                self.state = 303
                self.private_()
                pass
            elif token in [CoasmParser.CONST]:
                self.state = 304
                self.const_()
                pass
            elif token in [CoasmParser.PARAM]:
                self.state = 305
                self.param_()
                pass
            elif token in [CoasmParser.GLOBAL_]:
                self.state = 306
                self.global_()
                pass
            elif token in [CoasmParser.SHARED_]:
                self.state = 307
                self.shared_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mspace_globalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MSPACE(self):
            return self.getToken(CoasmParser.MSPACE, 0)

        def global_(self):
            return self.getTypedRuleContext(CoasmParser.Global_Context,0)


        def getRuleIndex(self):
            return CoasmParser.RULE_mspace_global

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMspace_global" ):
                listener.enterMspace_global(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMspace_global" ):
                listener.exitMspace_global(self)




    def mspace_global(self):

        localctx = CoasmParser.Mspace_globalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_mspace_global)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(CoasmParser.MSPACE)
            self.state = 311
            self.match(CoasmParser.T__0)
            self.state = 312
            self.global_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mspace_sharedContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MSPACE(self):
            return self.getToken(CoasmParser.MSPACE, 0)

        def shared_(self):
            return self.getTypedRuleContext(CoasmParser.Shared_Context,0)


        def getRuleIndex(self):
            return CoasmParser.RULE_mspace_shared

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMspace_shared" ):
                listener.enterMspace_shared(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMspace_shared" ):
                listener.exitMspace_shared(self)




    def mspace_shared(self):

        localctx = CoasmParser.Mspace_sharedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_mspace_shared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(CoasmParser.MSPACE)
            self.state = 315
            self.match(CoasmParser.T__0)
            self.state = 316
            self.shared_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mspace_flatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MSPACE(self):
            return self.getToken(CoasmParser.MSPACE, 0)

        def flat_(self):
            return self.getTypedRuleContext(CoasmParser.Flat_Context,0)


        def getRuleIndex(self):
            return CoasmParser.RULE_mspace_flat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMspace_flat" ):
                listener.enterMspace_flat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMspace_flat" ):
                listener.exitMspace_flat(self)




    def mspace_flat(self):

        localctx = CoasmParser.Mspace_flatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_mspace_flat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(CoasmParser.MSPACE)
            self.state = 319
            self.match(CoasmParser.T__0)
            self.state = 320
            self.flat_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Flat_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLAT(self):
            return self.getToken(CoasmParser.FLAT, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_flat_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFlat_" ):
                listener.enterFlat_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFlat_" ):
                listener.exitFlat_(self)




    def flat_(self):

        localctx = CoasmParser.Flat_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_flat_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(CoasmParser.FLAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Private_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRIVATE(self):
            return self.getToken(CoasmParser.PRIVATE, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_private_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrivate_" ):
                listener.enterPrivate_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrivate_" ):
                listener.exitPrivate_(self)




    def private_(self):

        localctx = CoasmParser.Private_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_private_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(CoasmParser.PRIVATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(CoasmParser.CONST, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_const_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConst_" ):
                listener.enterConst_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConst_" ):
                listener.exitConst_(self)




    def const_(self):

        localctx = CoasmParser.Const_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_const_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(CoasmParser.CONST)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAM(self):
            return self.getToken(CoasmParser.PARAM, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_param_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_" ):
                listener.enterParam_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_" ):
                listener.exitParam_(self)




    def param_(self):

        localctx = CoasmParser.Param_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_param_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(CoasmParser.PARAM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Global_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GLOBAL_(self):
            return self.getToken(CoasmParser.GLOBAL_, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_global_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobal_" ):
                listener.enterGlobal_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobal_" ):
                listener.exitGlobal_(self)




    def global_(self):

        localctx = CoasmParser.Global_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_global_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(CoasmParser.GLOBAL_)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Shared_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHARED_(self):
            return self.getToken(CoasmParser.SHARED_, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_shared_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShared_" ):
                listener.enterShared_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShared_" ):
                listener.exitShared_(self)




    def shared_(self):

        localctx = CoasmParser.Shared_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_shared_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.match(CoasmParser.SHARED_)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Special_operandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(CoasmParser.IdentContext,0)


        def special_reg(self):
            return self.getTypedRuleContext(CoasmParser.Special_regContext,0)


        def getRuleIndex(self):
            return CoasmParser.RULE_special_operand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecial_operand" ):
                listener.enterSpecial_operand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecial_operand" ):
                listener.exitSpecial_operand(self)




    def special_operand(self):

        localctx = CoasmParser.Special_operandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_special_operand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.ident()
            self.state = 335
            self.match(CoasmParser.T__0)
            self.state = 336
            self.special_reg()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Special_regContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sreg(self):
            return self.getTypedRuleContext(CoasmParser.SregContext,0)


        def tcc(self):
            return self.getTypedRuleContext(CoasmParser.TccContext,0)


        def getRuleIndex(self):
            return CoasmParser.RULE_special_reg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecial_reg" ):
                listener.enterSpecial_reg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecial_reg" ):
                listener.exitSpecial_reg(self)




    def special_reg(self):

        localctx = CoasmParser.Special_regContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_special_reg)
        try:
            self.state = 340
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CoasmParser.T__6, CoasmParser.T__7, CoasmParser.SREG, CoasmParser.SREG_INDEX]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.sreg()
                pass
            elif token in [CoasmParser.TCC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                self.tcc()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Special_cc_regContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sreg(self):
            return self.getTypedRuleContext(CoasmParser.SregContext,0)


        def tcc(self):
            return self.getTypedRuleContext(CoasmParser.TccContext,0)


        def getRuleIndex(self):
            return CoasmParser.RULE_special_cc_reg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecial_cc_reg" ):
                listener.enterSpecial_cc_reg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecial_cc_reg" ):
                listener.exitSpecial_cc_reg(self)




    def special_cc_reg(self):

        localctx = CoasmParser.Special_cc_regContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_special_cc_reg)
        try:
            self.state = 344
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CoasmParser.T__6, CoasmParser.T__7, CoasmParser.SREG, CoasmParser.SREG_INDEX]:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.sreg()
                pass
            elif token in [CoasmParser.TCC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 343
                self.tcc()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vmem_special_operandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(CoasmParser.IdentContext,0)


        def getRuleIndex(self):
            return CoasmParser.RULE_vmem_special_operand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVmem_special_operand" ):
                listener.enterVmem_special_operand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVmem_special_operand" ):
                listener.exitVmem_special_operand(self)




    def vmem_special_operand(self):

        localctx = CoasmParser.Vmem_special_operandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_vmem_special_operand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.ident()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Builtin_operandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(CoasmParser.IdentContext,0)


        def getRuleIndex(self):
            return CoasmParser.RULE_builtin_operand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBuiltin_operand" ):
                listener.enterBuiltin_operand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBuiltin_operand" ):
                listener.exitBuiltin_operand(self)




    def builtin_operand(self):

        localctx = CoasmParser.Builtin_operandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_builtin_operand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.ident()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TccContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TCC(self):
            return self.getToken(CoasmParser.TCC, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_tcc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTcc" ):
                listener.enterTcc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTcc" ):
                listener.exitTcc(self)




    def tcc(self):

        localctx = CoasmParser.TccContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_tcc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(CoasmParser.TCC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Section_directiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def section_name(self):
            return self.getTypedRuleContext(CoasmParser.Section_nameContext,0)


        def section_modifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoasmParser.Section_modifierContext)
            else:
                return self.getTypedRuleContext(CoasmParser.Section_modifierContext,i)


        def getRuleIndex(self):
            return CoasmParser.RULE_section_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSection_directive" ):
                listener.enterSection_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSection_directive" ):
                listener.exitSection_directive(self)




    def section_directive(self):

        localctx = CoasmParser.Section_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_section_directive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.section_name()
            self.state = 357
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CoasmParser.T__1:
                self.state = 353
                self.match(CoasmParser.T__1)
                self.state = 354
                self.section_modifier()
                self.state = 359
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Section_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREDEF_SECTION(self, i:int=None):
            if i is None:
                return self.getTokens(CoasmParser.PREDEF_SECTION)
            else:
                return self.getToken(CoasmParser.PREDEF_SECTION, i)

        def SECTION(self):
            return self.getToken(CoasmParser.SECTION, 0)

        def NAME(self):
            return self.getToken(CoasmParser.NAME, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_section_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSection_name" ):
                listener.enterSection_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSection_name" ):
                listener.exitSection_name(self)




    def section_name(self):

        localctx = CoasmParser.Section_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_section_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            _la = self._input.LA(1)
            if not(_la==CoasmParser.PREDEF_SECTION or _la==CoasmParser.SECTION):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 361
                self.match(CoasmParser.PREDEF_SECTION)


            self.state = 372
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CoasmParser.T__8 or _la==CoasmParser.T__9:
                self.state = 365
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CoasmParser.T__8:
                    self.state = 364
                    self.match(CoasmParser.T__8)


                self.state = 367
                self.match(CoasmParser.T__9)
                self.state = 368
                self.match(CoasmParser.NAME)
                self.state = 370
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CoasmParser.T__8:
                    self.state = 369
                    self.match(CoasmParser.T__8)




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Section_modifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(CoasmParser.NAME, 0)

        def DIGIT(self):
            return self.getToken(CoasmParser.DIGIT, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_section_modifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSection_modifier" ):
                listener.enterSection_modifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSection_modifier" ):
                listener.exitSection_modifier(self)




    def section_modifier(self):

        localctx = CoasmParser.Section_modifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_section_modifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CoasmParser.T__8) | (1 << CoasmParser.T__10) | (1 << CoasmParser.T__11))) != 0):
                self.state = 374
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CoasmParser.T__8) | (1 << CoasmParser.T__10) | (1 << CoasmParser.T__11))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 377
            _la = self._input.LA(1)
            if not(_la==CoasmParser.NAME or _la==CoasmParser.DIGIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 379
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CoasmParser.T__8:
                self.state = 378
                self.match(CoasmParser.T__8)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Link_directiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXTERN(self):
            return self.getToken(CoasmParser.EXTERN, 0)

        def ident(self):
            return self.getTypedRuleContext(CoasmParser.IdentContext,0)


        def VISIBLE(self):
            return self.getToken(CoasmParser.VISIBLE, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_link_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLink_directive" ):
                listener.enterLink_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLink_directive" ):
                listener.exitLink_directive(self)




    def link_directive(self):

        localctx = CoasmParser.Link_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_link_directive)
        try:
            self.state = 385
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CoasmParser.EXTERN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.match(CoasmParser.EXTERN)
                self.state = 382
                self.ident()
                pass
            elif token in [CoasmParser.VISIBLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 383
                self.match(CoasmParser.VISIBLE)
                self.state = 384
                self.ident()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instrvalu(self):
            return self.getTypedRuleContext(CoasmParser.InstrvaluContext,0)


        def instrsalu(self):
            return self.getTypedRuleContext(CoasmParser.InstrsaluContext,0)


        def instrsmem(self):
            return self.getTypedRuleContext(CoasmParser.InstrsmemContext,0)


        def instrvmem(self):
            return self.getTypedRuleContext(CoasmParser.InstrvmemContext,0)


        def instrdmem(self):
            return self.getTypedRuleContext(CoasmParser.InstrdmemContext,0)


        def getRuleIndex(self):
            return CoasmParser.RULE_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction" ):
                listener.enterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction" ):
                listener.exitInstruction(self)




    def instruction(self):

        localctx = CoasmParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_instruction)
        try:
            self.state = 392
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CoasmParser.VALU_VOP2, CoasmParser.VALU_VOP1, CoasmParser.VALU_VOP3A, CoasmParser.VALU_VOP3B, CoasmParser.VALU_VOPCspecial_cc_reg]:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.instrvalu()
                pass
            elif token in [CoasmParser.SALU_SOP1, CoasmParser.SALU_SOP2, CoasmParser.SALU_SOPK, CoasmParser.SALU_SOPC, CoasmParser.SALU_SOPP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self.instrsalu()
                pass
            elif token in [CoasmParser.SMEM_SLS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 389
                self.instrsmem()
                pass
            elif token in [CoasmParser.VMEM_VMUBUF, CoasmParser.VMEM_VLS]:
                self.enterOuterAlt(localctx, 4)
                self.state = 390
                self.instrvmem()
                pass
            elif token in [CoasmParser.DMEM_DLS]:
                self.enterOuterAlt(localctx, 5)
                self.state = 391
                self.instrdmem()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Alu_expr_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def register_(self):
            return self.getTypedRuleContext(CoasmParser.Register_Context,0)


        def alu_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoasmParser.Alu_exprContext)
            else:
                return self.getTypedRuleContext(CoasmParser.Alu_exprContext,i)


        def FP_NUMBER(self):
            return self.getToken(CoasmParser.FP_NUMBER, 0)

        def HEX_NUMBER(self):
            return self.getToken(CoasmParser.HEX_NUMBER, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_alu_expr_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlu_expr_list" ):
                listener.enterAlu_expr_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlu_expr_list" ):
                listener.exitAlu_expr_list(self)




    def alu_expr_list(self):

        localctx = CoasmParser.Alu_expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_alu_expr_list)
        self._la = 0 # Token type
        try:
            self.state = 405
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CoasmParser.T__6, CoasmParser.T__7, CoasmParser.DREG, CoasmParser.DREG_INDEX, CoasmParser.VREG, CoasmParser.VREG_INDEX, CoasmParser.SREG, CoasmParser.SREG_INDEX]:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.register_()
                pass
            elif token in [CoasmParser.T__4, CoasmParser.TID, CoasmParser.PC, CoasmParser.NAME, CoasmParser.DIGIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.alu_expr()
                self.state = 400
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CoasmParser.T__1:
                    self.state = 396
                    self.match(CoasmParser.T__1)
                    self.state = 397
                    self.alu_expr()
                    self.state = 402
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [CoasmParser.FP_NUMBER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 403
                self.match(CoasmParser.FP_NUMBER)
                pass
            elif token in [CoasmParser.HEX_NUMBER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 404
                self.match(CoasmParser.HEX_NUMBER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Alu_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def alu_multiply_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoasmParser.Alu_multiply_exprContext)
            else:
                return self.getTypedRuleContext(CoasmParser.Alu_multiply_exprContext,i)


        def SIGN(self, i:int=None):
            if i is None:
                return self.getTokens(CoasmParser.SIGN)
            else:
                return self.getToken(CoasmParser.SIGN, i)

        def getRuleIndex(self):
            return CoasmParser.RULE_alu_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlu_expr" ):
                listener.enterAlu_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlu_expr" ):
                listener.exitAlu_expr(self)




    def alu_expr(self):

        localctx = CoasmParser.Alu_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_alu_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.alu_multiply_expr()
            self.state = 412
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CoasmParser.SIGN:
                self.state = 408
                self.match(CoasmParser.SIGN)
                self.state = 409
                self.alu_multiply_expr()
                self.state = 414
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Alu_multiply_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def alu_argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoasmParser.Alu_argumentContext)
            else:
                return self.getTypedRuleContext(CoasmParser.Alu_argumentContext,i)


        def MSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(CoasmParser.MSIGN)
            else:
                return self.getToken(CoasmParser.MSIGN, i)

        def getRuleIndex(self):
            return CoasmParser.RULE_alu_multiply_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlu_multiply_expr" ):
                listener.enterAlu_multiply_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlu_multiply_expr" ):
                listener.exitAlu_multiply_expr(self)




    def alu_multiply_expr(self):

        localctx = CoasmParser.Alu_multiply_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_alu_multiply_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.alu_argument()
            self.state = 420
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CoasmParser.MSIGN:
                self.state = 416
                self.match(CoasmParser.MSIGN)
                self.state = 417
                self.alu_argument()
                self.state = 422
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Alu_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self):
            return self.getToken(CoasmParser.DIGIT, 0)

        def ident(self):
            return self.getTypedRuleContext(CoasmParser.IdentContext,0)


        def internal_id(self):
            return self.getTypedRuleContext(CoasmParser.Internal_idContext,0)


        def alu_expr(self):
            return self.getTypedRuleContext(CoasmParser.Alu_exprContext,0)


        def getRuleIndex(self):
            return CoasmParser.RULE_alu_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlu_argument" ):
                listener.enterAlu_argument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlu_argument" ):
                listener.exitAlu_argument(self)




    def alu_argument(self):

        localctx = CoasmParser.Alu_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_alu_argument)
        try:
            self.state = 430
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CoasmParser.DIGIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 423
                self.match(CoasmParser.DIGIT)
                pass
            elif token in [CoasmParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 424
                self.ident()
                pass
            elif token in [CoasmParser.TID, CoasmParser.PC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 425
                self.internal_id()
                pass
            elif token in [CoasmParser.T__4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 426
                self.match(CoasmParser.T__4)
                self.state = 427
                self.alu_expr()
                self.state = 428
                self.match(CoasmParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lop_immContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self):
            return self.getToken(CoasmParser.DIGIT, 0)

        def HEX_NUMBER(self):
            return self.getToken(CoasmParser.HEX_NUMBER, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_lop_imm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLop_imm" ):
                listener.enterLop_imm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLop_imm" ):
                listener.exitLop_imm(self)




    def lop_imm(self):

        localctx = CoasmParser.Lop_immContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_lop_imm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            _la = self._input.LA(1)
            if not(_la==CoasmParser.DIGIT or _la==CoasmParser.HEX_NUMBER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrvaluContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VALU_VOP2(self):
            return self.getToken(CoasmParser.VALU_VOP2, 0)

        def vreg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoasmParser.VregContext)
            else:
                return self.getTypedRuleContext(CoasmParser.VregContext,i)


        def generic_reg_or_number(self):
            return self.getTypedRuleContext(CoasmParser.Generic_reg_or_numberContext,0)


        def special_operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoasmParser.Special_operandContext)
            else:
                return self.getTypedRuleContext(CoasmParser.Special_operandContext,i)


        def VALU_VOP1(self):
            return self.getToken(CoasmParser.VALU_VOP1, 0)

        def register_(self):
            return self.getTypedRuleContext(CoasmParser.Register_Context,0)


        def builtin_operand(self):
            return self.getTypedRuleContext(CoasmParser.Builtin_operandContext,0)


        def VALU_VOPCspecial_cc_reg(self):
            return self.getToken(CoasmParser.VALU_VOPCspecial_cc_reg, 0)

        def generic_reg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoasmParser.Generic_regContext)
            else:
                return self.getTypedRuleContext(CoasmParser.Generic_regContext,i)


        def VALU_VOP3A(self):
            return self.getToken(CoasmParser.VALU_VOP3A, 0)

        def VALU_VOP3B(self):
            return self.getToken(CoasmParser.VALU_VOP3B, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_instrvalu

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrvalu" ):
                listener.enterInstrvalu(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrvalu" ):
                listener.exitInstrvalu(self)




    def instrvalu(self):

        localctx = CoasmParser.InstrvaluContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_instrvalu)
        self._la = 0 # Token type
        try:
            self.state = 482
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CoasmParser.VALU_VOP2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 434
                self.match(CoasmParser.VALU_VOP2)
                self.state = 435
                self.vreg()
                self.state = 436
                self.match(CoasmParser.T__1)
                self.state = 437
                self.generic_reg_or_number()
                self.state = 438
                self.match(CoasmParser.T__1)
                self.state = 439
                self.vreg()
                self.state = 444
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CoasmParser.T__1:
                    self.state = 440
                    self.match(CoasmParser.T__1)
                    self.state = 441
                    self.special_operand()
                    self.state = 446
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [CoasmParser.VALU_VOP1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 447
                self.match(CoasmParser.VALU_VOP1)
                self.state = 448
                self.vreg()
                self.state = 449
                self.match(CoasmParser.T__1)
                self.state = 452
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CoasmParser.T__6, CoasmParser.T__7, CoasmParser.DREG, CoasmParser.DREG_INDEX, CoasmParser.VREG, CoasmParser.VREG_INDEX, CoasmParser.SREG, CoasmParser.SREG_INDEX]:
                    self.state = 450
                    self.register_()
                    pass
                elif token in [CoasmParser.NAME]:
                    self.state = 451
                    self.builtin_operand()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [CoasmParser.VALU_VOPCspecial_cc_reg]:
                self.enterOuterAlt(localctx, 3)
                self.state = 454
                self.match(CoasmParser.VALU_VOPCspecial_cc_reg)
                self.state = 455
                self.match(CoasmParser.T__1)
                self.state = 456
                self.vreg()
                self.state = 457
                self.match(CoasmParser.T__1)
                self.state = 458
                self.generic_reg()
                pass
            elif token in [CoasmParser.VALU_VOP3A]:
                self.enterOuterAlt(localctx, 4)
                self.state = 460
                self.match(CoasmParser.VALU_VOP3A)
                self.state = 461
                self.vreg()
                self.state = 462
                self.match(CoasmParser.T__1)
                self.state = 463
                self.generic_reg()
                self.state = 464
                self.match(CoasmParser.T__1)
                self.state = 465
                self.generic_reg()
                self.state = 466
                self.match(CoasmParser.T__1)
                self.state = 467
                self.generic_reg()
                pass
            elif token in [CoasmParser.VALU_VOP3B]:
                self.enterOuterAlt(localctx, 5)
                self.state = 469
                self.match(CoasmParser.VALU_VOP3B)
                self.state = 470
                self.vreg()
                self.state = 471
                self.match(CoasmParser.T__1)
                self.state = 472
                self.generic_reg_or_number()
                self.state = 473
                self.match(CoasmParser.T__1)
                self.state = 474
                self.vreg()
                self.state = 479
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CoasmParser.T__1:
                    self.state = 475
                    self.match(CoasmParser.T__1)
                    self.state = 476
                    self.special_operand()
                    self.state = 481
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrsaluContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SALU_SOP1(self):
            return self.getToken(CoasmParser.SALU_SOP1, 0)

        def sreg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoasmParser.SregContext)
            else:
                return self.getTypedRuleContext(CoasmParser.SregContext,i)


        def SALU_SOP2(self):
            return self.getToken(CoasmParser.SALU_SOP2, 0)

        def SALU_SOPK(self):
            return self.getToken(CoasmParser.SALU_SOPK, 0)

        def number(self):
            return self.getTypedRuleContext(CoasmParser.NumberContext,0)


        def SALU_SOPC(self):
            return self.getToken(CoasmParser.SALU_SOPC, 0)

        def SALU_SOPP(self):
            return self.getToken(CoasmParser.SALU_SOPP, 0)

        def wait_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoasmParser.Wait_exprContext)
            else:
                return self.getTypedRuleContext(CoasmParser.Wait_exprContext,i)


        def getRuleIndex(self):
            return CoasmParser.RULE_instrsalu

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrsalu" ):
                listener.enterInstrsalu(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrsalu" ):
                listener.exitInstrsalu(self)




    def instrsalu(self):

        localctx = CoasmParser.InstrsaluContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_instrsalu)
        self._la = 0 # Token type
        try:
            self.state = 518
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CoasmParser.SALU_SOP1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 484
                self.match(CoasmParser.SALU_SOP1)
                self.state = 485
                self.sreg()
                self.state = 486
                self.match(CoasmParser.T__1)
                self.state = 487
                self.sreg()
                pass
            elif token in [CoasmParser.SALU_SOP2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 489
                self.match(CoasmParser.SALU_SOP2)
                self.state = 490
                self.sreg()
                self.state = 491
                self.match(CoasmParser.T__1)
                self.state = 492
                self.sreg()
                self.state = 493
                self.match(CoasmParser.T__1)
                self.state = 494
                self.sreg()
                pass
            elif token in [CoasmParser.SALU_SOPK]:
                self.enterOuterAlt(localctx, 3)
                self.state = 496
                self.match(CoasmParser.SALU_SOPK)
                self.state = 497
                self.sreg()
                self.state = 498
                self.match(CoasmParser.T__1)
                self.state = 499
                self.number()
                pass
            elif token in [CoasmParser.SALU_SOPC]:
                self.enterOuterAlt(localctx, 4)
                self.state = 501
                self.match(CoasmParser.SALU_SOPC)
                self.state = 502
                self.sreg()
                self.state = 503
                self.match(CoasmParser.T__1)
                self.state = 504
                self.sreg()
                pass
            elif token in [CoasmParser.SALU_SOPP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 506
                self.match(CoasmParser.SALU_SOPP)
                self.state = 516
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CoasmParser.DIGIT, CoasmParser.HEX_NUMBER, CoasmParser.FP_NUMBER]:
                    self.state = 507
                    self.number()
                    pass
                elif token in [CoasmParser.WAIT_TYPE]:
                    self.state = 508
                    self.wait_expr()
                    self.state = 513
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==CoasmParser.T__1:
                        self.state = 509
                        self.match(CoasmParser.T__1)
                        self.state = 510
                        self.wait_expr()
                        self.state = 515
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass
                elif token in [CoasmParser.EOF, CoasmParser.KERNEL_OPTION_KEY, CoasmParser.ALIAS, CoasmParser.REG, CoasmParser.VALU_VOP2, CoasmParser.VALU_VOP1, CoasmParser.VALU_VOP3A, CoasmParser.VALU_VOP3B, CoasmParser.SALU_SOP1, CoasmParser.SALU_SOP2, CoasmParser.SALU_SOPK, CoasmParser.SALU_SOPC, CoasmParser.SALU_SOPP, CoasmParser.SMEM_SLS, CoasmParser.VMEM_VMUBUF, CoasmParser.VMEM_VLS, CoasmParser.DMEM_DLS, CoasmParser.LINE_COMMENT, CoasmParser.NAME, CoasmParser.MEM_SPACE, CoasmParser.DATA_DIRECTIVE, CoasmParser.START_KERNEL, CoasmParser.END_KERNEL, CoasmParser.TYPE, CoasmParser.INST, CoasmParser.P2ALIGN, CoasmParser.SIZE, CoasmParser.IDENT, CoasmParser.EXTERN, CoasmParser.VISIBLE, CoasmParser.PREDEF_SECTION, CoasmParser.SECTION, CoasmParser.VALU_VOPCspecial_cc_reg]:
                    pass
                else:
                    pass
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrsmemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SMEM_SLS(self):
            return self.getToken(CoasmParser.SMEM_SLS, 0)

        def sreg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoasmParser.SregContext)
            else:
                return self.getTypedRuleContext(CoasmParser.SregContext,i)


        def ident(self):
            return self.getTypedRuleContext(CoasmParser.IdentContext,0)


        def number(self):
            return self.getTypedRuleContext(CoasmParser.NumberContext,0)


        def mspace_all(self):
            return self.getTypedRuleContext(CoasmParser.Mspace_allContext,0)


        def getRuleIndex(self):
            return CoasmParser.RULE_instrsmem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrsmem" ):
                listener.enterInstrsmem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrsmem" ):
                listener.exitInstrsmem(self)




    def instrsmem(self):

        localctx = CoasmParser.InstrsmemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_instrsmem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self.match(CoasmParser.SMEM_SLS)
            self.state = 523
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CoasmParser.T__6, CoasmParser.T__7, CoasmParser.SREG, CoasmParser.SREG_INDEX]:
                self.state = 521
                self.sreg()
                pass
            elif token in [CoasmParser.NAME]:
                self.state = 522
                self.ident()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 525
            self.match(CoasmParser.T__1)
            self.state = 526
            self.sreg()
            self.state = 527
            self.match(CoasmParser.T__1)
            self.state = 530
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CoasmParser.T__6, CoasmParser.T__7, CoasmParser.SREG, CoasmParser.SREG_INDEX]:
                self.state = 528
                self.sreg()
                pass
            elif token in [CoasmParser.DIGIT, CoasmParser.HEX_NUMBER, CoasmParser.FP_NUMBER]:
                self.state = 529
                self.number()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 534
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CoasmParser.T__12:
                self.state = 532
                self.match(CoasmParser.T__12)
                self.state = 533
                self.mspace_all()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrvmemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VMEM_VMUBUF(self):
            return self.getToken(CoasmParser.VMEM_VMUBUF, 0)

        def vreg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoasmParser.VregContext)
            else:
                return self.getTypedRuleContext(CoasmParser.VregContext,i)


        def sreg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoasmParser.SregContext)
            else:
                return self.getTypedRuleContext(CoasmParser.SregContext,i)


        def VMEM_VLS(self):
            return self.getToken(CoasmParser.VMEM_VLS, 0)

        def dreg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoasmParser.DregContext)
            else:
                return self.getTypedRuleContext(CoasmParser.DregContext,i)


        def vmem_special_operand(self):
            return self.getTypedRuleContext(CoasmParser.Vmem_special_operandContext,0)


        def number(self):
            return self.getTypedRuleContext(CoasmParser.NumberContext,0)


        def mspace_all(self):
            return self.getTypedRuleContext(CoasmParser.Mspace_allContext,0)


        def getRuleIndex(self):
            return CoasmParser.RULE_instrvmem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrvmem" ):
                listener.enterInstrvmem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrvmem" ):
                listener.exitInstrvmem(self)




    def instrvmem(self):

        localctx = CoasmParser.InstrvmemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_instrvmem)
        self._la = 0 # Token type
        try:
            self.state = 563
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CoasmParser.VMEM_VMUBUF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 536
                self.match(CoasmParser.VMEM_VMUBUF)
                self.state = 537
                self.vreg()
                self.state = 538
                self.match(CoasmParser.T__1)
                self.state = 539
                self.vreg()
                self.state = 540
                self.match(CoasmParser.T__1)
                self.state = 541
                self.sreg()
                self.state = 542
                self.match(CoasmParser.T__1)
                self.state = 543
                self.sreg()
                pass
            elif token in [CoasmParser.VMEM_VLS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 545
                self.match(CoasmParser.VMEM_VLS)
                self.state = 546
                self.vreg()
                self.state = 547
                self.match(CoasmParser.T__1)
                self.state = 551
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                if la_ == 1:
                    self.state = 548
                    self.vreg()
                    pass

                elif la_ == 2:
                    self.state = 549
                    self.dreg()
                    pass

                elif la_ == 3:
                    self.state = 550
                    self.vmem_special_operand()
                    pass


                self.state = 553
                self.match(CoasmParser.T__1)
                self.state = 557
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
                if la_ == 1:
                    self.state = 554
                    self.vreg()
                    pass

                elif la_ == 2:
                    self.state = 555
                    self.dreg()
                    pass

                elif la_ == 3:
                    self.state = 556
                    self.number()
                    pass


                self.state = 561
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CoasmParser.T__12:
                    self.state = 559
                    self.match(CoasmParser.T__12)
                    self.state = 560
                    self.mspace_all()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrdmemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DMEM_DLS(self):
            return self.getToken(CoasmParser.DMEM_DLS, 0)

        def mem_expr_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoasmParser.Mem_expr_listContext)
            else:
                return self.getTypedRuleContext(CoasmParser.Mem_expr_listContext,i)


        def vreg(self):
            return self.getTypedRuleContext(CoasmParser.VregContext,0)


        def ident(self):
            return self.getTypedRuleContext(CoasmParser.IdentContext,0)


        def getRuleIndex(self):
            return CoasmParser.RULE_instrdmem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrdmem" ):
                listener.enterInstrdmem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrdmem" ):
                listener.exitInstrdmem(self)




    def instrdmem(self):

        localctx = CoasmParser.InstrdmemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_instrdmem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 565
            self.match(CoasmParser.DMEM_DLS)
            self.state = 569
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CoasmParser.T__6, CoasmParser.T__7, CoasmParser.VREG, CoasmParser.VREG_INDEX]:
                self.state = 566
                self.vreg()
                pass
            elif token in [CoasmParser.NAME]:
                self.state = 567
                self.ident()
                pass
            elif token in [CoasmParser.T__2]:
                self.state = 568
                self.mem_expr_list()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 571
            self.match(CoasmParser.T__1)
            self.state = 572
            self.mem_expr_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mem_expr_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mem_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CoasmParser.Mem_exprContext)
            else:
                return self.getTypedRuleContext(CoasmParser.Mem_exprContext,i)


        def SIGN(self, i:int=None):
            if i is None:
                return self.getTokens(CoasmParser.SIGN)
            else:
                return self.getToken(CoasmParser.SIGN, i)

        def getRuleIndex(self):
            return CoasmParser.RULE_mem_expr_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMem_expr_list" ):
                listener.enterMem_expr_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMem_expr_list" ):
                listener.exitMem_expr_list(self)




    def mem_expr_list(self):

        localctx = CoasmParser.Mem_expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_mem_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            self.match(CoasmParser.T__2)
            self.state = 575
            self.mem_expr()
            self.state = 580
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CoasmParser.SIGN:
                self.state = 576
                self.match(CoasmParser.SIGN)
                self.state = 577
                self.mem_expr()
                self.state = 582
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 583
            self.match(CoasmParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mem_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mem_off(self):
            return self.getTypedRuleContext(CoasmParser.Mem_offContext,0)


        def mem_idx_expr(self):
            return self.getTypedRuleContext(CoasmParser.Mem_idx_exprContext,0)


        def getRuleIndex(self):
            return CoasmParser.RULE_mem_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMem_expr" ):
                listener.enterMem_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMem_expr" ):
                listener.exitMem_expr(self)




    def mem_expr(self):

        localctx = CoasmParser.Mem_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_mem_expr)
        try:
            self.state = 587
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 585
                self.mem_off()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 586
                self.mem_idx_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mem_offContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self):
            return self.getToken(CoasmParser.DIGIT, 0)

        def HEX_NUMBER(self):
            return self.getToken(CoasmParser.HEX_NUMBER, 0)

        def ident(self):
            return self.getTypedRuleContext(CoasmParser.IdentContext,0)


        def sreg(self):
            return self.getTypedRuleContext(CoasmParser.SregContext,0)


        def vreg(self):
            return self.getTypedRuleContext(CoasmParser.VregContext,0)


        def getRuleIndex(self):
            return CoasmParser.RULE_mem_off

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMem_off" ):
                listener.enterMem_off(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMem_off" ):
                listener.exitMem_off(self)




    def mem_off(self):

        localctx = CoasmParser.Mem_offContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_mem_off)
        try:
            self.state = 594
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 589
                self.match(CoasmParser.DIGIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 590
                self.match(CoasmParser.HEX_NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 591
                self.ident()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 592
                self.sreg()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 593
                self.vreg()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mem_idx_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mem_idx(self):
            return self.getTypedRuleContext(CoasmParser.Mem_idxContext,0)


        def MSIGN(self):
            return self.getToken(CoasmParser.MSIGN, 0)

        def mem_stride(self):
            return self.getTypedRuleContext(CoasmParser.Mem_strideContext,0)


        def getRuleIndex(self):
            return CoasmParser.RULE_mem_idx_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMem_idx_expr" ):
                listener.enterMem_idx_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMem_idx_expr" ):
                listener.exitMem_idx_expr(self)




    def mem_idx_expr(self):

        localctx = CoasmParser.Mem_idx_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_mem_idx_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 596
            self.mem_idx()
            self.state = 597
            self.match(CoasmParser.MSIGN)
            self.state = 598
            self.mem_stride()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mem_idxContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vreg(self):
            return self.getTypedRuleContext(CoasmParser.VregContext,0)


        def ident(self):
            return self.getTypedRuleContext(CoasmParser.IdentContext,0)


        def TID(self):
            return self.getToken(CoasmParser.TID, 0)

        def SIGN(self):
            return self.getToken(CoasmParser.SIGN, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_mem_idx

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMem_idx" ):
                listener.enterMem_idx(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMem_idx" ):
                listener.exitMem_idx(self)




    def mem_idx(self):

        localctx = CoasmParser.Mem_idxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_mem_idx)
        try:
            self.state = 612
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CoasmParser.T__6, CoasmParser.T__7, CoasmParser.VREG, CoasmParser.VREG_INDEX]:
                self.enterOuterAlt(localctx, 1)
                self.state = 600
                self.vreg()
                pass
            elif token in [CoasmParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 601
                self.ident()
                pass
            elif token in [CoasmParser.TID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 602
                self.match(CoasmParser.TID)
                pass
            elif token in [CoasmParser.T__4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 603
                self.match(CoasmParser.T__4)
                self.state = 606
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CoasmParser.T__6, CoasmParser.T__7, CoasmParser.VREG, CoasmParser.VREG_INDEX]:
                    self.state = 604
                    self.vreg()
                    pass
                elif token in [CoasmParser.NAME]:
                    self.state = 605
                    self.ident()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 608
                self.match(CoasmParser.SIGN)
                self.state = 609
                self.match(CoasmParser.TID)
                self.state = 610
                self.match(CoasmParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mem_strideContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self):
            return self.getToken(CoasmParser.DIGIT, 0)

        def HEX_NUMBER(self):
            return self.getToken(CoasmParser.HEX_NUMBER, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_mem_stride

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMem_stride" ):
                listener.enterMem_stride(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMem_stride" ):
                listener.exitMem_stride(self)




    def mem_stride(self):

        localctx = CoasmParser.Mem_strideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_mem_stride)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 614
            _la = self._input.LA(1)
            if not(_la==CoasmParser.DIGIT or _la==CoasmParser.HEX_NUMBER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mem_baseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def register_(self):
            return self.getTypedRuleContext(CoasmParser.Register_Context,0)


        def ident(self):
            return self.getTypedRuleContext(CoasmParser.IdentContext,0)


        def getRuleIndex(self):
            return CoasmParser.RULE_mem_base

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMem_base" ):
                listener.enterMem_base(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMem_base" ):
                listener.exitMem_base(self)




    def mem_base(self):

        localctx = CoasmParser.Mem_baseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_mem_base)
        try:
            self.state = 618
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CoasmParser.T__6, CoasmParser.T__7, CoasmParser.DREG, CoasmParser.DREG_INDEX, CoasmParser.VREG, CoasmParser.VREG_INDEX, CoasmParser.SREG, CoasmParser.SREG_INDEX]:
                self.enterOuterAlt(localctx, 1)
                self.state = 616
                self.register_()
                pass
            elif token in [CoasmParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 617
                self.ident()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(CoasmParser.COMMENT, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = CoasmParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 620
            self.match(CoasmParser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Line_commentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINE_COMMENT(self):
            return self.getToken(CoasmParser.LINE_COMMENT, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_line_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine_comment" ):
                listener.enterLine_comment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine_comment" ):
                listener.exitLine_comment(self)




    def line_comment(self):

        localctx = CoasmParser.Line_commentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_line_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 622
            self.match(CoasmParser.LINE_COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Wait_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WAIT_TYPE(self):
            return self.getToken(CoasmParser.WAIT_TYPE, 0)

        def DIGIT(self):
            return self.getToken(CoasmParser.DIGIT, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_wait_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWait_expr" ):
                listener.enterWait_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWait_expr" ):
                listener.exitWait_expr(self)




    def wait_expr(self):

        localctx = CoasmParser.Wait_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_wait_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 624
            self.match(CoasmParser.WAIT_TYPE)
            self.state = 628
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CoasmParser.T__4:
                self.state = 625
                self.match(CoasmParser.T__4)
                self.state = 626
                self.match(CoasmParser.DIGIT)
                self.state = 627
                self.match(CoasmParser.T__5)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(CoasmParser.NAME, 0)

        def getRuleIndex(self):
            return CoasmParser.RULE_ident

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdent" ):
                listener.enterIdent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdent" ):
                listener.exitIdent(self)




    def ident(self):

        localctx = CoasmParser.IdentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_ident)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 630
            self.match(CoasmParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





