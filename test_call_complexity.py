import ast
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "sample_repository"))

from sample_repository.main import main_function


def test_call_complexity(solution):
    expected = len(
        list(
            ast.walk(
                ast.parse(Path("sample_repository/expected_bundle.py").read_text())
            )
        )
    )
    actual = solution(main_function, "sample_repository")
    assert actual == expected, f"Expected {expected}, got {actual}"
