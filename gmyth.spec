%define name gmyth
%define version 0.7
%define rel %mkrel 3

%define major 0
%define libname %mklibname %{name} %{major}
%define libname_devel %mklibname -d %{name}

Summary: MythTV remote access libraries
Name: %{name}
Version: %version
Release: %rel
# COPYING file states GPL but all source indicates LGPL.
# http://sourceforge.net/tracker/index.php?func=detail&aid=1790620&group_id=177106&atid=879914
License: LGPLv2+
Group: System/Libraries
Source0: http://downloads.sourceforge.net/%{name}/%{name}_%{version}-indt1.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
URL: http://gmyth.sf.net
BuildRequires: mysql-devel
BuildRequires: curl-devel
BuildRequires: libxml2-devel
BuildRequires: glib2-devel

%description
A library and utilities used by applications to access content provided by the
MythTV set-top box framework, such as Live TV broadcasts, TV recordings, or
TV listings.

%package -n %{libname}
Summary: Library files for MythTV remote access
Group: System/Libraries
Requires: %{name} = %{version}-%{release}

%description -n %{libname}
The GMyth library.

%package -n %{libname_devel}
Summary: Development libraries/headers for MythTV remote access
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{libname_devel}
Development libraries and headers for the GMyth library.

%prep
%setup -q -n %{name}

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall
rm -f %{buildroot}/%{_libdir}/*.la
rm -f %{buildroot}/%{_libdir}/*.a

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files
%defattr(-, root, root)
%doc AUTHORS
%{_bindir}/*

%files -n %{libname}
%{_libdir}/libgmyth.so.%{major}*

%files -n %{libname_devel}
%defattr(-,root,root)
%{_includedir}/gmyth
%{_libdir}/libgmyth.so
%{_libdir}/pkgconfig/*.pc

