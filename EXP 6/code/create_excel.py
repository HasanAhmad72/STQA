import openpyxl


def generate_sample_data(file_path="students.xlsx"):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "StudentRecords"

    # Header Row
    ws.append(["Roll No", "Name", "Java", "Python", "DBMS"])

    # Sample Dataset from Experiment Sheet
    data = [
        [101, "Amit", 75, 68, 80],
        [102, "Neha", 58, 62, 55],
        [103, "Raj", 45, 52, 61],
        [104, "Sneha", 85, 72, 91],
        [105, "Ajay", 59, 57, 60],
        [106, "Pooja", 65, 48, 55],
        [107, "Rohan", 61, 66, 64],
        [108, "Anita", 39, 45, 50],
        [109, "Kiran", 70, 75, 80],
        [110, "Priya", 60, 59, 58]
    ]

    for row in data:
        ws.append(row)

    wb.save(file_path)
    print(f"File '{file_path}' created successfully!")


if __name__ == "__main__":
    generate_sample_data()
