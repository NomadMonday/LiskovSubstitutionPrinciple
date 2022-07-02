from abc import ABC, abstractmethod

class ABCBaseEmployee(ABC):
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.salary: float = None

    @abstractmethod
    def calculate_per_hour_rate(self, rank: int) -> None:
        base_amount = 12.5
        self.salary = base_amount + (rank * 2)
