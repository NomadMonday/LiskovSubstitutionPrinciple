from employee import Employee

class Manager(Employee):
    def calculate_per_hour_rate(self, rank):
        base_amount = 19.75
        self.salary = base_amount + (rank * 4)

    def generage_performance_review(self):
        # Simulate reviewing a direct report.
        print("I'm reviewing a direct report's performance.")
