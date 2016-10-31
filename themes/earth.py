
# -*- coding: utf-8 -*-

"""
    Ex.Co. LICENSE :
        This file is part of Ex.Co..

        Ex.Co. is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        Ex.Co. is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.

        You should have received a copy of the GNU General Public License
        along with Ex.Co..  If not, see <http://www.gnu.org/licenses/>.


    PYTHON LICENSE :
        "Python" and the Python logos are trademarks or registered trademarks of the Python Software Foundation,
        used by Ex.Co. with permission from the Foundation


    Cython LICENSE:
        Cython is freely available under the open source Apache License


    PyQt4 LICENSE :
        PyQt4 is licensed under the GNU General Public License version 3
    PyQt Alternative Logo LICENSE:
        The PyQt Alternative Logo is licensed under Creative Commons CC0 1.0 Universal Public Domain Dedication


    Qt Logo LICENSE:
        The Qt logo is copyright of Digia Plc and/or its subsidiaries.
        Digia, Qt and their respective logos are trademarks of Digia Corporation in Finland and/or other countries worldwide.


    Tango Icons LICENSE:
        The Tango base icon theme is released to the Public Domain.
        The Tango base icon theme is made possible by the Tango Desktop Project.
    
    My Tango Style Icons LICENSE:
        The Tango icons I created are released under the GNU General Public License version 3.
    
    
    Eric6 LICENSE:
        Eric6 IDE is licensed under the GNU General Public License version 3


    Nuitka LICENSE:
        Nuitka is a Python compiler compatible with Ex.Co..
        Nuitka is freely available under the open source Apache License.
"""

##  FILE DESCRIPTION:
##      Earth theme

import PyQt4.QtGui


Form = "#585a55"
Cursor = PyQt4.QtGui.QColor(0xff, 0xff, 0xff)


class FoldMargin:
    ForeGround = PyQt4.QtGui.QColor(0xffffffff)
    BackGround = PyQt4.QtGui.QColor(0xff2e3436)


class LineMargin:
    ForeGround = PyQt4.QtGui.QColor(0xffffffff)
    BackGround = PyQt4.QtGui.QColor(0xff2e3436)


class Indication:
    Font = "#e6e6e6"
    ActiveBackGround = "#1a0f0b"
    ActiveBorder = "#e6e6e6"
    PassiveBackGround = "#585a55"
    PassiveBorder = "#b3935c"


class TextDifferColors:
    Indicator_Unique_1_Color = PyQt4.QtGui.QColor(0x72, 0x9f, 0xcf, 80)
    Indicator_Unique_2_Color = PyQt4.QtGui.QColor(0xad, 0x7f, 0xa8, 80)
    Indicator_Similar_Color = PyQt4.QtGui.QColor(0x8a, 0xe2, 0x34, 80)

    
