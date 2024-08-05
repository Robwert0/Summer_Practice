from pydantic import BaseModel, ValidationError, field_validator, EmailStr, Field
from pydantic_core.core_schema import FieldValidationInfo
import pandas as pd
from datetime import datetime
import re
from typing import Optional
from ref_table import european_languages, europe, counties, programming_languages
import os
import csv

class final_project(BaseModel):
    employee_id: str = Field(alias='id')
    first_name: str
    last_name: str
    email: Optional[EmailStr] = None
    cnp: str
    gender: str
    number: int
    year: datetime 
    title: str
    language1: Optional[str] = None
    language2: Optional[str] = None
    language3: Optional[str] = None
    country: str
    county: str
    city: str
    street: Optional[str] = None
    number: Optional[int] = None
    postalcode: int
    mother_language: str
    language_2: Optional[str] = None
    language_3: Optional[str] = None

    @field_validator("mother_language")
    def check_mother_language(cls, mother_language):
        if mother_language not in european_languages:
            raise ValueError('Not a valid Language')
        
        return mother_language
    
    @field_validator("language_2", "language_3")
    def check_other_languages(cls, language, info: FieldValidationInfo):
        if language is not None and language not in european_languages:
            field_name = info.field_name
            raise ValueError(f'{field_name} "{language}" is not a valid language. Valid languages are: {european_languages}')
        
        return language
    
    @field_validator('country')
    def check_country(cls, country):
        if country not in europe:
            raise ValueError('Not a European Country')
        return country
    
    @field_validator('county')
    def check_county(cls, county, info: FieldValidationInfo):
        country = info.data['country']
        if country and county not in counties.get(country, []):
            raise ValueError(f'Not a county in {country}')
        return county

    @field_validator('email')
    def validate_email(cls, email, info: FieldValidationInfo):
        first_name = info.data['first_name']
        last_name = info.data['last_name']
        expected_format = f"{first_name.lower()}.{last_name.lower()}@company.com"
        if email != expected_format:
            raise ValueError('Email must be in the format first.last@company.com with lowercase')
        return email
    
    @field_validator('cnp')
    def validate_identifier(cls, cnp, info: FieldValidationInfo):
        if not re.match(r'^[1256]\d{12}$', cnp):
            raise ValueError('Identifier must start with 1, 2, 5, or 6 and have 13 digits')

        if 'gender' in info.data:
            gender_indicator = cnp[0]
            gender_from_cnp = 'male' if gender_indicator in '15' else 'female'
            gender = info.data['gender'].strip().lower()
            if gender != gender_from_cnp:
                raise ValueError(f'Gender from CNP ({gender_from_cnp}) does not match provided gender ({gender})')

        cnp_year = int(cnp[1:3])
        current_year = datetime.now().year
        if cnp[0] in '12':
            birth_year = 1900 + cnp_year
        elif cnp[0] in '56':
            birth_year = 2000 + cnp_year

        if birth_year > current_year:
            raise ValueError(f'Extracted year from CNP ({birth_year}) cannot be greater than the current year ({current_year})')

        return cnp
    
    @field_validator("language1", "language2", "language3")
    def check_prog_language(cls, language, info: FieldValidationInfo):
        if language is not None and language not in programming_languages:
            field_name = info.field_name
            raise ValueError(f'{field_name}"{language} is not a valid programming language. Valid Programming languages are {programming_languages}"')

        return language
    
    @field_validator('number')
    def check_number(cls, number):
        str_number = str(number)
        if len(str_number) != 6:
            raise ValueError('number must be a six digit number')
        if not (str_number.startswith('200') or str_number.startswith('100')):
            raise ValueError('number must start with 100 or 200')
        return number
    
    @field_validator('year')
    def modelate_year(cls, year):
        return year.strftime('%Y')
    
    def to_string(self) -> str:
        return f"{self.number}_{self.year.strftime('%Y')}_{self.title}"

def load_data_from_csv(csv_file: str) -> dict:
    df = pd.read_csv(csv_file, dtype={'cnp':str}, parse_dates=['year'])
    instances = {}

    for index, row in df.iterrows():
        try:
            row = row.where(pd.notnull(row), None)
            instance = final_project(**row.to_dict())
            instance_key = str(index + 1)
            instances[instance_key] = instance

        except ValidationError as e:
            print(f"Validation error for row {row}: {e}")

    return instances

def read_existing_entries(file_name: str) -> set:
    existing_entries = set()
    if os.path.isfile(file_name):
        with open(file_name, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                employee_id = row.get('employee_id')
                if employee_id:
                    existing_entries.add(employee_id)
    return existing_entries

if __name__ =="__main__":
    csv_file = "CSVs\\all_in.csv"
    validated_data = load_data_from_csv(csv_file)

    data_dir = 'CSVs'
    validated_csv_file = os.path.join(data_dir, "validated_data.csv")
    headers = [field for field in final_project.__annotations__.keys()]

    if not os.path.isfile(validated_csv_file):
        with open(validated_csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            print(f'{validated_csv_file} created with headers.')

    existing_entries = read_existing_entries(validated_csv_file)

    with open(validated_csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        for key, instance in validated_data.items():
            data = instance.dict()
            employee_id = data.get('employee_id')
            
            # Check if the employee_id already exists
            if employee_id in existing_entries:
                print(f"Skipping duplicate entry for employee_id: {employee_id}")
                continue
            
            # Write row to CSV
            writer.writerow([data.get(header, '') for header in headers])
            print(f'Data for {key} added to the CSV file.')

            existing_entries.add(employee_id)
