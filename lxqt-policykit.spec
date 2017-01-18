Name:    lxqt-policykit
Summary: PolicyKit agent for LXQt desktop suite
Version: 0.11.1
Release: 2%{?dist}
License: LGPLv2+
URL:     http://lxqt.org/
Source0: http://downloads.lxqt.org/lxqt/%{version}/%{name}-%{version}.tar.xz
Patch0: lxqt-policykit-0.11.0-authdialog.patch
BuildRequires: pkgconfig(polkit-qt5-1)
BuildRequires: pkgconfig(polkit-agent-1)
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: pkgconfig(Qt5Xdg) >= 1.0.0
BuildRequires: pkgconfig(lxqt) >= 0.11.0
BuildRequires: kf5-kwindowsystem-devel >= 5.5
BuildRequires: desktop-file-utils
Provides: PolicyKit-authentication-agent = %{version}
Requires: lxqt-common >= 0.11.0

%description
%{summary}.

%prep
%setup -q
%patch0 -p1 -b .hide

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
    %{cmake_lxqt} \
        -DPOLKIT_AGENT_BINARY_DIR=%{_libexecdir} \
        -DPULL_TRANSLATIONS=NO ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

install -d %{buildroot}/%{_sysconfdir}/xdg/autostart


%files
%{_libexecdir}/lxqt-policykit-agent

%changelog
* Wed Jan 18 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-2
- moved translations to lxqt-l10n

* Sat Jan 07 2017 Christian Dersch <lupinix@mailbox.org> - 0.11.1-1
- new version

* Thu Sep 29 2016 Helio Chissini de Castro <helio@kde.org> - 0.11.0-2
- Fix rpmlint issues
- Build for epel
- Bring translations back

* Mon Sep 26 2016 Helio Chissini de Castro <helio@kde.org> - 0.11.0-1
- New upstream release 0.11.0

* Tue Jun 07 2016 Than Ngo <than@redhat.com> - 0.10.0-5
- hide the identity because it's alway root

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Helio Chissini de Castro <helio@kde.org> - 0.10.0-3
- Another razorqt obsoletes

* Thu Dec 10 2015 Helio Chissini de Castro <helio@kde.org> - 0.10.0-2
- Use new cmake_lxqt infra

* Mon Nov 02 2015 Helio Chissini de Castro <helio@kde.org> - 0.10.0-1
- New upstream version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 18 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-4
- Rebuild (gcc5)

* Tue Feb 10 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-3
- Obsoletes razorqt-policykit-agent

* Mon Feb 09 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-2
- Proper add locale for Qt tm files

* Sun Feb 08 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-1
- New upstream release 0.9.0

* Tue Feb 03 2015 Helio Chissini de Castro <hcastro@redhat.com> - 0.9.0-0.1
- Preparing 0.9.0 release

* Mon Dec 29 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-7
- Rebuild against new Qt 5.4.0

* Sat Dec 20 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-6
- Unify naming as discussed on Fedora IRC

* Fri Dec 19 2014 Rex Dieter <rdieter@fedoraproject.org> 0.8.0-5
- Provides: PolicyKit-authentication-agent

* Mon Dec 08 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-4
- Remove agent autostart already provided by lxqt-common.

* Mon Nov 10 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-3
- Update for review on https://bugzilla.redhat.com/show_bug.cgi?id=1159874

* Mon Nov 03 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-2
- Update to Fedora package review

* Mon Oct 27 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-1
- First release to LxQt new base
