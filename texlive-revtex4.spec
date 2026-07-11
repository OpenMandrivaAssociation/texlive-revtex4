%global tl_name revtex4
%global tl_revision 56589

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.0a
Release:	%{tl_revision}.1
Summary:	Styles for various Physics Journals (old version)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/obsolete/macros/latex/contrib/revtex4-0
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/revtex4.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/revtex4.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/revtex4.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is an old version of revtex, and is kept as a courtesy to users
having difficulty with the incompatibility of that latest version.

