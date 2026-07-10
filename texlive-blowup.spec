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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package blowup only defines the user-level macro \blowUp, which can
be used to upscale or downscale all pages of a document. It is similar
to the TeX primitive \magnification but more accurate and user-friendly.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/blowup
%dir %{_datadir}/texmf-dist/source/latex/blowup
%dir %{_datadir}/texmf-dist/tex/latex/blowup
%doc %{_datadir}/texmf-dist/doc/latex/blowup/README.md
%doc %{_datadir}/texmf-dist/doc/latex/blowup/blowup-ex1.pdf
%doc %{_datadir}/texmf-dist/doc/latex/blowup/blowup-ex1.tex
%doc %{_datadir}/texmf-dist/doc/latex/blowup/blowup-ex2.pdf
%doc %{_datadir}/texmf-dist/doc/latex/blowup/blowup-ex2.tex
%doc %{_datadir}/texmf-dist/doc/latex/blowup/blowup-ex3.pdf
%doc %{_datadir}/texmf-dist/doc/latex/blowup/blowup-ex3.tex
%doc %{_datadir}/texmf-dist/doc/latex/blowup/blowup-ex4.pdf
%doc %{_datadir}/texmf-dist/doc/latex/blowup/blowup-ex4.tex
%doc %{_datadir}/texmf-dist/doc/latex/blowup/blowup-ex5.pdf
%doc %{_datadir}/texmf-dist/doc/latex/blowup/blowup-ex5.tex
%doc %{_datadir}/texmf-dist/doc/latex/blowup/blowup-ex6.pdf
%doc %{_datadir}/texmf-dist/doc/latex/blowup/blowup-ex6.tex
%doc %{_datadir}/texmf-dist/doc/latex/blowup/blowup.pdf
%doc %{_datadir}/texmf-dist/source/latex/blowup/blowup.dtx
%doc %{_datadir}/texmf-dist/source/latex/blowup/blowup.ins
%{_datadir}/texmf-dist/tex/latex/blowup/blowup.sty
