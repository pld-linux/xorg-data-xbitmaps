Summary:	Bitmaps that are shared between X applications
Summary(pl.UTF-8):	Bitmapy współdzielone między aplikacjami X
Name:		xorg-data-xbitmaps
Version:	1.1.1
Release:	3
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/data/xbitmaps-%{version}.tar.bz2
# Source0-md5:	7444bbbd999b53bec6a60608a5301f4c
Patch0:		noarch.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	rpmbuild(macros) >= 1.446
BuildRequires:	xorg-util-util-macros >= 1.3
Requires:	filesystem >= 3.0-32
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if %{_host_cpu} == "x32"
%define	build_arch %{_target_platform}
%else
%define	build_arch %{_host}
%endif

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
	--host=%{build_arch} \
	--build=%{build_arch} \
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
