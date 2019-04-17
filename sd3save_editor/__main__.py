#!/usr/bin/env python3

import argparse
import sys
import sd3save_editor.save as save


def main():
    parser = argparse.ArgumentParser(description="Edit a Seiken Densetsu 3 save file")
    parser.add_argument("file", type=argparse.FileType("r+b"),
                        help="The Seiken3 save (srm format)")
    parser.add_argument("entry", type=int,
                        help="Save entry", choices=[1, 2, 3])
    parser.add_argument("--location", type=int,
                        help="ID of the in-game location")
    parser.add_argument("--player1-name", type=str,
                        help="Name of the first player")
    parser.add_argument("--player2-name", type=str,
                        help="Name of the second player")
    parser.add_argument("--player3-name", type=str,
                        help="Name of the third player")
    parser.add_argument("--luc", type=int,
                        help="""Amount of money.
                                Warning: too much money that the game can't
                                handle will corrupt your save""")
    args = parser.parse_args()
    save_data = save.save_format.parse(args.file.read())
    save_index = args.entry - 1
    if not save.check_valid_save(save_data):
        print("Please choose a valid Seiken3 save file")
        parser.print_help()
        sys.exit(-1)
    if save_data[save_index] is None:
        print("Save entry doesn't exist")
        sys.exit(-2)
    if args.location:
        save_data[save_index].data.value.location = args.location
    if args.player1_name or args.player2_name or args.player3_name:
        character_names = save_data[save_index].data.value.character_names
        if args.player1_name:
            character_names[0] = args.player1_name
        if args.player2_name:
            character_names[1] = args.player2_name
        if args.player3_name:
            character_names[2] = args.player3_name
        try:
            save.write_character_names(save_data, character_names, save_index)
        except save.NameTooLongException:
            print("One of the player names is too long")
            sys.exit(-3)
    if args.luc:
        save_data[save_index].data.value.luc = args.luc
    save.write_save_stream(args.file, save_data)
    args.file.close()
    sys.exit(0)


if __name__ == "__main__":
    main()
