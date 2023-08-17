#include "employee.h"
#include <iostream>

Employee::Employee(const std::string& name, int id) // 생성자
    : name(name), id(id) {}

std::string Employee::getName() const {
    return name;
}

int Employee::getId() const {
    return id;
}

void Employee::printDetails() const {
    std::cout << "Name: " << name << ", ID: " << id;
}

Manager::Manager(const std::string& name, int id, const std::string& department)
    : Employee(name, id), department(department) {} //셍상지

void Manager::printDetails() const {
    Employee::printDetails();
    std::cout << ", Department: " << department;
}
