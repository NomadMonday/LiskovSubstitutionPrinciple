from abc import ABC, abstractmethod

class ABCEmployee(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = None

    @abstractmethod
    def calculate_per_hour_rate(self, rank):
        pass
