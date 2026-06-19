import json


def parse_record(line: str) -> tuple[str, int]:
    """Read a JSON access record or raise ValueError for invalid input."""
    record = json.loads(line)
    if not isinstance(record, dict):
        raise ValueError("expected a JSON object")
    path = record.get("path")
    status = record.get("status")
    if not isinstance(path, str) or not path.startswith("/"):
        raise ValueError("expected an absolute request path")
    if type(status) is not int or not 100 <= status <= 599:
        raise ValueError("invalid HTTP status")
    return path, status
