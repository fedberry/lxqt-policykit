%if 0%{?rhel} == 6
%define cmake_pkg cmake28
%else
%define cmake_pkg cmake
%endif

Name:    lxqt-policykit
Summary: PolicyKit agent for LXQt desktop suite
Version: 0.8.0
Release: 4%{?dist}
License: LGPLv2+
URL:     http://lxqt.org/
Source0: http://lxqt.org/downloads/lxqt/0.8.0/%{name}-%{version}.tar.xz
# ( Upstream ? )
Patch0:  lxqt-policykit-0.8.0-cmake-libexec.patch
Requires: lxqt-common >= 0.8.0

BuildRequires: %{cmake_pkg} >= 2.8.9
BuildRequires: pkgconfig(polkit-qt5-1)
BuildRequires: pkgconfig(polkit-agent-1)
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: pkgconfig(Qt5Xdg) >= 1.0.0
BuildRequires: pkgconfig(lxqt-qt5)
BuildRequires: desktop-file-utils

%description
%{summary}.

%prep
%setup -q

%patch0 -p1

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{?cmake28}%{!?cmake28:%{?cmake}} -DUSE_QT5=TRUE ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

install -d %{buildroot}/%{_sysconfdir}/xdg/autostart

%files
%doc COPYING
%{_libexecdir}/lxqt-policykit-agent

%changelog
* Mon Dec 08 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-4
- Remove agent autostart already provided by lxqt-common.

* Mon Nov 10 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-3
- Update for review on https://bugzilla.redhat.com/show_bug.cgi?id=1159874

* Mon Nov 03 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-2
- Update to Fedora package review

* Mon Oct 27 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-1
- First release to LxQt new base
