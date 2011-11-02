Name:		texlive-juraabbrev
Version:	20070108
Release:	1
Summary:	Abbreviations for typesetting (German) juridical documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/juraabbrev
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/juraabbrev.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/juraabbrev.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/juraabbrev.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package should be helpful for people working on (German)
law. It helps you to handle abbreviations and creates a list of
those (pre-defined) abbreviations that have actually been used
in the document.

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
%{_texmfdistdir}/makeindex/juraabbrev/laws.ist
%{_texmfdistdir}/tex/latex/juraabbrev/juraabbrev.4ht
%{_texmfdistdir}/tex/latex/juraabbrev/juraabbrev.sty
%doc %{_texmfdistdir}/doc/latex/juraabbrev/README
%doc %{_texmfdistdir}/doc/latex/juraabbrev/abbrevtest.tex
%doc %{_texmfdistdir}/doc/latex/juraabbrev/juraabbrev.pdf
#- source
%doc %{_texmfdistdir}/source/latex/juraabbrev/juraabbrev.dtx
%doc %{_texmfdistdir}/source/latex/juraabbrev/juraabbrev.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc source %{buildroot}%{_texmfdistdir}
