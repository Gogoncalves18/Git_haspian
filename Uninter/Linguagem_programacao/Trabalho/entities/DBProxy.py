import sqlite3


class DBproxy:
    def __init__(self, nome_db: str):
        self.db_name = nome_db
        self.conexao_db = sqlite3.connect(self.db_name)
        self.conexao_db.execute('''
                               CREATE TABLE IF NOT EXISTS PontosGhostMago(
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               nome TEXT NOT NULL,
                               score_mago INTEGER NOT NULL,
                               score_ghost INTEGER NOT NULL
                               )
                               '''
                                )

    def save(self, dados: dict):
        self.conexao_db.execute('INSERT INTO PontosGhostMago (nome, score_mago, score_ghost) VALUES (:nome, :score_mago, :score_ghost)', dados)
        self.conexao_db.commit()

    def select_top5(self) -> list:
        return self.conexao_db.execute('SELECT * FROM PontosGhostMago ORDER BY score_mago DESC LIMIT 5').fetchall()

    def close(self):
        return self.conexao_db.close()
