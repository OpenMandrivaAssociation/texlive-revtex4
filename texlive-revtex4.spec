Name:		texlive-revtex4
Version:	20180303
Release:	2
Summary:	TeXLive revtex4 package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/revtex4.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/revtex4.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/revtex4.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive revtex4 package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bib/revtex4
%{_texmfdistdir}/bibtex/bst/revtex4
%{_texmfdistdir}/tex/latex/revtex4
%doc %{_texmfdistdir}/doc/latex/revtex4
#- source
%doc %{_texmfdistdir}/source/latex/revtex4

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
