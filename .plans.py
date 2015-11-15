from plan import run

def plan_upload(args):
    if_bumpversion = input("bumpversion? (y/n): ")
    if if_bumpversion == "y":
        run(["bumpversion", "patch"])
    run(["python", "setup.py", "sdist", "upload"])

plans = {
    "upload": plan_upload,
}
