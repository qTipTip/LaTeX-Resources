% A LaTeX class for homework in
% mathematical subjects.

% Contains a environment for the problem text, one for the solution. a command
% for a list of results used in the margin.
% 

% Identification part
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{homework}[2015/10/14 Homework class for mathematical subjects]

% Declaration of options

% Passes unrecognized options to the parent class

% EXECUTION OF OPTIONS:

% PACKAGE LOADING

% SPECIAL COMMANDS FOR PACKAGE AND CLASS FILES

%variables

\def\course#1{\def\@course{#1}}
\def\weekno#1{\def\@weekno{Week #1}}

\newcommand{\comment}[1]{\footnote{#1}}
\newcommand{\week}[1]{%
  \newpage
  \weekno{#1}
}


\newcommand{\problem}[1]{\section*{Problem #1}}
\newenvironment{problemtext}
{\begin{center} \textsc{Problem Statement} \end{center}\itshape \begin{quote}}{\end{quote}\rmfamily}

\LoadClass{article}

\AtEndOfClass{\RequirePackage[ragged, side]{footmisc}}
\AtEndOfClass{\RequirePackage{fancyhdr}}
\AtEndOfClass{\RequirePackage{enumerate}}
\AtEndOfClass{\pagestyle{fancy}}
\AtEndOfClass{\RequirePackage{amsthm, amsmath, amssymb}}
\AtEndOfClass{\lhead{\@course}}
\AtEndOfClass{\chead{\@author}}
\AtEndOfClass{\rhead{\@weekno}}
\AtEndOfClass{\theoremstyle{definition}}
\AtEndOfClass{\newtheorem*{solution}{Solution}}

