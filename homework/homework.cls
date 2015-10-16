% A LaTeX class for homework in
% mathematical subjects.

% Contains a environment for the problem text, one for the solution. a command
% for a list of results used in the margin.
% 

% Identification part
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{homework}[2015/10/14 Homework class for mathematical subjects]

\def\course#1{\def\@course{#1}}
\def\weekno#1{\def\@weekno{Week #1}}

\newcommand{\comment}[1]{\footnote{\color{blue} #1}}
\newcommand{\unsure}[1]{\footnote{\color{red} #1}}
\newcommand{\week}[1]{%
  \newpage
  \weekno{#1}
  \section{Week #1}
  \secttoc
}

\newcommand{\problem}[1]{\subsection{Problem #1}}
\newenvironment{problemtext}
{\itshape\begin{flushleft}}{\end{flushleft}\rmfamily}

\LoadClass{article}

%\renewcommand{\maketitle}{%
%  
%  \@title
%  \@author
% \@course
%}
\AtEndOfClass{\RequirePackage[flushmargin, ragged, side]{footmisc}}
\AtEndOfClass{\RequirePackage{fancyhdr}}
\AtEndOfClass{\RequirePackage{enumerate}}
\AtEndOfClass{\RequirePackage{minitoc}}
\AtEndOfClass{\RequirePackage{amsthm, amsmath, amssymb}}
\AtEndOfClass{\RequirePackage{color}}

\AtEndOfClass{\pagestyle{fancy}}
\AtEndOfClass{\lhead{\@course}}
\AtEndOfClass{\chead{\@author}}
\AtEndOfClass{\rhead{\@weekno}}

\AtEndOfClass{\theoremstyle{definition}}
\AtEndOfClass{\newtheorem*{solution}{Solution}}
\AtEndOfClass{\setcounter{secnumdepth}{0}}
\AtEndOfClass{\setcounter{tocdepth}{1}}
\AtBeginDocument{%
  \weekno{0}
  \maketitle
  \dosecttoc
  \tableofcontents
}
