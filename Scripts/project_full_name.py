from pydantic import BaseModel, ValidationError, field_validator
from datetime import datetime
import pandas as pd


class pydantic2csv(BaseModel):
    number: int
    year: datetime 
    title: str

    @field_validator('number')
    def check_number(cls, number):
        str_number = str(number)
        if len(str_number) != 6:
            raise ValueError('number must be a six digit number')
        if not (str_number.startswith('200') or str_number.startswith('100')):
            raise ValueError('number must start with 100 or 200')
        return number
    
    def to_string(self) -> str:
        return f"{self.number}_{self.year.strftime('%Y')}_{self.title}"


def load_data_from_csv(csv_file: str)->list[str]:
    df = pd.read_csv(csv_file, parse_dates=['year'])
    result = []
    for index, row in df.iterrows():
        try:
            row = row.where(pd.notnull(row), None)
            instance = pydantic2csv(**row.to_dict())
            result.append(instance.to_string())
        except ValidationError as e:
            print(f"Validation error at row {index}: {e}")

    return result


if __name__ =='__main__':
    csv_file = 'CSVs\\regular_python_class.csv'
    strings = load_data_from_csv(csv_file)

    project_full_name={}
    project_full_name['full_name'] = strings

    print(project_full_name)