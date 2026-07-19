import argparse
import sys


def main():
    parser = argparse.ArgumentParser(
        prog="pkcli",
        description="Pythkernel Engine CLI",
    )

    sub = parser.add_subparsers(dest="command")

    sub.add_parser("version", help="Show engine version")

    args = parser.parse_args()

    if args.command == "version":
        print("Pythkernel Engine v0.0.3")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
