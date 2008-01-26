Summary:	C++ wrappers for libgnomeui
Summary(pl.UTF-8):	Interfejsy C++ dla libgnomeui
Name:		libgnomeuimm
Version:	2.20.0
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgnomeuimm/2.20/%{name}-%{version}.tar.bz2
# Source0-md5:	350d3424247611a009432395aff8619f
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gconfmm-devel >= 2.20.0
BuildRequires:	gnome-vfsmm-devel >= 2.20.0
# "We would need libbonobuimm to support Bonobo::Dock, but it's not worth the bother"
#BuildRequires:	libbonobouimm-devel >= 1.3.6`
BuildRequires:	libglademm-devel >= 2.6.4
BuildRequires:	libgnomecanvasmm-devel >= 2.20.0
BuildRequires:	libgnomemm-devel >= 2.20.0
BuildRequires:	libgnomeui-devel >= 2.19.1
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	pkgconfig
Requires:	libgnomeui >= 2.19.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for libgnomeui.

%description -l pl.UTF-8
Interfejsy C++ dla libgnomeui.

%package devel
Summary:	Devel files for libgnomeuimm
Summary(pl.UTF-8):	Pliki nagłówkowe dla libgnomeuimm
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gconfmm-devel >= 2.20.0
Requires:	gnome-vfsmm-devel >= 2.20.0
Requires:	libglademm-devel >= 2.6.4
Requires:	libgnomecanvasmm-devel >= 2.20.0
Requires:	libgnomemm-devel >= 2.20.0
Requires:	libgnomeui-devel >= 2.19.1

%description devel
Devel files for libgnomeuimm.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla libgnomeuimm.

%package static
Summary:	libgnomeuimm static library
Summary(pl.UTF-8):	Biblioteka statyczna libgnomeuimm
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libgnomeuimm static library.

%description static -l pl.UTF-8
Biblioteka statyczna libgnomeuimm.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I scripts
%{__autoconf}
%{__automake}
%configure \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{_libdir}/libgnomeuimm-2.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnomeuimm-2.6.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomeuimm-2.6.so
%{_libdir}/libgnomeuimm-2.6.la
%{_libdir}/%{name}-2.6
%{_includedir}/%{name}-2.6
%{_pkgconfigdir}/%{name}-2.6.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomeuimm-2.6.a
