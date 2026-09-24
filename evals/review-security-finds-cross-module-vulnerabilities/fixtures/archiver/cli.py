import argparse

from . import accounts, commands


def main(argv=None):
    parser = argparse.ArgumentParser(prog="archiver")
    sub = parser.add_subparsers(dest="command", required=True)
    pack = sub.add_parser("pack")
    pack.add_argument("folder")
    restore = sub.add_parser("restore")
    restore.add_argument("archive")
    share = sub.add_parser("share")
    share.add_argument("doc_id")
    sub.add_parser("rotate-key")
    args = parser.parse_args(argv)

    user = accounts.current()
    if args.command == "pack":
        print(commands.pack(user, args.folder))
    elif args.command == "restore":
        print(f"{commands.restore(user, args.archive)} documents restored")
    elif args.command == "share":
        print(commands.share(user, args.doc_id))
    elif args.command == "rotate-key":
        print(commands.rotate_key(user))
