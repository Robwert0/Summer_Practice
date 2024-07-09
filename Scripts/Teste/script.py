from pydantic import BaseModel, Field, field_validator, ValidationError
from pydantic_core.core_schema import FieldValidationInfo
from datetime import datetime
import pandas as pd
from typing import Any


class pydantic2csv(BaseModel):
    number: str
    year: str 
    title: str
    full_name: Any

    # @field_validator('number')
    # def check_number(cls, number):
    #     str_number = str(number)
    #     if len(str_number) != 6:
    #         raise ValueError('number must be a six digit number')
    #     if not (str_number.startswith('200') or str_number.startswith('100')):
    #         raise ValueError('number must start with 100 or 200')
    #     return number
    
    @field_validator('full_name')
    def check_full_name(cls, value,  info: FieldValidationInfo):
        number = info.data['number']
        year = info.data['year']
        title = info.data['title']
        value = f'{number}_{year}_{title}'
        return value
    



csv_file = 'regular_python_class.csv'
dataset = pd.read_csv(csv_file, encoding='UTF-8')
df = pd.DataFrame(dataset)
# print(df)
validated_items=[]

for _, row in df.iterrows():
    try:
        cr = pydantic2csv(**row)
        validated_items.append(cr.model_dump())
    except ValidationError as e:
        print(e)
# for row in validated_items:
#     print(row)
print(validated_items)

