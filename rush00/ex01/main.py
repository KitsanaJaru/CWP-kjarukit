import sys
from checkmate import checkmate, print_pretty_board

def main():
    if len(sys.argv) < 2:
        print("Error")
        return

    for filepath in sys.argv[1:]:
        try:
            with open(filepath, 'r') as f:
                board_str = f.read()

            print(f"=== {filepath} ===")
            print_pretty_board(board_str)

            checkmate(board_str)
            print()

        except Exception:
            print("Error")

if __name__ == "__main__":
    main()