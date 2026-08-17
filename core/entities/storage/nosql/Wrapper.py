from typing import Protocol


class Nosql_db_wrapper(Protocol):
    """
    No sql database protocol
    """

    def insert(self) -> None:
        pass

    def update(self) -> None:
        pass

    def delete(self) -> None:
        pass

    def find(self):
        pass
