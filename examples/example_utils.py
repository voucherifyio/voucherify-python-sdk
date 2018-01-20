import argparse


def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--wait", action="store_true", help="if set, the program will wait after every example")
    return parser.parse_args()


def waitForInput(wait=False):
    if not wait:
        return
    try:
        input('Press Enter to continue...')
    except SyntaxError:
        pass
