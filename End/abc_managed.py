from abc import abstractmethod
from abc_base_employee import ABCBaseEmployee

class ABCManaged(ABCBaseEmployee):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.manager: ABCBaseEmployee = None
    
    @abstractmethod
    def assign_manager(self, manager: ABCBaseEmployee) -> None:
        pass
