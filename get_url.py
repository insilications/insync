#!/usr/bin/env python

import re
import sys
import os
import requests
#import natsort
import subprocess

#from operator import attrgetter, itemgetter
#from bs4 import BeautifulSoup

def write_out(filename, content, mode="w"):
    """File.write convenience wrapper."""
    with open_auto(filename, mode) as require_f:
        require_f.write(content)

def open_auto(*args, **kwargs):
    """Open a file with UTF-8 encoding.

    Open file with UTF-8 encoding and "surrogate" escape characters that are
    not valid UTF-8 to avoid data corruption.
    """
    # 'encoding' and 'errors' are fourth and fifth positional arguments, so
    # restrict the args tuple to (file, mode, buffering) at most
    assert len(args) <= 3
    assert "encoding" not in kwargs
    assert "errors" not in kwargs
    return open(*args, encoding="utf-8", errors="surrogateescape", **kwargs)

def main():
    cwd = os.getcwd()
    filename = ""
    filename = [f.path for f in os.scandir(cwd) if f.is_file() and "insync-v" in f.name]

# /insilications/Downloads/insync-3.7.0.50216-fc35.x86_64.rpm
# https://d2t3ff60b2tol4.cloudfront.net/builds/insync-3.7.0.50216-fc35.x86_64.rpm
#       var rpmLink = 'https://d2t3ff60b2tol4.cloudfront.net/builds/insync-'
# https://d2t3ff60b2tol4.cloudfront.net/builds/insync-dolphin-3.4.0.40973-1.noarch.rpm
# https://d2t3ff60b2tol4.cloudfront.net/builds/insync-dolphin-3.4.2.40983-1.noarch.rpm
# https://d2t3ff60b2tol4.cloudfront.net/builds/fedora/35/noarch/insync-dolphin-3.4.2.40983-1.noarch.rpm
    if not filename:
        linux_releases_js = requests.get("https://d2t3ff60b2tol4.cloudfront.net/changelogs/desktop/linuxReleases.js").text
        linux_releases_js_re = re.compile(r"(?:\"version\":\")((?:\d+)(?:[-._]*\d+)*)(?:\",)")

        #for m in linux_releases_js_re.finditer(linux_releases_js):
            #print('%02d-%02d: %s' % (m.start(), m.end(), m.group(1)))

        linux_releases_js_version_list = linux_releases_js_re.findall(linux_releases_js)
        #print(linux_releases_js_version_list)
        last_version = linux_releases_js_version_list[0]
        found_url = f"https://d2t3ff60b2tol4.cloudfront.net/builds/insync-{last_version}-fc36.x86_64.rpm"
        filename = f"{cwd}/{os.path.basename(found_url)}"

        #print(f"Last version: {last_version}")
        #print(f"URL download: {found_url}")
        #print(f"Filename: {filename}")

        if not os.path.exists(filename):
            curl_cmd = f"curl -L -O {found_url}"
            #print(f"curl_cmd: {curl_cmd}")
            try:
                process = subprocess.run(
                    curl_cmd,
                    check=True,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    universal_newlines=True,
                    cwd=cwd,
                )
            except subprocess.CalledProcessError as err:
                print(f"Unable to download {found_url} in {cwd}: {err}")
                sys.exit(1)

        if os.path.isfile(filename):
            rpm_extract_cmd = f'rpm2cpio {filename} | cpio -ivdm --directory="{cwd}"'
            #print(f"{rpm_extract_cmd}")
            try:
                process = subprocess.run(
                    rpm_extract_cmd,
                    check=True,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    universal_newlines=True,
                    cwd=cwd,
                )
            except subprocess.CalledProcessError as err:
                print(f"Unable to extract {filename} in {cwd}: {err}")
                sys.exit(1)

            fix_insync_cmd1 = f'rm -f libX11* libxkbcommon.so* libtinfo.so* libpng16.so* lib{{drm,GLX,GLdispatch}}.so* libgdk_pixbuf-2.0.so* libxkbcommon.so* libxcb* libncurses*'
            fix_insync_cwd1 = f"{cwd}/usr/lib/insync/"
            #print(f"{fix_insync_cmd1}")
            #print(f"{fix_insync_cwd1}")
            process = subprocess.run(
                fix_insync_cmd1,
                check=False,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                universal_newlines=True,
                cwd=fix_insync_cwd1,
            )

            fix_insync_cwd2 = f"{cwd}/usr/bin/"
            fix_insync_cmd2 = f"sd '/usr/lib/insync/insync' '/usr/lib64/insync/insync' 'insync'"
            #print(f"{fix_insync_cmd2}")
            #print(f"{fix_insync_cwd2}")
            process = subprocess.run(
                fix_insync_cmd2,
                check=False,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                universal_newlines=True,
                cwd=fix_insync_cwd2,
            )
            fix_insync_cmd3 = f"sd '\"\$@\"' '\"$@\" --ca-path /var/cache/ca-certs/anchors/ --qt-qpa-platform xcb' 'insync'"
            #print(f"{fix_insync_cmd3}")
            #print(f"{fix_insync_cwd2}")
            process = subprocess.run(
                fix_insync_cmd3,
                check=False,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                universal_newlines=True,
                cwd=fix_insync_cwd2,
            )
            fix_insync_cmd4 = f"sd 'LC_TIME=C' 'LC_TIME=C QT_QPA_PLATFORM=xcb' 'insync'"
            #print(f"{fix_insync_cmd4}")
            #print(f"{fix_insync_cwd2}")
            process = subprocess.run(
                fix_insync_cmd4,
                check=False,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                universal_newlines=True,
                cwd=fix_insync_cwd2,
            )

        filename_cmake = f"{cwd}/CMakeLists.txt"
        if not os.path.exists(filename_cmake):
            cmake_cmd = f"curl --location https://raw.githubusercontent.com/insilications/insync-clr/master/CMakeLists.txt -o CMakeLists.txt"
            #print(f"cmake_cmd: {cmake_cmd}")
            try:
                process = subprocess.run(
                    cmake_cmd,
                    check=True,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    universal_newlines=True,
                    cwd=cwd,
                )
            except subprocess.CalledProcessError as err:
                print(f"Unable to download {filename_cmake} in {cwd}: {err}")
                sys.exit(1)

        filename_tar = f"{cwd}/insync-v{last_version}.tar.gz"
        if not os.path.exists(filename_tar):
            tar_cmd = f"tar --create --add-file=CMakeLists.txt --file=- usr/ | pigz -9 -p 16 > {filename_tar}"
            #print(f"tar_cmd: {tar_cmd}")
            try:
                process = subprocess.run(
                    tar_cmd,
                    check=True,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    universal_newlines=True,
                    cwd=cwd,
                )
            except subprocess.CalledProcessError as err:
                print(f"Unable to tar {filename_tar} in {cwd}: {err}")
                sys.exit(1)

        filename_uri = f"file://{filename_tar}"
        print(filename_uri)
    else:
        filename_uri = f"file://{filename[0]}"
        print(filename_uri)

if __name__ == "__main__":
    main()
