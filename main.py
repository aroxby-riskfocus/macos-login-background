#!/usr/bin/env python
"""
Finds your current wallpaper and copies it to the login screen
"""

from os import path
from shutil import copyfile
import subprocess
from urllib.parse import unquote, urlparse


def system(*args):
    process = subprocess.run(args, capture_output=True, check=True)
    return process.stdout.decode('utf-8')


def get_bg_path():
    script = """
        tell application "Finder"
            set bgImage to desktop picture
            set bgPath to url of bgImage
            get bgPath
        end tell
    """
    output = system('osascript', '-e', script).strip()
    bg_path = unquote(urlparse(output).path)
    return bg_path


def backup_mojave():
    sys_path = '/Library/Desktop Pictures/Mojave.heic'
    backup_path = '/Library/Desktop Pictures/MacOS Mojave.heic'
    if not path.exists(backup_path):
        print('Backing up original image...')
        copyfile(sys_path, backup_path)


def overwrite_mojave(bg_path):
    sys_path = '/Library/Desktop Pictures/Mojave.heic'
    print('Copying file...')
    copyfile(bg_path, sys_path)


def main():
    bg_path = get_bg_path()
    backup_mojave()
    overwrite_mojave(bg_path)


if __name__ == '__main__':
    main()
