
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
Source2:	webapp-bash_completion.sh
Requires:	coreutils
Requires:	webserver
Conflicts:	apache < 2.0.55-2.2
Conflicts:	apache1 < 1.3.34-3.2
Conflicts:	lighttpd < 1.4.7-2.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _appdir       	/usr/share/%{name}
%define		_sysconfdir	/etc/webapps/%{name}
%define		_bashcompletiondir	/etc/bash_completion.d

%description
TUPA is a webbased PowerDNS administration frontend programed in PHP / Javascript(AJAX) and MySQL. Supports creating of groups, users, templates and a 
lot more.

%package -n bash-completion-tupa
Summary:	bash completion for tupa
Summary(pl.UTF-8):	Dopełnienia basha dlatupa
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion

%description -n bash-completion-tupa
Bash completion for TUPA.

%prep
%setup -q -n %{name}-v%{version}%{_rc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_sbindir},%{_appdir},%{_bashcompletiondir}}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/config
ln -s %{_sysconfdir} $RPM_BUILD_ROOT%{_appdir}/config
cp -a backup images lib skins stats installer lang $RPM_BUILD_ROOT%{_appdir}
install *.php $RPM_BUILD_ROOT%{_appdir}
install *.html $RPM_BUILD_ROOT%{_appdir}
install config/config_site-dist.inc.php $RPM_BUILD_ROOT%{_sysconfdir}/config/config_site.php
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf
install %{SOURCE2} $RPM_BUILD_ROOT%{_bashcompletiondir}/tupa

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog.txt
%dir %attr(751,root,http) %{_sysconfdir}
%attr(640,root,http) %{_sysconfdir}/config/config_site.php
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
%{_appdir}/stats


%files -n bash-completion-tupa
%defattr(644,root,root,755)
%{_bashcompletiondir}/tupa
