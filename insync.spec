#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : insync
Version  : 3.6.1.50206
Release  : 63
URL      : file:///aot/build/clearlinux/packages/insync/insync-v3.6.1.50206.tar.gz
Source0  : file:///aot/build/clearlinux/packages/insync/insync-v3.6.1.50206.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: insync-bin = %{version}-%{release}
Requires: insync-data = %{version}-%{release}
Requires: insync-libexec = %{version}-%{release}
Requires: insync-man = %{version}-%{release}
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
BuildRequires : requests
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

%package bin
Summary: bin components for the insync package.
Group: Binaries
Requires: insync-data = %{version}-%{release}
Requires: insync-libexec = %{version}-%{release}
# Disable automatic requeriments processing
AutoReq: no

%description bin
bin components for the insync package.


%package data
Summary: data components for the insync package.
Group: Data
# Disable automatic requeriments processing
AutoReq: no

%description data
data components for the insync package.


%package dev
Summary: dev components for the insync package.
Group: Development
Requires: insync-bin = %{version}-%{release}
Requires: insync-data = %{version}-%{release}
Provides: insync-devel = %{version}-%{release}
Requires: insync = %{version}-%{release}
# Disable automatic requeriments processing
AutoReq: no

%description dev
dev components for the insync package.


%package libexec
Summary: libexec components for the insync package.
Group: Default
# Disable automatic requeriments processing
AutoReq: no

%description libexec
libexec components for the insync package.


%package man
Summary: man components for the insync package.
Group: Default
# Disable automatic requeriments processing
AutoReq: no

%description man
man components for the insync package.


%prep
%setup -q -c -n insync-v3.6.1.50206.tar
cd %{_builddir}/insync-v3.6.1.50206.tar

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639093963
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
export SOURCE_DATE_EPOCH=1639093963
rm -rf %{buildroot}
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}*/usr/lib64/insync/lib/python3.7/config-3.7m-x86_64-linux-gnu/Makefile

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/insync

