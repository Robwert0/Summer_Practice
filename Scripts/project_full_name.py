from pydantic import BaseModel, Field, field_validator
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
    for _, row in df.iterrows():
        instance = pydantic2csv(number=row['number'], year=row['year'], title=row['title'])
        result.append(instance.to_string())

    return result


if __name__ =='__main__':
    csv_file = 'CSVs\\regular_python_class.csv'
    strings = load_data_from_csv(csv_file)

    project_full_name={}
    project_full_name['full_name'] = strings

    print(project_full_name)