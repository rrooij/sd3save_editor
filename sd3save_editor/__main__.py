#!/usr/bin/env python3

import argparse
import sys
import sd3save_editor.save as save


def main():
    parser = argparse.ArgumentParser(description="Edit a Seiken Densetsu 3 save file")
    parser.add_argument("file", type=argparse.FileType("r+b"), help="The Seiken3 save (srm format)")
    parser.add_argument("--location", type=int, help="ID of the in-game location")

    args = parser.parse_args()
    save_data = save.save_format.parse(args.file.read())
    if save_data[0] is False:
        print("Please choose a valid Seiken3 save file")
        parser.print_help()
        sys.exit(-1)
    if (args.location):
        save_data[0].data.value.location = args.location
        save.write_save_stream(args.file, save_data)
    args.file.close()
    sys.exit(0)

if __name__ == "__main__":
    main()
