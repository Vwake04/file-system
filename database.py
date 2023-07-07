import os
from typing import List

from table import Table

class FileSystemDatabase:
    def __init__(self, database_path: str):
        self.database_path = database_path

    def create_table(self, table_name: str) -> None:
        table_path = os.path.join(self.database_path, table_name)
        with open(table_path, 'w') as table_file:
            pass

    def delete_table(self, table_name: str) -> None:
        table_path = os.path.join(self.database_path, table_name)
        os.remove(table_path)

    def get_table(self, table_name: str) -> 'Table':
        table_path = os.path.join(self.database_path, table_name)
        return Table(table_path)

    def get_all_tables(self) -> List[str]:
        tables = []
        for item in os.listdir(self.database_path):
            if os.path.isfile(os.path.join(self.database_path, item)):
                tables.append(item)
        return tables

    def search_all_tables(self, search_terms: List[str]) -> List[str]:
        tables = self.get_all_tables()
        results = []
        for table in tables:
            table_path = os.path.join(self.database_path, table)
            with open(table_path, 'r') as table_file:
                for line in table_file:
                    if any(term in line for term in search_terms):
                        results.append(line)
        return results
    
