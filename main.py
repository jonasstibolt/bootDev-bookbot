from stats import analyze
import sys

    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    analyze(sys.argv[1])
