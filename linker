#!/bin/python
import argparse
import quads

def ReadWorld(args):
    # example function for subcommand
    # (these will be calling functions in other files)
    print(args)

def main():
    app = argparse.ArgumentParser(description=
        f"Linker\n{'':=<50}\nA tool for planning locations for "
        "and resolving conflicts with nether portals in Minecraft",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    commands = app.add_subparsers()

    # command added as follows:
    read_world_help="Read world files to locate portal coordinates"
    read_world = commands.add_parser("read-world", description=read_world_help, help=read_world_help)
    read_world.add_argument('world', type=str, help="path to the save file")
    read_world.set_defaults(func=ReadWorld)

    # MC WORLD > LINKER CONFIG
    # if this is overwriting an existing config, the user will need to provide options
    # as to what happens when a portal in the config is not found in the world
    # (e.g. auto-remove, auto-keep, check interactively with user, etc.)

    # LINKER CONFIG > PRINT LINKS FOR ALL PORTALS

    # LINKER CONFIG > CHECK FOR CONFLICTS

    # LINKER CONFIG (prospective portal) > TEST FOR POSSIBLE LOCATIONS

    # parse arguments and call function corresponding to selected command
    args = app.parse_args()
    if vars(args).get('func'): args.func(args)

if __name__ == "__main__":
    main()
