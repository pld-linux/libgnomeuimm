Summary:	C++ wrappers for libgnomeui
Summary(pl):	Interfejsy C++ dla libgnomeui
Name:		libgnomeuimm
Version:	2.5.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.5/%{name}-%{version}.tar.bz2
# Source0-md5:	c6397f03db076afaace2e23786762f40
URL:		http://www.gnome.org/
BuildRequires:	gconfmm-devel >= 2.5.1
# "We would need libbonobuimm to support Bonobo::Dock, but it's not worth the bother"
#BuildRequires:	libbonobouimm-devel >= 1.3.6
BuildRequires:	libglademm-devel >= 2.3.2
BuildRequires:	libgnomecanvasmm-devel >= 2.5.1
BuildRequires:	libgnomemm-devel >= 2.5.1
BuildRequires:	libgnomeui-devel >= 2.5.4
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for libgnomeui.

%description -l pl
Interfejsy C++ dla libgnomeui.

%package devel
Summary:	Devel files for libgnomeuimm
Summary(pl):	Pliki nag³ówkowe dla libgnomeuimm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gconfmm-devel >= 2.5.1
Requires:	libglademm-devel >= 2.3.2
Requires:	libgnomecanvasmm-devel >= 2.5.1
Requires:	libgnomemm-devel >= 2.5.1
Requires:	libgnomeui-devel >= 2.5.4

%description devel
Devel files for libgnomeuimm.

%description devel -l pl
Pliki nag³ówkowe dla libgnomeuimm.

%package static
Summary:	libgnomeuimm static library
Summary(pl):	Biblioteka statyczna libgnomeuimm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libgnomeuimm static library.

%description static -l pl
Biblioteka statyczna libgnomeuimm.

%prep
%setup -q

%build
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
%attr(755,root,root) %{_libdir}/libgnomeuimm*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomeuimm*.so
%{_libdir}/libgnomeuimm*.la
%{_libdir}/%{name}-2.0
%{_libdir}/%{name}-2.6
%{_includedir}/%{name}-2.6
%{_pkgconfigdir}/%{name}-2.6.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomeuimm*.a
