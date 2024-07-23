from pydantic import BaseModel, ValidationError, field_validator, EmailStr
from pydantic_core.core_schema import FieldValidationInfo
import pandas as pd
from datetime import datetime
import re

class personal_information(BaseModel):
    # employee_id: int
    first_name: str
    last_name: str
    email: EmailStr
    cnp: int
    gender: str

    @field_validator('email')
    def validate_email(cls, email, info: FieldValidationInfo):
        first_name = info.data['first_name']
        last_name = info.data['last_name']
        expected_format = f"{first_name.lower()}.{last_name.lower()}@company.com"
        if email != expected_format:
            raise ValueError('Email must be in the format first.last@company.com with lowercase')
        return email
    
    
    def job_workload(cls, value, info: FieldValidationInfo):
        if info.data['job_role'] and value <= 50:
            raise ValueError(f"{info.data['name']} does not have enough workload")
    
    @field_validator('cnp')
    def validate_identifier(cls, cnp, info:FieldValidationInfo):
        if not re.match(r'^[1256]\d{9}$', cnp):
            raise ValueError('Identifier must start with 1, 2, 5, or 6 and have 10 digits')

        gender_indicator = cnp[0]

        gender_from_cnp = 'male' if gender_indicator in '15' else 'female'
        if 'gender' in cnp and cls.gender != gender_from_cnp:
            raise ValueError(f'Gender from CNP ({gender_from_cnp}) does not match provided gender ({info.data['gender']})')

        cnp_year = int(cnp[1:3])
        current_year = datetime.now().year
        if cnp[0] in '12':
            birth_year = 1900 + cnp_year
        elif cnp[0] in '56':
            birth_year = 2000 + cnp_year

        if birth_year > current_year:
             raise ValueError(f'Extracted year from CNP ({birth_year}) cannot be greater than the current year ({current_year})')

        return cnp
        

def load_data_from_csv(csv_file: str) -> list[str]:
    df = pd.read_csv(csv_file)
    instances = []

    for _, row in df.iterrows():
        try:
            instance = personal_information(**row.to_dict())
            print(instance)
            instances.append(instance)
        except ValidationError as e:
            print(f"Validation error for row {row}: {e}")

    return instances
    
if __name__ =="__main__":
    csv_file = "CSVs\\personal_information.csv"
    personal_informations = load_data_from_csv(csv_file)