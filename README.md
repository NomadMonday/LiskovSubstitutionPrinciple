## Summary
- I created this project as a demonstration of the Liskov Substitution Principle (the L in SOLID).
- It is a recreation of this demonstration by Tim Corey, except rewritten in Python: https://youtu.be/-3UXq2krhyw
- I wanted to create a semi-guided exercise where the objective is known, but the exact solution is not due to language differences. In this way, I could create a more challenging and engaging problem to solve, while also learning how to apply SOLID principles in Python.
- The Begin folder contains the starting point of the code before the principle is applied, and the End folder contains the refactored code after.

## Notes
- Since we are using abstract base classes instead of interfaces in Python, the final model can be simplified using inheritance from the abstract base classes instead of combining an abstract base class with an interface, as in the C# version.
- We can also consolidate the BaseEmployee abstract base class and the IEmployee interface into a single abstract base class in Python (ABCBaseEmployee).
- As an example, in C# we have the Employee class, which inherits from the BaseEmployee abstract base class and implements the IManaged interface like so:
```C#
public class Employee : BaseEmployee, IManaged
{
  public IEmployee Manager { get; set; } = null;
  
  public void AssignManager(IEmployee manager)
  {
    //Simulate other tasks here.
    Manager = manager;
  }
}
```
- But in Python, we can have our ABCManaged abstract base class inherit from ABCBaseEmployee. So the Employee class implementation only needs to inherit from ABCManaged in order to inherit from both:
```Python
class ABCBaseEmployee(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = None

    @abstractmethod
    def calculate_per_hour_rate(self, rank):
        base_amount = 12.5
        self.salary = base_amount + (rank * 2)

class ABCManaged(ABCBaseEmployee):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.manager = None
    
    @abstractmethod
    def assign_manager(self, manager: ABCBaseEmployee):
        pass

class Employee(ABCManaged):
    def calculate_per_hour_rate(self, rank):
        return super().calculate_per_hour_rate(rank)
        
    def assign_manager(self, manager):
        # Simulate doing other tasks here.
        self.manager = manager
```
