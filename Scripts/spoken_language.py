from pydantic import BaseModel, ValidationError, field_validator
from pydantic_core.core_schema import FieldValidationInfo
from typing import Optional
import pandas as pd
from ref_table import european_languages

class SpokenLanguages(BaseModel):
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
    
def load_data_from_csv(csv_file: str) -> dict:
    df = pd.read_csv(csv_file)
    instances = {}

    for index, row in df.iterrows():
        try:
            row = row.where(pd.notnull(row), None)
            instance = SpokenLanguages(**row.to_dict())
            instance_key = 'Person ' + str(index + 1)
            instances[instance_key] = instance
            
        except ValidationError as e:
            print(f"Validation error at row {index}: {e}")

    return instances
        

if __name__ == "__main__":
    csv_file = 'CSVs\\spoken_languages.csv'
    spoken_language = load_data_from_csv(csv_file)

    for key, instance in spoken_language.items():
        print(f"{key} : {instance}")