class Font:
    Default = PyQt4.QtGui.QColor(0xfff7f1c1)
    
    class Repl:
        """
        THE MESSAGE COLORS ARE: 0xBBGGRR (BB-blue,GG-green,RR-red)
        """
        Error = 0x0000ff
        Warning = 0xe4761f
        Success = 0x007f00
        Diff_Unique_1 = 0xcf9f72
        Diff_Unique_2 = 0xa87fad
        Diff_Similar = 0x069a4e
        
    
    class Ada:
        Default = ('Courier', 0xfff7f1c1, 10, None)
        Comment = ('Courier', 0xff679d47, 10, None)
        Keyword = ('Courier', 0xff519872, 10, None)
        String = ('Courier', 0xff7ca563, 10, None)
        Procedure = ('Courier', 0xffb3935c, 10, None)
        Number = ('Courier', 0xff6c9686, 10, None)
        Type = ('Courier', 0xff519872, 10, None)
        Package = ('Courier', 0xffe1aa7d, 10, None)
    
    class Nim:
        Default = ('Courier', 0xfff7f1c1, 10, None)
        Comment = ('Courier', 0xff679d47, 10, None)
        BasicKeyword = ('Courier', 0xff519872, 10, True)
        TopKeyword = ('Courier', 0xff407fc0, 10, True)
        String = ('Courier', 0xff7ca563, 10, None)
        LongString = ('Courier', 0xffe1aa7d, 10, None)
        Number = ('Courier', 0xff6c9686, 10, None)
        Operator = ('Courier', 0xff7f7f7f, 10, None)
        Unsafe = ('Courier', 0xffc00000, 10, True)
        Type = ('Courier', 0xff6e6e00, 10, True)
        DocumentationComment = ('Courier', 0xff7f0a0a, 10, None)
        Definition = ('Courier', 0xff6c9686, 10, None)
        Class = ('Courier', 0xffb3935c, 10, None)
        KeywordOperator = ('Courier', 0xff963cc8, 10, None)
        CharLiteral = ('Courier', 0xff00c8ff, 10, None)
        CaseOf = ('Courier', 0xff8000ff, 10, None)
        UserKeyword = ('Courier', 0xffff8040, 10, None)
        MultilineComment = ('Courier', 0xff006c6c, 10, None)
        MultilineDocumentation = ('Courier', 0xff6e3296, 10, None)
        Pragma = ('Courier', 0xffc07f40, 10, None)
    
    class Oberon:
        Default = ('Courier', 0xfff7f1c1, 10, None)
        Comment = ('Courier', 0xff679d47, 10, None)
        Keyword = ('Courier', 0xff519872, 10, None)
        String = ('Courier', 0xff7ca563, 10, None)
        Procedure = ('Courier', 0xffb3935c, 10, None)
        Module = ('Courier', 0xffe1aa7d, 10, None)
        Number = ('Courier', 0xff6c9686, 10, None)
        Type = ('Courier', 0xff519872, 10, None)
    
    
    class AVS:
        BlockComment = ('Courier', 0xff679d47, 10, None)
        ClipProperty = ('Courier', 0xff519872, 10, None)
        Default = ('Courier', 0xfff7f1c1, 10, None)
        Filter = ('Courier', 0xff519872, 10, None)
        Function = ('Courier', 0xff6c9686, 10, None)
        Identifier = ('Courier', 0xfff7f1c1, 10, None)
        Keyword = ('Courier', 0xff519872, 10, None)
        KeywordSet6 = ('Courier', 0xff8000ff, 10, None)
        LineComment = ('Courier', 0xff679d47, 10, None)
        NestedBlockComment = ('Courier', 0xff679d47, 10, None)
        Number = ('Courier', 0xff6c9686, 10, None)
        Operator = ('Courier', 0xfff7f1c1, 10, None)
        Plugin = ('Courier', 0xff0080c0, 10, None)
        String = ('Courier', 0xff7ca563, 10, None)
        TripleString = ('Courier', 0xff7ca563, 10, None)
    
    class Bash:
        Backticks = ('Courier', 0xffffff00, 10, None)
        Comment = ('Courier', 0xff679d47, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xffc48e7b, 10, None)
        Error = ('Courier', 0xffaa0000, 10, True)
        HereDocumentDelimiter = ('Courier', 0xfff7f1c1, 10, None)
        Identifier = ('Courier', 0xfff7f1c1, 10, None)
        Keyword = ('Courier', 0xff519872, 10, None)
        Number = ('Courier', 0xff6c9686, 10, None)
        Operator = ('Courier', 0xfff7f1c1, 10, None)
        ParameterExpansion = ('Courier', 0xfff7f1c1, 10, None)
        Scalar = ('Courier', 0xfffce94f, 10, True)
        SingleQuotedHereDocument = ('Courier', 0xff7ca563, 10, None)
        SingleQuotedString = ('Courier', 0xff7ca563, 10, None)
    
    class Batch:
        Comment = ('Courier', 0xff679d47, 10, None)
        Default = ('Courier', 0xfff7f1c1, 10, None)
        ExternalCommand = ('Courier', 0xff519872, 10, None)
        HideCommandChar = ('Courier', 0xff7f7f00, 10, None)
        Keyword = ('Courier', 0xff519872, 10, None)
        Label = ('Courier', 0xff7ca563, 10, None)
        Operator = ('Courier', 0xfff7f1c1, 10, None)
        Variable = ('Courier', 0xff800080, 10, None)
    
    class CMake:
        BlockForeach = ('Courier', 0xff519872, 10, None)
        BlockIf = ('Courier', 0xff519872, 10, None)
        BlockMacro = ('Courier', 0xff519872, 10, None)
        BlockWhile = ('Courier', 0xff519872, 10, None)
        Comment = ('Courier', 0xff679d47, 10, None)
        Default = ('Courier', 0xfff7f1c1, 10, None)
        Function = ('Courier', 0xff519872, 10, None)
        KeywordSet3 = ('Courier', 0xfff7f1c1, 10, None)
        Label = ('Courier', 0xffcc3300, 10, None)
        Number = ('Courier', 0xff6c9686, 10, None)
        String = ('Courier', 0xff7ca563, 10, None)
        StringLeftQuote = ('Courier', 0xff7ca563, 10, None)
        StringRightQuote = ('Courier', 0xff7ca563, 10, None)
        StringVariable = ('Courier', 0xffcc3300, 10, None)
        Variable = ('Courier', 0xff800000, 10, None)
    
    class CPP:
        Comment = ('Courier', 0xff679d47, 10, None)
        CommentDoc = ('Courier', 0xff3f703f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff679d47, 10, None)
        CommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xff7ca563, 10, None)
        GlobalClass = ('Courier', 0xfff7f1c1, 10, None)
        HashQuotedString = ('Courier', 0xff679d47, 10, None)
        Identifier = ('Courier', 0xfff7f1c1, 10, None)
        InactiveComment = ('Courier', 0xff90b090, 10, None)
        InactiveCommentDoc = ('Courier', 0xffd0d0d0, 10, None)
        InactiveCommentDocKeyword = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentDocKeywordError = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentLine = ('Courier', 0xff90b090, 10, None)
        InactiveCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDefault = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDoubleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveGlobalClass = ('Courier', 0xffb0b0b0, 10, None)
        InactiveHashQuotedString = ('Courier', 0xfff7f1c1, 10, None)
        InactiveIdentifier = ('Courier', 0xffb0b0b0, 10, None)
        InactiveKeyword = ('Courier', 0xff9090b0, 10, None)
        InactiveKeywordSet2 = ('Courier', 0xffc0c0c0, 10, None)
        InactiveNumber = ('Courier', 0xff90b090, 10, None)
        InactiveOperator = ('Courier', 0xffb0b0b0, 10, None)
        InactivePreProcessor = ('Courier', 0xffb0b090, 10, None)
        InactivePreProcessorComment = ('Courier', 0xff1a0f0b, 10, None)
        InactivePreProcessorCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveRawString = ('Courier', 0xfff7f1c1, 10, None)
        InactiveRegex = ('Courier', 0xff7faf7f, 10, None)
        InactiveSingleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveTripleQuotedVerbatimString = ('Courier', 0xfff7f1c1, 10, None)
        InactiveUUID = ('Courier', 0xffc0c0c0, 10, None)
        InactiveUnclosedString = ('Courier', 0xfff7f1c1, 10, None)
        InactiveVerbatimString = ('Courier', 0xff90b090, 10, None)
        Keyword = ('Courier', 0xff519872, 10, None)
        KeywordSet2 = ('Courier', 0xfff7f1c1, 10, None)
        Number = ('Courier', 0xff6c9686, 10, None)
        Operator = ('Courier', 0xfff7f1c1, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        PreProcessorComment = ('Courier', 0xff659900, 10, None)
        PreProcessorCommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        RawString = ('Courier', 0xff7ca563, 10, None)
        Regex = ('Courier', 0xff3f7f3f, 10, None)
        SingleQuotedString = ('Courier', 0xff7ca563, 10, None)
        TripleQuotedVerbatimString = ('Courier', 0xff679d47, 10, None)
        UUID = ('Courier', 0xfff7f1c1, 10, None)
        UnclosedString = ('Courier', 0xfff7f1c1, 10, None)
        VerbatimString = ('Courier', 0xff679d47, 10, None)
    
    class CSS:
        AtRule = ('Courier', 0xff7f7f00, 10, None)
        Attribute = ('Courier', 0xff800000, 10, None)
        CSS1Property = ('Courier', 0xff0040e0, 10, None)
        CSS2Property = ('Courier', 0xff00a0e0, 10, None)
        CSS3Property = ('Courier', 0xfff7f1c1, 10, None)
        ClassSelector = ('Courier', 0xfff7f1c1, 10, None)
        Comment = ('Courier', 0xff679d47, 10, None)
        Default = ('Courier', 0xffff0080, 10, None)
        DoubleQuotedString = ('Courier', 0xff7ca563, 10, None)
        ExtendedCSSProperty = ('Courier', 0xfff7f1c1, 10, None)
        ExtendedPseudoClass = ('Courier', 0xfff7f1c1, 10, None)
        ExtendedPseudoElement = ('Courier', 0xfff7f1c1, 10, None)
        IDSelector = ('Courier', 0xff6c9686, 10, None)
        Important = ('Courier', 0xffff8000, 10, None)
        MediaRule = ('Courier', 0xff7f7f00, 10, None)
        Operator = ('Courier', 0xfff7f1c1, 10, None)
        PseudoClass = ('Courier', 0xff800000, 10, None)
        PseudoElement = ('Courier', 0xfff7f1c1, 10, None)
        SingleQuotedString = ('Courier', 0xff7ca563, 10, None)
        Tag = ('Courier', 0xff519872, 10, None)
        UnknownProperty = ('Courier', 0xffff0000, 10, None)
        UnknownPseudoClass = ('Courier', 0xffff0000, 10, None)
        Value = ('Courier', 0xff7ca563, 10, None)
        Variable = ('Courier', 0xfff7f1c1, 10, None)
    
    class CSharp:
        Comment = ('Courier', 0xff679d47, 10, None)
        CommentDoc = ('Courier', 0xff3f703f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff679d47, 10, None)
        CommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xff7ca563, 10, None)
        GlobalClass = ('Courier', 0xfff7f1c1, 10, None)
        HashQuotedString = ('Courier', 0xff679d47, 10, None)
        Identifier = ('Courier', 0xfff7f1c1, 10, None)
        InactiveComment = ('Courier', 0xff90b090, 10, None)
        InactiveCommentDoc = ('Courier', 0xffd0d0d0, 10, None)
        InactiveCommentDocKeyword = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentDocKeywordError = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentLine = ('Courier', 0xff90b090, 10, None)
        InactiveCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDefault = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDoubleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveGlobalClass = ('Courier', 0xffb0b0b0, 10, None)
        InactiveHashQuotedString = ('Courier', 0xfff7f1c1, 10, None)
        InactiveIdentifier = ('Courier', 0xffb0b0b0, 10, None)
        InactiveKeyword = ('Courier', 0xff9090b0, 10, None)
        InactiveKeywordSet2 = ('Courier', 0xffc0c0c0, 10, None)
        InactiveNumber = ('Courier', 0xff90b090, 10, None)
        InactiveOperator = ('Courier', 0xffb0b0b0, 10, None)
        InactivePreProcessor = ('Courier', 0xffb0b090, 10, None)
        InactivePreProcessorComment = ('Courier', 0xff1a0f0b, 10, None)
        InactivePreProcessorCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveRawString = ('Courier', 0xfff7f1c1, 10, None)
        InactiveRegex = ('Courier', 0xff7faf7f, 10, None)
        InactiveSingleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveTripleQuotedVerbatimString = ('Courier', 0xfff7f1c1, 10, None)
        InactiveUUID = ('Courier', 0xffc0c0c0, 10, None)
        InactiveUnclosedString = ('Courier', 0xfff7f1c1, 10, None)
        InactiveVerbatimString = ('Courier', 0xff90b090, 10, None)
        Keyword = ('Courier', 0xff519872, 10, None)
        KeywordSet2 = ('Courier', 0xfff7f1c1, 10, None)
        Number = ('Courier', 0xff6c9686, 10, None)
        Operator = ('Courier', 0xfff7f1c1, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        PreProcessorComment = ('Courier', 0xff659900, 10, None)
        PreProcessorCommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        RawString = ('Courier', 0xff7ca563, 10, None)
        Regex = ('Courier', 0xff3f7f3f, 10, None)
        SingleQuotedString = ('Courier', 0xff7ca563, 10, None)
        TripleQuotedVerbatimString = ('Courier', 0xff679d47, 10, None)
        UUID = ('Courier', 0xfff7f1c1, 10, None)
        UnclosedString = ('Courier', 0xfff7f1c1, 10, None)
        VerbatimString = ('Courier', 0xff679d47, 10, None)
    
    class CoffeeScript:
        BlockRegex = ('Courier', 0xff3f7f3f, 10, None)
        BlockRegexComment = ('Courier', 0xff679d47, 10, None)
        Comment = ('Courier', 0xff679d47, 10, None)
        CommentBlock = ('Courier', 0xff679d47, 10, None)
        CommentDoc = ('Courier', 0xff3f703f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff679d47, 10, None)
        CommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xff7ca563, 10, None)
        GlobalClass = ('Courier', 0xfff7f1c1, 10, None)
        Identifier = ('Courier', 0xfff7f1c1, 10, None)
        Keyword = ('Courier', 0xff519872, 10, None)
        KeywordSet2 = ('Courier', 0xfff7f1c1, 10, None)
        Number = ('Courier', 0xff6c9686, 10, None)
        Operator = ('Courier', 0xfff7f1c1, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        Regex = ('Courier', 0xff3f7f3f, 10, None)
        SingleQuotedString = ('Courier', 0xff7ca563, 10, None)
        UUID = ('Courier', 0xfff7f1c1, 10, None)
        UnclosedString = ('Courier', 0xfff7f1c1, 10, None)
        VerbatimString = ('Courier', 0xff679d47, 10, None)
    
    class D:
        BackquoteString = ('Courier', 0xfff7f1c1, 10, None)
        Character = ('Courier', 0xff7ca563, 10, None)
        Comment = ('Courier', 0xff679d47, 10, None)
        CommentDoc = ('Courier', 0xff3f703f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff679d47, 10, None)
        CommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        CommentNested = ('Courier', 0xffa0c0a0, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        Identifier = ('Courier', 0xfff7f1c1, 10, None)
        Keyword = ('Courier', 0xff519872, 10, None)
        KeywordDoc = ('Courier', 0xff519872, 10, None)
        KeywordSecondary = ('Courier', 0xff519872, 10, None)
        KeywordSet5 = ('Courier', 0xfff7f1c1, 10, None)
        KeywordSet6 = ('Courier', 0xfff7f1c1, 10, None)
        KeywordSet7 = ('Courier', 0xfff7f1c1, 10, None)
        Number = ('Courier', 0xff6c9686, 10, None)
        Operator = ('Courier', 0xfff7f1c1, 10, None)
        RawString = ('Courier', 0xfff7f1c1, 10, None)
        String = ('Courier', 0xff7ca563, 10, None)
        Typedefs = ('Courier', 0xff519872, 10, None)
        UnclosedString = ('Courier', 0xfff7f1c1, 10, None)
    
    class Diff:
        Command = ('Courier', 0xff7f7f00, 10, None)
        Comment = ('Courier', 0xff679d47, 10, None)
        Default = ('Courier', 0xfff7f1c1, 10, None)
        Header = ('Courier', 0xffe1aa7d, 10, None)
        LineAdded = ('Courier', 0xff519872, 10, None)
        LineChanged = ('Courier', 0xff7f7f7f, 10, None)
        LineRemoved = ('Courier', 0xff6c9686, 10, None)
        Position = ('Courier', 0xff7ca563, 10, None)
    
    class Fortran:
        Comment = ('Courier', 0xff679d47, 10, None)
        Continuation = ('Courier', 0xfff7f1c1, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DottedOperator = ('Courier', 0xfff7f1c1, 10, None)
        DoubleQuotedString = ('Courier', 0xff7ca563, 10, None)
        ExtendedFunction = ('Courier', 0xffb04080, 10, None)
        Identifier = ('Courier', 0xfff7f1c1, 10, None)
        IntrinsicFunction = ('Courier', 0xffb00040, 10, None)
        Keyword = ('Courier', 0xff519872, 10, None)
        Label = ('Courier', 0xffe0c0e0, 10, None)
        Number = ('Courier', 0xff6c9686, 10, None)
        Operator = ('Courier', 0xfff7f1c1, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        SingleQuotedString = ('Courier', 0xff7ca563, 10, None)
        UnclosedString = ('Courier', 0xfff7f1c1, 10, None)
    
    class Fortran77:
        Comment = ('Courier', 0xff679d47, 10, None)
        Continuation = ('Courier', 0xfff7f1c1, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DottedOperator = ('Courier', 0xfff7f1c1, 10, None)
        DoubleQuotedString = ('Courier', 0xff7ca563, 10, None)
        ExtendedFunction = ('Courier', 0xffb04080, 10, None)
        Identifier = ('Courier', 0xfff7f1c1, 10, None)
        IntrinsicFunction = ('Courier', 0xffb00040, 10, None)
        Keyword = ('Courier', 0xff519872, 10, None)
        Label = ('Courier', 0xffe0c0e0, 10, None)
        Number = ('Courier', 0xff6c9686, 10, None)
        Operator = ('Courier', 0xfff7f1c1, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        SingleQuotedString = ('Courier', 0xff7ca563, 10, None)
        UnclosedString = ('Courier', 0xfff7f1c1, 10, None)
    
    class HTML:
        ASPAtStart = ('Courier', 0xfff7f1c1, 10, None)
        ASPJavaScriptComment = ('Courier', 0xff679d47, 10, None)
        ASPJavaScriptCommentDoc = ('Courier', 0xff7f7f7f, 10, None)
        ASPJavaScriptCommentLine = ('Courier', 0xff679d47, 10, None)
        ASPJavaScriptDefault = ('Courier', 0xfff7f1c1, 10, None)
        ASPJavaScriptDoubleQuotedString = ('Courier', 0xff7ca563, 10, None)
        ASPJavaScriptKeyword = ('Courier', 0xff519872, 10, None)
        ASPJavaScriptNumber = ('Courier', 0xff6c9686, 10, None)
        ASPJavaScriptRegex = ('Courier', 0xfff7f1c1, 10, None)
        ASPJavaScriptSingleQuotedString = ('Courier', 0xff7ca563, 10, None)
        ASPJavaScriptStart = ('Courier', 0xff7f7f00, 10, None)
        ASPJavaScriptSymbol = ('Courier', 0xfff7f1c1, 10, None)
        ASPJavaScriptUnclosedString = ('Courier', 0xfff7f1c1, 10, None)
        ASPJavaScriptWord = ('Courier', 0xfff7f1c1, 10, None)
        ASPPythonClassName = ('Courier', 0xffb3935c, 10, None)
        ASPPythonComment = ('Courier', 0xff679d47, 10, None)
        ASPPythonDefault = ('Courier', 0xff808080, 10, None)
        ASPPythonDoubleQuotedString = ('Courier', 0xff7ca563, 10, None)
        ASPPythonFunctionMethodName = ('Courier', 0xff6c9686, 10, None)
        ASPPythonIdentifier = ('Courier', 0xfff7f1c1, 10, None)
        ASPPythonKeyword = ('Courier', 0xff519872, 10, None)
        ASPPythonNumber = ('Courier', 0xff6c9686, 10, None)
        ASPPythonOperator = ('Courier', 0xfff7f1c1, 10, None)
        ASPPythonSingleQuotedString = ('Courier', 0xff7ca563, 10, None)
        ASPPythonStart = ('Courier', 0xff808080, 10, None)
        ASPPythonTripleDoubleQuotedString = ('Courier', 0xffe1aa7d, 10, None)
        ASPPythonTripleSingleQuotedString = ('Courier', 0xffe1aa7d, 10, None)
        ASPStart = ('Courier', 0xfff7f1c1, 10, None)
        ASPVBScriptComment = ('Courier', 0xff008000, 10, None)
        ASPVBScriptDefault = ('Courier', 0xfff7f1c1, 10, None)
        ASPVBScriptIdentifier = ('Courier', 0xff007fff, 10, None)
        ASPVBScriptKeyword = ('Courier', 0xff007fff, 10, None)
        ASPVBScriptNumber = ('Courier', 0xff008080, 10, None)
        ASPVBScriptStart = ('Courier', 0xfff7f1c1, 10, None)
        ASPVBScriptString = ('Courier', 0xff800080, 10, None)
        ASPVBScriptUnclosedString = ('Courier', 0xff007fff, 10, None)
        ASPXCComment = ('Courier', 0xff1a0f0b, 10, None)
        Attribute = ('Courier', 0xff008080, 10, None)
        CDATA = ('Courier', 0xfff7f1c1, 10, None)
        Default = ('Courier', 0xfff7f1c1, 10, None)
        Entity = ('Courier', 0xff800080, 10, None)
        HTMLComment = ('Courier', 0xff808000, 10, None)
        HTMLDoubleQuotedString = ('Courier', 0xff7ca563, 10, None)
        HTMLNumber = ('Courier', 0xff6c9686, 10, None)
        HTMLSingleQuotedString = ('Courier', 0xff7ca563, 10, None)
        HTMLValue = ('Courier', 0xffff00ff, 10, None)
        JavaScriptComment = ('Courier', 0xff679d47, 10, None)
        JavaScriptCommentDoc = ('Courier', 0xff3f703f, 10, None)
        JavaScriptCommentLine = ('Courier', 0xff679d47, 10, None)
        JavaScriptDefault = ('Courier', 0xfff7f1c1, 10, None)
        JavaScriptDoubleQuotedString = ('Courier', 0xff7ca563, 10, None)
        JavaScriptKeyword = ('Courier', 0xff519872, 10, None)
        JavaScriptNumber = ('Courier', 0xff6c9686, 10, None)
        JavaScriptRegex = ('Courier', 0xfff7f1c1, 10, None)
        JavaScriptSingleQuotedString = ('Courier', 0xff7ca563, 10, None)
        JavaScriptStart = ('Courier', 0xff7f7f00, 10, None)
        JavaScriptSymbol = ('Courier', 0xfff7f1c1, 10, None)
        JavaScriptUnclosedString = ('Courier', 0xfff7f1c1, 10, None)
        JavaScriptWord = ('Courier', 0xfff7f1c1, 10, None)
        OtherInTag = ('Courier', 0xff800080, 10, None)
        PHPComment = ('Courier', 0xff999999, 10, None)
        PHPCommentLine = ('Courier', 0xff666666, 10, None)
        PHPDefault = ('Courier', 0xff000033, 10, None)
        PHPDoubleQuotedString = ('Courier', 0xff679d47, 10, None)
        PHPDoubleQuotedVariable = ('Courier', 0xff519872, 10, None)
        PHPKeyword = ('Courier', 0xff7ca563, 10, None)
        PHPNumber = ('Courier', 0xffcc9900, 10, None)
        PHPOperator = ('Courier', 0xfff7f1c1, 10, None)
        PHPSingleQuotedString = ('Courier', 0xff009f00, 10, None)
        PHPStart = ('Courier', 0xffb3935c, 10, None)
        PHPVariable = ('Courier', 0xff519872, 10, None)
        PythonClassName = ('Courier', 0xffb3935c, 10, None)
        PythonComment = ('Courier', 0xff679d47, 10, None)
        PythonDefault = ('Courier', 0xff808080, 10, None)
        PythonDoubleQuotedString = ('Courier', 0xff7ca563, 10, None)
        PythonFunctionMethodName = ('Courier', 0xff6c9686, 10, None)
        PythonIdentifier = ('Courier', 0xfff7f1c1, 10, None)
        PythonKeyword = ('Courier', 0xff519872, 10, None)
        PythonNumber = ('Courier', 0xff6c9686, 10, None)
        PythonOperator = ('Courier', 0xfff7f1c1, 10, None)
        PythonSingleQuotedString = ('Courier', 0xff7ca563, 10, None)
        PythonStart = ('Courier', 0xff808080, 10, None)
        PythonTripleDoubleQuotedString = ('Courier', 0xffe1aa7d, 10, None)
        PythonTripleSingleQuotedString = ('Courier', 0xffe1aa7d, 10, None)
        SGMLBlockDefault = ('Courier', 0xff000066, 10, None)
        SGMLCommand = ('Courier', 0xff007fff, 10, None)
        SGMLComment = ('Courier', 0xff808000, 10, None)
        SGMLDefault = ('Courier', 0xff007fff, 10, None)
        SGMLDoubleQuotedString = ('Courier', 0xff800000, 10, None)
        SGMLEntity = ('Courier', 0xff333333, 10, None)
        SGMLError = ('Courier', 0xff800000, 10, None)
        SGMLParameter = ('Courier', 0xff006600, 10, None)
        SGMLParameterComment = ('Courier', 0xff1a0f0b, 10, None)
        SGMLSingleQuotedString = ('Courier', 0xff993300, 10, None)
        SGMLSpecial = ('Courier', 0xff3366ff, 10, None)
        Script = ('Courier', 0xff007fff, 10, None)
        Tag = ('Courier', 0xff007fff, 10, None)
        UnknownAttribute = ('Courier', 0xffff0000, 10, None)
        UnknownTag = ('Courier', 0xffff0000, 10, None)
        VBScriptComment = ('Courier', 0xff008000, 10, None)
        VBScriptDefault = ('Courier', 0xfff7f1c1, 10, None)
        VBScriptIdentifier = ('Courier', 0xff007fff, 10, None)
        VBScriptKeyword = ('Courier', 0xff007fff, 10, None)
        VBScriptNumber = ('Courier', 0xff008080, 10, None)
        VBScriptStart = ('Courier', 0xfff7f1c1, 10, None)
        VBScriptString = ('Courier', 0xff800080, 10, None)
        VBScriptUnclosedString = ('Courier', 0xff007fff, 10, None)
        XMLEnd = ('Courier', 0xffb3935c, 10, None)
        XMLStart = ('Courier', 0xffb3935c, 10, None)
        XMLTagEnd = ('Courier', 0xff007fff, 10, None)
    
    class IDL:
        Comment = ('Courier', 0xff679d47, 10, None)
        CommentDoc = ('Courier', 0xff3f703f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff679d47, 10, None)
        CommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xff7ca563, 10, None)
        GlobalClass = ('Courier', 0xfff7f1c1, 10, None)
        HashQuotedString = ('Courier', 0xff679d47, 10, None)
        Identifier = ('Courier', 0xfff7f1c1, 10, None)
        InactiveComment = ('Courier', 0xff90b090, 10, None)
        InactiveCommentDoc = ('Courier', 0xffd0d0d0, 10, None)
        InactiveCommentDocKeyword = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentDocKeywordError = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentLine = ('Courier', 0xff90b090, 10, None)
        InactiveCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDefault = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDoubleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveGlobalClass = ('Courier', 0xffb0b0b0, 10, None)
        InactiveHashQuotedString = ('Courier', 0xfff7f1c1, 10, None)
        InactiveIdentifier = ('Courier', 0xffb0b0b0, 10, None)
        InactiveKeyword = ('Courier', 0xff9090b0, 10, None)
        InactiveKeywordSet2 = ('Courier', 0xffc0c0c0, 10, None)
        InactiveNumber = ('Courier', 0xff90b090, 10, None)
        InactiveOperator = ('Courier', 0xffb0b0b0, 10, None)
        InactivePreProcessor = ('Courier', 0xffb0b090, 10, None)
        InactivePreProcessorComment = ('Courier', 0xff1a0f0b, 10, None)
        InactivePreProcessorCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveRawString = ('Courier', 0xfff7f1c1, 10, None)
        InactiveRegex = ('Courier', 0xff7faf7f, 10, None)
        InactiveSingleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveTripleQuotedVerbatimString = ('Courier', 0xfff7f1c1, 10, None)
        InactiveUUID = ('Courier', 0xffc0c0c0, 10, None)
        InactiveUnclosedString = ('Courier', 0xfff7f1c1, 10, None)
        InactiveVerbatimString = ('Courier', 0xff90b090, 10, None)
        Keyword = ('Courier', 0xff519872, 10, None)
        KeywordSet2 = ('Courier', 0xfff7f1c1, 10, None)
        Number = ('Courier', 0xff6c9686, 10, None)
        Operator = ('Courier', 0xfff7f1c1, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        PreProcessorComment = ('Courier', 0xff659900, 10, None)
        PreProcessorCommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        RawString = ('Courier', 0xff7ca563, 10, None)
        Regex = ('Courier', 0xff3f7f3f, 10, None)
        SingleQuotedString = ('Courier', 0xff7ca563, 10, None)
        TripleQuotedVerbatimString = ('Courier', 0xff679d47, 10, None)
        UUID = ('Courier', 0xff804080, 10, None)
        UnclosedString = ('Courier', 0xfff7f1c1, 10, None)
        VerbatimString = ('Courier', 0xff679d47, 10, None)
    
    class Java:
        Comment = ('Courier', 0xff679d47, 10, None)
        CommentDoc = ('Courier', 0xff3f703f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff679d47, 10, None)
        CommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xff7ca563, 10, None)
        GlobalClass = ('Courier', 0xfff7f1c1, 10, None)
        HashQuotedString = ('Courier', 0xff679d47, 10, None)
        Identifier = ('Courier', 0xfff7f1c1, 10, None)
        InactiveComment = ('Courier', 0xff90b090, 10, None)
        InactiveCommentDoc = ('Courier', 0xffd0d0d0, 10, None)
        InactiveCommentDocKeyword = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentDocKeywordError = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentLine = ('Courier', 0xff90b090, 10, None)
        InactiveCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDefault = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDoubleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveGlobalClass = ('Courier', 0xffb0b0b0, 10, None)
        InactiveHashQuotedString = ('Courier', 0xfff7f1c1, 10, None)
        InactiveIdentifier = ('Courier', 0xffb0b0b0, 10, None)
        InactiveKeyword = ('Courier', 0xff9090b0, 10, None)
        InactiveKeywordSet2 = ('Courier', 0xffc0c0c0, 10, None)
        InactiveNumber = ('Courier', 0xff90b090, 10, None)
        InactiveOperator = ('Courier', 0xffb0b0b0, 10, None)
        InactivePreProcessor = ('Courier', 0xffb0b090, 10, None)
        InactivePreProcessorComment = ('Courier', 0xff1a0f0b, 10, None)
        InactivePreProcessorCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveRawString = ('Courier', 0xfff7f1c1, 10, None)
        InactiveRegex = ('Courier', 0xff7faf7f, 10, None)
        InactiveSingleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveTripleQuotedVerbatimString = ('Courier', 0xfff7f1c1, 10, None)
        InactiveUUID = ('Courier', 0xffc0c0c0, 10, None)
        InactiveUnclosedString = ('Courier', 0xfff7f1c1, 10, None)
        InactiveVerbatimString = ('Courier', 0xff90b090, 10, None)
        Keyword = ('Courier', 0xff519872, 10, None)
        KeywordSet2 = ('Courier', 0xfff7f1c1, 10, None)
        Number = ('Courier', 0xff6c9686, 10, None)
        Operator = ('Courier', 0xfff7f1c1, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        PreProcessorComment = ('Courier', 0xff659900, 10, None)
        PreProcessorCommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        RawString = ('Courier', 0xff7ca563, 10, None)
        Regex = ('Courier', 0xff3f7f3f, 10, None)
        SingleQuotedString = ('Courier', 0xff7ca563, 10, None)
        TripleQuotedVerbatimString = ('Courier', 0xff679d47, 10, None)
        UUID = ('Courier', 0xfff7f1c1, 10, None)
        UnclosedString = ('Courier', 0xfff7f1c1, 10, None)
        VerbatimString = ('Courier', 0xff679d47, 10, None)
    
    class JavaScript:
        Comment = ('Courier', 0xff679d47, 10, None)
        CommentDoc = ('Courier', 0xff3f703f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff679d47, 10, None)
        CommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xff7ca563, 10, None)
        GlobalClass = ('Courier', 0xfff7f1c1, 10, None)
        HashQuotedString = ('Courier', 0xff679d47, 10, None)
        Identifier = ('Courier', 0xfff7f1c1, 10, None)
        InactiveComment = ('Courier', 0xff90b090, 10, None)
        InactiveCommentDoc = ('Courier', 0xffd0d0d0, 10, None)
        InactiveCommentDocKeyword = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentDocKeywordError = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentLine = ('Courier', 0xff90b090, 10, None)
        InactiveCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDefault = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDoubleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveGlobalClass = ('Courier', 0xffb0b0b0, 10, None)
        InactiveHashQuotedString = ('Courier', 0xfff7f1c1, 10, None)
        InactiveIdentifier = ('Courier', 0xffb0b0b0, 10, None)
        InactiveKeyword = ('Courier', 0xff9090b0, 10, None)
        InactiveKeywordSet2 = ('Courier', 0xffc0c0c0, 10, None)
        InactiveNumber = ('Courier', 0xff90b090, 10, None)
        InactiveOperator = ('Courier', 0xffb0b0b0, 10, None)
        InactivePreProcessor = ('Courier', 0xffb0b090, 10, None)
        InactivePreProcessorComment = ('Courier', 0xff1a0f0b, 10, None)
        InactivePreProcessorCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveRawString = ('Courier', 0xfff7f1c1, 10, None)
        InactiveRegex = ('Courier', 0xff7faf7f, 10, None)
        InactiveSingleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveTripleQuotedVerbatimString = ('Courier', 0xfff7f1c1, 10, None)
        InactiveUUID = ('Courier', 0xffc0c0c0, 10, None)
        InactiveUnclosedString = ('Courier', 0xfff7f1c1, 10, None)
        InactiveVerbatimString = ('Courier', 0xff90b090, 10, None)
        Keyword = ('Courier', 0xff519872, 10, None)
        KeywordSet2 = ('Courier', 0xfff7f1c1, 10, None)
        Number = ('Courier', 0xff6c9686, 10, None)
        Operator = ('Courier', 0xfff7f1c1, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        PreProcessorComment = ('Courier', 0xff659900, 10, None)
        PreProcessorCommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        RawString = ('Courier', 0xff7ca563, 10, None)
        Regex = ('Courier', 0xff3f7f3f, 10, None)
        SingleQuotedString = ('Courier', 0xff7ca563, 10, None)
        TripleQuotedVerbatimString = ('Courier', 0xff679d47, 10, None)
        UUID = ('Courier', 0xfff7f1c1, 10, None)
        UnclosedString = ('Courier', 0xfff7f1c1, 10, None)
        VerbatimString = ('Courier', 0xff679d47, 10, None)
    
    class Lua:
        BasicFunctions = ('Courier', 0xff519872, 10, None)
        Character = ('Courier', 0xff7ca563, 10, None)
        Comment = ('Courier', 0xff679d47, 10, None)
        CoroutinesIOSystemFacilities = ('Courier', 0xff519872, 10, None)
        Default = ('Courier', 0xfff7f1c1, 10, None)
        Identifier = ('Courier', 0xfff7f1c1, 10, None)
        Keyword = ('Courier', 0xff519872, 10, None)
        KeywordSet5 = ('Courier', 0xfff7f1c1, 10, None)
        KeywordSet6 = ('Courier', 0xfff7f1c1, 10, None)
        KeywordSet7 = ('Courier', 0xfff7f1c1, 10, None)
        KeywordSet8 = ('Courier', 0xfff7f1c1, 10, None)
        Label = ('Courier', 0xff7f7f00, 10, None)
        LineComment = ('Courier', 0xff679d47, 10, None)
        LiteralString = ('Courier', 0xff7ca563, 10, None)
        Number = ('Courier', 0xff6c9686, 10, None)
        Operator = ('Courier', 0xfff7f1c1, 10, None)
        Preprocessor = ('Courier', 0xff7f7f00, 10, None)
        String = ('Courier', 0xff7ca563, 10, None)
        StringTableMathsFunctions = ('Courier', 0xff519872, 10, None)
        UnclosedString = ('Courier', 0xfff7f1c1, 10, None)
    
    class Makefile:
        Comment = ('Courier', 0xff679d47, 10, None)
        Default = ('Courier', 0xfff7f1c1, 10, None)
        Error = ('Courier', 0xffffff00, 10, None)
        Operator = ('Courier', 0xfff7f1c1, 10, None)
        Preprocessor = ('Courier', 0xff7f7f00, 10, None)
        Target = ('Courier', 0xffa00000, 10, None)
        Variable = ('Courier', 0xff007fff, 10, None)
    
    class Matlab:
        Command = ('Courier', 0xff7f7f00, 10, None)
        Comment = ('Courier', 0xff679d47, 10, None)
        Default = ('Courier', 0xfff7f1c1, 10, None)
        DoubleQuotedString = ('Courier', 0xff7ca563, 10, None)
        Identifier = ('Courier', 0xfff7f1c1, 10, None)
        Keyword = ('Courier', 0xff519872, 10, None)
        Number = ('Courier', 0xff6c9686, 10, None)
        Operator = ('Courier', 0xfff7f1c1, 10, None)
        SingleQuotedString = ('Courier', 0xff7ca563, 10, None)
    
    class Octave:
        Command = ('Courier', 0xff7f7f00, 10, None)
        Comment = ('Courier', 0xff679d47, 10, None)
        Default = ('Courier', 0xfff7f1c1, 10, None)
        DoubleQuotedString = ('Courier', 0xff7ca563, 10, None)
        Identifier = ('Courier', 0xfff7f1c1, 10, None)
        Keyword = ('Courier', 0xff519872, 10, None)
        Number = ('Courier', 0xff6c9686, 10, None)
        Operator = ('Courier', 0xfff7f1c1, 10, None)
        SingleQuotedString = ('Courier', 0xff7ca563, 10, None)
    
    class PO:
        Comment = ('Courier', 0xff679d47, 10, None)
        Default = ('Courier', 0xfff7f1c1, 10, None)
        Flags = ('Courier', 0xfff7f1c1, 10, None)
        Fuzzy = ('Courier', 0xfff7f1c1, 10, None)
        MessageContext = ('Courier', 0xfff7f1c1, 10, None)
        MessageContextText = ('Courier', 0xfff7f1c1, 10, None)
        MessageContextTextEOL = ('Courier', 0xfff7f1c1, 10, None)
        MessageId = ('Courier', 0xfff7f1c1, 10, None)
        MessageIdText = ('Courier', 0xfff7f1c1, 10, None)
        MessageIdTextEOL = ('Courier', 0xfff7f1c1, 10, None)
        MessageString = ('Courier', 0xfff7f1c1, 10, None)
        MessageStringText = ('Courier', 0xfff7f1c1, 10, None)
        MessageStringTextEOL = ('Courier', 0xfff7f1c1, 10, None)
        ProgrammerComment = ('Courier', 0xff1a0f0b, 10, None)
        Reference = ('Courier', 0xfff7f1c1, 10, None)
    
    class POV:
        BadDirective = ('Courier', 0xff804020, 10, None)
        Comment = ('Courier', 0xff679d47, 10, None)
        CommentLine = ('Courier', 0xff679d47, 10, None)
        Default = ('Courier', 0xffff0080, 10, None)
        Directive = ('Courier', 0xff7f7f00, 10, None)
        Identifier = ('Courier', 0xfff7f1c1, 10, None)
        KeywordSet6 = ('Courier', 0xff519872, 10, None)
        KeywordSet7 = ('Courier', 0xff519872, 10, None)
        KeywordSet8 = ('Courier', 0xff519872, 10, None)
        Number = ('Courier', 0xff6c9686, 10, None)
        ObjectsCSGAppearance = ('Courier', 0xff519872, 10, None)
        Operator = ('Courier', 0xfff7f1c1, 10, None)
        PredefinedFunctions = ('Courier', 0xff519872, 10, None)
        PredefinedIdentifiers = ('Courier', 0xff519872, 10, None)
        String = ('Courier', 0xff7ca563, 10, None)
        TypesModifiersItems = ('Courier', 0xff519872, 10, None)
        UnclosedString = ('Courier', 0xfff7f1c1, 10, None)
    
    class Pascal:
        Asm = ('Courier', 0xff804080, 10, None)
        Character = ('Courier', 0xff7ca563, 10, None)
        Comment = ('Courier', 0xff679d47, 10, None)
        CommentLine = ('Courier', 0xff679d47, 10, None)
        CommentParenthesis = ('Courier', 0xff679d47, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        HexNumber = ('Courier', 0xff6c9686, 10, None)
        Identifier = ('Courier', 0xfff7f1c1, 10, None)
        Keyword = ('Courier', 0xff519872, 10, None)
        Number = ('Courier', 0xff6c9686, 10, None)
        Operator = ('Courier', 0xfff7f1c1, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        PreProcessorParenthesis = ('Courier', 0xff7f7f00, 10, None)
        SingleQuotedString = ('Courier', 0xff7ca563, 10, None)
        UnclosedString = ('Courier', 0xfff7f1c1, 10, None)
    
    class Perl:
        Array = ('Courier', 0xfff7f1c1, 10, None)
        BacktickHereDocument = ('Courier', 0xff7ca563, 10, None)
        BacktickHereDocumentVar = ('Courier', 0xffd00000, 10, None)
        Backticks = ('Courier', 0xffffff00, 10, None)
        BackticksVar = ('Courier', 0xffd00000, 10, None)
        Comment = ('Courier', 0xff679d47, 10, None)
        DataSection = ('Courier', 0xff600000, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedHereDocument = ('Courier', 0xff7ca563, 10, None)
        DoubleQuotedHereDocumentVar = ('Courier', 0xffd00000, 10, None)
        DoubleQuotedString = ('Courier', 0xff7ca563, 10, None)
        DoubleQuotedStringVar = ('Courier', 0xffd00000, 10, None)
        Error = ('Courier', 0xffffff00, 10, None)
        FormatBody = ('Courier', 0xffc000c0, 10, None)
        FormatIdentifier = ('Courier', 0xffc000c0, 10, None)
        Hash = ('Courier', 0xfff7f1c1, 10, None)
        HereDocumentDelimiter = ('Courier', 0xfff7f1c1, 10, None)
        Identifier = ('Courier', 0xfff7f1c1, 10, None)
        Keyword = ('Courier', 0xff519872, 10, None)
        Number = ('Courier', 0xff6c9686, 10, None)
        Operator = ('Courier', 0xfff7f1c1, 10, None)
        POD = ('Courier', 0xff004000, 10, None)
        PODVerbatim = ('Courier', 0xff004000, 10, None)
        QuotedStringQ = ('Courier', 0xff7ca563, 10, None)
        QuotedStringQQ = ('Courier', 0xff7ca563, 10, None)
        QuotedStringQQVar = ('Courier', 0xffd00000, 10, None)
        QuotedStringQR = ('Courier', 0xfff7f1c1, 10, None)
        QuotedStringQRVar = ('Courier', 0xffd00000, 10, None)
        QuotedStringQW = ('Courier', 0xfff7f1c1, 10, None)
        QuotedStringQX = ('Courier', 0xffffff00, 10, None)
        QuotedStringQXVar = ('Courier', 0xffd00000, 10, None)
        Regex = ('Courier', 0xfff7f1c1, 10, None)
        RegexVar = ('Courier', 0xffd00000, 10, None)
        Scalar = ('Courier', 0xfff7f1c1, 10, None)
        SingleQuotedHereDocument = ('Courier', 0xff7ca563, 10, None)
        SingleQuotedString = ('Courier', 0xff7ca563, 10, None)
        SubroutinePrototype = ('Courier', 0xfff7f1c1, 10, None)
        Substitution = ('Courier', 0xfff7f1c1, 10, None)
        SubstitutionVar = ('Courier', 0xffd00000, 10, None)
        SymbolTable = ('Courier', 0xfff7f1c1, 10, None)
        Translation = ('Courier', 0xfff7f1c1, 10, None)
    
    class PostScript:
        ArrayParenthesis = ('Courier', 0xff519872, 10, None)
        BadStringCharacter = ('Courier', 0xffffff00, 10, None)
        Base85String = ('Courier', 0xff7ca563, 10, None)
        Comment = ('Courier', 0xff679d47, 10, None)
        DSCComment = ('Courier', 0xff3f703f, 10, None)
        DSCCommentValue = ('Courier', 0xff3060a0, 10, None)
        Default = ('Courier', 0xfff7f1c1, 10, None)
        DictionaryParenthesis = ('Courier', 0xff3060a0, 10, None)
        HexString = ('Courier', 0xff3f7f3f, 10, None)
        ImmediateEvalLiteral = ('Courier', 0xff7f7f00, 10, None)
        Keyword = ('Courier', 0xff519872, 10, None)
        Literal = ('Courier', 0xff7f7f00, 10, None)
        Name = ('Courier', 0xfff7f1c1, 10, None)
        Number = ('Courier', 0xff6c9686, 10, None)
        ProcedureParenthesis = ('Courier', 0xfff7f1c1, 10, None)
        Text = ('Courier', 0xff7ca563, 10, None)
    
    class Properties:
        Assignment = ('Courier', 0xffb06000, 10, None)
        Comment = ('Courier', 0xff6c9686, 10, None)
        Default = ('Courier', 0xfff7f1c1, 10, None)
        DefaultValue = ('Courier', 0xff7f7f00, 10, None)
        Key = ('Courier', 0xfff7f1c1, 10, None)
        Section = ('Courier', 0xff7ca563, 10, None)
    
    class Python:
        ClassName = ('Courier', 0xffb3935c, 10, None)
        Comment = ('Courier', 0xff679d47, 10, None)
        CommentBlock = ('Courier', 0xff7f7f7f, 10, None)
        Decorator = ('Courier', 0xff805000, 10, None)
        Default = ('Courier', 0xfff7f1c1, 10, None)
        DoubleQuotedString = ('Courier', 0xff7ca563, 10, None)
        FunctionMethodName = ('Courier', 0xff6c9686, 10, None)
        HighlightedIdentifier = ('Courier', 0xff407090, 10, None)
        Identifier = ('Courier', 0xfff7f1c1, 10, None)
        Inconsistent = ('Courier', 0xff679d47, 10, None)
        Keyword = ('Courier', 0xff519872, 10, None)
        NoWarning = ('Courier', 0xff808080, 10, None)
        Number = ('Courier', 0xff6c9686, 10, None)
        Operator = ('Courier', 0xfff7f1c1, 10, None)
        SingleQuotedString = ('Courier', 0xff7ca563, 10, None)
        Spaces = ('Courier', 0xff7ca563, 10, None)
        Tabs = ('Courier', 0xff7ca563, 10, None)
        TabsAfterSpaces = ('Courier', 0xff6c9686, 10, None)
        TripleDoubleQuotedString = ('Courier', 0xffe1aa7d, 10, None)
        TripleSingleQuotedString = ('Courier', 0xffe1aa7d, 10, None)
        UnclosedString = ('Courier', 0xfff7f1c1, 10, None)
    
    class Ruby:
        Backticks = ('Courier', 0xffffff00, 10, None)
        ClassName = ('Courier', 0xffb3935c, 10, None)
        ClassVariable = ('Courier', 0xff8000b0, 10, None)
        Comment = ('Courier', 0xff679d47, 10, None)
        DataSection = ('Courier', 0xff600000, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DemotedKeyword = ('Courier', 0xff519872, 10, None)
        DoubleQuotedString = ('Courier', 0xff7ca563, 10, None)
        Error = ('Courier', 0xfff7f1c1, 10, None)
        FunctionMethodName = ('Courier', 0xff6c9686, 10, None)
        Global = ('Courier', 0xff800080, 10, None)
        HereDocument = ('Courier', 0xff7ca563, 10, None)
        HereDocumentDelimiter = ('Courier', 0xfff7f1c1, 10, None)
        Identifier = ('Courier', 0xfff7f1c1, 10, None)
        InstanceVariable = ('Courier', 0xffb00080, 10, None)
        Keyword = ('Courier', 0xff519872, 10, None)
        ModuleName = ('Courier', 0xffa000a0, 10, None)
        Number = ('Courier', 0xff6c9686, 10, None)
        Operator = ('Courier', 0xfff7f1c1, 10, None)
        POD = ('Courier', 0xff004000, 10, None)
        PercentStringQ = ('Courier', 0xff7ca563, 10, None)
        PercentStringq = ('Courier', 0xff7ca563, 10, None)
        PercentStringr = ('Courier', 0xfff7f1c1, 10, None)
        PercentStringw = ('Courier', 0xfff7f1c1, 10, None)
        PercentStringx = ('Courier', 0xffffff00, 10, None)
        Regex = ('Courier', 0xfff7f1c1, 10, None)
        SingleQuotedString = ('Courier', 0xff7ca563, 10, None)
        Stderr = ('Courier', 0xfff7f1c1, 10, None)
        Stdin = ('Courier', 0xfff7f1c1, 10, None)
        Stdout = ('Courier', 0xfff7f1c1, 10, None)
        Symbol = ('Courier', 0xffc0a030, 10, None)
    
    class SQL:
        Comment = ('Courier', 0xff679d47, 10, None)
        CommentDoc = ('Courier', 0xff7f7f7f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff679d47, 10, None)
        CommentLineHash = ('Courier', 0xff679d47, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xff7ca563, 10, None)
        Identifier = ('Courier', 0xfff7f1c1, 10, None)
        Keyword = ('Courier', 0xff519872, 10, None)
        KeywordSet5 = ('Courier', 0xff4b0082, 10, None)
        KeywordSet6 = ('Courier', 0xffb00040, 10, None)
        KeywordSet7 = ('Courier', 0xff8b0000, 10, None)
        KeywordSet8 = ('Courier', 0xff800080, 10, None)
        Number = ('Courier', 0xff6c9686, 10, None)
        Operator = ('Courier', 0xfff7f1c1, 10, None)
        PlusComment = ('Courier', 0xff679d47, 10, None)
        PlusKeyword = ('Courier', 0xff7f7f00, 10, None)
        PlusPrompt = ('Courier', 0xff679d47, 10, None)
        QuotedIdentifier = ('Courier', 0xfff7f1c1, 10, None)
        SingleQuotedString = ('Courier', 0xff7ca563, 10, None)
    
    class Spice:
        Command = ('Courier', 0xff519872, 10, None)
        Comment = ('Courier', 0xff679d47, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        Delimiter = ('Courier', 0xfff7f1c1, 10, None)
        Function = ('Courier', 0xff519872, 10, None)
        Identifier = ('Courier', 0xfff7f1c1, 10, None)
        Number = ('Courier', 0xff6c9686, 10, None)
        Parameter = ('Courier', 0xff0040e0, 10, None)
        Value = ('Courier', 0xff7ca563, 10, None)
    
    class TCL:
        Comment = ('Courier', 0xff679d47, 10, None)
        CommentBlock = ('Courier', 0xfff7f1c1, 10, None)
        CommentBox = ('Courier', 0xff679d47, 10, None)
        CommentLine = ('Courier', 0xff679d47, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        ExpandKeyword = ('Courier', 0xff519872, 10, None)
        ITCLKeyword = ('Courier', 0xff519872, 10, None)
        Identifier = ('Courier', 0xff519872, 10, None)
        KeywordSet6 = ('Courier', 0xff519872, 10, None)
        KeywordSet7 = ('Courier', 0xff519872, 10, None)
        KeywordSet8 = ('Courier', 0xff519872, 10, None)
        KeywordSet9 = ('Courier', 0xff519872, 10, None)
        Modifier = ('Courier', 0xff7ca563, 10, None)
        Number = ('Courier', 0xff6c9686, 10, None)
        Operator = ('Courier', 0xfff7f1c1, 10, None)
        QuotedKeyword = ('Courier', 0xff7ca563, 10, None)
        QuotedString = ('Courier', 0xff7ca563, 10, None)
        Substitution = ('Courier', 0xff7f7f00, 10, None)
        SubstitutionBrace = ('Courier', 0xff7f7f00, 10, None)
        TCLKeyword = ('Courier', 0xff519872, 10, None)
        TkCommand = ('Courier', 0xff519872, 10, None)
        TkKeyword = ('Courier', 0xff519872, 10, None)
    
    class TeX:
        Command = ('Courier', 0xff679d47, 10, None)
        Default = ('Courier', 0xff3f3f3f, 10, None)
        Group = ('Courier', 0xffe1aa7d, 10, None)
        Special = ('Courier', 0xff6c9686, 10, None)
        Symbol = ('Courier', 0xff7f7f00, 10, None)
        Text = ('Courier', 0xfff7f1c1, 10, None)
    
    class VHDL:
        Attribute = ('Courier', 0xff804020, 10, None)
        Comment = ('Courier', 0xff679d47, 10, None)
        CommentLine = ('Courier', 0xff3f7f3f, 10, None)
        Default = ('Courier', 0xff800080, 10, None)
        Identifier = ('Courier', 0xfff7f1c1, 10, None)
        Keyword = ('Courier', 0xff519872, 10, None)
        KeywordSet7 = ('Courier', 0xff804020, 10, None)
        Number = ('Courier', 0xff6c9686, 10, None)
        Operator = ('Courier', 0xfff7f1c1, 10, None)
        StandardFunction = ('Courier', 0xff808020, 10, None)
        StandardOperator = ('Courier', 0xff6c9686, 10, None)
        StandardPackage = ('Courier', 0xff208020, 10, None)
        StandardType = ('Courier', 0xff208080, 10, None)
        String = ('Courier', 0xff7ca563, 10, None)
        UnclosedString = ('Courier', 0xfff7f1c1, 10, None)
    
    class Verilog:
        Comment = ('Courier', 0xff679d47, 10, None)
        CommentBang = ('Courier', 0xff3f7f3f, 10, None)
        CommentLine = ('Courier', 0xff679d47, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        Identifier = ('Courier', 0xfff7f1c1, 10, None)
        Keyword = ('Courier', 0xff519872, 10, None)
        KeywordSet2 = ('Courier', 0xff6c9686, 10, None)
        Number = ('Courier', 0xff6c9686, 10, None)
        Operator = ('Courier', 0xff007070, 10, None)
        Preprocessor = ('Courier', 0xff7f7f00, 10, None)
        String = ('Courier', 0xff7ca563, 10, None)
        SystemTask = ('Courier', 0xff804020, 10, None)
        UnclosedString = ('Courier', 0xfff7f1c1, 10, None)
        UserKeywordSet = ('Courier', 0xff2a00ff, 10, None)
    
    class XML:
        ASPAtStart = ('Courier', 0xfff7f1c1, 10, None)
        ASPJavaScriptComment = ('Courier', 0xff679d47, 10, None)
        ASPJavaScriptCommentDoc = ('Courier', 0xff7f7f7f, 10, None)
        ASPJavaScriptCommentLine = ('Courier', 0xff679d47, 10, None)
        ASPJavaScriptDefault = ('Courier', 0xfff7f1c1, 10, None)
        ASPJavaScriptDoubleQuotedString = ('Courier', 0xff7ca563, 10, None)
        ASPJavaScriptKeyword = ('Courier', 0xff519872, 10, None)
        ASPJavaScriptNumber = ('Courier', 0xff6c9686, 10, None)
        ASPJavaScriptRegex = ('Courier', 0xfff7f1c1, 10, None)
        ASPJavaScriptSingleQuotedString = ('Courier', 0xff7ca563, 10, None)
        ASPJavaScriptStart = ('Courier', 0xff7f7f00, 10, None)
        ASPJavaScriptSymbol = ('Courier', 0xfff7f1c1, 10, None)
        ASPJavaScriptUnclosedString = ('Courier', 0xfff7f1c1, 10, None)
        ASPJavaScriptWord = ('Courier', 0xfff7f1c1, 10, None)
        ASPPythonClassName = ('Courier', 0xffb3935c, 10, None)
        ASPPythonComment = ('Courier', 0xff679d47, 10, None)
        ASPPythonDefault = ('Courier', 0xff808080, 10, None)
        ASPPythonDoubleQuotedString = ('Courier', 0xff7ca563, 10, None)
        ASPPythonFunctionMethodName = ('Courier', 0xff6c9686, 10, None)
        ASPPythonIdentifier = ('Courier', 0xfff7f1c1, 10, None)
        ASPPythonKeyword = ('Courier', 0xff519872, 10, None)
        ASPPythonNumber = ('Courier', 0xff6c9686, 10, None)
        ASPPythonOperator = ('Courier', 0xfff7f1c1, 10, None)
        ASPPythonSingleQuotedString = ('Courier', 0xff7ca563, 10, None)
        ASPPythonStart = ('Courier', 0xff808080, 10, None)
        ASPPythonTripleDoubleQuotedString = ('Courier', 0xffe1aa7d, 10, None)
        ASPPythonTripleSingleQuotedString = ('Courier', 0xffe1aa7d, 10, None)
        ASPStart = ('Courier', 0xfff7f1c1, 10, None)
        ASPVBScriptComment = ('Courier', 0xff008000, 10, None)
        ASPVBScriptDefault = ('Courier', 0xfff7f1c1, 10, None)
        ASPVBScriptIdentifier = ('Courier', 0xff007fff, 10, None)
        ASPVBScriptKeyword = ('Courier', 0xff007fff, 10, None)
        ASPVBScriptNumber = ('Courier', 0xff008080, 10, None)
        ASPVBScriptStart = ('Courier', 0xfff7f1c1, 10, None)
        ASPVBScriptString = ('Courier', 0xff800080, 10, None)
        ASPVBScriptUnclosedString = ('Courier', 0xff007fff, 10, None)
        ASPXCComment = ('Courier', 0xff1a0f0b, 10, None)
        Attribute = ('Courier', 0xff008080, 10, None)
        CDATA = ('Courier', 0xff800000, 10, None)
        Default = ('Courier', 0xfff7f1c1, 10, None)
        Entity = ('Courier', 0xff800080, 10, None)
        HTMLComment = ('Courier', 0xff808000, 10, None)
        HTMLDoubleQuotedString = ('Courier', 0xff7ca563, 10, None)
        HTMLNumber = ('Courier', 0xff6c9686, 10, None)
        HTMLSingleQuotedString = ('Courier', 0xff7ca563, 10, None)
        HTMLValue = ('Courier', 0xff608060, 10, None)
        JavaScriptComment = ('Courier', 0xff679d47, 10, None)
        JavaScriptCommentDoc = ('Courier', 0xff3f703f, 10, None)
        JavaScriptCommentLine = ('Courier', 0xff679d47, 10, None)
        JavaScriptDefault = ('Courier', 0xfff7f1c1, 10, None)
        JavaScriptDoubleQuotedString = ('Courier', 0xff7ca563, 10, None)
        JavaScriptKeyword = ('Courier', 0xff519872, 10, None)
        JavaScriptNumber = ('Courier', 0xff6c9686, 10, None)
        JavaScriptRegex = ('Courier', 0xfff7f1c1, 10, None)
        JavaScriptSingleQuotedString = ('Courier', 0xff7ca563, 10, None)
        JavaScriptStart = ('Courier', 0xff7f7f00, 10, None)
        JavaScriptSymbol = ('Courier', 0xfff7f1c1, 10, None)
        JavaScriptUnclosedString = ('Courier', 0xfff7f1c1, 10, None)
        JavaScriptWord = ('Courier', 0xfff7f1c1, 10, None)
        OtherInTag = ('Courier', 0xff800080, 10, None)
        PHPComment = ('Courier', 0xff999999, 10, None)
        PHPCommentLine = ('Courier', 0xff666666, 10, None)
        PHPDefault = ('Courier', 0xff000033, 10, None)
        PHPDoubleQuotedString = ('Courier', 0xff679d47, 10, None)
        PHPDoubleQuotedVariable = ('Courier', 0xff519872, 10, None)
        PHPKeyword = ('Courier', 0xff7ca563, 10, None)
        PHPNumber = ('Courier', 0xffcc9900, 10, None)
        PHPOperator = ('Courier', 0xfff7f1c1, 10, None)
        PHPSingleQuotedString = ('Courier', 0xff009f00, 10, None)
        PHPStart = ('Courier', 0xff800000, 10, None)
        PHPVariable = ('Courier', 0xff519872, 10, None)
        PythonClassName = ('Courier', 0xffb3935c, 10, None)
        PythonComment = ('Courier', 0xff679d47, 10, None)
        PythonDefault = ('Courier', 0xff808080, 10, None)
        PythonDoubleQuotedString = ('Courier', 0xff7ca563, 10, None)
        PythonFunctionMethodName = ('Courier', 0xff6c9686, 10, None)
        PythonIdentifier = ('Courier', 0xfff7f1c1, 10, None)
        PythonKeyword = ('Courier', 0xff519872, 10, None)
        PythonNumber = ('Courier', 0xff6c9686, 10, None)
        PythonOperator = ('Courier', 0xfff7f1c1, 10, None)
        PythonSingleQuotedString = ('Courier', 0xff7ca563, 10, None)
        PythonStart = ('Courier', 0xff808080, 10, None)
        PythonTripleDoubleQuotedString = ('Courier', 0xffe1aa7d, 10, None)
        PythonTripleSingleQuotedString = ('Courier', 0xffe1aa7d, 10, None)
        SGMLBlockDefault = ('Courier', 0xff000066, 10, None)
        SGMLCommand = ('Courier', 0xff007fff, 10, None)
        SGMLComment = ('Courier', 0xff808000, 10, None)
        SGMLDefault = ('Courier', 0xff007fff, 10, None)
        SGMLDoubleQuotedString = ('Courier', 0xff800000, 10, None)
        SGMLEntity = ('Courier', 0xff333333, 10, None)
        SGMLError = ('Courier', 0xff800000, 10, None)
        SGMLParameter = ('Courier', 0xff006600, 10, None)
        SGMLParameterComment = ('Courier', 0xff1a0f0b, 10, None)
        SGMLSingleQuotedString = ('Courier', 0xff993300, 10, None)
        SGMLSpecial = ('Courier', 0xff3366ff, 10, None)
        Script = ('Courier', 0xff007fff, 10, None)
        Tag = ('Courier', 0xff007fff, 10, None)
        UnknownAttribute = ('Courier', 0xff008080, 10, None)
        UnknownTag = ('Courier', 0xff007fff, 10, None)
        VBScriptComment = ('Courier', 0xff008000, 10, None)
        VBScriptDefault = ('Courier', 0xfff7f1c1, 10, None)
        VBScriptIdentifier = ('Courier', 0xff007fff, 10, None)
        VBScriptKeyword = ('Courier', 0xff007fff, 10, None)
        VBScriptNumber = ('Courier', 0xff008080, 10, None)
        VBScriptStart = ('Courier', 0xfff7f1c1, 10, None)
        VBScriptString = ('Courier', 0xff800080, 10, None)
        VBScriptUnclosedString = ('Courier', 0xff007fff, 10, None)
        XMLEnd = ('Courier', 0xff800080, 10, None)
        XMLStart = ('Courier', 0xff800080, 10, None)
        XMLTagEnd = ('Courier', 0xff007fff, 10, None)
    
    class YAML:
        Comment = ('Courier', 0xff008800, 10, None)
        Default = ('Courier', 0xfff7f1c1, 10, None)
        DocumentDelimiter = ('Courier', 0xff1a0f0b, 10, None)
        Identifier = ('Courier', 0xff000088, 10, None)
        Keyword = ('Courier', 0xff880088, 10, None)
        Number = ('Courier', 0xff880000, 10, None)
        Operator = ('Courier', 0xfff7f1c1, 10, None)
        Reference = ('Courier', 0xff008888, 10, None)
        SyntaxErrorMarker = ('Courier', 0xffffffff, 10, None)
        TextBlockMarker = ('Courier', 0xff333366, 10, None)


class Paper:
    Default = PyQt4.QtGui.QColor(0xff1a0f0b)
    
    class Ada:
        Default = 0xff1a0f0b
        Comment = 0xff1a0f0b
        Keyword = 0xff1a0f0b
        String = 0xff1a0f0b
        Procedure = 0xff1a0f0b
        Number = 0xff1a0f0b
        Type = 0xff1a0f0b
        Package = 0xff1a0f0b
    
    class Nim:
        Default = 0xff1a0f0b
        Comment = 0xff1a0f0b
        BasicKeyword = 0xff1a0f0b
        TopKeyword = 0xff1a0f0b
        String = 0xff1a0f0b
        LongString = 0xff1a0f0b
        Number = 0xff1a0f0b
        Operator = 0xff1a0f0b
        Unsafe = 0xff1a0f0b
        Type = 0xff1a0f0b
        DocumentationComment = 0xff1a0f0b
        Definition = 0xff1a0f0b
        Class = 0xff1a0f0b
        KeywordOperator = 0xff1a0f0b
        CharLiteral = 0xff1a0f0b
        CaseOf = 0xff1a0f0b
        UserKeyword = 0xff1a0f0b
        MultilineComment = 0xff1a0f0b
        MultilineDocumentation = 0xff1a0f0b
        Pragma = 0xff1a0f0b
    
    class Oberon:
        Default = 0xff1a0f0b
        Comment = 0xff1a0f0b
        Keyword = 0xff1a0f0b
        String = 0xff1a0f0b
        Procedure = 0xff1a0f0b
        Module = 0xff1a0f0b
        Number = 0xff1a0f0b
        Type = 0xff1a0f0b
    
    
    # Generated
    class AVS:
        Function = 0xff1a0f0b
        KeywordSet6 = 0xff1a0f0b
        TripleString = 0xff1a0f0b
        LineComment = 0xff1a0f0b
        Plugin = 0xff1a0f0b
        String = 0xff1a0f0b
        ClipProperty = 0xff1a0f0b
        Default = 0xff1a0f0b
        Operator = 0xff1a0f0b
        Number = 0xff1a0f0b
        Filter = 0xff1a0f0b
        Identifier = 0xff1a0f0b
        NestedBlockComment = 0xff1a0f0b
        Keyword = 0xff1a0f0b
        BlockComment = 0xff1a0f0b
    
    class Bash:
        Error = 0xffff0000
        Backticks = 0xffa08080
        SingleQuotedHereDocument = 0xffddd0dd
        Scalar = 0xffffe0e0
        HereDocumentDelimiter = 0xffddd0dd
        Comment = 0xff1a0f0b
        SingleQuotedString = 0xff1a0f0b
        Default = 0xff1a0f0b
        Operator = 0xff1a0f0b
        ParameterExpansion = 0xffffffe0
        Number = 0xff1a0f0b
        Identifier = 0xff1a0f0b
        Keyword = 0xff1a0f0b
        DoubleQuotedString = 0xff1a0f0b
    
    class Batch:
        Label = 0xff606060
        Default = 0xff1a0f0b
        Keyword = 0xff1a0f0b
        ExternalCommand = 0xff1a0f0b
        Variable = 0xff1a0f0b
        Comment = 0xff1a0f0b
        HideCommandChar = 0xff1a0f0b
        Operator = 0xff1a0f0b
    
    class CMake:
        Function = 0xff1a0f0b
        BlockForeach = 0xff1a0f0b
        BlockWhile = 0xff1a0f0b
        StringLeftQuote = 0xffeeeeee
        Label = 0xff1a0f0b
        Comment = 0xff1a0f0b
        BlockMacro = 0xff1a0f0b
        StringRightQuote = 0xffeeeeee
        Default = 0xff1a0f0b
        Number = 0xff1a0f0b
        BlockIf = 0xff1a0f0b
        Variable = 0xff1a0f0b
        KeywordSet3 = 0xff1a0f0b
        String = 0xffeeeeee
        StringVariable = 0xffeeeeee
    
    class CPP:
        CommentDocKeywordError = 0xff1a0f0b
        InactiveRegex = 0xffe0f0e0
        InactivePreProcessorComment = 0xff1a0f0b
        UUID = 0xff1a0f0b
        InactiveVerbatimString = 0xffe0ffe0
        SingleQuotedString = 0xff1a0f0b
        Operator = 0xff1a0f0b
        InactiveOperator = 0xff1a0f0b
        InactivePreProcessor = 0xff1a0f0b
        UnclosedString = 0xffe0c0e0
        Identifier = 0xff1a0f0b
        InactiveRawString = 0xff1a0f0b
        PreProcessor = 0xff1a0f0b
        KeywordSet2 = 0xff1a0f0b
        InactiveUnclosedString = 0xffe0c0e0
        InactiveCommentLine = 0xff1a0f0b
        InactiveNumber = 0xff1a0f0b
        InactivePreProcessorCommentLineDoc = 0xff1a0f0b
        Number = 0xff1a0f0b
        InactiveUUID = 0xff1a0f0b
        CommentDoc = 0xff1a0f0b
        InactiveCommentDoc = 0xff1a0f0b
        GlobalClass = 0xff1a0f0b
        InactiveSingleQuotedString = 0xff1a0f0b
        HashQuotedString = 0xffe7ffd7
        VerbatimString = 0xffe0ffe0
        InactiveHashQuotedString = 0xff1a0f0b
        Regex = 0xffe0f0e0
        InactiveGlobalClass = 0xff1a0f0b
        InactiveIdentifier = 0xff1a0f0b
        CommentLineDoc = 0xff1a0f0b
        TripleQuotedVerbatimString = 0xffe0ffe0
        InactiveKeywordSet2 = 0xff1a0f0b
        InactiveCommentDocKeyword = 0xff1a0f0b
        Keyword = 0xff1a0f0b
        InactiveCommentLineDoc = 0xff1a0f0b
        InactiveDefault = 0xff1a0f0b
        InactiveCommentDocKeywordError = 0xff1a0f0b
        InactiveTripleQuotedVerbatimString = 0xff1a0f0b
        CommentDocKeyword = 0xff1a0f0b
        InactiveDoubleQuotedString = 0xff1a0f0b
        CommentLine = 0xff1a0f0b
        Comment = 0xff1a0f0b
        PreProcessorComment = 0xff1a0f0b
        InactiveComment = 0xff1a0f0b
        RawString = 0xfffff3ff
        Default = 0xff1a0f0b
        PreProcessorCommentLineDoc = 0xff1a0f0b
        DoubleQuotedString = 0xff1a0f0b
        InactiveKeyword = 0xff1a0f0b
    
    class CSS:
        Important = 0xff1a0f0b
        CSS3Property = 0xff1a0f0b
        Attribute = 0xff1a0f0b
        Comment = 0xff1a0f0b
        SingleQuotedString = 0xff1a0f0b
        MediaRule = 0xff1a0f0b
        AtRule = 0xff1a0f0b
        UnknownPseudoClass = 0xff1a0f0b
        PseudoClass = 0xff1a0f0b
        Tag = 0xff1a0f0b
        CSS2Property = 0xff1a0f0b
        CSS1Property = 0xff1a0f0b
        IDSelector = 0xff1a0f0b
        ExtendedCSSProperty = 0xff1a0f0b
        Variable = 0xff1a0f0b
        ExtendedPseudoClass = 0xff1a0f0b
        ClassSelector = 0xff1a0f0b
        Default = 0xff1a0f0b
        PseudoElement = 0xff1a0f0b
        UnknownProperty = 0xff1a0f0b
        Value = 0xff1a0f0b
        ExtendedPseudoElement = 0xff1a0f0b
        DoubleQuotedString = 0xff1a0f0b
        Operator = 0xff1a0f0b
    
    class CSharp:
        CommentDocKeywordError = 0xff1a0f0b
        InactiveRegex = 0xff1a0f0b
        InactivePreProcessorComment = 0xff1a0f0b
        UUID = 0xff1a0f0b
        InactiveVerbatimString = 0xff1a0f0b
        SingleQuotedString = 0xff1a0f0b
        Operator = 0xff1a0f0b
        InactiveOperator = 0xff1a0f0b
        InactivePreProcessor = 0xff1a0f0b
        UnclosedString = 0xff1a0f0b
        Identifier = 0xff1a0f0b
        InactiveRawString = 0xff1a0f0b
        PreProcessor = 0xff1a0f0b
        KeywordSet2 = 0xff1a0f0b
        InactiveUnclosedString = 0xff1a0f0b
        InactiveCommentLine = 0xff1a0f0b
        InactiveNumber = 0xff1a0f0b
        InactivePreProcessorCommentLineDoc = 0xff1a0f0b
        Number = 0xff1a0f0b
        InactiveUUID = 0xff1a0f0b
        CommentDoc = 0xff1a0f0b
        InactiveCommentDoc = 0xff1a0f0b
        GlobalClass = 0xff1a0f0b
        InactiveSingleQuotedString = 0xff1a0f0b
        HashQuotedString = 0xff1a0f0b
        VerbatimString = 0xffe0ffe0
        InactiveHashQuotedString = 0xff1a0f0b
        Regex = 0xff1a0f0b
        InactiveGlobalClass = 0xff1a0f0b
        InactiveIdentifier = 0xff1a0f0b
        CommentLineDoc = 0xff1a0f0b
        TripleQuotedVerbatimString = 0xff1a0f0b
        InactiveKeywordSet2 = 0xff1a0f0b
        InactiveCommentDocKeyword = 0xff1a0f0b
        Keyword = 0xff1a0f0b
        InactiveCommentLineDoc = 0xff1a0f0b
        InactiveDefault = 0xff1a0f0b
        InactiveCommentDocKeywordError = 0xff1a0f0b
        InactiveTripleQuotedVerbatimString = 0xff1a0f0b
        CommentDocKeyword = 0xff1a0f0b
        InactiveDoubleQuotedString = 0xff1a0f0b
        CommentLine = 0xff1a0f0b
        Comment = 0xff1a0f0b
        PreProcessorComment = 0xff1a0f0b
        InactiveComment = 0xff1a0f0b
        RawString = 0xff1a0f0b
        Default = 0xff1a0f0b
        PreProcessorCommentLineDoc = 0xff1a0f0b
        DoubleQuotedString = 0xff1a0f0b
        InactiveKeyword = 0xff1a0f0b
    
    class CoffeeScript:
        UUID = 0xff1a0f0b
        CommentDocKeywordError = 0xff1a0f0b
        GlobalClass = 0xff1a0f0b
        VerbatimString = 0xffe0ffe0
        SingleQuotedString = 0xff1a0f0b
        Operator = 0xff1a0f0b
        Number = 0xff1a0f0b
        Identifier = 0xff1a0f0b
        Keyword = 0xff1a0f0b
        UnclosedString = 0xffe0c0e0
        Regex = 0xffe0f0e0
        CommentDocKeyword = 0xff1a0f0b
        BlockRegex = 0xff1a0f0b
        CommentLineDoc = 0xff1a0f0b
        PreProcessor = 0xff1a0f0b
        CommentLine = 0xff1a0f0b
        CommentBlock = 0xff1a0f0b
        Comment = 0xff1a0f0b
        KeywordSet2 = 0xff1a0f0b
        BlockRegexComment = 0xff1a0f0b
        Default = 0xff1a0f0b
        DoubleQuotedString = 0xff1a0f0b
        CommentDoc = 0xff1a0f0b
    
    class D:
        BackquoteString = 0xff1a0f0b
        CommentDocKeywordError = 0xff1a0f0b
        Operator = 0xff1a0f0b
        CommentNested = 0xff1a0f0b
        KeywordDoc = 0xff1a0f0b
        KeywordSet7 = 0xff1a0f0b
        Keyword = 0xff1a0f0b
        KeywordSecondary = 0xff1a0f0b
        Identifier = 0xff1a0f0b
        KeywordSet5 = 0xff1a0f0b
        CommentDocKeyword = 0xff1a0f0b
        KeywordSet6 = 0xff1a0f0b
        CommentLineDoc = 0xff1a0f0b
        CommentLine = 0xff1a0f0b
        Comment = 0xff1a0f0b
        Typedefs = 0xff1a0f0b
        Character = 0xff1a0f0b
        RawString = 0xff1a0f0b
        Default = 0xff1a0f0b
        Number = 0xff1a0f0b
        UnclosedString = 0xffe0c0e0
        String = 0xff1a0f0b
        CommentDoc = 0xff1a0f0b
    
    class Diff:
        Header = 0xff1a0f0b
        LineChanged = 0xff1a0f0b
        Default = 0xff1a0f0b
        LineRemoved = 0xff1a0f0b
        Command = 0xff1a0f0b
        Position = 0xff1a0f0b
        LineAdded = 0xff1a0f0b
        Comment = 0xff1a0f0b
    
    class Fortran:
        Label = 0xff1a0f0b
        Identifier = 0xff1a0f0b
        DottedOperator = 0xff1a0f0b
        PreProcessor = 0xff1a0f0b
        Comment = 0xff1a0f0b
        SingleQuotedString = 0xff1a0f0b
        Default = 0xff1a0f0b
        DoubleQuotedString = 0xff1a0f0b
        ExtendedFunction = 0xff1a0f0b
        UnclosedString = 0xffe0c0e0
        Number = 0xff1a0f0b
        Continuation = 0xfff0e080
        IntrinsicFunction = 0xff1a0f0b
        Keyword = 0xff1a0f0b
        Operator = 0xff1a0f0b
    
    class Fortran77:
        Label = 0xff1a0f0b
        Identifier = 0xff1a0f0b
        DottedOperator = 0xff1a0f0b
        PreProcessor = 0xff1a0f0b
        Comment = 0xff1a0f0b
        SingleQuotedString = 0xff1a0f0b
        Default = 0xff1a0f0b
        DoubleQuotedString = 0xff1a0f0b
        ExtendedFunction = 0xff1a0f0b
        UnclosedString = 0xffe0c0e0
        Number = 0xff1a0f0b
        Continuation = 0xfff0e080
        IntrinsicFunction = 0xff1a0f0b
        Keyword = 0xff1a0f0b
        Operator = 0xff1a0f0b
    
    class HTML:
        HTMLValue = 0xffffefff
        PythonDefault = 0xffefffef
        Entity = 0xff1a0f0b
        SGMLParameter = 0xffefefff
        SGMLDefault = 0xffefefff
        PHPVariable = 0xfffff8f8
        SGMLCommand = 0xffefefff
        PythonClassName = 0xffefffef
        VBScriptUnclosedString = 0xff7f7fff
        ASPJavaScriptDefault = 0xffdfdf7f
        ASPVBScriptStart = 0xff1a0f0b
        VBScriptDefault = 0xffefefff
        PythonNumber = 0xffefffef
        PythonOperator = 0xffefffef
        ASPJavaScriptSingleQuotedString = 0xffdfdf7f
        PHPDefault = 0xfffff8f8
        XMLStart = 0xff1a0f0b
        PythonFunctionMethodName = 0xffefffef
        ASPJavaScriptStart = 0xff1a0f0b
        JavaScriptWord = 0xfff0f0ff
        PHPSingleQuotedString = 0xfffff8f8
        PythonTripleDoubleQuotedString = 0xffefffef
        JavaScriptComment = 0xfff0f0ff
        Default = 0xff1a0f0b
        SGMLSingleQuotedString = 0xffefefff
        VBScriptComment = 0xffefefff
        ASPVBScriptNumber = 0xffcfcfef
        ASPJavaScriptCommentDoc = 0xffdfdf7f
        PythonIdentifier = 0xffefffef
        VBScriptKeyword = 0xffefefff
        JavaScriptDefault = 0xfff0f0ff
        PythonStart = 0xff1a0f0b
        ASPPythonComment = 0xffcfefcf
        ASPJavaScriptWord = 0xffdfdf7f
        SGMLParameterComment = 0xff1a0f0b
        JavaScriptSingleQuotedString = 0xfff0f0ff
        PythonSingleQuotedString = 0xffefffef
        HTMLSingleQuotedString = 0xff1a0f0b
        ASPVBScriptString = 0xffcfcfef
        SGMLBlockDefault = 0xffcccce0
        PythonKeyword = 0xffefffef
        XMLTagEnd = 0xff1a0f0b
        ASPVBScriptComment = 0xffcfcfef
        ASPPythonSingleQuotedString = 0xffcfefcf
        PHPDoubleQuotedVariable = 0xfffff8f8
        ASPJavaScriptComment = 0xffdfdf7f
        JavaScriptUnclosedString = 0xffbfbbb0
        JavaScriptDoubleQuotedString = 0xfff0f0ff
        UnknownAttribute = 0xff1a0f0b
        ASPPythonOperator = 0xffcfefcf
        ASPJavaScriptSymbol = 0xffdfdf7f
        ASPPythonFunctionMethodName = 0xffcfefcf
        SGMLDoubleQuotedString = 0xffefefff
        PHPOperator = 0xfffff8f8
        JavaScriptNumber = 0xfff0f0ff
        PythonDoubleQuotedString = 0xffefffef
        ASPAtStart = 0xffffff00
        Script = 0xff1a0f0b
        PHPCommentLine = 0xfffff8f8
        SGMLComment = 0xffefefff
        JavaScriptStart = 0xff1a0f0b
        ASPPythonIdentifier = 0xffcfefcf
        ASPVBScriptKeyword = 0xffcfcfef
        ASPPythonTripleDoubleQuotedString = 0xffcfefcf
        ASPPythonKeyword = 0xffcfefcf
        ASPJavaScriptNumber = 0xffdfdf7f
        PHPStart = 0xffffefbf
        PythonTripleSingleQuotedString = 0xffefffef
        PHPNumber = 0xfffff8f8
        ASPPythonDefault = 0xffcfefcf
        SGMLSpecial = 0xffefefff
        OtherInTag = 0xff1a0f0b
        JavaScriptCommentDoc = 0xfff0f0ff
        Tag = 0xff1a0f0b
        XMLEnd = 0xff1a0f0b
        CDATA = 0xffffdf00
        HTMLNumber = 0xff1a0f0b
        SGMLError = 0xffff6666
        PHPKeyword = 0xfffff8f8
        ASPVBScriptUnclosedString = 0xff7f7fff
        ASPPythonNumber = 0xffcfefcf
        VBScriptString = 0xffefefff
        ASPPythonClassName = 0xffcfefcf
        ASPPythonStart = 0xff1a0f0b
        JavaScriptRegex = 0xffffbbb0
        ASPJavaScriptUnclosedString = 0xffbfbbb0
        ASPJavaScriptCommentLine = 0xffdfdf7f
        SGMLEntity = 0xffefefff
        ASPJavaScriptDoubleQuotedString = 0xffdfdf7f
        ASPStart = 0xffffdf00
        Attribute = 0xff1a0f0b
        ASPJavaScriptKeyword = 0xffdfdf7f
        ASPVBScriptDefault = 0xffcfcfef
        ASPVBScriptIdentifier = 0xffcfcfef
        ASPJavaScriptRegex = 0xffffbbb0
        VBScriptNumber = 0xffefefff
        HTMLDoubleQuotedString = 0xff1a0f0b
        ASPXCComment = 0xff1a0f0b
        VBScriptStart = 0xff1a0f0b
        PHPDoubleQuotedString = 0xfffff8f8
        PHPComment = 0xfffff8f8
        ASPPythonTripleSingleQuotedString = 0xffcfefcf
        ASPPythonDoubleQuotedString = 0xffcfefcf
        JavaScriptKeyword = 0xfff0f0ff
        JavaScriptSymbol = 0xfff0f0ff
        VBScriptIdentifier = 0xffefefff
        HTMLComment = 0xff1a0f0b
        UnknownTag = 0xff1a0f0b
        JavaScriptCommentLine = 0xfff0f0ff
        PythonComment = 0xffefffef
    
    class IDL:
        CommentDocKeywordError = 0xff1a0f0b
        InactiveRegex = 0xffe0f0e0
        InactivePreProcessorComment = 0xff1a0f0b
        UUID = 0xff1a0f0b
        InactiveVerbatimString = 0xffe0ffe0
        SingleQuotedString = 0xff1a0f0b
        Operator = 0xff1a0f0b
        InactiveOperator = 0xff1a0f0b
        InactivePreProcessor = 0xff1a0f0b
        UnclosedString = 0xffe0c0e0
        Identifier = 0xff1a0f0b
        InactiveRawString = 0xff1a0f0b
        PreProcessor = 0xff1a0f0b
        KeywordSet2 = 0xff1a0f0b
        InactiveUnclosedString = 0xffe0c0e0
        InactiveCommentLine = 0xff1a0f0b
        InactiveNumber = 0xff1a0f0b
        InactivePreProcessorCommentLineDoc = 0xff1a0f0b
        Number = 0xff1a0f0b
        InactiveUUID = 0xff1a0f0b
        CommentDoc = 0xff1a0f0b
        InactiveCommentDoc = 0xff1a0f0b
        GlobalClass = 0xff1a0f0b
        InactiveSingleQuotedString = 0xff1a0f0b
        HashQuotedString = 0xffe7ffd7
        VerbatimString = 0xffe0ffe0
        InactiveHashQuotedString = 0xff1a0f0b
        Regex = 0xffe0f0e0
        InactiveGlobalClass = 0xff1a0f0b
        InactiveIdentifier = 0xff1a0f0b
        CommentLineDoc = 0xff1a0f0b
        TripleQuotedVerbatimString = 0xffe0ffe0
        InactiveKeywordSet2 = 0xff1a0f0b
        InactiveCommentDocKeyword = 0xff1a0f0b
        Keyword = 0xff1a0f0b
        InactiveCommentLineDoc = 0xff1a0f0b
        InactiveDefault = 0xff1a0f0b
        InactiveCommentDocKeywordError = 0xff1a0f0b
        InactiveTripleQuotedVerbatimString = 0xff1a0f0b
        CommentDocKeyword = 0xff1a0f0b
        InactiveDoubleQuotedString = 0xff1a0f0b
        CommentLine = 0xff1a0f0b
        Comment = 0xff1a0f0b
        PreProcessorComment = 0xff1a0f0b
        InactiveComment = 0xff1a0f0b
        RawString = 0xfffff3ff
        Default = 0xff1a0f0b
        PreProcessorCommentLineDoc = 0xff1a0f0b
        DoubleQuotedString = 0xff1a0f0b
        InactiveKeyword = 0xff1a0f0b
    
    class Java:
        CommentDocKeywordError = 0xff1a0f0b
        InactiveRegex = 0xffe0f0e0
        InactivePreProcessorComment = 0xff1a0f0b
        UUID = 0xff1a0f0b
        InactiveVerbatimString = 0xffe0ffe0
        SingleQuotedString = 0xff1a0f0b
        Operator = 0xff1a0f0b
        InactiveOperator = 0xff1a0f0b
        InactivePreProcessor = 0xff1a0f0b
        UnclosedString = 0xffe0c0e0
        Identifier = 0xff1a0f0b
        InactiveRawString = 0xff1a0f0b
        PreProcessor = 0xff1a0f0b
        KeywordSet2 = 0xff1a0f0b
        InactiveUnclosedString = 0xffe0c0e0
        InactiveCommentLine = 0xff1a0f0b
        InactiveNumber = 0xff1a0f0b
        InactivePreProcessorCommentLineDoc = 0xff1a0f0b
        Number = 0xff1a0f0b
        InactiveUUID = 0xff1a0f0b
        CommentDoc = 0xff1a0f0b
        InactiveCommentDoc = 0xff1a0f0b
        GlobalClass = 0xff1a0f0b
        InactiveSingleQuotedString = 0xff1a0f0b
        HashQuotedString = 0xffe7ffd7
        VerbatimString = 0xffe0ffe0
        InactiveHashQuotedString = 0xff1a0f0b
        Regex = 0xffe0f0e0
        InactiveGlobalClass = 0xff1a0f0b
        InactiveIdentifier = 0xff1a0f0b
        CommentLineDoc = 0xff1a0f0b
        TripleQuotedVerbatimString = 0xffe0ffe0
        InactiveKeywordSet2 = 0xff1a0f0b
        InactiveCommentDocKeyword = 0xff1a0f0b
        Keyword = 0xff1a0f0b
        InactiveCommentLineDoc = 0xff1a0f0b
        InactiveDefault = 0xff1a0f0b
        InactiveCommentDocKeywordError = 0xff1a0f0b
        InactiveTripleQuotedVerbatimString = 0xff1a0f0b
        CommentDocKeyword = 0xff1a0f0b
        InactiveDoubleQuotedString = 0xff1a0f0b
        CommentLine = 0xff1a0f0b
        Comment = 0xff1a0f0b
        PreProcessorComment = 0xff1a0f0b
        InactiveComment = 0xff1a0f0b
        RawString = 0xfffff3ff
        Default = 0xff1a0f0b
        PreProcessorCommentLineDoc = 0xff1a0f0b
        DoubleQuotedString = 0xff1a0f0b
        InactiveKeyword = 0xff1a0f0b
    
    class JavaScript:
        CommentDocKeywordError = 0xff1a0f0b
        InactiveRegex = 0xff1a0f0b
        InactivePreProcessorComment = 0xff1a0f0b
        UUID = 0xff1a0f0b
        InactiveVerbatimString = 0xff1a0f0b
        SingleQuotedString = 0xff1a0f0b
        Operator = 0xff1a0f0b
        InactiveOperator = 0xff1a0f0b
        InactivePreProcessor = 0xff1a0f0b
        UnclosedString = 0xff1a0f0b
        Identifier = 0xff1a0f0b
        InactiveRawString = 0xff1a0f0b
        PreProcessor = 0xff1a0f0b
        KeywordSet2 = 0xff1a0f0b
        InactiveUnclosedString = 0xff1a0f0b
        InactiveCommentLine = 0xff1a0f0b
        InactiveNumber = 0xff1a0f0b
        InactivePreProcessorCommentLineDoc = 0xff1a0f0b
        Number = 0xff1a0f0b
        InactiveUUID = 0xff1a0f0b
        CommentDoc = 0xff1a0f0b
        InactiveCommentDoc = 0xff1a0f0b
        GlobalClass = 0xff1a0f0b
        InactiveSingleQuotedString = 0xff1a0f0b
        HashQuotedString = 0xff1a0f0b
        VerbatimString = 0xff1a0f0b
        InactiveHashQuotedString = 0xff1a0f0b
        Regex = 0xffe0f0ff
        InactiveGlobalClass = 0xff1a0f0b
        InactiveIdentifier = 0xff1a0f0b
        CommentLineDoc = 0xff1a0f0b
        TripleQuotedVerbatimString = 0xff1a0f0b
        InactiveKeywordSet2 = 0xff1a0f0b
        InactiveCommentDocKeyword = 0xff1a0f0b
        Keyword = 0xff1a0f0b
        InactiveCommentLineDoc = 0xff1a0f0b
        InactiveDefault = 0xff1a0f0b
        InactiveCommentDocKeywordError = 0xff1a0f0b
        InactiveTripleQuotedVerbatimString = 0xff1a0f0b
        CommentDocKeyword = 0xff1a0f0b
        InactiveDoubleQuotedString = 0xff1a0f0b
        CommentLine = 0xff1a0f0b
        Comment = 0xff1a0f0b
        PreProcessorComment = 0xff1a0f0b
        InactiveComment = 0xff1a0f0b
        RawString = 0xff1a0f0b
        Default = 0xff1a0f0b
        PreProcessorCommentLineDoc = 0xff1a0f0b
        DoubleQuotedString = 0xff1a0f0b
        InactiveKeyword = 0xff1a0f0b
    
    class Lua:
        Label = 0xff1a0f0b
        Identifier = 0xff1a0f0b
        StringTableMathsFunctions = 0xffd0d0ff
        CoroutinesIOSystemFacilities = 0xffffd0d0
        KeywordSet5 = 0xff1a0f0b
        KeywordSet6 = 0xff1a0f0b
        PreProcessor = 0xff1a0f0b
        LineComment = 0xff1a0f0b
        Comment = 0xffd0f0f0
        String = 0xff1a0f0b
        Character = 0xff1a0f0b
        Default = 0xff1a0f0b
        Operator = 0xff1a0f0b
        LiteralString = 0xffe0ffff
        Number = 0xff1a0f0b
        KeywordSet8 = 0xff1a0f0b
        KeywordSet7 = 0xff1a0f0b
        BasicFunctions = 0xffd0ffd0
        Keyword = 0xff1a0f0b
        UnclosedString = 0xffe0c0e0
    
    class Makefile:
        Default = 0xff1a0f0b
        Operator = 0xff1a0f0b
        Target = 0xff1a0f0b
        PreProcessor = 0xff1a0f0b
        Variable = 0xff1a0f0b
        Comment = 0xff1a0f0b
        Error = 0xffff0000
    
    class Matlab:
        SingleQuotedString = 0xff1a0f0b
        Default = 0xff1a0f0b
        Keyword = 0xff1a0f0b
        Number = 0xff1a0f0b
        Command = 0xff1a0f0b
        Identifier = 0xff1a0f0b
        Comment = 0xff1a0f0b
        DoubleQuotedString = 0xff1a0f0b
        Operator = 0xff1a0f0b
    
    class Octave:
        SingleQuotedString = 0xff1a0f0b
        Default = 0xff1a0f0b
        Keyword = 0xff1a0f0b
        Number = 0xff1a0f0b
        Command = 0xff1a0f0b
        Identifier = 0xff1a0f0b
        Comment = 0xff1a0f0b
        DoubleQuotedString = 0xff1a0f0b
        Operator = 0xff1a0f0b
    
    class PO:
        ProgrammerComment = 0xff1a0f0b
        Flags = 0xff1a0f0b
        MessageContextText = 0xff1a0f0b
        MessageStringTextEOL = 0xff1a0f0b
        MessageId = 0xff1a0f0b
        MessageIdText = 0xff1a0f0b
        Reference = 0xff1a0f0b
        Comment = 0xff1a0f0b
        MessageStringText = 0xff1a0f0b
        MessageContext = 0xff1a0f0b
        Fuzzy = 0xff1a0f0b
        Default = 0xff1a0f0b
        MessageString = 0xff1a0f0b
        MessageContextTextEOL = 0xff1a0f0b
        MessageIdTextEOL = 0xff1a0f0b
    
    class POV:
        KeywordSet7 = 0xffd0d0d0
        KeywordSet6 = 0xffd0ffd0
        PredefinedFunctions = 0xffd0d0ff
        CommentLine = 0xff1a0f0b
        PredefinedIdentifiers = 0xff1a0f0b
        Comment = 0xff1a0f0b
        Directive = 0xff1a0f0b
        String = 0xff1a0f0b
        BadDirective = 0xff1a0f0b
        TypesModifiersItems = 0xffffffd0
        Default = 0xff1a0f0b
        Operator = 0xff1a0f0b
        Number = 0xff1a0f0b
        KeywordSet8 = 0xffe0e0e0
        Identifier = 0xff1a0f0b
        ObjectsCSGAppearance = 0xffffd0d0
        UnclosedString = 0xffe0c0e0
    
    class Pascal:
        PreProcessorParenthesis = 0xff1a0f0b
        SingleQuotedString = 0xff1a0f0b
        PreProcessor = 0xff1a0f0b
        CommentLine = 0xff1a0f0b
        Comment = 0xff1a0f0b
        CommentParenthesis = 0xff1a0f0b
        Asm = 0xff1a0f0b
        Character = 0xff1a0f0b
        Default = 0xff1a0f0b
        Operator = 0xff1a0f0b
        UnclosedString = 0xffe0c0e0
        Number = 0xff1a0f0b
        Identifier = 0xff1a0f0b
        Keyword = 0xff1a0f0b
        HexNumber = 0xff1a0f0b
    
    class Perl:
        Translation = 0xfff0e080
        BacktickHereDocument = 0xffddd0dd
        Array = 0xffffffe0
        QuotedStringQXVar = 0xffa08080
        PODVerbatim = 0xffc0ffc0
        DoubleQuotedStringVar = 0xff1a0f0b
        Regex = 0xffa0ffa0
        HereDocumentDelimiter = 0xffddd0dd
        SubroutinePrototype = 0xff1a0f0b
        BacktickHereDocumentVar = 0xffddd0dd
        QuotedStringQR = 0xff1a0f0b
        SingleQuotedString = 0xff1a0f0b
        QuotedStringQRVar = 0xff1a0f0b
        SubstitutionVar = 0xff1a0f0b
        Operator = 0xff1a0f0b
        DoubleQuotedHereDocumentVar = 0xffddd0dd
        Identifier = 0xff1a0f0b
        QuotedStringQX = 0xff1a0f0b
        BackticksVar = 0xffa08080
        Keyword = 0xff1a0f0b
        QuotedStringQ = 0xff1a0f0b
        QuotedStringQQVar = 0xff1a0f0b
        QuotedStringQQ = 0xff1a0f0b
        POD = 0xffe0ffe0
        FormatIdentifier = 0xff1a0f0b
        RegexVar = 0xff1a0f0b
        Backticks = 0xffa08080
        DoubleQuotedHereDocument = 0xffddd0dd
        Scalar = 0xffffe0e0
        FormatBody = 0xfffff0ff
        Comment = 0xff1a0f0b
        QuotedStringQW = 0xff1a0f0b
        SymbolTable = 0xffe0e0e0
        Default = 0xff1a0f0b
        Error = 0xffff0000
        SingleQuotedHereDocument = 0xffddd0dd
        Number = 0xff1a0f0b
        Hash = 0xffffe0ff
        Substitution = 0xfff0e080
        DataSection = 0xfffff0d8
        DoubleQuotedString = 0xff1a0f0b
    
    class PostScript:
        DictionaryParenthesis = 0xff1a0f0b
        HexString = 0xff1a0f0b
        DSCCommentValue = 0xff1a0f0b
        ProcedureParenthesis = 0xff1a0f0b
        Comment = 0xff1a0f0b
        ImmediateEvalLiteral = 0xff1a0f0b
        Name = 0xff1a0f0b
        DSCComment = 0xff1a0f0b
        Default = 0xff1a0f0b
        Base85String = 0xff1a0f0b
        Number = 0xff1a0f0b
        ArrayParenthesis = 0xff1a0f0b
        Literal = 0xff1a0f0b
        BadStringCharacter = 0xffff0000
        Text = 0xff1a0f0b
        Keyword = 0xff1a0f0b
    
    class Properties:
        DefaultValue = 0xff1a0f0b
        Default = 0xff1a0f0b
        Section = 0xffe0f0f0
        Assignment = 0xff1a0f0b
        Key = 0xff1a0f0b
        Comment = 0xff1a0f0b
    
    class Python:
        TripleDoubleQuotedString = 0xff1a0f0b
        FunctionMethodName = 0xff1a0f0b
        TabsAfterSpaces = 0xff1a0f0b
        Tabs = 0xff1a0f0b
        Decorator = 0xff1a0f0b
        NoWarning = 0xff1a0f0b
        UnclosedString = 0xffe0c0e0
        Spaces = 0xff1a0f0b
        CommentBlock = 0xff1a0f0b
        Comment = 0xff1a0f0b
        TripleSingleQuotedString = 0xff1a0f0b
        SingleQuotedString = 0xff1a0f0b
        Inconsistent = 0xff1a0f0b
        Default = 0xff1a0f0b
        DoubleQuotedString = 0xff1a0f0b
        Operator = 0xff1a0f0b
        Number = 0xff1a0f0b
        Identifier = 0xff1a0f0b
        ClassName = 0xff1a0f0b
        Keyword = 0xff1a0f0b
        HighlightedIdentifier = 0xff1a0f0b
    
    class Ruby:
        Symbol = 0xff1a0f0b
        Stderr = 0xffff8080
        Global = 0xff1a0f0b
        FunctionMethodName = 0xff1a0f0b
        Stdin = 0xffff8080
        HereDocumentDelimiter = 0xffddd0dd
        PercentStringr = 0xffa0ffa0
        PercentStringQ = 0xff1a0f0b
        ModuleName = 0xff1a0f0b
        HereDocument = 0xffddd0dd
        SingleQuotedString = 0xff1a0f0b
        PercentStringQ = 0xff1a0f0b
        Regex = 0xffa0ffa0
        Operator = 0xff1a0f0b
        PercentStringw = 0xffffffe0
        PercentStringx = 0xffa08080
        POD = 0xffc0ffc0
        Keyword = 0xff1a0f0b
        Stdout = 0xffff8080
        ClassVariable = 0xff1a0f0b
        Identifier = 0xff1a0f0b
        DemotedKeyword = 0xff1a0f0b
        Backticks = 0xffa08080
        InstanceVariable = 0xff1a0f0b
        Comment = 0xff1a0f0b
        Default = 0xff1a0f0b
        Error = 0xffff0000
        Number = 0xff1a0f0b
        DataSection = 0xfffff0d8
        ClassName = 0xff1a0f0b
        DoubleQuotedString = 0xff1a0f0b
    
    class SQL:
        PlusComment = 0xff1a0f0b
        KeywordSet7 = 0xff1a0f0b
        PlusPrompt = 0xffe0ffe0
        CommentDocKeywordError = 0xff1a0f0b
        CommentDocKeyword = 0xff1a0f0b
        KeywordSet6 = 0xff1a0f0b
        CommentLine = 0xff1a0f0b
        Comment = 0xff1a0f0b
        Operator = 0xff1a0f0b
        QuotedIdentifier = 0xff1a0f0b
        SingleQuotedString = 0xff1a0f0b
        PlusKeyword = 0xff1a0f0b
        Default = 0xff1a0f0b
        DoubleQuotedString = 0xff1a0f0b
        CommentLineHash = 0xff1a0f0b
        KeywordSet5 = 0xff1a0f0b
        Number = 0xff1a0f0b
        KeywordSet8 = 0xff1a0f0b
        Identifier = 0xff1a0f0b
        Keyword = 0xff1a0f0b
        CommentDoc = 0xff1a0f0b
    
    class Spice:
        Function = 0xff1a0f0b
        Delimiter = 0xff1a0f0b
        Value = 0xff1a0f0b
        Default = 0xff1a0f0b
        Number = 0xff1a0f0b
        Parameter = 0xff1a0f0b
        Command = 0xff1a0f0b
        Identifier = 0xff1a0f0b
        Comment = 0xff1a0f0b
    
    class TCL:
        SubstitutionBrace = 0xff1a0f0b
        CommentBox = 0xfff0fff0
        ITCLKeyword = 0xfffff0f0
        TkKeyword = 0xffe0fff0
        Operator = 0xff1a0f0b
        QuotedString = 0xfffff0f0
        ExpandKeyword = 0xffffff80
        KeywordSet7 = 0xff1a0f0b
        TCLKeyword = 0xff1a0f0b
        TkCommand = 0xffffd0d0
        Identifier = 0xff1a0f0b
        KeywordSet6 = 0xff1a0f0b
        CommentLine = 0xff1a0f0b
        CommentBlock = 0xfff0fff0
        Comment = 0xfff0ffe0
        Default = 0xff1a0f0b
        KeywordSet9 = 0xff1a0f0b
        Modifier = 0xff1a0f0b
        Number = 0xff1a0f0b
        KeywordSet8 = 0xff1a0f0b
        Substitution = 0xffeffff0
        QuotedKeyword = 0xfffff0f0
    
    class TeX:
        Symbol = 0xff1a0f0b
        Default = 0xff1a0f0b
        Command = 0xff1a0f0b
        Group = 0xff1a0f0b
        Text = 0xff1a0f0b
        Special = 0xff1a0f0b
    
    class VHDL:
        StandardOperator = 0xff1a0f0b
        Attribute = 0xff1a0f0b
        CommentLine = 0xff1a0f0b
        Comment = 0xff1a0f0b
        String = 0xff1a0f0b
        Default = 0xff1a0f0b
        Operator = 0xff1a0f0b
        StandardPackage = 0xff1a0f0b
        Number = 0xff1a0f0b
        Identifier = 0xff1a0f0b
        KeywordSet7 = 0xff1a0f0b
        StandardFunction = 0xff1a0f0b
        StandardType = 0xff1a0f0b
        Keyword = 0xff1a0f0b
        UnclosedString = 0xffe0c0e0
    
    class Verilog:
        CommentBang = 0xffe0f0ff
        UserKeywordSet = 0xff1a0f0b
        PreProcessor = 0xff1a0f0b
        CommentLine = 0xff1a0f0b
        Comment = 0xff1a0f0b
        KeywordSet2 = 0xff1a0f0b
        Default = 0xff1a0f0b
        Operator = 0xff1a0f0b
        Number = 0xff1a0f0b
        Identifier = 0xff1a0f0b
        SystemTask = 0xff1a0f0b
        String = 0xff1a0f0b
        Keyword = 0xff1a0f0b
        UnclosedString = 0xffe0c0e0
    
    class XML:
        HTMLValue = 0xffffefff
        PythonDefault = 0xffefffef
        Entity = 0xff1a0f0b
        SGMLParameter = 0xffefefff
        SGMLDefault = 0xffefefff
        PHPVariable = 0xfffff8f8
        SGMLCommand = 0xffefefff
        PythonClassName = 0xffefffef
        VBScriptUnclosedString = 0xff7f7fff
        ASPJavaScriptDefault = 0xffdfdf7f
        ASPVBScriptStart = 0xff1a0f0b
        VBScriptDefault = 0xffefefff
        PythonNumber = 0xffefffef
        PythonOperator = 0xffefffef
        ASPJavaScriptSingleQuotedString = 0xffdfdf7f
        PHPDefault = 0xfffff8f8
        XMLStart = 0xff1a0f0b
        PythonFunctionMethodName = 0xffefffef
        ASPJavaScriptStart = 0xff1a0f0b
        JavaScriptWord = 0xfff0f0ff
        PHPSingleQuotedString = 0xfffff8f8
        PythonTripleDoubleQuotedString = 0xffefffef
        JavaScriptComment = 0xfff0f0ff
        Default = 0xff1a0f0b
        SGMLSingleQuotedString = 0xffefefff
        VBScriptComment = 0xffefefff
        ASPVBScriptNumber = 0xffcfcfef
        ASPJavaScriptCommentDoc = 0xffdfdf7f
        PythonIdentifier = 0xffefffef
        VBScriptKeyword = 0xffefefff
        JavaScriptDefault = 0xfff0f0ff
        PythonStart = 0xff1a0f0b
        ASPPythonComment = 0xffcfefcf
        ASPJavaScriptWord = 0xffdfdf7f
        SGMLParameterComment = 0xff1a0f0b
        JavaScriptSingleQuotedString = 0xfff0f0ff
        PythonSingleQuotedString = 0xffefffef
        HTMLSingleQuotedString = 0xff1a0f0b
        ASPVBScriptString = 0xffcfcfef
        SGMLBlockDefault = 0xffcccce0
        PythonKeyword = 0xffefffef
        XMLTagEnd = 0xff1a0f0b
        ASPVBScriptComment = 0xffcfcfef
        ASPPythonSingleQuotedString = 0xffcfefcf
        PHPDoubleQuotedVariable = 0xfffff8f8
        ASPJavaScriptComment = 0xffdfdf7f
        JavaScriptUnclosedString = 0xffbfbbb0
        JavaScriptDoubleQuotedString = 0xfff0f0ff
        UnknownAttribute = 0xff1a0f0b
        ASPPythonOperator = 0xffcfefcf
        ASPJavaScriptSymbol = 0xffdfdf7f
        ASPPythonFunctionMethodName = 0xffcfefcf
        SGMLDoubleQuotedString = 0xffefefff
        PHPOperator = 0xfffff8f8
        JavaScriptNumber = 0xfff0f0ff
        PythonDoubleQuotedString = 0xffefffef
        ASPAtStart = 0xffffff00
        Script = 0xff1a0f0b
        PHPCommentLine = 0xfffff8f8
        SGMLComment = 0xffefefff
        JavaScriptStart = 0xff1a0f0b
        ASPPythonIdentifier = 0xffcfefcf
        ASPVBScriptKeyword = 0xffcfcfef
        ASPPythonTripleDoubleQuotedString = 0xffcfefcf
        ASPPythonKeyword = 0xffcfefcf
        ASPJavaScriptNumber = 0xffdfdf7f
        PHPStart = 0xffffefbf
        PythonTripleSingleQuotedString = 0xffefffef
        PHPNumber = 0xfffff8f8
        ASPPythonDefault = 0xffcfefcf
        SGMLSpecial = 0xffefefff
        OtherInTag = 0xff1a0f0b
        JavaScriptCommentDoc = 0xfff0f0ff
        Tag = 0xff1a0f0b
        XMLEnd = 0xff1a0f0b
        CDATA = 0xfffff0f0
        HTMLNumber = 0xff1a0f0b
        SGMLError = 0xffff6666
        PHPKeyword = 0xfffff8f8
        ASPVBScriptUnclosedString = 0xff7f7fff
        ASPPythonNumber = 0xffcfefcf
        VBScriptString = 0xffefefff
        ASPPythonClassName = 0xffcfefcf
        ASPPythonStart = 0xff1a0f0b
        JavaScriptRegex = 0xffffbbb0
        ASPJavaScriptUnclosedString = 0xffbfbbb0
        ASPJavaScriptCommentLine = 0xffdfdf7f
        SGMLEntity = 0xffefefff
        ASPJavaScriptDoubleQuotedString = 0xffdfdf7f
        ASPStart = 0xffffdf00
        Attribute = 0xff1a0f0b
        ASPJavaScriptKeyword = 0xffdfdf7f
        ASPVBScriptDefault = 0xffcfcfef
        ASPVBScriptIdentifier = 0xffcfcfef
        ASPJavaScriptRegex = 0xffffbbb0
        VBScriptNumber = 0xffefefff
        HTMLDoubleQuotedString = 0xff1a0f0b
        ASPXCComment = 0xff1a0f0b
        VBScriptStart = 0xff1a0f0b
        PHPDoubleQuotedString = 0xfffff8f8
        PHPComment = 0xfffff8f8
        ASPPythonTripleSingleQuotedString = 0xffcfefcf
        ASPPythonDoubleQuotedString = 0xffcfefcf
        JavaScriptKeyword = 0xfff0f0ff
        JavaScriptSymbol = 0xfff0f0ff
        VBScriptIdentifier = 0xffefefff
        HTMLComment = 0xff1a0f0b
        UnknownTag = 0xff1a0f0b
        JavaScriptCommentLine = 0xfff0f0ff
        PythonComment = 0xffefffef
    
    class YAML:
        TextBlockMarker = 0xff1a0f0b
        DocumentDelimiter = 0xff000088
        Operator = 0xff1a0f0b
        Number = 0xff1a0f0b
        Default = 0xff1a0f0b
        Identifier = 0xff1a0f0b
        Reference = 0xff1a0f0b
        Comment = 0xff1a0f0b
        Keyword = 0xff1a0f0b
        SyntaxErrorMarker = 0xffff0000
