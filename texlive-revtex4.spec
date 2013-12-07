# revision 16488
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-revtex4
Version:	20111104
Release:	6
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111104-2
+ Revision: 755663
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111104-1
+ Revision: 719453
- texlive-revtex4
- texlive-revtex4
- texlive-revtex4
- texlive-revtex4

