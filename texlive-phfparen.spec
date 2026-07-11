%global tl_name phfparen
%global tl_revision 41859

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Parenthetic math expressions made simpler and less redundant
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/phfparen
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/phfparen.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/phfparen.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/phfparen.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a more condensed and flexible syntax for
parenthesis-delimited expressions in math mode which also allows for an
easier switching of brace sizes. For example, the syntax " `\big( a + b
) " can be used to replace "\bigl( a + b \bigr)".

