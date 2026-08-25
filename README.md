# 🎓 GPA Calculator using Python

A simple and user-friendly **GPA Calculator built with Python** that calculates a student's semester GPA based on course grades and credit hours.

The program takes student information and course details as input, calculates the GPA using a grade-point system, and displays the final result in a clean and organized format.

## ✨ Features

* 👤 Takes student information as input
* 📚 Supports multiple courses
* 📝 Accepts course grades/scores
* 🧮 Calculates GPA based on credit hours
* 🎯 Converts scores into grade points
* 📊 Displays individual course grades and GPA
* 🖥️ Clean and organized terminal output
* 🔢 Handles different credit-hour values

## 🛠️ Technologies Used

* **Python 3**
* Functions
* Lists
* Loops
* Conditional statements
* User input
* Basic calculations
* Formatted string output

## 📂 Project Structure

```text
GPA-Calculator-using-python/
│
├── main.py
├── README.md
└── .gitignore
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/shozzCodes/GPA-Calculator-using-python.git
```

### 2. Navigate to the project directory

```bash
cd GPA-Calculator-using-python
```

### 3. Run the program

```bash
python main.py
```

## 💻 How It Works

The calculator follows a simple process:

```text
Start Program
      ↓
Enter Student Information
      ↓
Enter Number of Courses
      ↓
Enter Course Details
      ↓
Enter Scores / Grades
      ↓
Convert Scores → Grade Points
      ↓
Calculate Weighted GPA
      ↓
Display Results
```

The GPA is calculated using the credit hours of each course, so courses with more credit hours have a greater effect on the final GPA.

### 📐 GPA Formula

The general formula used is:

```text
GPA = Σ(Grade Point × Credit Hours) / Σ(Credit Hours)
```

For example:

```text
Course 1 → Grade Point × Credit Hours
Course 2 → Grade Point × Credit Hours
Course 3 → Grade Point × Credit Hours
                     ↓
              Total Quality Points
                     ÷
              Total Credit Hours
                     ↓
                  Final GPA
```

## 📊 Example

A simplified example:

```text
Student Name: Shozab Ali

Course             Credit Hours    Grade
------------------------------------------
Programming            3             A
Database               3             B+
Mathematics            3             A-
English                2             B

------------------------------------------
Semester GPA: 3.45
```

*The actual GPA depends on the grading scale and values implemented in the program.*

## 🧠 What I Learned

This project helped me practice several important Python concepts:

* Defining and calling functions
* Passing arguments to functions
* Using return values
* Working with variables and data types
* Using `if`, `elif`, and `else`
* Using `for` loops
* Taking and validating user input
* Performing calculations
* Formatting terminal output
* Organizing a Python program into functions
* Using Git and GitHub for version control

## 🔮 Future Improvements

Possible improvements for future versions:

* Add support for different grading scales
* Add input validation for invalid scores
* Support multiple semesters
* Calculate CGPA
* Save student results to a file
* Export results as PDF
* Add a graphical user interface
* Store course information using JSON
* Add automated tests
* Improve the user interface

## 👨‍💻 Author

**Shozab Ali**

GitHub: [@shozzCodes](https://github.com/shozzCodes)

---

⭐ If you find this project useful, consider giving the repository a star!
