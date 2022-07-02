from abc_manager import ABCManager
from employee import Employee

class Manager(Employee, ABCManager):
    def calculate_per_hour_rate(self, rank: int) -> None:
        base_amount = 19.75
        self.salary = base_amount + (rank * 4)

    def generate_performance_review(self) -> None:
        # Simulate reviewing a direct report.
        print("I'm reviewing a direct report's performance.")
