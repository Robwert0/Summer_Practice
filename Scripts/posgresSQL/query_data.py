import psycopg2
from colum_configurator import colum_config
from config import load_config

def get_data():
    config = load_config()  # Load database connection configuration

    try:
        # Establish a connection to the database
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Iterate through the tables in the column configuration
                for table in set(column_info["table_name"] for column_info in colum_config["practica_bp"].values()):
                    print(f"Fetching data from table: {table}")
                    
                    # Construct the SQL query
                    sql_query = f"SELECT * FROM {table};"
                    cur.execute(sql_query)

                    # Print the number of rows retrieved
                    print(f"The number of rows in table '{table}': {cur.rowcount}")
                    
                    # Fetch and print each row
                    row = cur.fetchone()
                    while row is not None:
                        print(row)
                        row = cur.fetchone()
                    
                    print("\n")  # Separate outputs for readability

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"An error occurred: {error}")

if __name__ == '__main__':
    get_data()
