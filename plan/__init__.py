import subprocess
import os


def shell(s, on=None, start_new_session=False):

    if on is not None:
        on = os.path.expanduser(on)

    return subprocess.Popen(s, cwd=on, start_new_session=start_new_session)
