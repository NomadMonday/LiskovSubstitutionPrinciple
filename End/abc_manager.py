from abc import abstractmethod
from abc_employee import ABCEmployee

class ABCManager(ABCEmployee):
    @abstractmethod
    def generate_performance_review(self):
        pass
