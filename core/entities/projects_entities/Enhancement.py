"""
Some enhancement to existing project
"""
from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class Enhancement:
    description: str
    created_at: str
