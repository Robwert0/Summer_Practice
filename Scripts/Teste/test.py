from pydantic import BaseModel, Field, field_validator, ValidationError
from datetime import datetime
import pandas as pd

class pydantic2csv(BaseModel):
    number: int
    year: datetime 
    title: str
    full_name: str | None

    @field_validator('number')
    def check_number(cls, number):
        str_number = str(number)
        if len(str_number) != 6:
            raise ValueError('number must be a six digit number')
        if not (str_number.startswith('200') or str_number.startswith('100')):
            raise ValueError('number must start with 100 or 200')
        return number
    
    @field_validator('full_name')
    def check_full_name(cls, value):
        value = f'{cls.number}_{cls.year.strftime('%Y')}_{cls.title}'
        return value


csv_file = 'regular_python_class.csv'
dataset = pd.read_csv(csv_file, encoding='UTF-8')
df = pd.DataFrame(dataset)
print(df)
# validated_items=[]

# for _, row in df.iterrows():
#     try:
#         cr = pydantic2csv(**row.to_dict())
#         validated_items.append(cr)
#     except ValidationError as e:
#         print(e)
# for row in validated_items:
#     print(row)