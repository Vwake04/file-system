core classes, functions, and methods:

1. FileSystemDatabase:
   - `create_table(table_name: str) -> None`: Creates a new table in the database.
   - `delete_table(table_name: str) -> None`: Deletes a table from the database.
   - `get_table(table_name: str) -> Table`: Retrieves a table from the database.
   - `get_all_tables() -> List[str]`: Retrieves a list of all table names in the database.
   - `search_all_tables(self, search_terms: List[str]) -> List[str]`: Retrieves a list of all table names in the database based on the keywords match with the table content.

2. Table:
   - `read() -> str`: Reads the content of the table.
   - `write(data: str) -> None`: Writes text data to the table.
   - `update(data: str) -> None`: Appends text data to the existing table.


