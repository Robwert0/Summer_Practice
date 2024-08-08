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

        "employee_ID":{
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
                "db_data_type": "integer",
                "db_is_null": False, 
                "table_name":"personal_information"
            },
            "gender":{
                "db_data_type": "VARCHAR",
                "db_is_null": False, 
                "table_name":"personal_information"
            },
        },

        "name_1":{
            "db_data_type": "VARCHAR",
            "db_is_null": False, 
            "table_name":"spoken_language"
        },
        "name_2":{
            "db_data_type": "VARCHAR",
            "db_is_null": True, 
            "table_name":"spoken_language"
        },
        "name_3":{
            "db_data_type": "VARCHAR",
            "db_is_null": True, 
            "table_name":"spoken_language"
        },

        "programming_language1":{
            "db_data_type": "VARCHAR",
            "db_is_null": True, 
            "table_name":"digital_sklill"
        },
        "programming_language2":{
            "db_data_type": "VARCHAR",
            "db_is_null": True, 
            "table_name":"digital_sklill"
        },
        "programming_language3":{
            "db_data_type": "VARCHAR",
            "db_is_null": True, 
            "table_name":"digital_sklill"
        }
    }
}

# colum_config = {
#     "suppliers":{
#         "full_name": {
#             "number": {
#                 "db_data_type": "integer",
#                 "db_is_null": False,
#                 "table_name": "project"
#             },
#             "year": {
#                 "db_data_type": "integer",
#                 "db_is_null": False,
#                 "table_name": "project"
#             },
#             "title": {
#                 "db_data_type": "varchar",
#                 "db_is_null": False,
#                 "table_name": "project"
#             },
#             "full_name": {
#                 "db_data_type": "varchar",
#                 "db_is_null": False,
#                 "table_name": "project"
#             }
#         },
#         "location": {
#             "country": {
#                 "db_data_type": "varchar",
#                 "db_is_null": False,
#                 "table_name": "project",
#                 "jsonb_key": True
#             },
#             "county": {
#                 "db_data_type": "varchar",
#                 "db_is_null": False,
#                 "table_name": "project",
#                 "jsonb_key": True
#             },
#             "city": {
#                 "db_data_type": "varchar",
#                 "db_is_null": False,
#                 "table_name": "project",
#                 "jsonb_key": True
#             },
#             "street": {
#                 "db_data_type": "varchar",
#                 "db_is_null": True,
#                 "table_name": "project",
#                 "jsonb_key": True
#             },
#             "number": {
#                 "db_data_type": "integer",
#                 "db_is_null": True,
#                 "table_name": "project",
#                 "jsonb_key": True
#             },
#             "postalcode": {
#                 "db_data_type": "integer",
#                 "db_is_null": False,
#                 "table_name": "project",
#                 "jsonb_key": True
#             }
#         }
#     }
# }
