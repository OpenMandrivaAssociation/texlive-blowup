Name:		texlive-blowup
Version:	1.0
Release:	2
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
%{_texmfdistdir}/tex/latex/blowup
%doc %{_texmfdistdir}/doc/latex/blowup
#- source
%doc %{_texmfdistdir}/source/latex/blowup

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
