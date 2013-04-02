%define major 0
%define libname %mklibname lqr1 %{major}
%define develname %mklibname lqr1 -d

%define libname_old %mklibname lqr1_ 0

Name:		liblqr
Version:	0.4.1
Release:	9
Summary:	LiquidRescale seam-carving library
Group:		System/Libraries
License:	LGPLv3 and GPLv3
URL:		http://liblqr.wikidot.com/
Source0:	%{name}-1-%{version}.tar.bz2
Patch0:		liblqr-docbook_fixes.diff

BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-dtd45-xml
BuildRequires:	xsltproc

%description
The Liquid Rescale (lqr) library provides a C/C++ API for performing
non-uniform resizing of images by the seam-carving technique.

%package -n	%{libname}
Summary:	LiquidRescale seam-carving library
Group:		System/Libraries
Obsoletes:	%{libname_old} < 0.4.1-8

%description -n	%{libname}
The Liquid Rescale (lqr) library provides a C/C++ API for performing
non-uniform resizing of images by the seam-carving technique.

%package -n	%{develname}
Summary:	Development library and header files for the LiquidRescale library
Group:		Development/C
Provides:	lqr-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{develname}
The Liquid Rescale (lqr) library provides a C/C++ API for performing
non-uniform resizing of images by the seam-carving technique.

This package contains the static LiquidRescale library and its header files.

%prep
%setup -q -n %{name}-1-%{version}
%apply_patches

%build
%configure2_5x \
	--disable-static

%make

# make the html docs
pushd docs
make
popd

%install
%makeinstall_std

%files -n %{libname}
%doc COPYING
%{_libdir}/liblqr-1.so.%{major}*

%files -n %{develname}
%doc AUTHORS COPYING ChangeLog README
%doc docs/html/* examples
%dir %{_includedir}/lqr-1
%dir %{_includedir}/lqr-1/lqr
%{_includedir}/lqr-1/*.h
%{_includedir}/lqr-1/lqr/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Fri May 11 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.4.1-7
+ Revision: 798234
- rel bump and rebuild

* Sat Dec 24 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.4.1-6
+ Revision: 745056
- rebuild
- cleaned up spec

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-5
+ Revision: 661486
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-4mdv2011.0
+ Revision: 602570
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-3mdv2010.1
+ Revision: 520880
- rebuilt for 2010.1

* Tue Jul 07 2009 Helio Chissini de Castro <helio@mandriva.com> 0.4.1-2mdv2010.0
+ Revision: 393320
- We need obsolete wrong named library

* Tue Jul 07 2009 Helio Chissini de Castro <helio@mandriva.com> 0.4.1-1mdv2010.0
+ Revision: 393314
- New upstream required version for digikam

* Wed Mar 18 2009 Funda Wang <fwang@mandriva.org> 0.3.0-1mdv2009.1
+ Revision: 357133
- New version 0.3.0

* Sat Aug 23 2008 Götz Waschk <waschk@mandriva.org> 0.1.0-4mdv2009.0
+ Revision: 275367
- new patch release
- update license
- drop patch 1
- spec fixes

* Sun Jul 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-3mdv2009.0
+ Revision: 232145
- added P1 to fix linkage

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Feb 07 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-1mdv2008.1
+ Revision: 163365
- import liblqr

