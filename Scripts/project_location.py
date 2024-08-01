from pydantic import BaseModel, ValidationError, field_validator
from pydantic_core.core_schema import FieldValidationInfo
from typing import Optional
import pandas as pd
from ref_table import europe, counties


class ProjectLocation(BaseModel):
    country: str
    county: str
    city: str
    street: Optional[str] = None
    number: Optional[int] = None
    # number: Union[int, None]
    # number: int | None
    postalcode: int
    
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

def load_data_from_csv(csv_file: str) -> dict:
    df = pd.read_csv(csv_file)
    instances = {}
    
    for index, row in df.iterrows():
        try:
            row = row.where(pd.notnull(row), None)
            instance = ProjectLocation(**row.to_dict())
            instance_key = "Locatia " + str(index+1)
            instances[instance_key] = instance.model_dump()
        except ValidationError as e:
            print(f"Validation error at row {index}: {e}")
    
    return instances


if __name__ == "__main__":
    csv_file = "CSVs\\project_locations.csv"
    project_locations = load_data_from_csv(csv_file)
    
    for key, instance in project_locations.items():
        print(f"{key}: {instance}")
