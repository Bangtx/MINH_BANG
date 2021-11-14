import sqlite3


class Database:
    db = sqlite3.connect('data.sqlite3')
    cursor = db.cursor()

    def __init__(self):
        sql = """
            CREATE TABLE IF NOT EXISTS `mon_an` (
                `id` INTEGER PRIMARY KEY,
                `name` TEXT NOT NULL,
                `cal` TEXT NOT NULL
            );"""

        self.cursor.execute(sql)

        sql2 = """
            CREATE TABLE IF NOT EXISTS `calo` (
                `date` TEXT NOT NULL,
                `cal` TEXT NOT NULL
                );
            """

        self.execute(sql2)

        self.db.commit()