%files data
%defattr(-,root,root,-)
/usr/share/applications/insync-helper.desktop
/usr/share/applications/insync.desktop
/usr/share/icons/hicolor/1024x1024/mimetypes/application-vnd.insync.link.drive.doc.png
/usr/share/icons/hicolor/1024x1024/mimetypes/application-vnd.insync.link.drive.draw.png
/usr/share/icons/hicolor/1024x1024/mimetypes/application-vnd.insync.link.drive.form.png
/usr/share/icons/hicolor/1024x1024/mimetypes/application-vnd.insync.link.drive.link.png
/usr/share/icons/hicolor/1024x1024/mimetypes/application-vnd.insync.link.drive.note.png
/usr/share/icons/hicolor/1024x1024/mimetypes/application-vnd.insync.link.drive.script.png
/usr/share/icons/hicolor/1024x1024/mimetypes/application-vnd.insync.link.drive.sheet.png
/usr/share/icons/hicolor/1024x1024/mimetypes/application-vnd.insync.link.drive.slides.png
/usr/share/icons/hicolor/1024x1024/mimetypes/application-vnd.insync.link.drive.table.png
/usr/share/icons/hicolor/1024x1024/mimetypes/application-vnd.insync.link.dropbox.gdoc.png
/usr/share/icons/hicolor/1024x1024/mimetypes/application-vnd.insync.link.dropbox.gsheet.png
/usr/share/icons/hicolor/1024x1024/mimetypes/application-vnd.insync.link.dropbox.gslides.png
/usr/share/icons/hicolor/1024x1024/mimetypes/application-vnd.insync.link.dropbox.paper.png
/usr/share/icons/hicolor/1024x1024/mimetypes/application-vnd.insync.link.dropbox.papert.png
/usr/share/icons/hicolor/1024x1024/mimetypes/application-vnd.insync.link.dropbox.web.png
/usr/share/icons/hicolor/1024x1024/mimetypes/dxpaper.png
/usr/share/icons/hicolor/1024x1024/mimetypes/dxpapert.png
/usr/share/icons/hicolor/1024x1024/mimetypes/dxweb.png
/usr/share/icons/hicolor/1024x1024/mimetypes/gddoc.png
/usr/share/icons/hicolor/1024x1024/mimetypes/gddraw.png
/usr/share/icons/hicolor/1024x1024/mimetypes/gdform.png
/usr/share/icons/hicolor/1024x1024/mimetypes/gdlink.png
/usr/share/icons/hicolor/1024x1024/mimetypes/gdnote.png
/usr/share/icons/hicolor/1024x1024/mimetypes/gdscript.png
/usr/share/icons/hicolor/1024x1024/mimetypes/gdsheet.png
/usr/share/icons/hicolor/1024x1024/mimetypes/gdslides.png
/usr/share/icons/hicolor/1024x1024/mimetypes/gdtable.png
/usr/share/icons/hicolor/128x128/places/insync-folder.png
/usr/share/icons/hicolor/16x16/mimetypes/application-vnd.insync.link.drive.doc.png
/usr/share/icons/hicolor/16x16/mimetypes/application-vnd.insync.link.drive.draw.png
/usr/share/icons/hicolor/16x16/mimetypes/application-vnd.insync.link.drive.form.png
/usr/share/icons/hicolor/16x16/mimetypes/application-vnd.insync.link.drive.link.png
/usr/share/icons/hicolor/16x16/mimetypes/application-vnd.insync.link.drive.note.png
/usr/share/icons/hicolor/16x16/mimetypes/application-vnd.insync.link.drive.script.png
/usr/share/icons/hicolor/16x16/mimetypes/application-vnd.insync.link.drive.sheet.png
/usr/share/icons/hicolor/16x16/mimetypes/application-vnd.insync.link.drive.slides.png
/usr/share/icons/hicolor/16x16/mimetypes/application-vnd.insync.link.drive.table.png
/usr/share/icons/hicolor/16x16/mimetypes/application-vnd.insync.link.dropbox.gdoc.png
/usr/share/icons/hicolor/16x16/mimetypes/application-vnd.insync.link.dropbox.gsheet.png
/usr/share/icons/hicolor/16x16/mimetypes/application-vnd.insync.link.dropbox.gslides.png
/usr/share/icons/hicolor/16x16/mimetypes/application-vnd.insync.link.dropbox.paper.png
/usr/share/icons/hicolor/16x16/mimetypes/application-vnd.insync.link.dropbox.papert.png
/usr/share/icons/hicolor/16x16/mimetypes/application-vnd.insync.link.dropbox.web.png
/usr/share/icons/hicolor/16x16/mimetypes/dxpaper.png
/usr/share/icons/hicolor/16x16/mimetypes/dxpapert.png
/usr/share/icons/hicolor/16x16/mimetypes/dxweb.png
/usr/share/icons/hicolor/16x16/mimetypes/gddoc.png
/usr/share/icons/hicolor/16x16/mimetypes/gddraw.png
/usr/share/icons/hicolor/16x16/mimetypes/gdform.png
/usr/share/icons/hicolor/16x16/mimetypes/gdlink.png
/usr/share/icons/hicolor/16x16/mimetypes/gdnote.png
/usr/share/icons/hicolor/16x16/mimetypes/gdscript.png
/usr/share/icons/hicolor/16x16/mimetypes/gdsheet.png
/usr/share/icons/hicolor/16x16/mimetypes/gdslides.png
/usr/share/icons/hicolor/16x16/mimetypes/gdtable.png
/usr/share/icons/hicolor/16x16/places/insync-folder.png
/usr/share/icons/hicolor/192x192/places/insync-folder.png
/usr/share/icons/hicolor/22x22/places/insync-folder.png
/usr/share/icons/hicolor/24x24/places/insync-folder.png
/usr/share/icons/hicolor/256x256/mimetypes/application-vnd.insync.link.drive.doc.png
/usr/share/icons/hicolor/256x256/mimetypes/application-vnd.insync.link.drive.draw.png
/usr/share/icons/hicolor/256x256/mimetypes/application-vnd.insync.link.drive.form.png
/usr/share/icons/hicolor/256x256/mimetypes/application-vnd.insync.link.drive.link.png
/usr/share/icons/hicolor/256x256/mimetypes/application-vnd.insync.link.drive.note.png
/usr/share/icons/hicolor/256x256/mimetypes/application-vnd.insync.link.drive.script.png
/usr/share/icons/hicolor/256x256/mimetypes/application-vnd.insync.link.drive.sheet.png
/usr/share/icons/hicolor/256x256/mimetypes/application-vnd.insync.link.drive.slides.png
/usr/share/icons/hicolor/256x256/mimetypes/application-vnd.insync.link.drive.table.png
/usr/share/icons/hicolor/256x256/mimetypes/application-vnd.insync.link.dropbox.gdoc.png
/usr/share/icons/hicolor/256x256/mimetypes/application-vnd.insync.link.dropbox.gsheet.png
/usr/share/icons/hicolor/256x256/mimetypes/application-vnd.insync.link.dropbox.gslides.png
/usr/share/icons/hicolor/256x256/mimetypes/application-vnd.insync.link.dropbox.paper.png
/usr/share/icons/hicolor/256x256/mimetypes/application-vnd.insync.link.dropbox.papert.png
/usr/share/icons/hicolor/256x256/mimetypes/application-vnd.insync.link.dropbox.web.png
/usr/share/icons/hicolor/256x256/mimetypes/dxpaper.png
/usr/share/icons/hicolor/256x256/mimetypes/dxpapert.png
/usr/share/icons/hicolor/256x256/mimetypes/dxweb.png
/usr/share/icons/hicolor/256x256/mimetypes/gddoc.png
/usr/share/icons/hicolor/256x256/mimetypes/gddraw.png
/usr/share/icons/hicolor/256x256/mimetypes/gdform.png
/usr/share/icons/hicolor/256x256/mimetypes/gdlink.png
/usr/share/icons/hicolor/256x256/mimetypes/gdnote.png
/usr/share/icons/hicolor/256x256/mimetypes/gdscript.png
/usr/share/icons/hicolor/256x256/mimetypes/gdsheet.png
/usr/share/icons/hicolor/256x256/mimetypes/gdslides.png
/usr/share/icons/hicolor/256x256/mimetypes/gdtable.png
/usr/share/icons/hicolor/256x256/places/insync-folder.png
/usr/share/icons/hicolor/32x32/mimetypes/application-vnd.insync.link.drive.doc.png
/usr/share/icons/hicolor/32x32/mimetypes/application-vnd.insync.link.drive.draw.png
/usr/share/icons/hicolor/32x32/mimetypes/application-vnd.insync.link.drive.form.png
/usr/share/icons/hicolor/32x32/mimetypes/application-vnd.insync.link.drive.link.png
/usr/share/icons/hicolor/32x32/mimetypes/application-vnd.insync.link.drive.note.png
/usr/share/icons/hicolor/32x32/mimetypes/application-vnd.insync.link.drive.script.png
/usr/share/icons/hicolor/32x32/mimetypes/application-vnd.insync.link.drive.sheet.png
/usr/share/icons/hicolor/32x32/mimetypes/application-vnd.insync.link.drive.slides.png
/usr/share/icons/hicolor/32x32/mimetypes/application-vnd.insync.link.drive.table.png
/usr/share/icons/hicolor/32x32/mimetypes/application-vnd.insync.link.dropbox.gdoc.png
/usr/share/icons/hicolor/32x32/mimetypes/application-vnd.insync.link.dropbox.gsheet.png
/usr/share/icons/hicolor/32x32/mimetypes/application-vnd.insync.link.dropbox.gslides.png
/usr/share/icons/hicolor/32x32/mimetypes/application-vnd.insync.link.dropbox.paper.png
/usr/share/icons/hicolor/32x32/mimetypes/application-vnd.insync.link.dropbox.papert.png
/usr/share/icons/hicolor/32x32/mimetypes/application-vnd.insync.link.dropbox.web.png
/usr/share/icons/hicolor/32x32/mimetypes/dxpaper.png
/usr/share/icons/hicolor/32x32/mimetypes/dxpapert.png
/usr/share/icons/hicolor/32x32/mimetypes/dxweb.png
/usr/share/icons/hicolor/32x32/mimetypes/gddoc.png
/usr/share/icons/hicolor/32x32/mimetypes/gddraw.png
/usr/share/icons/hicolor/32x32/mimetypes/gdform.png
/usr/share/icons/hicolor/32x32/mimetypes/gdlink.png
/usr/share/icons/hicolor/32x32/mimetypes/gdnote.png
/usr/share/icons/hicolor/32x32/mimetypes/gdscript.png
/usr/share/icons/hicolor/32x32/mimetypes/gdsheet.png
/usr/share/icons/hicolor/32x32/mimetypes/gdslides.png
/usr/share/icons/hicolor/32x32/mimetypes/gdtable.png
/usr/share/icons/hicolor/32x32/places/insync-folder.png
/usr/share/icons/hicolor/36x36/places/insync-folder.png
/usr/share/icons/hicolor/48x48/places/insync-folder.png
/usr/share/icons/hicolor/48x48/status/insync-alert.png
/usr/share/icons/hicolor/48x48/status/insync-normal.png
/usr/share/icons/hicolor/48x48/status/insync-offline.png
/usr/share/icons/hicolor/48x48/status/insync-paused.png
/usr/share/icons/hicolor/48x48/status/insync-synced.png
/usr/share/icons/hicolor/48x48/status/insync-syncing.png
/usr/share/icons/hicolor/512x512/mimetypes/application-vnd.insync.link.drive.doc.png
/usr/share/icons/hicolor/512x512/mimetypes/application-vnd.insync.link.drive.draw.png
/usr/share/icons/hicolor/512x512/mimetypes/application-vnd.insync.link.drive.form.png
/usr/share/icons/hicolor/512x512/mimetypes/application-vnd.insync.link.drive.link.png
/usr/share/icons/hicolor/512x512/mimetypes/application-vnd.insync.link.drive.note.png
/usr/share/icons/hicolor/512x512/mimetypes/application-vnd.insync.link.drive.script.png
/usr/share/icons/hicolor/512x512/mimetypes/application-vnd.insync.link.drive.sheet.png
/usr/share/icons/hicolor/512x512/mimetypes/application-vnd.insync.link.drive.slides.png
/usr/share/icons/hicolor/512x512/mimetypes/application-vnd.insync.link.drive.table.png
/usr/share/icons/hicolor/512x512/mimetypes/application-vnd.insync.link.dropbox.gdoc.png
/usr/share/icons/hicolor/512x512/mimetypes/application-vnd.insync.link.dropbox.gsheet.png
/usr/share/icons/hicolor/512x512/mimetypes/application-vnd.insync.link.dropbox.gslides.png
/usr/share/icons/hicolor/512x512/mimetypes/application-vnd.insync.link.dropbox.paper.png
/usr/share/icons/hicolor/512x512/mimetypes/application-vnd.insync.link.dropbox.papert.png
/usr/share/icons/hicolor/512x512/mimetypes/application-vnd.insync.link.dropbox.web.png
/usr/share/icons/hicolor/512x512/mimetypes/dxpaper.png
/usr/share/icons/hicolor/512x512/mimetypes/dxpapert.png
/usr/share/icons/hicolor/512x512/mimetypes/dxweb.png
/usr/share/icons/hicolor/512x512/mimetypes/gddoc.png
/usr/share/icons/hicolor/512x512/mimetypes/gddraw.png
/usr/share/icons/hicolor/512x512/mimetypes/gdform.png
/usr/share/icons/hicolor/512x512/mimetypes/gdlink.png
/usr/share/icons/hicolor/512x512/mimetypes/gdnote.png
/usr/share/icons/hicolor/512x512/mimetypes/gdscript.png
/usr/share/icons/hicolor/512x512/mimetypes/gdsheet.png
/usr/share/icons/hicolor/512x512/mimetypes/gdslides.png
/usr/share/icons/hicolor/512x512/mimetypes/gdtable.png
/usr/share/icons/hicolor/64x64/places/insync-folder.png
/usr/share/icons/hicolor/72x72/places/insync-folder.png
/usr/share/icons/hicolor/96x96/places/insync-folder.png
/usr/share/icons/hicolor/scalable/apps/insync.svg
/usr/share/icons/hicolor/scalable/status/insync-alert.svg
/usr/share/icons/hicolor/scalable/status/insync-normal.svg
/usr/share/icons/hicolor/scalable/status/insync-offline.svg
/usr/share/icons/hicolor/scalable/status/insync-paused.svg
/usr/share/icons/hicolor/scalable/status/insync-synced.svg
/usr/share/icons/hicolor/scalable/status/insync-syncing.svg
/usr/share/mime-packages/insync-helper.xml

