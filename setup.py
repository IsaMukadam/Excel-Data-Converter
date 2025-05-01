from cx_Freeze import setup, Executable

setup(
    name="ExcelManipulator",
    version="1.0",
    description="Organises Excel Data of students and classes",
    executables=[Executable("main.py")]
)