#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : insync
Version  : 3.7.6.50356
Release  : 76
URL      : file:///aot/build/clearlinux/packages/insync/insync-v3.7.6.50356.tar.gz
Source0  : file:///aot/build/clearlinux/packages/insync/insync-v3.7.6.50356.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : bash
BuildRequires : buildreq-cmake
BuildRequires : ca-certs
BuildRequires : cpio-bin
BuildRequires : curl
BuildRequires : curl-bin
BuildRequires : curl-dev
BuildRequires : curl-lib
BuildRequires : findutils
BuildRequires : mlocate
BuildRequires : openssl-dev
BuildRequires : openssl-lib
BuildRequires : p11-kit
BuildRequires : pcre-dev
BuildRequires : pcre-extras
BuildRequires : pypi-requests
BuildRequires : sd
BuildRequires : xmlstarlet
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
# Ignore missing build ids
%undefine _missing_build_ids_terminate_build
# Disable automatic requeriments processing
AutoReq: no

%description
No detailed description available

%prep
%setup -q -c -n insync-v3.7.6.50356.tar
cd %{_builddir}/insync-v3.7.6.50356.tar

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1651555775
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=16 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=16 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=16 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=16 "
%cmake ..
make  %{?_smp_mflags}    V=1 VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1651555775
rm -rf %{buildroot}
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=16 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=16 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=16 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=16 "
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}*/usr/lib64/insync/lib/python3.7/config-3.7m-x86_64-linux-gnu/Makefile

%files
%defattr(-,root,root,-)
