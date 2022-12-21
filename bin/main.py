# Made by: Jess
# Github: 

import sqlite3

db = None

types = {
    "int": "INTEGER",
    "float": "REAL",
    "str": "varchar(255)",
    "bool": "BOOLEAN"
}

def create(database):
    print("Starting database creation...")
    sqlCommands = []

    for name in database["tables"]:
        print("Creating table " + name + "...")

        table = database["tables"][name]

        sql = "CREATE TABLE IF NOT EXISTS " + name + " ("
        insert = "INSERT INTO " + name + " ("

        for column in table["columns"]:
            coltype = type(table["columns"][column])
            coltype = str(coltype).replace("<class '", "").replace("'>", "")
            coltype = types[coltype]

            if coltype == "dict" or coltype == "list" or coltype == "tuple":
                print("ERROR: You can not use " + coltype + " as a column type! (column: " + column + ")")
                exit()

            if "autoIncrement" in table and table["autoIncrement"] and column == table["primaryKey"]:
                if not coltype == "INTEGER":
                    print("ERROR: The primary key must be an integer if you want to use auto increment!")
                    exit() 
                sql += column + " " + coltype + " AUTO_INCREMENT, "
            else:
                sql += column + " " + coltype + ", "
                insert += column + ", "

            

        insert = insert[:-2] + ") VALUES ("

        for column in table["columns"]:
            if not ("autoIncrement" in table and table["autoIncrement"] and column == table["primaryKey"]):
                insert += str(table["columns"][column]) + ", "   

        insert = insert[:-2] + ")"
        sql += "PRIMARY KEY (" + table["primaryKey"] + "))"
        sqlCommands.append({"name": name, "sql": sql, "insert": insert})

    if database["sql"]:
        print("Printing SQL to Console:")
        for sql in sqlCommands:
            print("\t" + sql["name"] + ": " + sql["sql"])

    if database["exportSQL"]:
        print("Exporting SQL...")
        file = open(f"export/" + database["name"] + "_sql.txt", "w")
        for sql in sqlCommands:
            file.write(sql["name"] + ":")
            file.write("\n\tCreate table: \n\t\t" + sql["sql"])
            file.write("\n\tInsert example data: \n\t\t" + sql["insert"] + ")")
            file.write("\n\n")

        file.close()

    if database["create"]:
        db = sqlite3.connect("export/" + database["name"] + ".db")
        print("Creating database...")
        for sql in sqlCommands:
            db.execute(sql["sql"])

        db.commit()
        db.close()

    print("All done!")
    print("You can find the database in the export folder. (export/" + database["name"] + ".db" + ")" )
    print("and any other files in the export folder. (export/)" )