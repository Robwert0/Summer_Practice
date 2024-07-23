import psycopg2
from config import load_config


def insert_data(data_list):
    sql = """INSERT INTO project(full_name) 
             VALUES(%s) RETURNING *"""
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.executemany(sql, data_list)

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)     