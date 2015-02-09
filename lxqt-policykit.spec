Name:    lxqt-policykit
Summary: PolicyKit agent for LXQt desktop suite
Version: 0.9.0
Release: 2%{?dist}
License: LGPLv2+
URL:     http://lxqt.org/
Source0: http://downloads.lxqt.org/lxqt/0.9.0/lxqt-policykit-0.9.0.tar.xz
# ( Upstream ? )
Patch0:  lxqt-policykit-0.9.0-cmake-libexec.patch

BuildRequires: cmake >= 2.8.9
BuildRequires: pkgconfig(polkit-qt5-1)
BuildRequires: pkgconfig(polkit-agent-1)
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: pkgconfig(Qt5Xdg) >= 1.0.0
BuildRequires: pkgconfig(lxqt)
BuildRequires: kf5-kwindowsystem-devel >= 5.5
BuildRequires: desktop-file-utils

Provides: PolicyKit-authentication-agent

Requires: lxqt-common >= 0.9.0

%description
%{summary}.

%prep
%setup -q

%patch0 -p1 -b .libexec

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
	%{cmake} -DPOLKIT_AGENT_BINARY_DIR=%{_libexecdir} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

install -d %{buildroot}/%{_sysconfdir}/xdg/autostart

%find_lang %{name}-agent --with-qt

%files -f %{name}-agent.lang
%doc COPYING
%{_libexecdir}/lxqt-policykit-agent

%changelog
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
