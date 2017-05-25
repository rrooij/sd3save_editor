import argparse
import sys
import sd3save_editor.save as save


def main():
    parser = argparse.ArgumentParser(description="Edit a Seiken Densetsu 3 save file")
    parser.add_argument("file", type=argparse.FileType("r+b"), help="The Seiken3 save (srm format)")
    parser.add_argument("--location", type=int, help="ID of the in-game location")

    args = parser.parse_args()

    if not save.check_valid_save(args.file):
        print("Please choose a valid Seiken3 save file")
        parser.print_help()
        sys.exit(-1)

    if (args.location):
        save.change_location(args.file, args.location)

    save.close_save(args.file)

if __name__ == "__main__":
    main()
