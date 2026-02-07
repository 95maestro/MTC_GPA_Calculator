# MTC GPA Calculator

A MTC Branded GPA Calcultor built to help students at **BPDC** manage their academic performance.

## 🚀 Key Features
- **BPDC Specific:** Uses the official 10-point scale (A=10, B=8, etc.).
- **Data Persistence:** Uses a **SQLite database** so your data isn't lost when you refresh the page.
- **Official Branding:** Designed with the **MTC Black Accent** color palette to match the club's identity.

## 🧠 How the Code Works

This application is built using the **Django** framework. It follows a simple "Three-Step" process to handle your data:

### 1. The Storage (The Model)
**Model** is a database table which saves three things everytime a course is being added:
- The **Name** of the course.
- The **Units** (how much the course is worth).
- The **Grade Point** (the value assigned to your letter grade).

### 2. The Logic (The View)
It performs the math (GPA Calculation)
1. Grabs all your courses from the storage.
2. Multiplies each course's **Units** by its **Grade Point**.
3. Divides that total by the **Sum of all Units** to find your CGPA.
4. It also checks your score against the BPDC Handbook to tell you if you are in "Distinction" or "First Division".

### 3. The Interface (The Template)
**HTML and CSS** is used to create a clean and professional dashboard. 
- It uses a **Form** to collect your course info.
- It uses a **Table** to list out everything you've already entered.
- It uses **Conditional Logic** to change the "Status" message based on your current GPA.

## 🛠️ Tech Stack
- **Language:** Python 3.11
- **Framework:** Django
- **Database:** SQLite 
- **Tools:** VS Code & Git 

## ⚙️ How to Run
1. Activate your environment: `.\venv\Scripts\activate`
2. Install requirements: `pip install django`
3. Run the server: `python manage.py runserver`
