class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.manager = None
        self.salary = None
    
    def assign_manager(self, manager):
        # Simulate doing other tasks here.
        self.manager = manager

    def calculate_per_hour_rate(self, rank):
        base_amount = 12.5
        self.salary = base_amount + (rank * 2)
