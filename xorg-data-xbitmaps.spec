Summary:	Bitmaps that are shared between X applications
Summary(pl.UTF-8):	Bitmapy współdzielone między aplikacjami X
Name:		xorg-data-xbitmaps
Version:	1.1.3
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/data/xbitmaps-%{version}.tar.xz
# Source0-md5:	2b03f89d78fb91671370e77d7ad46907
Patch0:		noarch.patch
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	rpmbuild(macros) >= 1.446
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-util-util-macros >= 1.20
BuildRequires:	xz
Requires:	filesystem >= 3.0-32
BuildArch:	noarch
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
%configure \
%ifnarch x32
	--host=%{_host} \
	--build=%{_host} \
%endif
	%{nil}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_includedir}/X11/bitmaps
%{_npkgconfigdir}/xbitmaps.pc
