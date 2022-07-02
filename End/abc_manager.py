from abc import abstractmethod
from tkinter.messagebox import NO
from abc_base_employee import ABCBaseEmployee

class ABCManager(ABCBaseEmployee):
    @abstractmethod
    def generate_performance_review(self) -> None:
        pass
