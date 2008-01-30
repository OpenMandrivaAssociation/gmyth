%define name gmyth
%define version 0.4
%define rel %mkrel 2

%define major 0
%define libname %mklibname %{name} %{major}
%define libname_devel %mklibname -d %{name}

Summary: MythTV remote access libraries
Name: %{name}
Version: %version
Release: %rel
License: LGPLv2+
Group: System/Libraries
Source0: http://downloads.sourceforge.net/%{name}/%{name}_%{version}.tar.gz
Source1: COPYING.LGPL
# http://bugzilla.gnome.org/show_bug.cgi?id=483748
Patch1: gmyth_file_transfer-missing-context-unlock-on-error.diff
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
URL: http://gmyth.sf.net
BuildRequires: mysql-devel
BuildRequires: curl-devel
BuildRequires: libxml2-devel
BuildRequires: glib2-devel

%description
GMyth is a library used by applications to access content provided by the
MythTV set-top box framework, such as Live TV broadcasts, TV recordings, or
TV listings.

%package -n %{libname}
Summary: Library files for MythTV remote access
Group: System/Libraries
Requires: %{name} = %{version}-%{release}

%description -n %{libname}
gmyth-devel contains development libraries and headers for the GMyth library.

%package -n %{libname_devel}
Summary: Development libraries for MythTV remote access
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{libname_devel}
Development libraries and headers for the GMyth library.

%prep
%setup -q -n %{name}
# Upstream used the default license from the autotools, all the
# files and the project page says LGPL, see:
# http://sourceforge.net/tracker/index.php?func=detail&aid=1790620&group_id=177106&atid=879914
cp -a %{SOURCE1} .
%patch1 -p1 -b .not-port-crasher

%build
%configure
make %{?_smp_mflags}
chmod a-x src/*.[ch]

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/*.la
rm -f %{buildroot}/%{_libdir}/*.a

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS COPYING.LGPL
%{_bindir}/*

%files -n %{libname}
%{_libdir}/libgmyth.so.%{major}*

%files -n %{libname_devel}
%defattr(-,root,root)
%{_includedir}/gmyth
%{_libdir}/libgmyth.so
%{_libdir}/pkgconfig/*.pc

