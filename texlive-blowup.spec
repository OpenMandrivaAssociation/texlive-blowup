%global tl_name blowup
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2.0
Release:	%{tl_revision}.1
Summary:	Upscale or downscale all pages of a document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/blowup
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/blowup.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/blowup.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/blowup.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package blowup only defines the user-level macro \blowUp, which can
be used to upscale or downscale all pages of a document. It is similar
to the TeX primitive \magnification but more accurate and user-friendly.

