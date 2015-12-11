import os
import sys
TIME_LIMIT = 3600


def generate_argpase(mod):
    import argparse
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    for planname, func in mod.plans.items():
        subparser = subparsers.add_parser(planname)
        subparser.add_argument("args", nargs=argparse.REMAINDER)
        subparser.set_defaults(func=func)
    return parser


class DetectionError(Exception):
    pass


def detect_rules():
    import importlib
    try:
        return importlib.machinery.SourceFileLoader("rules", os.path.join(os.getcwd(), ".plans.py")).load_module()

    except ImportError:
        raise DetectionError

    except FileNotFoundError:
        raise DetectionError


def main():
    import time
    from clint.textui import colored

    process_list = []

    try:
        parser = generate_argpase(detect_rules())
        args = parser.parse_args()

    except DetectionError:
        print(colored.red("No plan was found. [FAIL]"))
        return 1

    if not hasattr(args, "func"):
        print(parser.format_help())
        return 1

    try:
        process_list = list(args.func(args) or [])
        for proc in process_list:
            proc.wait(TIME_LIMIT)

    except KeyboardInterrupt:
        print("")
        print("Terminating.. ", end="")
        for proc in process_list:
            proc.terminate()
            proc.wait()
        print(colored.green("[SUCCESS]"))


if __name__ == '__main__':
    main()
