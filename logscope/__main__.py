import argparse
from pathlib import Path

from .report import count_errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Rank paths by HTTP 5xx errors")
    parser.add_argument("file", type=Path)
    parser.add_argument("--top", type=int, default=5)
    args = parser.parse_args()
    if args.top < 1:
        parser.error("--top must be positive")
    try:
        with args.file.open(encoding="utf-8-sig") as lines:
            counts, invalid = count_errors(lines)
    except (OSError, UnicodeError) as exc:
        parser.exit(1, f"{exc}\n")
    for path, count in counts.most_common(args.top):
        print(f"{count}\t{path}")
    print(f"Invalid records: {invalid}")


if __name__ == "__main__":
    main()
