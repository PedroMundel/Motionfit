from enum import Enum
from datetime import datetime

class EducationLevel(Enum):
    GRADUACAO = "Graduação" #graduation"
    POS_GRADUACAO = "Pós-Graduação" #postgraduate
    MESTRADO = "Mestrado" #master's degree
    DOUTORADO = "Doutorado" # doctorate degree

class Certificate:
    def __init__(self, id, institution, admission_year, completion_year, education_level):
        self.id = id
        self.institution = institution
        self.admission_year = datetime.strptime(admission_year, "%Y")
        self.completion_year = datetime.strptime(completion_year, "%Y")
        self.education_level = EducationLevel(education_level)
