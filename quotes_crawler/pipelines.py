import sqlite3

class DatabasePipeline:
    def __init__(self):
        self.connection = sqlite3.connect('quotes.db')
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS quotes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT,
                author TEXT,
                tags TEXT
            )
        """)
        self.connection.commit()

    def process_item(self, item, spider):
        self.cursor.execute("""
            INSERT INTO quotes (text, author, tags) 
            VALUES (?, ?, ?)
        """, (item['text'], item['author'], item['tags']))
        self.connection.commit()

        return item

    def close_spider(self, spider):
        self.connection.close()
