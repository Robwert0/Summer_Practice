import psycopg2
import pandas as pd
from config import load_config
from colum_configurator import colum_config

def insert_data_from_csv(csv_file):
    df = pd.read_csv(csv_file)

    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Initialize a dictionary to hold data by table
                data_by_table = {}

                # Iterate over each row in the DataFrame
                for _, row in df.iterrows():
                    for field, value in row.items():
                        # Convert NaN to None
                        if pd.isna(value):
                            value = None

                        # Get the configuration for the current field
                        if field in colum_config['practica_bp']:
                            table_name = colum_config['practica_bp'][field]['table_name']
                            column_name = field

                            # Initialize table entry if not exists
                            if table_name not in data_by_table:
                                data_by_table[table_name] = {}

                            # Add the value to the correct table and column
                            if column_name not in data_by_table[table_name]:
                                data_by_table[table_name][column_name] = []

                            # Append the value to the list for executemany
                            data_by_table[table_name][column_name].append(value)

                # Print the data being inserted for debugging
                for table_name, columns in data_by_table.items():
                    print(f"Inserting into table {table_name}")
                    for column_name, values in columns.items():
                        print(f"Column {column_name}: {values}")

                # Now iterate over each table and insert the data
                for table_name, columns in data_by_table.items():
                    sql_columns = ', '.join(columns.keys())
                    sql_values = ', '.join(['%s'] * len(columns.keys()))

                    sql = f"INSERT INTO {table_name} ({sql_columns}) VALUES ({sql_values}) RETURNING *"
                    values = list(zip(*columns.values()))

                    # Print the SQL statement and values for debugging
                    print(f"Executing SQL: {sql}")
                    print(f"Values: {values}\n")

                    # Execute the INSERT statement for the current table
                    cur.executemany(sql, values)

                # Commit all the changes
                conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Database error:", error)

if __name__ == "__main__":
    csv_file = "..\\CSVs\\validated_data.csv"
    insert_data_from_csv(csv_file)
