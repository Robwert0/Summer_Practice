colum_config = {
    "practica_bp":{
        "full_name": {
            "db_data_type": "VARCHAR", 
            "db_is_null": False, 
            "table_name":"project"
        }, 
        "location": {
            "db_data_type": "jsonb",
            "db_is_null": False,  
            "table_name": "project"
        },
        "country": {
            "db_data_type": "VARCHAR",
            "db_is_null": False,  
            "table_name": "project"
        },
        "county": {
            "db_data_type": "VARCHAR",
            "db_is_null": False,  
            "table_name": "project"
        },
        "city": {
            "db_data_type": "VARCHAR",
            "db_is_null": False,  
            "table_name": "project"
        },
        "street": {
            "db_data_type": "VARCHAR",
            "db_is_null": True,  
            "table_name": "project"
        },
        "st_number": {
            "db_data_type": "INTEGER",
            "db_is_null": True,  
            "table_name": "project"
        },
        "postalcode": {
            "db_data_type": "BIGINT",
            "db_is_null": False,  
            "table_name": "project"
        },

        "employee_id":{
            "db_data_type": "VARCHAR",
            "db_is_null": False, 
            "table_name":"personal_information"
        },
        "first_name":{
            "db_data_type": "VARCHAR",
            "db_is_null": False, 
            "table_name":"personal_information"
            },
        "last_name":{
            "db_data_type": "VARCHAR",
            "db_is_null": False, 
            "table_name":"personal_information"
        },
        "email":{
            "db_data_type": "VARCHAR",
            "db_is_null": True, 
            "table_name":"personal_information"
        },
        "cnp":{
            "db_data_type": "BIGINT",
            "db_is_null": False, 
            "table_name":"personal_information"
        },
        "gender":{
            "db_data_type": "VARCHAR",
            "db_is_null": False, 
            "table_name":"personal_information"
        },

        "mother_language":{
            "db_data_type": "VARCHAR",
            "db_is_null": False, 
            "table_name":"spoken_language"
        },
        "language_2":{
            "db_data_type": "VARCHAR",
            "db_is_null": True, 
            "table_name":"spoken_language"
        },
        "language_3":{
            "db_data_type": "VARCHAR",
            "db_is_null": True, 
            "table_name":"spoken_language"
        },

        "language1":{
            "db_data_type": "VARCHAR",
            "db_is_null": True, 
            "table_name":"digital_sklill"
        },
        "language2":{
            "db_data_type": "VARCHAR",
            "db_is_null": True, 
            "table_name":"digital_sklill"
        },
        "language3":{
            "db_data_type": "VARCHAR",
            "db_is_null": True, 
            "table_name":"digital_sklill"
        }
    }
}