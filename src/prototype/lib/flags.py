import argparse

added_arguments = []
frozen = False
parsed = False
args = None
parser = None

def add_argument(*args, **kwargs):
    global frozen

    assert not frozen
    added_arguments.append((args, kwargs))

def make_parser(description=None):
    global frozen
    global parsed
    global parser

    assert not parsed
    frozen = True

    if parser:
        return parser

    parser = argparse.ArgumentParser(description=description)
    for args, kwargs in added_arguments:
        parser.add_argument(*args, **kwargs)
    return parser

def parse_args():
    global args
    global frozen
    global parsed
    global parser

    if not frozen:
        make_parser(description='No description provided')

    parsed = True
    if args is None:
        args = parser.parse_args()
    return args