import json
import re
from collections import Counter
from pathlib import Path


ACCESS_LOG = Path("/app/access.log")
REPORT = Path("/app/report.json")
REQUEST_PATTERN = re.compile(
    r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH|OPTIONS)\s+(\S+)\s+HTTP/[^\"]+"'
)


def main() -> None:
    paths: Counter[str] = Counter()
    client_ips: set[str] = set()
    total_requests = 0

    for raw_line in ACCESS_LOG.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue

        total_requests += 1
        client_ips.add(line.split()[0])

        request = REQUEST_PATTERN.search(line)
        if request:
            paths[request.group(1)] += 1

    if not paths:
        raise ValueError("No valid HTTP request paths found in /app/access.log")

    report = {
        "total_requests": total_requests,
        "unique_ips": len(client_ips),
        "top_path": paths.most_common(1)[0][0],
    }
    REPORT.write_text(json.dumps(report) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
