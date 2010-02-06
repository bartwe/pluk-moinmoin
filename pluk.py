"""
 
 Author: Bart van der Werf aka bartwe <bluelive@gmail.com>
 Copyright (C) 2010 Bart van der Werf aka bartwe <bluelive@gmail.com>
 
 This library is free software; you can redistribute it and/or
 modify it under the terms of the GNU Library General Public
 License as published by the Free Software Foundation; either
 version 2 of the License, or (at your option) any later version.
 
 This library is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 Library General Public License for more details.
 
 You should have received a copy of the GNU Library General Public
 License along with this library; if not, write to the
 Free Software Foundation, Inc., 59 Temple Place - Suite 330,
 Boston, MA 02111-1307, USA.

    MoinMoin - Pluk Source Parser

css:

pre.plukarea     { font-style: sans-serif; color: #000000; }

pre.plukarea span.ID       { color: #000000; }
pre.plukarea span.Char     { color: #004080; }
pre.plukarea span.Comment  { color: #808080; }
pre.plukarea span.Number   { color: #008080; font-weight: bold; }
pre.plukarea span.String   { color: #004080; }
pre.plukarea span.SPChar   { color: #0000C0; }
pre.plukarea span.ResWord  { color: #4040ff; font-weight: bold; }
pre.plukarea span.ConsWord { color: #008080; font-weight: bold; }
pre.plukarea span.ResWord2 { color: #0080ff; font-weight: bold; }
pre.plukarea span.Special  { color: #0000ff; }
pre.plukarea span.Preprc   { color: #804000; }

"""

from MoinMoin.parser._ParserBase import ParserBase

Dependencies = ['user']

class Parser(ParserBase):

    parsername = "ColorizedPluk"
    extensions = ['.pluk']
    Dependencies = Dependencies

    def setupRules(self):
        ParserBase.setupRules(self)

        self.addRulePair("Comment", r"/[*]", r"[*]/")
        self.addRule("Comment", r"//.*$")
        self.addRulePair("String", r'"', r'[^\\]"')
        self.addRule("Number", r"[0-9](\.[0-9]*)?(eE[+-][0-9])?|0[xXcCbB][0-9a-fA-F]+[Ll]?")
        self.addRule("ID", r"[a-zA-Z_][0-9a-zA-Z_]*")
        self.addRule("SPChar", r"[~!%^&*()+=|\[\]:;,.<>/?{}-]")

        reserved_words = ['break', 'catch', 'continue', 'else', 'finally',
        'for', 'if', 'return', 'recur', 'throw', 'try', 'while', 'with',
        'scope', 'new', 'this', 'private', 'public', 'internal', 'class',
        'abstract', 'static', 'extern', 'override']

        self.addReserved(reserved_words)

        reserved_words2 = ['import']

        special_words = ['bool', 'byte', 'float', 'int', 'void',
        'string']

        constant_words = ['true', 'false', 'null']

        self.addConstant(constant_words)

        self.addWords(reserved_words2, 'ResWord2')
        self.addWords(special_words, 'Special')
