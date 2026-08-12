from pathlib import Path


def test_main_script_exists() -> None:
    project_root = Path(__file__).resolve().parents[1]
    assert (project_root / "se_01.py").is_file()
