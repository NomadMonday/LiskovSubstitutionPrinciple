from abc_manager import ABCManager
from abc_base_employee import ABCBaseEmployee

class CEO(ABCBaseEmployee, ABCManager):
    def calculate_per_hour_rate(self, rank):
        base_amount = 150
        self.salary = base_amount * rank

    def generate_performance_review(self):
        # Simulate reviewing a direct report.
        print("I'm reviewing a direct report's performance.")

    def fire_someone(self):
        # Simulate firing someone.
        print("You're fired!")
