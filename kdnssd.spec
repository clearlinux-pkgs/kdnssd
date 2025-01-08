#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 5424026
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : kdnssd
Version  : 6.9.0
Release  : 97
URL      : https://download.kde.org/stable/frameworks/6.9/kdnssd-6.9.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.9/kdnssd-6.9.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.9/kdnssd-6.9.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.0
Requires: kdnssd-data = %{version}-%{release}
Requires: kdnssd-lib = %{version}-%{release}
Requires: kdnssd-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : doxygen
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n kdnssd-6.9.0
cd %{_builddir}/kdnssd-6.9.0
pushd ..
cp -a kdnssd-6.9.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1735246451
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DBUILD_QCH=ON  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DBUILD_QCH=ON  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1735246451
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdnssd
cp %{_builddir}/kdnssd-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kdnssd/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kdnssd-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kdnssd/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kdnssd-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdnssd/20079e8f79713dce80ab09774505773c926afa2a || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/locale/af/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/ar/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/as/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/ast/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/az/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/be/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/be@latin/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/bg/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/bn/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/bn_IN/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/br/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/bs/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/ca/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/crh/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/cs/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/csb/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/cy/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/da/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/de/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/el/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/eo/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/es/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/et/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/eu/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/fa/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/fi/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/fr/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/fy/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/ga/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/gd/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/gl/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/gu/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/ha/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/he/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/hi/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/hne/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/hr/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/hsb/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/hu/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/hy/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/ia/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/id/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/is/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/it/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/ja/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/ka/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/kk/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/km/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/kn/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/ko/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/ku/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/lb/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/lt/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/lv/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/mai/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/mk/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/ml/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/mr/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/ms/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/nb/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/nds/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/ne/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/nl/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/nn/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/oc/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/or/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/pa/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/pl/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/ps/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/pt/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/ro/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/ru/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/sa/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/se/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/si/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/sk/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/sl/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/sq/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/sr/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/sv/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/ta/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/te/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/tg/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/th/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/tr/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/tt/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/ug/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/uk/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/uz/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/uz@cyrillic/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/vi/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/wa/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/xh/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/zh_HK/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/kdnssd6_qt.qm
/usr/share/qt6/doc/KF6DNSSD.qch
/usr/share/qt6/doc/KF6DNSSD.tags

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KDNSSD/KDNSSD/DomainBrowser
/usr/include/KF6/KDNSSD/KDNSSD/DomainModel
/usr/include/KF6/KDNSSD/KDNSSD/PublicService
/usr/include/KF6/KDNSSD/KDNSSD/RemoteService
/usr/include/KF6/KDNSSD/KDNSSD/ServiceBase
/usr/include/KF6/KDNSSD/KDNSSD/ServiceBrowser
/usr/include/KF6/KDNSSD/KDNSSD/ServiceModel
/usr/include/KF6/KDNSSD/KDNSSD/ServiceTypeBrowser
/usr/include/KF6/KDNSSD/kdnssd/domainbrowser.h
/usr/include/KF6/KDNSSD/kdnssd/domainmodel.h
/usr/include/KF6/KDNSSD/kdnssd/kdnssd_export.h
/usr/include/KF6/KDNSSD/kdnssd/publicservice.h
/usr/include/KF6/KDNSSD/kdnssd/remoteservice.h
/usr/include/KF6/KDNSSD/kdnssd/servicebase.h
/usr/include/KF6/KDNSSD/kdnssd/servicebrowser.h
/usr/include/KF6/KDNSSD/kdnssd/servicemodel.h
/usr/include/KF6/KDNSSD/kdnssd/servicetypebrowser.h
/usr/include/KF6/KDNSSD/kdnssd_version.h
/usr/lib64/cmake/KF6DNSSD/KF6DNSSDConfig.cmake
/usr/lib64/cmake/KF6DNSSD/KF6DNSSDConfigVersion.cmake
/usr/lib64/cmake/KF6DNSSD/KF6DNSSDQchTargets.cmake
/usr/lib64/cmake/KF6DNSSD/KF6DNSSDTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6DNSSD/KF6DNSSDTargets.cmake
/usr/lib64/libKF6DNSSD.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6DNSSD.so.6.9.0
/usr/lib64/libKF6DNSSD.so.6
/usr/lib64/libKF6DNSSD.so.6.9.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdnssd/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kdnssd/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kdnssd/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
