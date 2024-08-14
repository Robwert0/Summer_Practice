Overview
This project is a Python-based solution for validating employee data, transforming it, and exporting the validated records to a CSV file. The primary goal is to ensure that all employee data adheres to specified rules and formats before being saved.

Features
Validation of Employee Data: The program validates various fields like employee ID, email, CNP (Personal Numeric Code), languages, and more.
CSV Processing: Reads employee data from a CSV file, validates it, and appends the validated data to another CSV file.
Data Formatting: Ensures data such as email addresses and CNP codes follow specific patterns and logic.
Location Handling: Converts location-related fields into a structured JSON format for easy storage and access.
Components
final_project Class
The final_project class is a Pydantic-based model that represents an employee's data. The class includes field validation and custom methods for data processing.

Attributes:

employee_id, first_name, last_name, email, cnp, gender, number, year, title, language1, language2, language3, country, county, city, street, st_number, postalcode, mother_language, language_2, language_3
Custom Validators:

Language Validators: Ensures that specified languages are valid European languages.
Country and County Validators: Validates that the country is in Europe and the county exists within the specified country.
Email Validator: Ensures the email follows the format first.last@company.com.
CNP Validator: Validates the CNP format and checks that the gender derived from the CNP matches the provided gender.
Programming Languages Validator: Validates that specified programming languages are valid.
Number Validator: Ensures the number is six digits and starts with 100 or 200.
Year Formatter: Formats the year as a string (YYYY).
Methods:

to_string(): Returns a string composed of number, year, and title.
location: A property that returns a dictionary with location-related fields.
location_json(): Returns a JSON string representation of the location data.
Functions
load_data_from_csv(csv_file: str) -> dict:

Reads data from a CSV file, validates each row, and returns a dictionary of valid instances.
read_existing_entries(file_name: str) -> set:

Reads existing entries from a CSV file to avoid duplicate entries when appending new data.
