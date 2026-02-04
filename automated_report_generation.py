# -----------------------------
# AUTOMATED REPORT GENERATION
# -----------------------------

# Sample data (can be replaced with file/API data)
students = [
    {"name": "Amit", "marks": [78, 85, 90]},
    {"name": "Sneha", "marks": [88, 92, 81]},
    {"name": "Rahul", "marks": [65, 70, 72]},
    {"name": "Priya", "marks": [95, 91, 89]}
]

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

# Create report file
with open("report.txt", "w") as file:
    file.write("AUTOMATED STUDENT PERFORMANCE REPORT\n")
    file.write("=" * 40 + "\n\n")

    for student in students:
        total = sum(student["marks"])
        average = total / len(student["marks"])
        grade = calculate_grade(average)

        file.write(f"Name      : {student['name']}\n")
        file.write(f"Marks    : {student['marks']}\n")
        file.write(f"Total    : {total}\n")
        file.write(f"Average  : {average:.2f}\n")
        file.write(f"Grade    : {grade}\n")
        file.write("-" * 40 + "\n")

print("✅ Report generated successfully as 'report.txt'")
