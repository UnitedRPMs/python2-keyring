Name:           python2-keyring
Version:        18.0.0
Release:        1%{?dist}
Summary:        Python 2 library to access the system keyring service
License:        MIT and Python
URL:            https://github.com/jaraco/keyring
Source0:        https://files.pythonhosted.org/packages/15/88/c6ce9509438bc02d54cf214923cfba814412f90c31c95028af852b19f9b2/keyring-%{version}.tar.gz
BuildArch:      noarch

%description
The Python keyring lib provides a easy way to access the system keyring
service from python. It can be used in any application that needs safe
password storage.

BuildRequires:  python2
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-setuptools_scm
BuildRequires:  python2-keyczar
BuildRequires:  python2-mock 
BuildRequires:	python2-six
BuildRequires:	python2-appdirs
BuildRequires:	python2-packaging
Requires:       python2-SecretStorage
Requires:       python2-entrypoints

%prep
%autosetup -n keyring-%{version} 
rm -frv keyring.egg-info
# Drop redundant shebangs.
#sed -i '1{\@^#!/usr/bin/env python@d}' keyring/cli.py
# Drop slags from upstream of using his own versioning system.
#sed -i -e "\@use_vcs_version@s/^.*$/\tversion = \"%{version}\",/g" \
#       -e {/\'hgtools\'/d} setup.py

%build
#py2_build
/usr/bin/python2 setup.py build


%install
#py2_install
/usr/bin/python2 setup.py install --root %{buildroot} --optimize=1
mv %{buildroot}%{_bindir}/keyring %{buildroot}%{_bindir}/keyring-python2

%files 
%doc CHANGES.rst README.rst
%{_bindir}/keyring-python2
%{python2_sitelib}/keyring-*.egg-info/
%{python2_sitelib}/keyring/


%changelog

* Tue Feb 19 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.0.0-1
- Upstream
- Updated to 18.0.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 11 2018 David King <amigadave@amigadave.com> - 15.2.0-1
- Update to 15.2.0

