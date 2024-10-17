%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Summary:	MythTV remote access libraries
Name:		gmyth
Version:	0.7.1
Release:	9
# COPYING file states GPL but all source indicates LGPL.
# http://sourceforge.net/tracker/index.php?func=detail&aid=1790620&group_id=177106&atid=879914
License:	LGPLv2+
Group:		System/Libraries
URL:		https://gmyth.sf.net
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		gmyth-0.7.1-linkage.patch
Patch1:		gmyth-0.7.1-curlheader.patch
BuildRequires:	mysql-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libxml-2.0)

%description
A library and utilities used by applications to access content provided by the
MythTV set-top box framework, such as Live TV broadcasts, TV recordings, or
TV listings.

%package -n %{libname}
Summary:	Library files for MythTV remote access
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n %{libname}
The GMyth library.

%package -n %{devname}
Summary:	Development libraries/headers for MythTV remote access
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development libraries and headers for the GMyth library.

%prep
%setup -q
%patch0 -p0
%patch1 -p1

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files
%doc AUTHORS
%{_bindir}/*

%files -n %{libname}
%{_libdir}/libgmyth.so.%{major}*

%files -n %{devname}
%{_includedir}/gmyth
%{_libdir}/libgmyth.so
%{_libdir}/pkgconfig/*.pc

