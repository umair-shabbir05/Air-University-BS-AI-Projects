# 🎓 AI-Based GPA Prediction & Performance Analysis System

## 📌 Project Overview

This project is an **AI-Based GPA Prediction and Performance Analysis System** developed as a semester project for the subject **Programming for AI**.

It is a Python-based command-line application designed to calculate students' GPA, analyze academic performance, and provide personalized suggestions based on their marks.

The system collects student information, subjects, marks, and credit hours, then processes the data to generate a detailed academic performance report.

It uses NumPy for numerical calculations, Pandas for tabular output, and Matplotlib for data visualization. A rule-based AI classifier is also implemented to categorize student performance.

## 🎯 Project Objectives

- Develop an interactive Python application for GPA calculation.
- Implement a grading system that converts marks into letter grades and GPA points.
- Calculate weighted GPA using NumPy.
- Classify academic performance into different categories.
- Generate personalized suggestions for weak subjects.
- Perform statistical analysis of student marks.
- Generate graphical representations of academic performance.
- Save student performance reports in a text file.

## 🛠️ Technologies and Libraries Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| NumPy | Numerical calculations and array operations |
| Pandas | Grade-card generation and tabular output |
| Matplotlib | Data visualization and performance charts |
| datetime | Report date and timestamp generation |

## ✨ System Features

### 1. Student Information Input
- Collects student name and subject information.
- Accepts marks between 0 and 100.
- Accepts credit hours between 1 and 4.
- Validates user input to prevent invalid entries.

### 2. Automatic Grade Calculation
- Converts marks into letter grades.
- Assigns corresponding GPA points.
- Generates a subject-wise grade card.

### 3. Weighted GPA Calculation

The system calculates GPA using the weighted average formula:

GPA = Σ(Grade Points × Credit Hours) / Σ(Credit Hours)

NumPy's `np.dot()` and `np.sum()` functions are used to perform the calculation.

### 4. AI-Based Performance Classification

A rule-based classifier evaluates the calculated GPA and assigns one of four performance categories:

| GPA Range | Performance Category |
|---|---|
| 3.50 – 4.00 | Excellent |
| 2.50 – 3.49 | Good |
| 1.50 – 2.49 | Average |
| 0.00 – 1.49 | Weak |

The classifier also generates remarks according to the student's performance.

### 5. Intelligent Suggestion System

- Identifies subjects with marks below 60.
- Generates suggestions based on the student's marks.
- Provides different recommendations for failing and below-passing subjects.
- Displays encouraging feedback when no weak subjects are identified.

### 6. Statistical Performance Analysis

The system calculates:

- Highest marks.
- Lowest marks.
- Average marks.
- Standard deviation.
- Best-performing subject.
- Weakest subject.
- Number of subjects above 75 marks.
- Number of subjects below 60 marks.

### 7. Data Visualization

Using Matplotlib, the system generates:

- Subject-wise marks bar chart.
- Color-coded performance indicators.
- GPA performance zone chart.
- Visual representation of academic results.

### 8. Report Generation

- Displays a formatted academic report in the terminal.
- Saves the complete report in a `.txt` file.
- Generates and saves performance charts in PNG format.

## 🧠 AI and Programming Concepts Implemented

- Python functions and modular programming.
- Input validation and exception handling.
- NumPy arrays and numerical operations.
- Weighted GPA calculation using dot products.
- Rule-based classification using conditional statements.
- Statistical data analysis.
- Pandas DataFrames.
- Data visualization using Matplotlib.
- File handling and report generation.

**Note:** The performance classifier uses predefined GPA thresholds and conditional rules. It is a rule-based intelligent system, not a trained machine learning model.

## 📂 Project Structure

```text
Programming-for-AI-Project/
│
├── main.py
├── AI Smester Project Report.pdf
├── Umair_Shabbir_performance_chart.png
├── Umair_Shabbir_result.txt
└── README.md
```

## ▶️ How to Run the Project

1. Download or clone the repository.
2. Make sure Python is installed on your computer.
3. Open the project folder in VS Code or PyCharm.
4. Install the required libraries:

```bash
pip install numpy pandas matplotlib
```

5. Run the Python program:

```bash
python main.py
```

6. Enter the student information, subject names, marks, and credit hours.
7. View the generated GPA report and performance analysis.

## 📚 Concepts Learned

Through this project, I gained practical experience in:

- Developing modular Python applications.
- Working with NumPy for numerical computation.
- Using Pandas for structured data presentation.
- Performing statistical analysis.
- Implementing rule-based AI classification.
- Applying input validation and exception handling.
- Creating charts and visualizing data.
- Generating and saving reports using Python file handling.

## 🚀 Future Improvements

- Integrate a machine learning model for performance prediction.
- Add CGPA calculation across multiple semesters.
- Develop a graphical user interface using Tkinter or PyQt.
- Create a web-based academic performance dashboard.
- Add PDF and Excel report generation.
- Track and compare academic performance across semesters.

## 🎓 Academic Information

- **Students:** Umair Shabbir, Sayyed Abu Bakkar Khan, Musa Khan
- **Registration ID:** 2502027, 2502039, 2502067
- **University:** Air University Islamabad
- **Degree:** BS Artificial Intelligence
- **Semester:** 2nd Semester
- **Subject:** Programming for AI
- **Instructor:** Sir Wasim Wahid
- **Project:** AI-Based GPA Prediction & Performance Analysis System

---

*Developed as an academic project to explore Python programming, numerical computing, data analysis, visualization, and rule-based intelligent decision-making.*