* Thu Oct 18 2018 Miro Hrončok <mhroncok@redhat.com> - 13.2.1-4
- Remove python2 subpackage from Fedora 30+

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 13.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Miro Hrončok <mhroncok@redhat.com> - 13.2.1-2
- Add missing dependency on entrypoints (#1598998)

* Fri Jul 06 2018 Christopher Tubbs <ctubbsii@fedoraproject.org> - 13.2.1-1
- Update to 13.2.1

* Thu Jul 05 2018 Christopher Tubbs <ctubbsii@fedoraproject.org> - 13.2.0-1
- Update to 13.2.0

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 11.0.0-4
- Rebuilt for Python 3.7

* Fri Mar 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 11.0.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Mar 08 2018 Christopher Tubbs <ctubbsii@fedoraproject.org> - 11.0.0-2
- Remove unused BR pycryptopp (rhbz#1552676)

* Mon Mar  5 2018 Haïkel Guémar <hguemar@fedoraproject.org> - 11.0.0-1
- Upstream 11.0.0 (RHBZ#1539962)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 12 2018 Christopher Tubbs <ctubbsii@fedoraproject.org> - 10.6.0-1
- Update to 10.6.0 (rhbz#1532092)

* Thu Dec 21 2017 Christopher Tubbs <ctubbsii@fedoraproject.org> - 10.5.1-1
- Update to 10.5.1; fix AttributeError with kwallet backend (bz#1526653)

* Thu Nov 16 2017 Christopher Tubbs <ctubbsii@fedoraproject.org> - 10.5.0-1
- Update to 10.5.0; bz#1512519

* Mon Aug 28 2017 Christopher Tubbs <ctubbsii@fedoraproject.org> - 10.4.0-2
- Use python2-* naming conventions for *Requires

* Mon Aug 28 2017 Christopher Tubbs <ctubbsii@fedoraproject.org> - 10.4.0-1
- Update to python-keyring 10.4.0 (bz#1464676)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 11 2017 Christopher Tubbs <ctubbsii@fedoraproject.org> - 10.3.2-2
- Fix dependency on setuptools_scm for f25

* Mon Apr 10 2017 Christopher Tubbs <ctubbsii@fedoraproject.org> - 10.3.2-1
- Update to python-keyring 10.3.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 9.0-6
- Rebuild for Python 3.6

* Wed Dec 21 2016 Christopher Tubbs <ctubbsii@fedoraproject.org> - 9.0-5
- Add dependency on python-SecretStorage (bz#1328218,bz#1398710)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 9.0-4
- Rebuild for Python 3.6

* Mon Nov 21 2016 Orion Poplawski <orion@cora.nwra.com> - 9.0-3
- Enable python 3 build for EPEL
- Ship python2-keyring
- Modernize spec

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon May 02 2016 Matthias Runge <mrunge@redhat.com> - 9.0-1
- update to 9.0, resolves rhbz#1271641, rhbz#1195985

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 13 2015 Robert Kuska <rkuska@redhat.com> - 5.0-3
- Rebuilt for Python3.5 rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 04 2015 Christopher Meng <rpm@cicku.me> - 5.0-1
- Update to 5.0
- Revise license tag to match upstream.

* Sat Aug 02 2014 Christopher Meng <rpm@cicku.me> - 4.0-1
- Update to 4.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue May 13 2014 Christopher Meng <rpm@cicku.me> - 3.8-1
- Update to 3.8

* Sat Mar 08 2014 Christopher Meng <rpm@cicku.me> - 3.6-1
- Update to 3.6

* Thu Feb 13 2014 Christopher Meng <rpm@cicku.me> - 3.4-1
- Update to 3.4(BZ#1064256)
- Ensure the obsolete line works for the old packages really.

* Mon Dec 02 2013 Christopher Meng <rpm@cicku.me> - 3.3-1
- Update to 3.3(BZ#1007354,BZ#872262)
- Cleanup dependencies mess(BZ#1030944).
- Optimize the %%changelog section of the spec.

* Tue Oct 22 2013 Ratnadeep Debnath <rtnpro@gmail.com> - 3.1-1
- Bump to version 3.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Ratnadeep Debnath <rtnpro@gmail.com> 0.7-1
- Python 3 is now supported. All tests now pass under Python 3.2 on Windows and
Linux (although Linux backend support is limited). Fixes #28.
- Extension modules on Mac and Windows replaced by pure-Python ctypes
implementations. Thanks to Jérôme Laheurte.
- WinVaultKeyring now supports multiple passwords for the same service.
Fixes #47.
- Most of the tests don't require user interaction anymore.
- Entries stored in Gnome Keyring appears now with a meaningful name if you try
to browser your keyring (for ex. with Seahorse)
- Tests from Gnome Keyring no longer pollute the user own keyring.
- keyring.util.escape now accepts only unicode strings. Don't try to encode
strings passed to it.

* Tue Nov 08 2011 Ratnadeep Debnath <rtnpro@gmail.com> 0.6.2-1
- fix compiling on OSX with XCode 4.0
- Gnome keyring should not be used if there is no DISPLAY or if the dbus is not around
    (https://bugs.launchpad.net/launchpadlib/+bug/752282).
- Added keyring.http for facilitating HTTP Auth using keyring.
- Add a utility to access the keyring from the command line.

* Mon Jan 10 2011 Ratnadeep Debnath <rtnpro@gmail.com> 0.5.1-1
- Remove a spurious KDE debug message when using KWallet
- Fix a bug that caused an exception if the user canceled the KWallet dialog

* Sun Nov 28 2010 Ratnadeep Debnath <rtnpro@gmail.com> 0.5-2
- Removed sub-packages: gnome and kwallet; removed "Requires: PyKDE4 PyQt4"

* Mon Nov 22 2010 Ratnadeep Debnath <rtnpro@gmail.com> 0.5-1
- RPM for keyring-0.5

* Mon Nov 01 2010 Ratnadeep Debnath <rtnpro@gmail.com> 0.4-1
- Updated rpm to python-keyring version 0.4

* Sat Oct 30 2010 Ratnadeep Debnath <rtnpro@gmail.com> 0.2-4
- Filtered gnome_keyring.so from the provides list, removed kdelibs-devel

* Sat Oct 02 2010 Ratnadeep Debnath <rtnpro@gmail.com> 0.2-3
- Updated dependencies to kdelibs4-devel, some cleanup

* Tue Aug 24 2010 Ratnadeep Debnath <rtnpro@gmail.com> 0.2-2
- Some updates according to bugzilla reviews

* Sat Jun 26 2010 Ratnadeep Debnath <rtnpro@gmail.com> 0.2-1.3
- Some cleanup

* Sat Jun 26 2010 Felix Schwarz <felix.schwarz@oss.schwarz.eu> 0.2-1.2
- add KWallet subpackage

* Mon Jun 21 2010 Felix Schwarz <felix.schwarz@oss.schwarz.eu> 0.2-1.1
- add build dependencies
- create subpackage for gnome, disable KWallet for now
- look for files in arch-dependend site-packages

* Tue May 25 2010 Ratnadeep Debnath <rtnpro@gmail.com> 0.2-1
- Incorporated some changes with reference to http://vcrhonek.fedorapeople.org/python-keyring/python-keyring.spec
- Fixed some rpmlint errors

* Wed May 19 2010 Ratnadeep Debnath <rtnpro@gmail.com> 0.2
- Initial RPM package