%files dev
%defattr(-,root,root,-)
/usr/lib64/.build-id/24/675b0091f38f45c5c1c5484cf24925b439b164
/usr/lib64/insync/Crypto/Cipher/_ARC4.abi3.so
/usr/lib64/insync/Crypto/Cipher/_Salsa20.abi3.so
/usr/lib64/insync/Crypto/Cipher/_chacha20.abi3.so
/usr/lib64/insync/Crypto/Cipher/_pkcs1_decode.abi3.so
/usr/lib64/insync/Crypto/Cipher/_raw_aes.abi3.so
/usr/lib64/insync/Crypto/Cipher/_raw_aesni.abi3.so
/usr/lib64/insync/Crypto/Cipher/_raw_arc2.abi3.so
/usr/lib64/insync/Crypto/Cipher/_raw_blowfish.abi3.so
/usr/lib64/insync/Crypto/Cipher/_raw_cast.abi3.so
/usr/lib64/insync/Crypto/Cipher/_raw_cbc.abi3.so
/usr/lib64/insync/Crypto/Cipher/_raw_cfb.abi3.so
/usr/lib64/insync/Crypto/Cipher/_raw_ctr.abi3.so
/usr/lib64/insync/Crypto/Cipher/_raw_des.abi3.so
/usr/lib64/insync/Crypto/Cipher/_raw_des3.abi3.so
/usr/lib64/insync/Crypto/Cipher/_raw_ecb.abi3.so
/usr/lib64/insync/Crypto/Cipher/_raw_eksblowfish.abi3.so
/usr/lib64/insync/Crypto/Cipher/_raw_ocb.abi3.so
/usr/lib64/insync/Crypto/Cipher/_raw_ofb.abi3.so
/usr/lib64/insync/Crypto/Hash/_BLAKE2b.abi3.so
/usr/lib64/insync/Crypto/Hash/_BLAKE2s.abi3.so
/usr/lib64/insync/Crypto/Hash/_MD2.abi3.so
/usr/lib64/insync/Crypto/Hash/_MD4.abi3.so
/usr/lib64/insync/Crypto/Hash/_MD5.abi3.so
/usr/lib64/insync/Crypto/Hash/_RIPEMD160.abi3.so
/usr/lib64/insync/Crypto/Hash/_SHA1.abi3.so
/usr/lib64/insync/Crypto/Hash/_SHA224.abi3.so
/usr/lib64/insync/Crypto/Hash/_SHA256.abi3.so
/usr/lib64/insync/Crypto/Hash/_SHA384.abi3.so
/usr/lib64/insync/Crypto/Hash/_SHA512.abi3.so
/usr/lib64/insync/Crypto/Hash/_ghash_clmul.abi3.so
/usr/lib64/insync/Crypto/Hash/_ghash_portable.abi3.so
/usr/lib64/insync/Crypto/Hash/_keccak.abi3.so
/usr/lib64/insync/Crypto/Hash/_poly1305.abi3.so
/usr/lib64/insync/Crypto/Math/_modexp.abi3.so
/usr/lib64/insync/Crypto/Protocol/_scrypt.abi3.so
/usr/lib64/insync/Crypto/PublicKey/_ec_ws.abi3.so
/usr/lib64/insync/Crypto/Util/_cpuid_c.abi3.so
/usr/lib64/insync/Crypto/Util/_strxor.abi3.so
/usr/lib64/insync/PySide2/Qt/resources/icudtl.dat
/usr/lib64/insync/PySide2/Qt/resources/qtwebengine_devtools_resources.pak
/usr/lib64/insync/PySide2/Qt/resources/qtwebengine_resources.pak
/usr/lib64/insync/PySide2/Qt/resources/qtwebengine_resources_100p.pak
/usr/lib64/insync/PySide2/Qt/resources/qtwebengine_resources_200p.pak
/usr/lib64/insync/PySide2/Qt/translations/qtbase_ar.qm
/usr/lib64/insync/PySide2/Qt/translations/qtbase_bg.qm
/usr/lib64/insync/PySide2/Qt/translations/qtbase_ca.qm
/usr/lib64/insync/PySide2/Qt/translations/qtbase_cs.qm
/usr/lib64/insync/PySide2/Qt/translations/qtbase_da.qm
/usr/lib64/insync/PySide2/Qt/translations/qtbase_de.qm
/usr/lib64/insync/PySide2/Qt/translations/qtbase_en.qm
/usr/lib64/insync/PySide2/Qt/translations/qtbase_es.qm
/usr/lib64/insync/PySide2/Qt/translations/qtbase_fi.qm
/usr/lib64/insync/PySide2/Qt/translations/qtbase_fr.qm
/usr/lib64/insync/PySide2/Qt/translations/qtbase_gd.qm
/usr/lib64/insync/PySide2/Qt/translations/qtbase_he.qm
/usr/lib64/insync/PySide2/Qt/translations/qtbase_hu.qm
/usr/lib64/insync/PySide2/Qt/translations/qtbase_it.qm
/usr/lib64/insync/PySide2/Qt/translations/qtbase_ja.qm
/usr/lib64/insync/PySide2/Qt/translations/qtbase_ko.qm
/usr/lib64/insync/PySide2/Qt/translations/qtbase_lv.qm
/usr/lib64/insync/PySide2/Qt/translations/qtbase_pl.qm
/usr/lib64/insync/PySide2/Qt/translations/qtbase_ru.qm
/usr/lib64/insync/PySide2/Qt/translations/qtbase_sk.qm
/usr/lib64/insync/PySide2/Qt/translations/qtbase_uk.qm
/usr/lib64/insync/PySide2/Qt/translations/qtbase_zh_TW.qm
/usr/lib64/insync/PySide2/Qt/translations/qtdeclarative_bg.qm
/usr/lib64/insync/PySide2/Qt/translations/qtdeclarative_da.qm
/usr/lib64/insync/PySide2/Qt/translations/qtdeclarative_de.qm
/usr/lib64/insync/PySide2/Qt/translations/qtdeclarative_en.qm
/usr/lib64/insync/PySide2/Qt/translations/qtdeclarative_es.qm
/usr/lib64/insync/PySide2/Qt/translations/qtdeclarative_fi.qm
/usr/lib64/insync/PySide2/Qt/translations/qtdeclarative_fr.qm
/usr/lib64/insync/PySide2/Qt/translations/qtdeclarative_hu.qm
/usr/lib64/insync/PySide2/Qt/translations/qtdeclarative_ja.qm
/usr/lib64/insync/PySide2/Qt/translations/qtdeclarative_ko.qm
/usr/lib64/insync/PySide2/Qt/translations/qtdeclarative_lv.qm
/usr/lib64/insync/PySide2/Qt/translations/qtdeclarative_pl.qm
/usr/lib64/insync/PySide2/Qt/translations/qtdeclarative_ru.qm
/usr/lib64/insync/PySide2/Qt/translations/qtdeclarative_sk.qm
/usr/lib64/insync/PySide2/Qt/translations/qtdeclarative_uk.qm
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/am.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/ar.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/bg.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/bn.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/ca.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/cs.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/da.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/de.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/el.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/en-GB.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/en-US.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/es-419.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/es.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/et.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/fa.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/fi.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/fil.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/fr.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/gu.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/he.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/hi.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/hr.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/hu.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/id.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/it.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/ja.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/kn.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/ko.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/lt.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/lv.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/ml.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/mr.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/ms.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/nb.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/nl.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/pl.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/pt-BR.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/pt-PT.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/ro.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/ru.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/sk.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/sl.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/sr.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/sv.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/sw.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/ta.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/te.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/th.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/tr.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/uk.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/vi.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/zh-CN.pak
/usr/lib64/insync/PySide2/Qt/translations/qtwebengine_locales/zh-TW.pak
/usr/lib64/insync/PySide2/QtCore.abi3.so
/usr/lib64/insync/PySide2/QtGui.abi3.so
/usr/lib64/insync/PySide2/QtNetwork.abi3.so
/usr/lib64/insync/PySide2/QtPositioning.abi3.so
/usr/lib64/insync/PySide2/QtPrintSupport.abi3.so
/usr/lib64/insync/PySide2/QtQml.abi3.so
/usr/lib64/insync/PySide2/QtQuick.abi3.so
/usr/lib64/insync/PySide2/QtQuickWidgets.abi3.so
/usr/lib64/insync/PySide2/QtWebChannel.abi3.so
/usr/lib64/insync/PySide2/QtWebEngineCore.abi3.so
/usr/lib64/insync/PySide2/QtWebEngineWidgets.abi3.so
/usr/lib64/insync/PySide2/QtWidgets.abi3.so
/usr/lib64/insync/PySide2/plugins/bearer/libqconnmanbearer.so
/usr/lib64/insync/PySide2/plugins/bearer/libqgenericbearer.so
/usr/lib64/insync/PySide2/plugins/bearer/libqnmbearer.so
/usr/lib64/insync/PySide2/plugins/egldeviceintegrations/libqeglfs-emu-integration.so
/usr/lib64/insync/PySide2/plugins/egldeviceintegrations/libqeglfs-kms-egldevice-integration.so
/usr/lib64/insync/PySide2/plugins/egldeviceintegrations/libqeglfs-x11-integration.so
/usr/lib64/insync/PySide2/plugins/iconengines/libqsvgicon.so
/usr/lib64/insync/PySide2/plugins/imageformats/libqgif.so
/usr/lib64/insync/PySide2/plugins/imageformats/libqicns.so
/usr/lib64/insync/PySide2/plugins/imageformats/libqico.so
/usr/lib64/insync/PySide2/plugins/imageformats/libqjpeg.so
/usr/lib64/insync/PySide2/plugins/imageformats/libqsvg.so
/usr/lib64/insync/PySide2/plugins/imageformats/libqtga.so
/usr/lib64/insync/PySide2/plugins/imageformats/libqtiff.so
/usr/lib64/insync/PySide2/plugins/imageformats/libqwbmp.so
/usr/lib64/insync/PySide2/plugins/imageformats/libqwebp.so
/usr/lib64/insync/PySide2/plugins/platforminputcontexts/libcomposeplatforminputcontextplugin.so
/usr/lib64/insync/PySide2/plugins/platforminputcontexts/libibusplatforminputcontextplugin.so
/usr/lib64/insync/PySide2/plugins/platforminputcontexts/libqtvirtualkeyboardplugin.so
/usr/lib64/insync/PySide2/plugins/platforms/libqeglfs.so
/usr/lib64/insync/PySide2/plugins/platforms/libqlinuxfb.so
/usr/lib64/insync/PySide2/plugins/platforms/libqminimal.so
/usr/lib64/insync/PySide2/plugins/platforms/libqminimalegl.so
/usr/lib64/insync/PySide2/plugins/platforms/libqoffscreen.so
/usr/lib64/insync/PySide2/plugins/platforms/libqvnc.so
/usr/lib64/insync/PySide2/plugins/platforms/libqwayland-egl.so
/usr/lib64/insync/PySide2/plugins/platforms/libqwayland-generic.so
/usr/lib64/insync/PySide2/plugins/platforms/libqwayland-xcomposite-egl.so
/usr/lib64/insync/PySide2/plugins/platforms/libqwayland-xcomposite-glx.so
/usr/lib64/insync/PySide2/plugins/platforms/libqwebgl.so
/usr/lib64/insync/PySide2/plugins/platforms/libqxcb.so
/usr/lib64/insync/PySide2/plugins/platformthemes/libqgtk3.so
/usr/lib64/insync/PySide2/plugins/platformthemes/libqxdgdesktopportal.so
/usr/lib64/insync/PySide2/plugins/position/libqtposition_geoclue.so
/usr/lib64/insync/PySide2/plugins/position/libqtposition_geoclue2.so
/usr/lib64/insync/PySide2/plugins/position/libqtposition_positionpoll.so
/usr/lib64/insync/PySide2/plugins/position/libqtposition_serialnmea.so
/usr/lib64/insync/PySide2/plugins/printsupport/libcupsprintersupport.so
/usr/lib64/insync/PySide2/plugins/qmltooling/libqmldbg_debugger.so
/usr/lib64/insync/PySide2/plugins/qmltooling/libqmldbg_inspector.so
/usr/lib64/insync/PySide2/plugins/qmltooling/libqmldbg_local.so
/usr/lib64/insync/PySide2/plugins/qmltooling/libqmldbg_messages.so
/usr/lib64/insync/PySide2/plugins/qmltooling/libqmldbg_native.so
/usr/lib64/insync/PySide2/plugins/qmltooling/libqmldbg_nativedebugger.so
/usr/lib64/insync/PySide2/plugins/qmltooling/libqmldbg_preview.so
/usr/lib64/insync/PySide2/plugins/qmltooling/libqmldbg_profiler.so
/usr/lib64/insync/PySide2/plugins/qmltooling/libqmldbg_quickprofiler.so
/usr/lib64/insync/PySide2/plugins/qmltooling/libqmldbg_server.so
/usr/lib64/insync/PySide2/plugins/qmltooling/libqmldbg_tcp.so
/usr/lib64/insync/PySide2/plugins/wayland-decoration-client/libbradient.so
/usr/lib64/insync/PySide2/plugins/wayland-graphics-integration-client/libdmabuf-server.so
/usr/lib64/insync/PySide2/plugins/wayland-graphics-integration-client/libdrm-egl-server.so
/usr/lib64/insync/PySide2/plugins/wayland-graphics-integration-client/libqt-plugin-wayland-egl.so
/usr/lib64/insync/PySide2/plugins/wayland-graphics-integration-client/libshm-emulation-server.so
/usr/lib64/insync/PySide2/plugins/wayland-graphics-integration-client/libxcomposite-egl.so
/usr/lib64/insync/PySide2/plugins/wayland-graphics-integration-client/libxcomposite-glx.so
/usr/lib64/insync/PySide2/plugins/wayland-graphics-integration-server/libdmabuf-server.so
/usr/lib64/insync/PySide2/plugins/wayland-graphics-integration-server/libdrm-egl-server.so
/usr/lib64/insync/PySide2/plugins/wayland-graphics-integration-server/libqt-plugin-wayland-egl.so
/usr/lib64/insync/PySide2/plugins/wayland-graphics-integration-server/libshm-emulation-server.so
/usr/lib64/insync/PySide2/plugins/wayland-graphics-integration-server/libwayland-eglstream-controller.so
/usr/lib64/insync/PySide2/plugins/wayland-graphics-integration-server/libxcomposite-egl.so
/usr/lib64/insync/PySide2/plugins/wayland-graphics-integration-server/libxcomposite-glx.so
/usr/lib64/insync/PySide2/plugins/wayland-shell-integration/libivi-shell.so
/usr/lib64/insync/PySide2/plugins/wayland-shell-integration/libwl-shell.so
/usr/lib64/insync/PySide2/plugins/wayland-shell-integration/libxdg-shell-v5.so
/usr/lib64/insync/PySide2/plugins/wayland-shell-integration/libxdg-shell-v6.so
/usr/lib64/insync/PySide2/plugins/wayland-shell-integration/libxdg-shell.so
/usr/lib64/insync/PySide2/plugins/xcbglintegrations/libqxcb-egl-integration.so
/usr/lib64/insync/PySide2/plugins/xcbglintegrations/libqxcb-glx-integration.so
/usr/lib64/insync/_struct/cpython-37m-x86_64-linux-gnu/sotruct.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/base_library.zip
/usr/lib64/insync/gi/_gi.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/ideskui/build/asset-manifest.json
/usr/lib64/insync/ideskui/build/index.html
/usr/lib64/insync/ideskui/build/static/css/main.d1c363b2.chunk.css
/usr/lib64/insync/ideskui/build/static/css/main.d1c363b2.chunk.css.map
/usr/lib64/insync/ideskui/build/static/js/0.00df56b5.chunk.js
/usr/lib64/insync/ideskui/build/static/js/0.00df56b5.chunk.js.map
/usr/lib64/insync/ideskui/build/static/js/1.8f5538b5.chunk.js
/usr/lib64/insync/ideskui/build/static/js/1.8f5538b5.chunk.js.LICENSE.txt
/usr/lib64/insync/ideskui/build/static/js/1.8f5538b5.chunk.js.map
/usr/lib64/insync/ideskui/build/static/js/4.54079fdd.chunk.js
/usr/lib64/insync/ideskui/build/static/js/4.54079fdd.chunk.js.LICENSE.txt
/usr/lib64/insync/ideskui/build/static/js/4.54079fdd.chunk.js.map
/usr/lib64/insync/ideskui/build/static/js/5.d90a46dc.chunk.js
/usr/lib64/insync/ideskui/build/static/js/5.d90a46dc.chunk.js.LICENSE.txt
/usr/lib64/insync/ideskui/build/static/js/5.d90a46dc.chunk.js.map
/usr/lib64/insync/ideskui/build/static/js/6.ee8edd7a.chunk.js
/usr/lib64/insync/ideskui/build/static/js/6.ee8edd7a.chunk.js.map
/usr/lib64/insync/ideskui/build/static/js/main.0cdb9cad.chunk.js
/usr/lib64/insync/ideskui/build/static/js/main.0cdb9cad.chunk.js.map
/usr/lib64/insync/ideskui/build/static/js/runtime-main.31bc3f52.js
/usr/lib64/insync/ideskui/build/static/js/runtime-main.31bc3f52.js.map
/usr/lib64/insync/ideskui/build/static/media/Lato-Black.e5c10b5f.ttf
/usr/lib64/insync/ideskui/build/static/media/Lato-Bold.401bd636.ttf
/usr/lib64/insync/ideskui/build/static/media/Lato-Light.bd895b1e.ttf
/usr/lib64/insync/ideskui/build/static/media/Lato-Regular.79164ee5.ttf
/usr/lib64/insync/ideskui/build/static/media/od-avatar.e64639c8.png
/usr/lib64/insync/insync
/usr/lib64/insync/lib-dynload/_asyncio.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_bisect.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_blake2.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_bz2.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_codecs_cn.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_codecs_hk.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_codecs_iso2022.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_codecs_jp.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_codecs_kr.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_codecs_tw.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_contextvars.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_ctypes.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_curses.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_curses_panel.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_datetime.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_decimal.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_elementtree.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_hashlib.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_heapq.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_json.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_lzma.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_md5.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_multibytecodec.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_multiprocessing.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_opcode.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_pickle.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_posixsubprocess.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_queue.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_random.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_sha1.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_sha256.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_sha3.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_sha512.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_socket.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_sqlite3.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_ssl.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/_struct.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/array.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/binascii.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/fcntl.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/grp.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/math.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/mmap.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/pyexpat.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/readline.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/resource.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/select.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/termios.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/unicodedata.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/lib-dynload/zlib.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/libQt5Core.so.5
/usr/lib64/insync/libQt5DBus.so.5
/usr/lib64/insync/libQt5EglFSDeviceIntegration.so.5
/usr/lib64/insync/libQt5EglFsKmsSupport.so.5
/usr/lib64/insync/libQt5Gui.so.5
/usr/lib64/insync/libQt5Network.so.5
/usr/lib64/insync/libQt5Positioning.so.5
/usr/lib64/insync/libQt5PrintSupport.so.5
/usr/lib64/insync/libQt5Qml.so.5
/usr/lib64/insync/libQt5Quick.so.5
/usr/lib64/insync/libQt5QuickWidgets.so.5
/usr/lib64/insync/libQt5SerialPort.so.5
/usr/lib64/insync/libQt5Svg.so.5
/usr/lib64/insync/libQt5WaylandClient.so.5
/usr/lib64/insync/libQt5WaylandCompositor.so.5
/usr/lib64/insync/libQt5WebChannel.so.5
/usr/lib64/insync/libQt5WebEngine.so.5
/usr/lib64/insync/libQt5WebEngineCore.so.5
/usr/lib64/insync/libQt5WebEngineWidgets.so.5
/usr/lib64/insync/libQt5WebSockets.so.5
/usr/lib64/insync/libQt5WebView.so.5
/usr/lib64/insync/libQt5Widgets.so.5
/usr/lib64/insync/libQt5XcbQpa.so.5
/usr/lib64/insync/libXau.so.6
/usr/lib64/insync/libXcomposite.so.1
/usr/lib64/insync/libXcursor.so.1
/usr/lib64/insync/libXdamage.so.1
/usr/lib64/insync/libXext.so.6
/usr/lib64/insync/libXfixes.so.3
/usr/lib64/insync/libXi.so.6
/usr/lib64/insync/libXinerama.so.1
/usr/lib64/insync/libXrandr.so.2
/usr/lib64/insync/libXrender.so.1
/usr/lib64/insync/libXtst.so.6
/usr/lib64/insync/libasound.so.2
/usr/lib64/insync/libasyncns.so.0
/usr/lib64/insync/libatk-1.0.so.0
/usr/lib64/insync/libatk-bridge-2.0.so.0
/usr/lib64/insync/libatspi.so.0
/usr/lib64/insync/libavahi-client.so.3
/usr/lib64/insync/libavahi-common.so.3
/usr/lib64/insync/libblkid.so.1
/usr/lib64/insync/libbrotlicommon.so.1
/usr/lib64/insync/libbrotlidec.so.1
/usr/lib64/insync/libbz2.so.1
/usr/lib64/insync/libcairo-gobject.so.2
/usr/lib64/insync/libcairo.so.2
/usr/lib64/insync/libcap.so.2
/usr/lib64/insync/libcloudproviders.so.0
/usr/lib64/insync/libcom_err.so.2
/usr/lib64/insync/libcrypt.so.2
/usr/lib64/insync/libcrypto.so.1.1
/usr/lib64/insync/libcups.so.2
/usr/lib64/insync/libcurl.so.4
/usr/lib64/insync/libdatrie.so.1
/usr/lib64/insync/libdbus-1.so.3
/usr/lib64/insync/libepoxy.so.0
/usr/lib64/insync/libexpat.so.1
/usr/lib64/insync/libffi.so.6
/usr/lib64/insync/libfontconfig.so.1
/usr/lib64/insync/libfreetype.so.6
/usr/lib64/insync/libfribidi.so.0
/usr/lib64/insync/libgcc_s.so.1
/usr/lib64/insync/libgcrypt.so.20
/usr/lib64/insync/libgdk-3.so.0
/usr/lib64/insync/libgio-2.0.so.0
/usr/lib64/insync/libgirepository-1.0.so.1
/usr/lib64/insync/libglib-2.0.so.0
/usr/lib64/insync/libgmodule-2.0.so.0
/usr/lib64/insync/libgmp.so.10
/usr/lib64/insync/libgnutls.so.30
/usr/lib64/insync/libgobject-2.0.so.0
/usr/lib64/insync/libgpg-error.so.0
/usr/lib64/insync/libgraphite2.so.3
/usr/lib64/insync/libgsm.so.1
/usr/lib64/insync/libgssapi_krb5.so.2
/usr/lib64/insync/libgthread-2.0.so.0
/usr/lib64/insync/libgtk-3.so.0
/usr/lib64/insync/libharfbuzz.so.0
/usr/lib64/insync/libhogweed.so.6
/usr/lib64/insync/libicudata.so.56
/usr/lib64/insync/libicudata.so.69
/usr/lib64/insync/libicui18n.so.56
/usr/lib64/insync/libicui18n.so.69
/usr/lib64/insync/libicuuc.so.56
/usr/lib64/insync/libicuuc.so.69
/usr/lib64/insync/libidn2.so.0
/usr/lib64/insync/libjpeg.so.62
/usr/lib64/insync/libjson-glib-1.0.so.0
/usr/lib64/insync/libk5crypto.so.3
/usr/lib64/insync/libkeyutils.so.1
/usr/lib64/insync/libkrb5.so.3
/usr/lib64/insync/libkrb5support.so.0
/usr/lib64/insync/liblz4.so.1
/usr/lib64/insync/liblzma.so.5
/usr/lib64/insync/libmount.so.1
/usr/lib64/insync/libnettle.so.8
/usr/lib64/insync/libnspr4.so
/usr/lib64/insync/libogg.so.0
/usr/lib64/insync/libopus.so.0
/usr/lib64/insync/libp11-kit.so.0
/usr/lib64/insync/libpanelw.so.6
/usr/lib64/insync/libpango-1.0.so.0
/usr/lib64/insync/libpangocairo-1.0.so.0
/usr/lib64/insync/libpangoft2-1.0.so.0
/usr/lib64/insync/libpcre.so.1
/usr/lib64/insync/libpcre2-8.so.0
/usr/lib64/insync/libpixman-1.so.0
/usr/lib64/insync/libplc4.so
/usr/lib64/insync/libplds4.so
/usr/lib64/insync/libpulsecommon-15.0.so
/usr/lib64/insync/libpyside2.abi3.so.5.12
/usr/lib64/insync/libpython3.7m.so.1.0
/usr/lib64/insync/libreadline.so.8
/usr/lib64/insync/libselinux.so.1
/usr/lib64/insync/libshiboken2.abi3.so.5.12
/usr/lib64/insync/libsmime3.so
/usr/lib64/insync/libsndfile.so.1
/usr/lib64/insync/libsqlite3.so.0
/usr/lib64/insync/libssl.so.1.1
/usr/lib64/insync/libstdc++.so.6
/usr/lib64/insync/libstemmer.so.0
/usr/lib64/insync/libsystemd.so.0
/usr/lib64/insync/libtasn1.so.6
/usr/lib64/insync/libtracker-sparql-3.0.so.0
/usr/lib64/insync/libunistring.so.2
/usr/lib64/insync/libwayland-client.so.0
/usr/lib64/insync/libwayland-cursor.so.0
/usr/lib64/insync/libwayland-egl.so.1
/usr/lib64/insync/libwayland-server.so.0
/usr/lib64/insync/libxml2.so.2
/usr/lib64/insync/libz.so.1
/usr/lib64/insync/libzstd.so.1
/usr/lib64/insync/psutil/_psutil_linux.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/psutil/_psutil_posix.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/pycurl.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/insync/shiboken2/shiboken2.abi3.so
/usr/lib64/insync/zlib/cpython-37m-x86_64-linux-gnu/soib.cpython-37m-x86_64-linux-gnu.so

%files libexec
%defattr(-,root,root,-)
/usr/lib64/insync/PySide2/Qt/libexec/QtWebEngineProcess
/usr/lib64/insync/PySide2/Qt/libexec/qt.conf

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/insync-hide.1.gz
/usr/share/man/man1/insync-open-cloud.1.gz
/usr/share/man/man1/insync-open-share-dialog.1.gz
/usr/share/man/man1/insync-quit.1.gz
/usr/share/man/man1/insync-show.1.gz
/usr/share/man/man1/insync-start.1.gz
/usr/share/man/man1/insync-version.1.gz
/usr/share/man/man1/insync.1.gz
