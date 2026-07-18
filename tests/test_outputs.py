import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")


def load_report() -> object:
    return json.loads(REPORT_PATH.read_text(encoding="utf-8"))


def test_success_criterion_1_valid_json_object() -> None:
    """Success criterion 1: report.json exists and is a valid JSON object."""
    assert REPORT_PATH.is_file(), "Expected /app/report.json to exist"
    try:
        report = load_report()
    except json.JSONDecodeError as exc:
        raise AssertionError("report.json is not valid JSON") from exc
    assert isinstance(report, dict), "report.json must contain a JSON object"


def test_success_criterion_2_exact_schema_and_types() -> None:
    """Success criterion 2: the report has exactly the required keys and types."""
    report = load_report()
    assert isinstance(report, dict)
    assert set(report) == {"total_requests", "unique_ips", "top_path"}
    assert type(report["total_requests"]) is int
    assert type(report["unique_ips"]) is int
    assert type(report["top_path"]) is str


def test_success_criterion_3_total_requests() -> None:
    """Success criterion 3: total_requests equals the number of non-empty lines."""
    report = load_report()
    assert report["total_requests"] == 6


def test_success_criterion_4_unique_ips() -> None:
    """Success criterion 4: unique_ips equals the number of distinct client IPs."""
    report = load_report()
    assert report["unique_ips"] == 3


def test_success_criterion_5_top_path() -> None:
    """Success criterion 5: top_path is the most frequently requested path."""
    report = load_report()
    assert report["top_path"] == "/index.html"
