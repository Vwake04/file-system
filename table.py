class Table:
    def __init__(self, table_path: str):
        self.table_path = table_path

    def read(self) -> str:
        with open(self.table_path, 'r') as table_file:
            return table_file.read()

    def write(self, data: str) -> None:
        with open(self.table_path, 'w') as table_file:
            table_file.write(data)

    def update(self, data: str) -> None:
        with open(self.table_path, 'a') as table_file:
            table_file.write(data)
