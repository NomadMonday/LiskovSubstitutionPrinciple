from abc_employee import ABCEmployee

class ABCBaseEmployee(ABCEmployee):
    def calculate_per_hour_rate(self, rank):
        base_amount = 12.5
        self.salary = base_amount + (rank * 2)
