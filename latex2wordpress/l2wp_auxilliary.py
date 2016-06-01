import re

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

def extract_body(tex_code):
    begin_and_end_document = re.compile('\\\\begin\\{document}|\\\\end\\{document}')
    begin_document = re.compile('\\\\begin\s*') 
    end_document = re.compile('\\\\end\s*')
    ignored_text_when_parsed = re.compile('\\\\iffalse|\\\\ifblog|\\\\iftex|\\\\fi')
    math_mode = re.compile('\\$\\$')
    multiple_returns = re.compile('\n\n+')
    spaces = re.compile('(\n|[ ])+')
    tex_comments = re.compile('%.*?\n')

    tex_code = begin_document.sub('\\\\begin', tex_code)
    tex_code = end_document.sub('\\\\end', tex_code)

    parsed_code = begin_and_end_document.split(tex_code)
    if len(parsed_code) == 1:
        tex_code = parsed_code[0]
    else:
        tex_code = parsed_code[1]

    for escape_code in escaped_characters:
        tex_code = tex_code.replace(escape_code[0], escape_code[1])
    
    tex_code = tex_comments.sub(' ', tex_code)
    tex_code = multiple_returns.sub('<p>', tex_code)
    tex_code = spaces.sub(' ', tex_code)
   
    L = ignored_text_when_parsed.split(tex_code)
    I = ignored_text_when_parsed.findall(tex_code)
    tex_code = L[0] 
    for i in range(1, int((len(L) + 1)/ 2)):
        if (I[2*i - 2] == '\\ifblog'):
            tex_code = tex_code + L[2*i-1]
        tex_code = tex_code + L[2*i]

    L = math_mode.split(tex_code) 
    tex_code = L[0]
    for i in range(1, int((len(L) + 1)/2)):
        tex_code = tex_code + '\\[' + L[2*i - 1] + '\\]' + L[2*i]

    tex_code = tex_code.replace('\\begin{eqnarray*}', '\\[ \\begin{array}{rcl}')
    tex_code = tex_code.replace('\\end{eqnarray*}', '\\end{array} \\]')

    return tex_code
