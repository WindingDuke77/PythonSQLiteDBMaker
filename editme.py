# Read the README.md file for more information
database = {
    "name": "example", # This is the name of the database
    "sql": True, # This will print the SQL commands to the console
    "exportSQL": True, # This will export the SQL commands and examples to a file
    "create": True, # This will create the database, so you can copy and use it in other projects
    "tables": {} # DO NOT EDIT THIS LINE
}

tables = database["tables"] # DO NOT EDIT THIS LINE
# NOTE: You can add as many tables as you want

tables["example"] = { # This is the name of the table
    "columns": { # This is the columns of the table
        "name": "John Doe",
        "age": 18,
        "hight": 1.80,
        "isHuman": True
    },
    "primaryKey": "name", # This is the primary key of the table
    "autoIncrement": False
}

tables["example2"] = { # This is the name of the table
    "columns": { # This is the columns of the table
        "id": 1,
        "book": "Harry Potter",
        "author": "J.K. Rowling",
        "pages": 500,
        "price": 19.99,
        "isAvailable": True
    },
    "primaryKey": "id", # This is the primary key of the table
    "autoIncrement": True
}

# DO NOT EDIT BELOW THIS LINE
from bin.main import create
create(database)


