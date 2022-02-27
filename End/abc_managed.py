from abc import abstractmethod
from abc_employee import ABCEmployee

class ABCManaged(ABCEmployee):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.manager = None
    
    @abstractmethod
    def assign_manager(self, manager: ABCEmployee):
        pass
