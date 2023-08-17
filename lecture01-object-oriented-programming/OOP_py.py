class Employee:
    def __init__(self, name, id): #생성자
        self.name = name
        self.id = id

    def print_details(self):
        print(f"Name: {self.name}, ID: {self.id}")

class Manager(Employee):
    def __init__(self, name, id, department): # 생성자
        super().__init__(name, id)
        self.department = department

    def print_details(self):
        super().print_details()
        print(f"Department: {self.department}")

class EmployeeTable:
    def __init__(self):
        self.employees = []
    def add_employee(self, employee):
        self.employees.append(employee)

    def print_table(self):
        print("Employee Table:")
        for employee in self.employees:
            employee.print_details()

# Main 코드
if __name__ == "__main__":
    table = EmployeeTable()

    emp1 = Employee("John Doe", 1001)
    mgr1 = Manager("Jane Smith", 2001, "HR")

    table.add_employee(emp1)
    table.add_employee(mgr1)

    table.print_table()
