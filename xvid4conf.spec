Summary:	XviD configuration files wizard for transcode
Name:		xvid4conf
Version:	1.12
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://zebra.fh-weingarten.de/~transcode/xvid4conf/%{name}-%{version}.tar.gz
# Source0-md5:	5f1335e8a19aac58f6534f468c10a77a
BuildRequires:	gtk+2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This tool creates XviD configuration files. The generated configuration
file is meant to be read by transcodes xvid4 export module. This module
(and so the configuration file) is intended to be used with XviD 1.0
(dev-api-4).

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
