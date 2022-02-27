from abc_managed import ABCManaged

class Employee(ABCManaged):
    def calculate_per_hour_rate(self, rank):
        return super().calculate_per_hour_rate(rank)
        
    def assign_manager(self, manager):
        # Simulate doing other tasks here.
        self.manager = manager
