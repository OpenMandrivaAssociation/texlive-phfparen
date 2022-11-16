Name:		texlive-phfparen
Version:	41859
Release:	1
Summary:	Parenthetic math expressions made simpler and less redundant
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/phfparen
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phfparen.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phfparen.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phfparen.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a more condensed and flexible syntax for
parenthesis-delimited expressions in math mode which also
allows for an easier switching of brace sizes. For example, the
syntax " `\big( a + b ) " can be used to replace "\bigl( a + b
\bigr)".

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/phfparen
%{_texmfdistdir}/tex/latex/phfparen
%doc %{_texmfdistdir}/doc/latex/phfparen

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
