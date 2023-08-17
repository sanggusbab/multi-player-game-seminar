#ifndef EMPLOYEE_TABLE_H
#define EMPLOYEE_TABLE_H

#include <vector>
#include "employee.h"

class EmployeeTable {
public:
    void addEmployee(Employee* employee);
    void printTable() const;

private:
    std::vector<Employee*> employees;
};

#endif // EMPLOYEE_TABLE_H
