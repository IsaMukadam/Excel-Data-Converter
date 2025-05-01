# Excel Data Converter

A Python script that converts student class enrollment data from a wide format to a more suitable long format Excel file.

## Features

- Reads student data from an Excel file (.xlsx)
- Processes multiple classes per student
- Converts wide format (one row per student with multiple class columns) to long format (one row per student-class combination)
- Creates a new organized Excel file with simplified structure

## Technologies Used

- Python 3.x
- Libraries:
  - openpyxl (Excel file handling)
  - pydantic (data validation and model creation)
  - cx_Freeze (for executable creation)

## Input Format
The script expects an Excel file with:
- Student names in column A
- Class year in column B
- Class entries in columns D through U

## Output Format
Generates a new Excel file with:
- Column A: Student Name
- Column B: Class Name

Each row represents a single student-class combination, making the data more suitable for analysis and processing.

## Usage

```bash
python main.py
```

The script will process the "students-file.xlsx" and output "processed_file.xlsx" with the converted data format.