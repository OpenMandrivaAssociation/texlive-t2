# revision 29349
# category Package
# catalog-ctan /macros/latex/contrib/t2
# catalog-date 2012-06-05 14:57:36 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-t2
Version:	20120605
Release:	2
Summary:	Support for using T2 encoding
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/t2
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/t2.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/t2.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex

%description
The T2 bundle provides a variety of separate support functions,
for using Cyrillic characters in LaTeX: - the mathtext package,
for using Cyrillic letters 'transparently' in formulae - the
citehack package, for using Cyrillic (or indeed any non-ascii)
characters in citation keys; - support for Cyrillic in BibTeX;
- support for Cyrillic in Makeindex; and - various items of
font support.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/t2/t2a-mod1.enc
%{_texmfdistdir}/fonts/enc/t2/t2a-mod2.enc
%{_texmfdistdir}/fonts/enc/t2/t2a.enc
%{_texmfdistdir}/fonts/enc/t2/t2b.enc
%{_texmfdistdir}/fonts/enc/t2/t2c.enc
%{_texmfdistdir}/fonts/enc/t2/x2.enc
%{_texmfdistdir}/tex/generic/t2/cyrfinst/6r.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/README
%{_texmfdistdir}/tex/generic/t2/cyrfinst/cyrillic.mtx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/lcyc.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/lcyci.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/lcycij.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/lcycj.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/lcyctt.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/lcyi.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/lcyij.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/lcyitt.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/lcyj.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/lcytt.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/ot2c.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/ot2cj.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/ot2i.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/ot2ij.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/ot2j.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/t2ac.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/t2acj.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/t2ai.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/t2aij.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/t2aj.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/t2bc.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/t2bcj.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/t2bi.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/t2bij.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/t2bj.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/t2cc.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/t2ccj.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/t2ci.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/t2cij.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/t2cj.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/x2c.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/x2cj.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/x2i.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/x2ij.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/derivatives/x2j.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/etc/alias-cmc.tex
%{_texmfdistdir}/tex/generic/t2/cyrfinst/etc/alias-wncy.tex
%{_texmfdistdir}/tex/generic/t2/cyrfinst/etc/cyralias.tex
%{_texmfdistdir}/tex/generic/t2/cyrfinst/etc/fnstcorr.tex
%{_texmfdistdir}/tex/generic/t2/cyrfinst/etc/showenc
%{_texmfdistdir}/tex/generic/t2/cyrfinst/lcy-hi.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/lcy.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/ot2.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/t2a.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/t2b.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/t2c.etx
%{_texmfdistdir}/tex/generic/t2/cyrfinst/x2.etx
%{_texmfdistdir}/tex/latex/t2/citehack.sty
%{_texmfdistdir}/tex/latex/t2/mathtext.sty
%{_texmfdistdir}/tex/latex/t2/misccorr.sty
%_texmf_fmtutil_d/t2
%doc %{_texmfdistdir}/doc/generic/t2/Makefile
%doc %{_texmfdistdir}/doc/generic/t2/OT2uni.map
%doc %{_texmfdistdir}/doc/generic/t2/README
%doc %{_texmfdistdir}/doc/generic/t2/T2Auni.map
%doc %{_texmfdistdir}/doc/generic/t2/T2Buni.map
%doc %{_texmfdistdir}/doc/generic/t2/T2Cuni.map
%doc %{_texmfdistdir}/doc/generic/t2/X2uni.map
%doc %{_texmfdistdir}/doc/generic/t2/amscyr.txt
%doc %{_texmfdistdir}/doc/generic/t2/broken1.txt
%doc %{_texmfdistdir}/doc/generic/t2/broken2.txt
%doc %{_texmfdistdir}/doc/generic/t2/cyrcset7.txt
%doc %{_texmfdistdir}/doc/generic/t2/cyrcset8.txt
%doc %{_texmfdistdir}/doc/generic/t2/cyrcsets.ind
%doc %{_texmfdistdir}/doc/generic/t2/etc/amsppt.diff
%doc %{_texmfdistdir}/doc/generic/t2/etc/mathtext.dtx
%doc %{_texmfdistdir}/doc/generic/t2/etc/mathtext.ins
%doc %{_texmfdistdir}/doc/generic/t2/etc/rubibtex/README
%doc %{_texmfdistdir}/doc/generic/t2/etc/rubibtex/rubibtex
%doc %{_texmfdistdir}/doc/generic/t2/etc/rubibtex/rubibtex.bat
%doc %{_texmfdistdir}/doc/generic/t2/etc/rubibtex/rubibtex.old
%doc %{_texmfdistdir}/doc/generic/t2/etc/rubibtex/rubibtex.sed
%doc %{_texmfdistdir}/doc/generic/t2/etc/ruinpenc
%doc %{_texmfdistdir}/doc/generic/t2/etc/rumkidx/README
%doc %{_texmfdistdir}/doc/generic/t2/etc/rumkidx/rumakeindex
%doc %{_texmfdistdir}/doc/generic/t2/etc/rumkidx/rumkidx1.sed
%doc %{_texmfdistdir}/doc/generic/t2/etc/rumkidx/rumkidx2.sed
%doc %{_texmfdistdir}/doc/generic/t2/etc/rumkidx/rumkidx3.sed
%doc %{_texmfdistdir}/doc/generic/t2/etc/rumkidx/rumkidxd.bat
%doc %{_texmfdistdir}/doc/generic/t2/etc/rumkidx/rumkidxw.bat
%doc %{_texmfdistdir}/doc/generic/t2/etc/t2filter.c
%doc %{_texmfdistdir}/doc/generic/t2/etc/utf-8/test-utf8.tex
%doc %{_texmfdistdir}/doc/generic/t2/etc/utf-8/utf-8.def
%doc %{_texmfdistdir}/doc/generic/t2/etc/utf-8/utfcyr.def
%doc %{_texmfdistdir}/doc/generic/t2/etc/utf-8/utflat.def
%doc %{_texmfdistdir}/doc/generic/t2/examples/example1.tex
%doc %{_texmfdistdir}/doc/generic/t2/examples/example2.tex
%doc %{_texmfdistdir}/doc/generic/t2/examples/example3.tex
%doc %{_texmfdistdir}/doc/generic/t2/examples/example4.tex
%doc %{_texmfdistdir}/doc/generic/t2/examples/example5.tex
%doc %{_texmfdistdir}/doc/generic/t2/make-enc.pl
%doc %{_texmfdistdir}/doc/generic/t2/mkencs.sh
%doc %{_texmfdistdir}/doc/generic/t2/mtcyr.txt
%doc %{_texmfdistdir}/doc/generic/t2/t2cyr.txt
%doc %{_texmfdistdir}/doc/generic/t2/t2lat.txt
%doc %{_texmfdistdir}/doc/generic/t2/urwcyr.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/t2 <<EOF
#
# from t2:
#! cyramstex pdftex language.dat -translate-file=cp227.tcx *cyramstx.ini
#! cyrtex pdftex language.dat -translate-file=cp227.tcx *cyrtex.ini
#! cyrtexinfo pdftex language.dat -translate-file=cp227.tcx *cyrtxinf.ini
EOF
