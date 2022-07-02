from abc_base_employee import ABCBaseEmployee
from abc_managed import ABCManaged

class Employee(ABCManaged):
    def calculate_per_hour_rate(self, rank: int) -> None:
        return super().calculate_per_hour_rate(rank)
        
    def assign_manager(self, manager: ABCBaseEmployee) -> None:
        # Simulate doing other tasks here.
        self.manager = manager
