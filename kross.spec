%define major 5
%define libname %mklibname KF5KrossCore %{major}
%define devname %mklibname KF5KrossCore -d
%define ulibname %mklibname KF5KrossUi %{major}
%define udevname %mklibname KF5KrossUi -d
%define debug_package %{nil}

Name: kross
Version: 5.0.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/stable/frameworks/%{version}/portingAids/%{name}-%{version}.tar.xz
Source100: %{name}.rpmlintrc
Summary: Multi-language application scripting
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Parts)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: ninja
Requires: %{libname} = %{EVRD}

%description
Multi-language application scripting

%package -n %{libname}
Summary: Multi-language application scripting
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Multi-language application scripting

%package -n %{ulibname}
Summary: Multi-language application UI scripting
Group: System/Libraries
Requires: %{libname} = %{EVRD}

%description -n %{ulibname}
Multi-language application UI scripting

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 KrossCore library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 KrossCore library

%package -n %{udevname}
Summary: Development files for the KDE Frameworks 5 KrossUi library
Group: Development/KDE and Qt
Requires: %{ulibname} = %{EVRD}
Requires: %{devname} = %{EVRD}

%description -n %{udevname}
Development files for the KDE Frameworks 5 KrossUi library

%prep
%setup -q
%apply_patches
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}
%find_lang %{name}%{major}

%files -f %{name}%{major}.lang
%{_bindir}/kf5kross
%{_libdir}/plugins/*.so
%{_libdir}/plugins/script
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libKF5KrossCore.so.%{major}
%{_libdir}/libKF5KrossCore.so.%{version}

%files -n %{ulibname}
%{_libdir}/libKF5KrossUi.so.%{major}
%{_libdir}/libKF5KrossUi.so.%{version}

%files -n %{devname}
%{_includedir}/KF5/KrossCore
%{_includedir}/KF5/kross_version.h
%{_libdir}/libKF5KrossCore.so
%{_libdir}/cmake/KF5*
%{_prefix}/mkspecs/modules/qt_KrossCore.pri

%files -n %{udevname}
%{_includedir}/KF5/KrossUi
%{_libdir}/libKF5KrossUi.so
%{_prefix}/mkspecs/modules/qt_KrossUi.pri
