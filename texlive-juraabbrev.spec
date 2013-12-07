# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/juraabbrev
# catalog-date 2007-01-08 14:12:54 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-juraabbrev
Version:	20070108
Release:	4
Summary:	Abbreviations for typesetting (German) juridical documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/juraabbrev
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/juraabbrev.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/juraabbrev.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/juraabbrev.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package should be helpful for people working on (German)
law. It helps you to handle abbreviations and creates a list of
those (pre-defined) abbreviations that have actually been used
in the document.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070108-2
+ Revision: 752937
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070108-1
+ Revision: 718761
- texlive-juraabbrev
- texlive-juraabbrev
- texlive-juraabbrev
- texlive-juraabbrev

