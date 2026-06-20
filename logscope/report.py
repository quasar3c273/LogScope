from collections import Counter
from collections.abc import Iterable

from .parser import parse_record


def count_errors(lines: Iterable[str]) -> tuple[Counter[str], int]:
    counts: Counter[str] = Counter()
    invalid = 0
    for line in lines:
        try:
            path, status = parse_record(line)
        except ValueError:
            invalid += 1
            continue
        if status >= 500:
            counts[path] += 1
    return counts, invalid
