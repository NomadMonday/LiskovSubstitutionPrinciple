from employee import Employee

class CEO(Employee):
    def calculate_per_hour_rate(self, rank):
        base_amount = 150
        self.salary = base_amount * rank

    def assign_manager(self, manager):
        raise Exception("The CEO has no manager.")

    def generate_performance_review(self):
        # Simulate reviewing a direct report.
        print("I'm reviewing a direct report's performance.")

    def fire_someone(self):
        # Simulate firing someone.
        print("You're fired!")
