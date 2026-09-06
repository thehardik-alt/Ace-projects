import csv

def get_grade(marks):
    """Assigns a letter grade based on marks."""
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    elif marks >= 40:
        return "E"
    else:
        return "F"

def collect_student_data():
    """Collects student names and marks from user input."""
    students = []
    print("--- Student Data Entry (Type 'done' as name to finish) ---")
    while True:
        name = input("Enter student name: ").strip()
        if name.lower() == 'done':
            if not students:
                print("Please enter at least one student.")
                continue
            break
        if not name:
            print("Name cannot be blank.")
            continue

        while True:
            try:
                marks_input = float(input(f"Enter marks for {name} (0-100): "))
                if 0 <= marks_input <= 100:
                    students.append({
                        "name": name,
                        "marks": marks_input,
                        "grade": get_grade(marks_input)
                    })
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    return students

def analyze_class(students, passing_mark=40):
    """Computes statistical metrics for the class."""
    marks_list = [s["marks"] for s in students]
    total_students = len(students)
    
    avg_marks = sum(marks_list) / total_students
    highest_student = max(students, key=lambda s: s["marks"])
    lowest_student = min(students, key=lambda s: s["marks"])
    
    passed_count = sum(1 for s in students if s["marks"] >= passing_mark)
    failed_count = total_students - passed_count
    pass_pct = (passed_count / total_students) * 100

    return {
        "average": avg_marks,
        "highest": highest_student,
        "lowest": lowest_student,
        "passed": passed_count,
        "failed": failed_count,
        "pass_percentage": pass_pct,
        "total_students": total_students
    }

def print_report(students, analysis):
    """Prints the formatted analysis report to the console."""
    print("\n" + "=" * 45)
    print(f"{'Name':<20}{'Marks':<12}{'Grade':<8}")
    print("-" * 45)
    for s in students:
        print(f"{s['name']:<20}{s['marks']:<12.2f}{s['grade']:<8}")
    print("=" * 45)
    print(f"Total Students   : {analysis['total_students']}")
    print(f"Class Average    : {analysis['average']:.2f}")
    print(f"Highest Scorer   : {analysis['highest']['name']} ({analysis['highest']['marks']:.2f})")
    print(f"Lowest Scorer    : {analysis['lowest']['name']} ({analysis['lowest']['marks']:.2f})")
    print(f"Passed           : {analysis['passed']}")
    print(f"Failed           : {analysis['failed']}")
    print(f"Pass Percentage  : {analysis['pass_percentage']:.2f}%")
    print("=" * 45 + "\n")

def export_to_txt(students, analysis, filename="class_report.txt"):
    """Saves the student list and analysis summary to a text file."""
    with open(filename, "w") as f:
        f.write("CLASS PERFORMANCE REPORT\n")
        f.write("=" * 45 + "\n")
        f.write(f"{'Name':<20}{'Marks':<12}{'Grade':<8}\n")
        f.write("-" * 45 + "\n")
        for s in students:
            f.write(f"{s['name']:<20}{s['marks']:<12.2f}{s['grade']:<8}\n")
        f.write("=" * 45 + "\n")
        f.write(f"Class Average   : {analysis['average']:.2f}\n")
        f.write(f"Highest Scorer  : {analysis['highest']['name']} ({analysis['highest']['marks']:.2f})\n")
        f.write(f"Lowest Scorer   : {analysis['lowest']['name']} ({analysis['lowest']['marks']:.2f})\n")
        f.write(f"Passed / Failed : {analysis['passed']} / {analysis['failed']}\n")
        f.write(f"Pass Percentage : {analysis['pass_percentage']:.2f}%\n")
    print(f"Saved: {filename}")

def export_to_csv(students, filename="class_report.csv"):
    """Saves tabular student data to a CSV file."""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Marks", "Grade"])
        for s in students:
            writer.writerow([s["name"], s["marks"], s["grade"]])
    print(f"Saved: {filename}")

def export_to_pdf(students, analysis, filename="class_report.pdf"):
    """
    Generates a PDF report using pure standard-library PostScript/PDF formatting,
    requiring no external packages like reportlab or fpdf.
    """
    lines = [
        "CLASS PERFORMANCE REPORT",
        "--------------------------------------------------",
        f"{'Name':<25}{'Marks':<15}{'Grade':<10}",
        "--------------------------------------------------"
    ]
    for s in students:
        lines.append(f"{s['name']:<25}{s['marks']:<15.2f}{s['grade']:<10}")
    lines.extend([
        "--------------------------------------------------",
        f"Class Average   : {analysis['average']:.2f}",
        f"Highest Scorer  : {analysis['highest']['name']} ({analysis['highest']['marks']:.2f})",
        f"Lowest Scorer   : {analysis['lowest']['name']} ({analysis['lowest']['marks']:.2f})",
        f"Passed / Failed : {analysis['passed']} / {analysis['failed']}",
        f"Pass Percentage : {analysis['pass_percentage']:.2f}%"
    ])

    stream_content = "BT\n/F1 11 Tf\n14 TL\n50 750 Td\n"
    for line in lines:
        escaped_line = line.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
        stream_content += f"({escaped_line}) '\n"
    stream_content += "ET"

    stream_bytes = stream_content.encode("latin-1")
    length = len(stream_bytes)

    objects = [
        b"%PDF-1.4\n",
        b"1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n",
        b"2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n",
        b"3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>\nendobj\n",
        f"4 0 obj\n<< /Length {length} >>\nstream\n".encode("latin-1") + stream_bytes + b"\nendstream\nendobj\n",
        b"5 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Courier >>\nendobj\n"
    ]

    with open(filename, "wb") as f:
        xref_offsets = []
        offset = 0
        for obj in objects:
            if obj.startswith(b"%PDF"):
                f.write(obj)
                offset += len(obj)
            else:
                xref_offsets.append(offset)
                f.write(obj)
                offset += len(obj)
        
        xref_pos = offset
        f.write(f"xref\n0 {len(xref_offsets) + 1}\n0000000000 65535 f \n".encode("latin-1"))
        for off in xref_offsets:
            f.write(f"{off:010d} 00000 n \n".encode("latin-1"))
        f.write(f"trailer\n<< /Size {len(xref_offsets) + 1} /Root 1 0 R >>\nstartxref\n{xref_pos}\n%%EOF".encode("latin-1"))

    print(f"Saved: {filename}")

def main():
    students = collect_student_data()
    analysis = analyze_class(students)
    print_report(students, analysis)
    
    export_to_txt(students, analysis)
    export_to_csv(students)
    export_to_pdf(students, analysis)

if __name__ == "__main__":
    main()
