# revision 16488
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-revtex4
Version:	20111102
Release:	1
Summary:	TeXLive revtex4 package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/revtex4.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/revtex4.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/revtex4.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
TeXLive revtex4 package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bib/revtex4/apssamp.bib
%{_texmfdistdir}/bibtex/bst/revtex4/apsrev.bst
%{_texmfdistdir}/bibtex/bst/revtex4/apsrmp.bst
%{_texmfdistdir}/tex/latex/revtex4/10pt.rtx
%{_texmfdistdir}/tex/latex/revtex4/11pt.rtx
%{_texmfdistdir}/tex/latex/revtex4/12pt.rtx
%{_texmfdistdir}/tex/latex/revtex4/aps.rtx
%{_texmfdistdir}/tex/latex/revtex4/docs.sty
%{_texmfdistdir}/tex/latex/revtex4/revsymb.sty
%{_texmfdistdir}/tex/latex/revtex4/revtex4.cls
%{_texmfdistdir}/tex/latex/revtex4/rmp.rtx
%doc %{_texmfdistdir}/doc/latex/revtex4/DOWNLOAD
%doc %{_texmfdistdir}/doc/latex/revtex4/README
%doc %{_texmfdistdir}/doc/latex/revtex4/apssamp.end
%doc %{_texmfdistdir}/doc/latex/revtex4/apssamp.tex
%doc %{_texmfdistdir}/doc/latex/revtex4/auguide.tex
%doc %{_texmfdistdir}/doc/latex/revtex4/differ.tex
%doc %{_texmfdistdir}/doc/latex/revtex4/fig_1.eps
%doc %{_texmfdistdir}/doc/latex/revtex4/fig_2.eps
%doc %{_texmfdistdir}/doc/latex/revtex4/ltxdocext.pdf
%doc %{_texmfdistdir}/doc/latex/revtex4/ltxgrid.pdf
%doc %{_texmfdistdir}/doc/latex/revtex4/ltxutil.pdf
%doc %{_texmfdistdir}/doc/latex/revtex4/revtex4.pdf
%doc %{_texmfdistdir}/doc/latex/revtex4/summary.tex
%doc %{_texmfdistdir}/doc/latex/revtex4/template.aps
#- source
%doc %{_texmfdistdir}/source/latex/revtex4/ltxdocext.dtx
%doc %{_texmfdistdir}/source/latex/revtex4/ltxgrid.dtx
%doc %{_texmfdistdir}/source/latex/revtex4/ltxutil.dtx
%doc %{_texmfdistdir}/source/latex/revtex4/revtex4.dtx
%doc %{_texmfdistdir}/source/latex/revtex4/revtex4.ins
%doc %{_texmfdistdir}/source/latex/revtex4/textcase.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
