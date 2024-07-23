from pydantic import BaseModel, ValidationError, field_validator, Field
from typing import Optional, Union
import typing
import math
import pandas as pd

# List of European countries
european_countries = [
    'Albania', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria',
    'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Georgia', 'Germany', 'Greece',
    'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kazakhstan', 'Kosovo', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg',
    'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania',
    'Russia', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine',
    'United Kingdom', 'Vatican City'
]

# List of Romanian counties
romanian_counties = [
    'Alba', 'Arad', 'Arges', 'Bacau', 'Bihor', 'Bistrita-Nasaud', 'Botosani', 'Brasov', 'Braila', 'Buzau', 'Caras-Severin',
    'Calarasi', 'Cluj', 'Constanta', 'Covasna', 'Dambovita', 'Dolj', 'Galati', 'Giurgiu', 'Gorj', 'Harghita', 'Hunedoara',
    'Ialomita', 'Iasi', 'Ilfov', 'Maramures', 'Mehedinti', 'Mures', 'Neamt', 'Olt', 'Prahova', 'Salaj', 'Satu Mare', 'Sibiu',
    'Suceava', 'Teleorman', 'Timis', 'Tulcea', 'Vaslui', 'Valcea', 'Vrancea', 'Bucuresti'
]

class ProjectLocation(BaseModel):
    country: str
    county: str
    city: str
    street: str  | None
    number: Optional[float] = None
    # number: Union[int, None]
    # number: int | None
    postalcode: int
    
    @field_validator('country')
    def check_country(cls, country):
        if country not in european_countries:
            raise ValueError('Not a European Country')
        return country

def load_data_from_csv(csv_file: str) -> dict:
    df = pd.read_csv(csv_file)
    instances = {}
    
    for index, row in df.iterrows():
        try:
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
