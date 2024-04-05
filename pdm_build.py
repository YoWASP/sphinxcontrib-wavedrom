import os
from datetime import datetime
from pdm.backend.hooks.version import SCMVersion


def format_version(version: SCMVersion) -> str:
    major, minor = (int(n) for n in str(version.version).split(".")[:2])
    dirty = f"+{datetime.utcnow():%Y%m%d.%H%M%S}" if version.dirty else ""
    if version.distance is None:
        return f"{major}.{minor}{dirty}"
    else:
        return f"{major}.{minor}.dev{version.distance}{dirty}"
