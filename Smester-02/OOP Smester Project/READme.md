# 📚 Library Management System – OOP Semester Project

## 📌 Project Overview

This project is a **Library Management System** developed using C++ as a semester project for the subject **Object-Oriented Programming (OOP)**.

The application is a console-based, menu-driven system designed to manage library books and their availability. It allows users to add, display, search, issue, return, and delete books.

The main focus of this project is to understand and implement the core principles of Object-Oriented Programming through a practical real-world application.

## 🎯 Project Objectives

- Apply object-oriented programming concepts using C++.
- Understand the relationship between classes and objects.
- Implement encapsulation, inheritance, and polymorphism.
- Manage book records through a structured class-based system.
- Develop a menu-driven application with input validation.

## 🛠️ Technologies Used

- **Programming Language:** C++
- **IDE:** Visual Studio
- **Programming Paradigm:** Object-Oriented Programming

## ✨ System Features

The system provides six main operations:

1. **Add Book:** Add new books with automatically generated unique IDs.
2. **Display All Books:** View the available book records.
3. **Search Book:** Find a book using its Book ID.
4. **Issue Book:** Issue a book and update its available quantity.
5. **Return Book:** Return an issued book and update its stock.
6. **Delete Book:** Remove a book record from the system.

## 🧠 OOP Concepts Implemented

### 1. Classes and Objects
Three classes are used to organize the system:

- `LibraryItem`
- `Book`
- `LibraryManager`

### 2. Encapsulation
Data members are protected from direct external access through private and protected access specifiers. Getter and setter methods are used to access and validate data.

### 3. Inheritance
The `Book` class inherits from the abstract base class `LibraryItem`, allowing it to reuse common attributes and functionality.

### 4. Polymorphism
Virtual functions are declared in `LibraryItem` and overridden in `Book` to demonstrate runtime polymorphism.

### 5. Constructors
Default and parameterized constructors are used to initialize objects with appropriate values.

## 📂 Project Structure

```text
Library-Management-System/
│
├── OOP_Project/
│   ├── main.cpp
│   ├── OOP_Project.vcxproj
│   └── OOP_Project.vcxproj.filters
│
├── OOP_Project.slnx
└── README.md
```

## ▶️ How to Run the Project

1. Download or clone the repository.
2. Open `OOP_Project.slnx` in Visual Studio.
3. Allow Visual Studio to load the project.
4. Build the solution.
5. Run the application to access the main menu.

**Requirement:** Visual Studio with a compatible C++ compiler.

## 📚 Concepts Learned

Through this project, I gained practical experience in:

- Designing class-based applications.
- Implementing inheritance and runtime polymorphism.
- Protecting data through encapsulation.
- Using constructors for object initialization.
- Managing dynamic memory using `new` and `delete`.
- Developing menu-driven console applications.
- Implementing input validation.

## 🚀 Future Improvements

- Add file handling for permanent book record storage.
- Implement sorting by book title or author.
- Add support for additional library item types.
- Develop a graphical user interface.

## 🎓 Academic Information

- **Student:** Umair Shabbir
- **Registration ID:** 2502027
- **University:** Air University Islamabad (Main Campus)
- **Degree:** BS Artificial Intelligence
- **Semester:** 2nd Semester
- **Subject:** Object-Oriented Programming (OOP)
- **Project:** Library Management System

---

*Developed as an academic project to demonstrate the practical implementation of Object-Oriented Programming concepts in C++.*
