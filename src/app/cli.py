from pathlib import Path
from typing import Optional

import typer
from app.__version__ import __version__
from app.enums import DiffType
from app.enums import RuntimeConfig
from app.rich_diff import RichDiff

app = typer.Typer()


def invoke_rich_diff(
    diff_type: DiffType,
    file1: Path,
    file2: Path,
    lines: Optional[int] = 3,
):
    runtime_config = RuntimeConfig(diff_type, file1, file2, lines=lines)
    RichDiff.runtime_config = runtime_config
    RichDiff.run(title="Rich Diff Viewer")


@app.command()
def ndiff(file1: Path, file2: Path):
    invoke_rich_diff(DiffType.ndiff, file1, file2)


@app.command()
def unified_diff(
    file1: Path,
    file2: Path,
    lines: Optional[int] = typer.Argument(3),
):
    invoke_rich_diff(DiffType.unified_diff, file1, file2, lines)


@app.command()
def context_diff(
    file1: Path,
    file2: Path,
    lines: Optional[int] = typer.Argument(3),
):
    invoke_rich_diff(DiffType.context_diff, file1, file2, lines)


@app.command()
def version():
    print(f"rich-diff v{__version__}")


if __name__ == "__main__":
    app()
