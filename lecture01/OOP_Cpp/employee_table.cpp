#include "employee_table.h"
#include <iostream>

void EmployeeTable::addEmployee(Employee* employee) {
    employees.push_back(employee);
}

void EmployeeTable::printTable() const {
    std::cout << "Employee Table:" << std::endl;
    for (const Employee* employee : employees) {
        employee->printDetails();
        std::cout << std::endl;
    }
}
