%define prj Group

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-group
Version:       0.1.0
Release:       %mkrel 4
Summary:       Horde User Groups System
License:       LGPL
Group:         Networking/Mail
Url:           http://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre): php-pear
Requires:      php-pear
Requires:      horde-framework
Requires:      horde-datatree
Requires:      horde-auth
Requires:      php-gettext
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde


%description
Package for managing and accessing the Horde groups system.


%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde/Group
%{peardir}/Horde/Group.php
%{peardir}/Horde/Group/hooks.php
%{peardir}/Horde/Group/kolab.php
%{peardir}/Horde/Group/ldap.php
%{peardir}/Horde/Group/mock.php
%{peardir}/Horde/Group/sql.php



%changelog
* Mon Jul 26 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.1.0-4mdv2011.0
+ Revision: 560545
- Increased release for rebuild

* Sat Mar 20 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.1.0-3mdv2010.1
+ Revision: 525371
- replaced Requires(pre): %%{_bindir}/pear with Requires(pre): php-pear
  increased rel ver to 3

* Thu Mar 18 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.1.0-2mdv2010.1
+ Revision: 524839
- increased rel version to 2

* Sat Feb 27 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.1.0-1mdv2010.1
+ Revision: 512337
- removed BuildRequires: horde-group
- removed BuildRequires: horde-framework
- Initial import


