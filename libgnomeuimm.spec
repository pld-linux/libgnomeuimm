Summary:	C++ wrappers for libgnomeui
Summary(pl):	Interfejsy C++ dla libgnomeui
Name:		libgnomeuimm
Version:	1.3.17
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/1.3/%{name}-%{version}.tar.bz2
# Source0-md5:	d1a7401da06fc5bdd91d498f884df0b3
Patch0:		%{name}-gcc33.patch
URL:		http://www.gnome.org/
BuildRequires:	gconfmm-devel >= 2.0.1-2
BuildRequires:	gtkmm-devel >= 2.2.6
BuildRequires:	libbonobouimm-devel >= 1.3.6
BuildRequires:	libglademm-devel >= 2.1.0
Buildrequires:	libgnomecanvasmm-devel >= 2.0.1
BuildRequires:	libgnomemm-devel >= 1.3.10-2
BuildRequires:	libgnomeui-devel >= 2.3.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for libgnomeui.

%description -l pl
Interfejsy C++ dla libgnomeui.

%package devel
Summary:	Devel files for libgnomeuimm
Summary(pl):	Pliki nag³ówkowe dla libgnomeuimm
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Devel files for libgnomeuimm.

%description devel -l pl
Pliki nag³ówkowe dla libgnomeuimm.

%package static
Summary:	libgnomecanvasmm static library
Summary(pl):	Biblioteka statyczna libgnomeuimm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
libgnomeuimm static library.

%description static -l pl
Biblioteka statyczna libgnomeuimm.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--enable-static=yes

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
%attr(755,root,root) %{_libdir}/libgnomeuimm*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}-2.0
%{_libdir}/libgnomeuimm*.la
%{_libdir}/libgnomeuimm*.so
%{_libdir}/%{name}-2.0
%{_pkgconfigdir}/%{name}-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomeuimm*.a
