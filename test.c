#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_EMPLOYEES 100

struct Employee {
    int id;
    char name[256];
    int age;
    double salary;
};

// Function to add a new employee record
void addEmployee(struct Employee employees[], int *employeeCount) {
    if (*employeeCount >= MAX_EMPLOYEES) {
        printf("Employee database is full. Cannot add more employees.\n");
        return;
    }

    struct Employee newEmployee;
    newEmployee.id = *employeeCount + 1;

    printf("Enter employee name, age, and salary (e.g., John 30 50000.00): ");
    while (1) {
        int inputResult = scanf(" %s %d %lf", newEmployee.name, &newEmployee.age, &newEmployee.salary);

        if (inputResult != 3) {
            printf("Invalid input. Please try again: ");
            while (getchar() != '\n'); // Clear input buffer
            continue;
        }

        break;
    }

    employees[*employeeCount] = newEmployee;
    (*employeeCount)++;
    printf("Employee added successfully!\n");
}

// Function to display all employee records
void displayEmployees(struct Employee employees[], int employeeCount) {
    printf("Employee List:\n");
    for (int i = 0; i < employeeCount; i++) {
        printf("ID: %d\n", employees[i].id);
        printf("Name: %s\n", employees[i].name);
        printf("Age: %d\n", employees[i].age);
        printf("Salary: %.2lf\n", employees[i].salary);
        printf("----------------------------\n");
    }
}

// Function to search for an employee by ID
void searchEmployee(struct Employee employees[], int employeeCount) {
    int searchId;
    printf("Enter the ID of the employee to search for: ");
    while (1) {
        int inputResult = scanf("%d", &searchId);

        if (inputResult != 1) {
            printf("Invalid input. Please enter a valid ID: ");
            while (getchar() != '\n'); // Clear input buffer
            continue;
        }

        break;
    }

    int found = 0;
    for (int i = 0; i < employeeCount; i++) {
        if (employees[i].id == searchId) {
            printf("Employee Found:\n");
            printf("ID: %d\n", employees[i].id);
            printf("Name: %s\n", employees[i].name);
            printf("Age: %d\n", employees[i].age);
            printf("Salary: %.2lf\n", employees[i].salary);
            found = 1;
            break;
        }
    }

    if (!found) {
        printf("Employee with ID %d not found.\n", searchId);
    }
}

// Function to calculate and display the average salary of all employees
void calculateAverageSalary(struct Employee employees[], int employeeCount) {
    if (employeeCount == 0) {
        printf("No employees in the database.\n");
        return;
    }

    double totalSalary = 0.0;
    for (int i = 0; i < employeeCount; i++) {
        totalSalary += employees[i].salary;
    }

    double averageSalary = totalSalary / employeeCount;
    printf("Average Salary of Employees: %.2lf\n", averageSalary);
}

int main() {
    struct Employee employees[MAX_EMPLOYEES];
    int employeeCount = 0;
    int choice;

    while (1) {
        printf("\nEmployee Management System Menu:\n");
        printf("1. Add Employee\n");
        printf("2. Display Employees\n");
        printf("3. Search Employee\n");
        printf("4. Calculate Average Salary\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        while (1) {
            int inputResult = scanf("%d", &choice);

            if (inputResult != 1) {
                printf("Invalid input. Please enter a valid choice: ");
                while (getchar() != '\n'); // Clear input buffer
                continue;
            }

            if (choice < 1 || choice > 5) {
                printf("Invalid choice. Please enter a valid choice: ");
                continue;
            }

            break;
        }

        switch (choice) {
            case 1:
                addEmployee(employees, &employeeCount);
                break;
            case 2:
                displayEmployees(employees, employeeCount);
                break;
            case 3:
                searchEmployee(employees, employeeCount);
                break;
            case 4:
                calculateAverageSalary(employees, employeeCount);
                break;
            case 5:
                printf("Exiting the Employee Management System. Goodbye!\n");
                exit(0);
        }
    }

    return 0;
}
