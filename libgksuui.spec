Summary:	libgksuui library
Summary(pl):	Biblioteka libgksuui
Name:		libgksuui
Version:	1.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://people.debian.org/~kov/gksu/libgksuui1.0/%{name}1.0-%{version}.tar.gz
# Source0-md5:	357f9dacab3760f3b579abe5ea6f00eb
URL:		http://www.nongnu.org/gksu/
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgksuui library.

%description -l pl
Biblioteka libgksuui.

%package devel
Summary:	Header files for libgksuui library
Summary(pl):	Pliki nag³ówkowe biblioteki libgksuui
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2.0.0

%description devel
Header files for libgksuui library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libgksuui.

%package static
Summary:	Static libgksuui library
Summary(pl):	Statyczna biblioteka libgksuui
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgksuui library.

%description static -l pl
Statyczna biblioteka libgksuui.

%prep
%setup -q -n %{name}1.0-%{version}

%build
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}1.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}1.0.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/%{name}*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}*
%{_pkgconfigdir}/*.pc
%{_gtkdocdir}/%{name}*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
