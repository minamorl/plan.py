def shell(s, on=None, start_new_session=False, asynchronous=True):
    import subprocess
    import os

    if on is not None:
        on = os.path.expanduser(on)

    if asynchronous:
        return subprocess.Popen(s, cwd=on, start_new_session=start_new_session)
    return subprocess.run(s, cwd=on, start_new_session=start_new_session)


def run(s, on=None, start_new_session=False):
    return shell(s, on=on, start_new_session=start_new_session, asynchronous=False)
