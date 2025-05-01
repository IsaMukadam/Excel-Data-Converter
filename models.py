from pydantic import BaseModel
from typing import List

class Student(BaseModel):
    student_name: str
    classes: List