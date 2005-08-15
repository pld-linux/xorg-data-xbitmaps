# $Rev: 3338 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	X bitmaps data
Summary(pl):	Bitmapy dla X
Name:		xorg-data-xbitmaps
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/data/xbitmaps-%{version}.tar.bz2
# Source0-md5:	a910bcd038f2c557e062cf66a3b67acf
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/xbitmaps-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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
%{_includedir}/X11/bitmaps
%{_pkgconfigdir}/xbitmaps.pc
