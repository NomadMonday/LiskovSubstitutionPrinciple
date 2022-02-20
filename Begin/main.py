from ceo import CEO
from employee import Employee
from manager import Manager

def main():
    accountingVP = Manager("Emma", "Stone")
    accountingVP.calculate_per_hour_rate(4)

    emp = Employee("Tim", "Corey")
    emp.assign_manager(accountingVP)
    emp.calculate_per_hour_rate(2)

    input(f"{emp.first_name}'s salary is ${emp.salary}/hour.")

if __name__ == "__main__":
    main()
