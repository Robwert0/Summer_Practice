import psycopg2
from config import load_config
from colum_configurator import colum_config

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = []
    table_commands = {}

    for column, properties in colum_config['practica_bp'].items():
        table_name = properties['table_name']
        if table_name not in table_commands:
            table_commands[table_name] = []

        col_definition = f"{column} {properties['db_data_type']}"
        if properties['db_data_type'].upper() == 'VARCHAR':
            col_definition += "(255)"
        if not properties['db_is_null']:
            col_definition += " NOT NULL"
        
        table_commands[table_name].append(col_definition)

    for table_name, columns in table_commands.items():
        create_command = f"CREATE TABLE IF NOT EXISTS {table_name} (\n  " + ",\n  ".join(columns) + "\n);"
        commands.append(create_command)

    # commands = (
    #     """
    #     CREATE TABLE project(
    #         full_name VARCHAR(255) NOT NULL
    #         location VARCHAR(20) NOT NULL
    #     )
    #     """)
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()