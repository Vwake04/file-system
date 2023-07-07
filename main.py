from database import FileSystemDatabase

DB_PATH = "/home/ubuntu/workspace/file-system/my-db"

def main():
    database = FileSystemDatabase(DB_PATH)
    
    # Create a new table
    database.create_table('users.txt')

    # Get all table names
    tables = database.get_all_tables()
    print(f"All tables: {tables}")

    # Get a specific table
    table = database.get_table('users.txt')

    # Write data to the table
    table.write("John Doe\n")
    table.write("Jane Smith\n")

    # Read the content of the table
    content = table.read()
    print(f"Table content:\n{content}")

    # Update the table
    table.update("Mike Johnson\n")

    # Read the updated content of the table
    updated_content = table.read()
    print(f"Updated table content:\n{updated_content}")

    # Delete the table
    database.delete_table('users.txt')

if __name__ == "__main__":
    main()
