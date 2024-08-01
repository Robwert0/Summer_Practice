from pydantic import BaseModel, ValidationError, field_validator
from pydantic_core.core_schema import FieldValidationInfo
import pandas as pd
from typing import Optional
from ref_table import programming_languages

class ProgrammingLanguages(BaseModel):
    language1: Optional[str] = None
    language2: Optional[str] = None
    language3: Optional[str] = None

    @field_validator("language1", "language2", "language3")
    def check_prog_language(cls, language, info: FieldValidationInfo):
        if language is not None and language not in programming_languages:
            field_name = info.field_name
            raise ValueError(f'{field_name}"{language} is not a valid programming language. Valid Programming languages are {programming_languages}"')

        return language

def load_data_from_csv(csv_file: str) -> dict:
    df = pd.read_csv(csv_file)
    instances = {}

    for index, row in df.iterrows():
        try:
            row = row.where(pd.notnull(row), None)
            instance = ProgrammingLanguages(**row.to_dict())
            instance_key = "Prog_language " + str(index+1)
            instances[instance_key] = instance

        except ValidationError as e:
            print(f"Validation error at row {index}: {e}")

    return instances


if __name__ == '__main__':
    csv_file = 'CSVs\\programming_languages.csv'
    prog_language = load_data_from_csv(csv_file)

    for key, instance in prog_language.items():
        print(f"{key} : {instance}")