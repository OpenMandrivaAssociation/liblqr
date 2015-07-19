%define api	1
%define major	0
%define libname %mklibname lqr %{api} %{major}
%define devname %mklibname lqr %{api} -d

Summary:	LiquidRescale seam-carving library
Name:		liblqr
Version:	0.4.2
Release:	3
Group:		System/Libraries
License:	LGPLv3 and GPLv3
Url:		http://liblqr.wikidot.com/
Source0:	%{name}-1-%{version}.tar.bz2
Patch0:		liblqr-docbook_fixes.diff

BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-dtd45-xml
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(glib-2.0)

%description
The Liquid Rescale (lqr) library provides a C/C++ API for performing
non-uniform resizing of images by the seam-carving technique.

%package -n	%{libname}
Summary:	LiquidRescale seam-carving library
Group:		System/Libraries
Obsoletes:	%{_lib}lqr10 < 0.4.1-10

%description -n	%{libname}
The Liquid Rescale (lqr) library provides a C/C++ API for performing
non-uniform resizing of images by the seam-carving technique.

%package -n	%{devname}
Summary:	Development library and header files for the LiquidRescale library
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{devname}
This package contains the development LiquidRescale library and its header 
files.

%prep
%setup -qn %{name}-%{api}-%{version}
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
%{_libdir}/liblqr-%{api}.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING ChangeLog README
%doc docs/html/* examples
%dir %{_includedir}/lqr-%{api}
%dir %{_includedir}/lqr-%{api}/lqr
%{_includedir}/lqr-%{api}/*.h
%{_includedir}/lqr-%{api}/lqr/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

