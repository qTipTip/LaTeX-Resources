"""
Colors
"""
latex_color = '000000'
text_colors = {
    'red' : 'ff0000',
    'green' : '00ff00',
    'blue' : '0000ff'
}

"""
Proclamations
"""

proclamation_counters = {
    'claim' : 0,
    'corollary' : 0,
    'definition' : 0,
    'equation' : 0,
    'example' : 0,
    'exercise' : 0,
    'lemma' : 0,
    'proposition' : 0,
    'remark' : 0,
    'section' : 0,
    'subsection' : 0,
    'theorem' : 0
}

"""
Proclamation and environment identifiers
"""

begin_theorem = '\n<blockquote><b>_TheoremType_ _TheoremNumber_</b> <em>'
begin_theorem_named = '\n<blockquote><b>_TheoremType_ _TheoremNumber_ (_TheoremName_)</b> <em>'
end_theorem = '</em></blockquote>\n<p>\n'

begin_proof = '<em>Proof:</em> '
end_proof = '$latex \Box&fg=000000$\n\n'

section = '\n<p>\n<b>_SectionNumber_ . _SectionName_ </b>\n<p>\n'
section_starred = '\n<p>\n<b> _SectionName_ </b>\n<p>\n'
subsection = '\n<p>\n<b>  _SectionNumber_._SubsectionNumber_. _SectionName_ </b>\n<p>\n'
subsection_starred = '\n<p>\n<b> _SecName_ </b>\n<p>\n'

"""
Font styles
"""

fontstyles = {
  r'{\em ' : 'em',
  r'{\bf ' : 'b',
  r'{\it ' : 'i',
  r'{\sl ' : 'i',
  r'\textit{' : 'i',
  r'\textsl{' : 'i',
  r'\emph{' : 'em',
  r'\textbf{' : 'b',
}

math_macros =  [
    ["\\to","\\rightarrow"] ,
    ["\\B","\\{ 0,1 \\}" ],
    ["\\E","\mathop{\\mathbb E}"],
    ["\\P","\mathop{\\mathbb P}"],
    ["\\N","{\\mathbb N}"],
    ["\\Z","{\\mathbb Z}"],
    ["\\C","{\\mathbb C}"],
    ["\\R","{\\mathbb R}"],
    ["\\Q","{\\mathbb Q}"],
    ["\\xor","\\oplus"],
    ["\\eps","\\epsilon"],
    ['\\more', '<!--more-->'],
    ['\\newblock', '\\\\'],
    ['\\sloppy', ''],
    ['\\S', '&sect;']
]


nomath_macros = [
        ["\\\\","<br/>\n"],
        ["\\ "," "],
        ["\\`a","&agrave;"],
        ["\\'a","&aacute;"],
        ["\\\"a","&auml;"],
        ["\\aa ","&aring;"],
        ["{\\aa}","&aring;"],
        ["\\`e","&egrave;"],
        ["\\'e","&eacute;"],
        ["\\\"e","&euml;"],
        ["\\`i","&igrave;"],
        ["\\'i","&iacute;"],
        ["\\\"i","&iuml;"],
        ["\\`o","&ograve;"],
        ["\\'o","&oacute;"],
        ["\\\"o","&ouml;"],
        ["\\`o","&ograve;"],
        ["\\'o","&oacute;"],
        ["\\\"o","&ouml;"],
        ["\\H o","&ouml;"],
        ["\\`u","&ugrave;"],
        ["\\'u","&uacute;"],
        ["\\\"u","&uuml;"],
        ["\\`u","&ugrave;"],
        ["\\'u","&uacute;"],
        ["\\\"u","&uuml;"],
        ["\\v{C}","&#268;"]
]
        

escaped_characters = [
    ['\\$', '_dollar_', '&#36', '\\$'],
    ['\\%', '_percent_', '&#37', '\\%'],
    ['\\&', '_amp_', '&amp;', '\\&'],
    ['>', '_greaterthan_', '>', '&gt;'],
    ['<', '_lesserthan_', '<', '&lt;']
]
