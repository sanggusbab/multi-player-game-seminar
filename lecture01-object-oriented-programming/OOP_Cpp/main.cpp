#include "employee.h"
#include "employee_table.h"
#include <iostream>
using namespace std;

int main(int argc, char* argv£Û£Ý)
{
	EmployeeTable table;

	Employee* empl = new Employee("John Doe", 1001);
	Manager* mgr1 = new Manager("Jane Smith", 2001, "HR");

	table.addEmployee(empl);
	table.addEmployee(mgr1);

	table.printTable();
	cout << empl->getName() << endl;
	cout << empl->getName() << endl;
	cout << empl->getName() << endl;
	cout << empl->getName() << endl;
	cout << mgr1->getName() << endl;
	cout << mgr1->getName() << endl;
	cout << mgr1->getName() << endl;
	cout << mgr1->getName() << endl;
	// Clean up memory
	delete empl;
	delete mgr1;

	return 0;
}