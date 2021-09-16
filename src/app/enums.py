from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class DiffType(str, Enum):
    ndiff = "ndiff"
    unified_diff = "unified_diff"
    context_diff = "context_diff"


@dataclass(frozen=True)
class RuntimeConfig:
    diff_type: DiffType
    file1: Path
    file2: Path
    lines: int
