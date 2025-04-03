<<<<<<< HEAD
# Basic Calculator Program

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user to input a mathematical operation
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation and display the result
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of +, -, *, or /.")
=======
# 📝 Assignment: Data Manipulation and Transactions

## 🎯 **Learning Objectives**
* ➕ Create tables and define the structure of a database.
* ✍️ Insert records into a table.
* 🔄 Modify data in a table through updates.
* 💻 Practice basic SQL operations that are fundamental to database management.

---

## 📋 **What You'll Need**
* 💻 A computer with internet access.
* ✍️ A code editor (e.g., Visual Studio Code).
* 🖥️ MySQL Workbench or another SQL database environment.

---

## 📝 **Submission Instructions**  
📂 Write all your SQL queries in the **answers.sql** file.  
✍️ Answer each question concisely and ensure your queries are clear and correct.  
🗣️ Structure your responses clearly, and use comments if necessary to explain your approach.

---

## 📚 **Assignment Questions**

### **Question 1 🧑‍🎓**  
**Write an SQL statement** to create a table named **student** with the following columns:  
- **id** (an integer and the primary key)  
- **fullName** (a text field with a maximum of 100 characters)  
- **age** (an integer)

---

### **Question 2 ➕**  
**Write an SQL statement** to insert at least 3 records into the **student** table.

---

### **Question 3 🔄**  
**Write an SQL statement** to update the age of the student with ID **2** to **20** in the **student** table.

---

Good luck 🚀
>>>>>>> 30014ed09043fe37d08680cbbace88dff26fb863
