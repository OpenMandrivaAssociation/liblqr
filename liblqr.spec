%define	major 0
%define libname %mklibname lqr %{major}
%define develname %mklibname lqr -d

%define libname_old %mklibname lqr1_ 0

Name: liblqr
Version: 0.4.1
Release: 6
Summary:LiquidRescale seam-carving library
Group: System/Libraries
License: LGPLv3 and GPLv3
URL: http://liblqr.wikidot.com/
Source0: %{name}-1-%{version}.tar.bz2
Patch0: liblqr-docbook_fixes.diff

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
Obsoletes:  %{libname_old}

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
rm -rf %{buildroot}

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
