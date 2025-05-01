#import argparse
from excel_handler import ExcelHandler

if __name__ == "__main__":
    #parser = argparse.ArgumentParser(description="Process Excel file")
    #parser.add_argument("filepath", help="Path to the Excel file")
    #args = parser.parse_args()

    excel_file_path = "students-file.xlsx"  # Update with your Excel file path
    #excel = ExcelHandler(args.filepath)
    excel = ExcelHandler(excel_file_path)

    print(f"\nGetting info from existing file: {excel_file_path}")
    list_of_students = excel.get_excel_file_data()
    print(list_of_students)

    print("\nCreating new file...")
    excel.process_file(list_of_students)
