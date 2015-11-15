from plan import shell

def plan_upload(args):
    if_bumpversion = input("bumpversion? (y/n): ")
    if if_bumpversion == "y":
        shell(["bumpversion", "patch"], asynchronous=False)
    shell(["python", "setup.py", "sdist", "upload"], asynchronous=False)
    return []

plans = {
    "upload": plan_upload,
}
