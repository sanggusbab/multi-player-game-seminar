#ifndef EMPLOYEE_H
#define EMPLOYEE_H

#include <string>

class Employee {
public:
    Employee(const std::string& name, int id); // »ý¼ºÀÚ

    std::string getName() const;
    int getId() const;
    virtual void printDetails() const;

private:
    std::string name;
    int id;
};

class Manager : public Employee {
public:
    Manager(const std::string& name, int id, const std::string& department);
    void printDetails() const override;

private:
    std::string department;
};

#endif // EMPLOYEE_H
