import openpyxl

def analyze_student_marks(file_path):
    """
    Reads student records from Excel and returns counts of students scoring > 60:
    - in at least one subject
    - in all subjects
    """
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active

    count_any_subject = 0
    count_all_subjects = 0

    # Iterate through data rows (skipping header at row 1)
    for row in sheet.iter_rows(min_row=2, values_only=True):
        if not row or row[0] is None:
            continue

        # Extract marks for Java, Python, DBMS
        marks = [row[2], row[3], row[4]]

        # Condition 1: Scored > 60 in AT LEAST ONE subject
        if any(mark > 60 for mark in marks):
            count_any_subject += 1

        # Condition 2: Scored > 60 in ALL subjects
        if all(mark > 60 for mark in marks):
            count_all_subjects += 1

    wb.close()
    return count_any_subject, count_all_subjects


if __name__ == "__main__":
    any_count, all_count = analyze_student_marks("students.xlsx")
    print(f"Students with > 60 in ANY one subject: {any_count}")
    print(f"Students with > 60 in ALL subjects: {all_count}")
