Summary:	X bitmaps data
Summary(pl):	Bitmapy dla X
Name:		xorg-data-xbitmaps
Version:	1.0.0
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC4/data/xbitmaps-%{version}.tar.bz2
# Source0-md5:	fbe1dfefb35b3976bd9821ae7b8bfd10
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
# just for dir
Requires:	xorg-proto-xproto-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X bitmaps data.

%description -l pl
Bitmapy dla X.

%prep
%setup -q -n xbitmaps-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%{_includedir}/X11/bitmaps
%{_pkgconfigdir}/xbitmaps.pc
