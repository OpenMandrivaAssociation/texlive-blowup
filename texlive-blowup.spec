# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/blowup
# catalog-date 2009-06-04 13:48:19 +0200
# catalog-license lppl
# catalog-version 0.1j
Name:		texlive-blowup
Version:	0.1j
Release:	8
Summary:	Upscale or downscale all pages of a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/blowup
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/blowup.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/blowup.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/blowup.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package blowup only defines the user-level macro \blowup,
which can be used to upscale or downscale all pages of a
document. It is similar to the TeX primitive \magnification but
more accurate and user-friendly.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/blowup/blowup.sty
%doc %{_texmfdistdir}/doc/latex/blowup/README
%doc %{_texmfdistdir}/doc/latex/blowup/blowup-test0.tex
%doc %{_texmfdistdir}/doc/latex/blowup/blowup-test1.tex
%doc %{_texmfdistdir}/doc/latex/blowup/blowup-test2.tex
%doc %{_texmfdistdir}/doc/latex/blowup/blowup-test3.tex
%doc %{_texmfdistdir}/doc/latex/blowup/blowup-test4.tex
%doc %{_texmfdistdir}/doc/latex/blowup/blowup-test5.tex
%doc %{_texmfdistdir}/doc/latex/blowup/blowup.pdf
#- source
%doc %{_texmfdistdir}/source/latex/blowup/blowup.dtx
%doc %{_texmfdistdir}/source/latex/blowup/blowup.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1j-2
+ Revision: 749793
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1j-1
+ Revision: 717957
- texlive-blowup
- texlive-blowup
- texlive-blowup
- texlive-blowup
- texlive-blowup

