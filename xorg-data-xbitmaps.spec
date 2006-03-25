Summary:	X bitmaps data
Summary(pl):	Bitmapy dla X
Name:		xorg-data-xbitmaps
Version:	1.0.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/data/xbitmaps-X11R7.0-%{version}.tar.bz2
# Source0-md5:	22c6f4a17220cd6b41d9799905f8e357
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X bitmaps data.

%description -l pl
Bitmapy dla X.

%prep
%setup -q -n xbitmaps-X11R7.0-%{version}

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
%doc COPYING ChangeLog
# don't drag whole xorg-proto-xproto-devel just for this dir
%dir %{_includedir}/X11
%{_includedir}/X11/bitmaps
%{_pkgconfigdir}/xbitmaps.pc
