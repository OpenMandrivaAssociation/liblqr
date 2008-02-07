%define	major 0
%define libname %mklibname lqr %{major}
%define develname %mklibname lqr -d

Summary:	LiquidRescale seam-carving library
Name:		liblqr
Version:	0.1.0
Release:	%mkrel 1
Group:		System/Libraries
License:	GPLv2+
URL:		http://liquidrescale.wikidot.com/
Source0:	http://liblqr.wikidot.com/local--files/en:download-page/%{name}-1-%{version}-1.tar.gz
Patch0:		liblqr-docbook_fixes.diff
BuildRequires:	glib
BuildRequires:	gimp-devel >= 2.2.13
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-dtd45-xml
BuildRequires:	libxslt-proc
Requires:	gimp >= 2.2.13
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Liquid Rescale (lqr) library provides a C/C++ API for performing
non-uniform resizing of images by the seam-carving technique.

%package -n	%{libname}
Summary:	LiquidRescale seam-carving library
Group:		System/Libraries

%description -n	%{libname}
The Liquid Rescale (lqr) library provides a C/C++ API for performing
non-uniform resizing of images by the seam-carving technique.

%package -n	%{develname}
Summary:	Static library and header files for the LiquidRescale library
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lqr-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description -n	%{develname}
The Liquid Rescale (lqr) library provides a C/C++ API for performing
non-uniform resizing of images by the seam-carving technique.

This package contains the static LiquidRescale library and its header files.

%prep

%setup -q -n %{name}-1-%{version}
%patch0 -p1

%build

%configure2_5x

%make

# make the html docs
pushd docs
make
popd

%install
rm -rf %{buildroot}

%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc docs/html/* examples
%dir %{_includedir}/lqr-1
%dir %{_includedir}/lqr-1/lqr
%{_includedir}/lqr-1/*.h
%{_includedir}/lqr-1/lqr/*.h
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc

