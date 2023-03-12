Name:           bdwgc
Version:        8.3.0
Release:        1
Summary:        Boehm-Demers-Weiser Garbage Collector
Url:            http://www.hboehm.info/gc/
Source:         https://github.com/ivmai/bdwgc
License:        MIT
BuildRequires:  autoconf
BuildRequires:  libtool

%description
A conservative garbage collector for C and C++.

%package devel
Summary:        bdwgc development package
Requires:       %{name} = %{version}

%description devel
Development headers and libraries for bdwgc - A conservative garbage collector for C and C++.

%prep
%autosetup -n %{name}-%{version}/upstream

%build

autoreconf -vif
%configure --disable-docs --disable-dependency-tracking

%make_build

%install

%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license LICENSE
%{_libdir}/libcord.so.*
%{_libdir}/libgc.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/libcord.so
%{_libdir}/libgc.so
%{_libdir}/pkgconfig/bdw-gc.pc

%{_includedir}/gc.h
%dir %{_includedir}/gc
%{_includedir}/gc/*.h

