#!/usr/bin/env python
import sys
import subprocess

version = f"{sys.version_info.major}.{sys.version_info.minor}"
cmd = [
    sys.executable,
    "-m",
    "mypy",
    "--python-version",
    version,
    "--config-file",
    "mypy.ini",
    "src",
    "tests",
]
sys.exit(subprocess.run(cmd).returncode)
