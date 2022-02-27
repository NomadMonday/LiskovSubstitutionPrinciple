from abc_managed import ABCManaged
from abc_base_employee import ABCBaseEmployee

class Employee(ABCBaseEmployee, ABCManaged):
    def assign_manager(self, manager):
        # Simulate doing other tasks here.
        self.manager = manager
