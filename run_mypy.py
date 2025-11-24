#!/usr/bin/env python
import sys
import subprocess

py_version = f"{sys.version_info.major}.{sys.version_info.minor}"
cmd = [
    sys.executable,
    "-m",
    "mypy",
    "--python-version",
    py_version,
    "--config-file",
    "mypy.ini",
    "src",
    "tests",
]
exit_code = subprocess.run(cmd).returncode

exit(exit_code)
