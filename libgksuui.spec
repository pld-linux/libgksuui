Summary:	libgksuui library
Summary(pl.UTF-8):	Biblioteka libgksuui
Name:		libgksuui
Version:	1.0.7
Release:	8
License:	LGPL
Group:		Libraries
Source0:	http://people.debian.org/~kov/gksu/libgksuui1.0/%{name}1.0-%{version}.tar.gz
# Source0-md5:	c22648bbb17aa942a97cc325e3a85752
Patch0:		link.patch
Patch1:		gettext.patch
URL:		http://www.nongnu.org/gksu/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.10.1
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgksuui library.

%description -l pl.UTF-8
Biblioteka libgksuui.

%package devel
Summary:	Header files for libgksuui library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgksuui
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.10.1

%description devel
Header files for libgksuui library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgksuui.

%package static
Summary:	Static libgksuui library
Summary(pl.UTF-8):	Statyczna biblioteka libgksuui
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgksuui library.

%description static -l pl.UTF-8
Statyczna biblioteka libgksuui.

%package apidocs
Summary:	libgksuui API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libgksuui
Group:		Documentation

%description apidocs
API and internal documentation for libgksuui library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libgksuui.

%prep
%setup -q -n %{name}1.0-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}1.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}1.0.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/libgksuui1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgksuui1.0.so.1
%{_datadir}/libgksuui1.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgksuui1.0.so
%{_includedir}/libgksuui1.0
%{_pkgconfigdir}/libgksuui1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgksuui1.0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgksuui1.0
