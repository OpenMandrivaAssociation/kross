%define major 5
%define libname %mklibname KF5KrossCore %{major}
%define devname %mklibname KF5KrossCore -d
%define ulibname %mklibname KF5KrossUi %{major}
%define udevname %mklibname KF5KrossUi -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kross
Version: 5.34.0
Release: 1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/portingAids/%{name}-%{version}.tar.xz
Source100: %{name}.rpmlintrc
Summary: Multi-language application scripting
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: pkgconfig(Qt5UiTools)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
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
Requires: %{libname} = %{EVRD}

%description
Multi-language application scripting.

%package -n %{libname}
Summary: Multi-language application scripting
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Multi-language application scripting.

%package -n %{ulibname}
Summary: Multi-language application UI scripting
Group: System/Libraries
Requires: %{libname} = %{EVRD}

%description -n %{ulibname}
Multi-language application UI scripting.

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 KrossCore library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 KrossCore library.

%package -n %{udevname}
Summary: Development files for the KDE Frameworks 5 KrossUi library
Group: Development/KDE and Qt
Requires: %{ulibname} = %{EVRD}
Requires: %{devname} = %{EVRD}
Provides: cmake(KF5KrossUi)

%description -n %{udevname}
Development files for the KDE Frameworks 5 KrossUi library.

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name}%{major}

%files -f %{name}%{major}.lang
%{_bindir}/kf5kross
%{_libdir}/qt5/plugins/*.so
%{_libdir}/qt5/plugins/script
%{_mandir}/man1/kf5kross.1.*
%lang(ca) %{_mandir}/ca/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(nl) %{_mandir}/nl/man1/*
%lang(pt) %{_mandir}/pt/man1/*
%lang(pt_BR) %{_mandir}/pt_BR/man1/*
%lang(sv) %{_mandir}/sv/man1/*
%lang(uk) %{_mandir}/uk/man1/*

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
%{_libdir}/qt5/mkspecs/modules/qt_KrossCore.pri

%files -n %{udevname}
%{_includedir}/KF5/KrossUi
%{_libdir}/libKF5KrossUi.so
%{_libdir}/qt5/mkspecs/modules/qt_KrossUi.pri
