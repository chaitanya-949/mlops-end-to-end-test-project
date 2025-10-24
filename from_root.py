import os

"""Utility to return the project root directory.

This module provides a single function `from_root()` which returns the absolute
path to the repository root (the directory containing this file). It's used by
`src/logger/__init__.py` via the import `from from_root import from_root`.
"""


def from_root() -> str:
    """Return the absolute path of the project root (directory of this file).

    Returns:
        str: Absolute path to the project root.
    """
    return os.path.dirname(os.path.abspath(__file__))
