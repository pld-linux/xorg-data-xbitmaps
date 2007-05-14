Summary:	Bitmaps that are shared between X applications
Summary(pl.UTF-8):	Bitmapy współdzielone między aplikacjami X
Name:		xorg-data-xbitmaps
Version:	1.0.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/data/xbitmaps-%{version}.tar.bz2
# Source0-md5:	b28a9840cde3c38d7c09716372fea257
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bitmaps that are shared between X applications.

%description -l pl.UTF-8
Bitmapy współdzielone między aplikacjami X.

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
%doc COPYING ChangeLog
# don't drag whole xorg-proto-xproto-devel just for this dir
%dir %{_includedir}/X11
%{_includedir}/X11/bitmaps
%{_pkgconfigdir}/xbitmaps.pc
