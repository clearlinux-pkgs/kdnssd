#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kdnssd
Version  : 5.81.0
Release  : 43
URL      : https://download.kde.org/stable/frameworks/5.81/kdnssd-5.81.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.81/kdnssd-5.81.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.81/kdnssd-5.81.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.0
Requires: kdnssd-data = %{version}-%{release}
Requires: kdnssd-lib = %{version}-%{release}
Requires: kdnssd-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : qtbase-dev mesa-dev

%description
# KDE DNS-SD
Network service discovery using Zeroconf
## Introduction
KDNSSD is a library for handling the DNS-based Service Discovery Protocol
(DNS-SD), the layer of [Zeroconf](http://www.zeroconf.org) that allows network
services, such as printers, to be discovered without any user intervention or
centralized infrastructure.

%package data
Summary: data components for the kdnssd package.
Group: Data

%description data
data components for the kdnssd package.


%package dev
Summary: dev components for the kdnssd package.
Group: Development
Requires: kdnssd-lib = %{version}-%{release}
Requires: kdnssd-data = %{version}-%{release}
Provides: kdnssd-devel = %{version}-%{release}
Requires: kdnssd = %{version}-%{release}

%description dev
dev components for the kdnssd package.


%package lib
Summary: lib components for the kdnssd package.
Group: Libraries
Requires: kdnssd-data = %{version}-%{release}
Requires: kdnssd-license = %{version}-%{release}

%description lib
lib components for the kdnssd package.


%package license
Summary: license components for the kdnssd package.
Group: Default

%description license
license components for the kdnssd package.


%prep
%setup -q -n kdnssd-5.81.0
cd %{_builddir}/kdnssd-5.81.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1618648809
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1618648809
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdnssd
cp %{_builddir}/kdnssd-5.81.0/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kdnssd/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/kdnssd-5.81.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdnssd/20079e8f79713dce80ab09774505773c926afa2a
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/locale/af/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/ar/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/as/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/ast/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/az/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/be/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/be@latin/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/bg/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/bn/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/bn_IN/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/br/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/bs/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/ca/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/crh/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/cs/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/csb/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/cy/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/da/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/de/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/el/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/eo/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/es/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/et/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/eu/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/fa/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/fi/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/fr/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/fy/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/ga/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/gd/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/gl/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/gu/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/ha/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/he/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/hi/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/hne/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/hr/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/hsb/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/hu/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/hy/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/ia/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/id/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/is/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/it/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/ja/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/ka/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/kk/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/km/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/kn/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/ko/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/ku/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/lb/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/lt/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/lv/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/mai/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/mk/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/ml/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/mr/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/ms/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/nb/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/nds/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/ne/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/nl/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/nn/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/oc/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/or/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/pa/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/pl/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/ps/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/pt/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/ro/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/ru/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/se/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/si/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/sk/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/sl/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/sq/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/sr/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/sv/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/ta/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/te/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/tg/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/th/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/tr/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/tt/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/ug/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/uk/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/uz/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/uz@cyrillic/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/vi/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/wa/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/xh/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/zh_HK/LC_MESSAGES/kdnssd5_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/kdnssd5_qt.qm

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KDNSSD/DNSSD/DomainBrowser
/usr/include/KF5/KDNSSD/DNSSD/DomainModel
/usr/include/KF5/KDNSSD/DNSSD/PublicService
/usr/include/KF5/KDNSSD/DNSSD/RemoteService
/usr/include/KF5/KDNSSD/DNSSD/ServiceBase
/usr/include/KF5/KDNSSD/DNSSD/ServiceBrowser
/usr/include/KF5/KDNSSD/DNSSD/ServiceModel
/usr/include/KF5/KDNSSD/DNSSD/ServiceTypeBrowser
/usr/include/KF5/KDNSSD/dnssd/domainbrowser.h
/usr/include/KF5/KDNSSD/dnssd/domainmodel.h
/usr/include/KF5/KDNSSD/dnssd/kdnssd_export.h
/usr/include/KF5/KDNSSD/dnssd/publicservice.h
/usr/include/KF5/KDNSSD/dnssd/remoteservice.h
/usr/include/KF5/KDNSSD/dnssd/servicebase.h
/usr/include/KF5/KDNSSD/dnssd/servicebrowser.h
/usr/include/KF5/KDNSSD/dnssd/servicemodel.h
/usr/include/KF5/KDNSSD/dnssd/servicetypebrowser.h
/usr/include/KF5/kdnssd_version.h
/usr/lib64/cmake/KF5DNSSD/KF5DNSSDConfig.cmake
/usr/lib64/cmake/KF5DNSSD/KF5DNSSDConfigVersion.cmake
/usr/lib64/cmake/KF5DNSSD/KF5DNSSDTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5DNSSD/KF5DNSSDTargets.cmake
/usr/lib64/libKF5DNSSD.so
/usr/lib64/qt5/mkspecs/modules/qt_KDNSSD.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5DNSSD.so.5
/usr/lib64/libKF5DNSSD.so.5.81.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdnssd/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kdnssd/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
