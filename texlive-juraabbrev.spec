%global tl_name juraabbrev
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Abbreviations for typesetting (German) juridical documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/juraabbrev
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/juraabbrev.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/juraabbrev.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/juraabbrev.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package should be helpful for people working on (German) law. It
helps you to handle abbreviations and creates a list of those (pre-
defined) abbreviations that have actually been used in the document

