"""
Sometimes you have got an insight, that's the idea
"""

from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class Idea:
    title: str   # name of the project
    description: str  # project description with details
