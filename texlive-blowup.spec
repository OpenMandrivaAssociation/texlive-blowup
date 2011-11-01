Name:		texlive-blowup
Version:	0.1j
Release:	1
Summary:	Upscale or downscale all pages of a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/blowup
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/blowup.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/blowup.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/blowup.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package blowup only defines the user-level macro \blowup,
which can be used to upscale or downscale all pages of a
document. It is similar to the TeX primitive \magnification but
more accurate and user-friendly.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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
