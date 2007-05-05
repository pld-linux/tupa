
%define _rc     rc1

Summary:	TUPA - The Ultimate PowerDNS Admin
Summary(pl.UTF-8):	TUPA - The Ultimate PowerDNS Admin
Name:		tupa
Version:	0.1
Release:	0.%{_rc}.1
License:	GPL
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/tupa/%{name}-v%{version}%{_rc}.tgz
# Source-md5:	cf0d38f296dd5fa65c9087dd08342a22
Source1:	%{name}.conf
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	pdns
Requires:	php(mysql)
Requires:	rrdtool
Requires:	webapps
Requires:	webserver(access)
Requires:	webserver(php)
Conflicts:	apache < 2.0.55-2.2
Conflicts:	apache1 < 1.3.34-3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _webapps        /etc/webapps
%define         _webapp         %{name}
%define         _sysconfdir     %{_webapps}/%{_webapp}
%define         _appdir         %{_datadir}/%{_webapp}

%description
TUPA is a webbased PowerDNS administration frontend programed in PHP /
Javascript(AJAX) and MySQL. Supports creating of groups, users,
templates and a lot more.

%prep
%setup -q -n %{name}-v%{version}%{_rc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_sbindir},%{_appdir}}
install -d $RPM_BUILD_ROOT%{_appdir}/config
cp -a backup images lib skins stats installer lang $RPM_BUILD_ROOT%{_appdir}
install *.php $RPM_BUILD_ROOT%{_appdir}
install *.html $RPM_BUILD_ROOT%{_appdir}
install config/config_site-dist.inc.php $RPM_BUILD_ROOT%{_sysconfdir}/config_site.inc.php
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf
ln -s %{_sysconfdir}/config_site.inc.php $RPM_BUILD_ROOT%{_appdir}/config/config_site.inc.php

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{_webapp}

%triggerun -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{_webapp}

%triggerin -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

%files
%defattr(644,root,root,755)
%doc Changelog.txt
%dir %attr(751,root,http) %{_sysconfdir}
%attr(664,root,http) %{_sysconfdir}/config_site.inc.php
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf

%dir %{_appdir}
%{_appdir}/*.php
%{_appdir}/*.html
%{_appdir}/backup
%{_appdir}/config
%{_appdir}/images
%{_appdir}/installer
%{_appdir}/lang
%{_appdir}/lib
%{_appdir}/skins

%dir %attr(771,root,http) %{_appdir}/stats
%{_appdir}/stats/*.html
%{_appdir}/stats/db
