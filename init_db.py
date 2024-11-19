import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Crear la tabla escape_rooms si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS escape_rooms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    difficulty TEXT NOT NULL
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    review TEXT NOT NULL,
    rating INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5)
)
''')

# Insertar datos ficticios
escape_rooms = [
    ('La Casa Embrujada', 'Una casa llena de misterios y fantasmas.', 'Difícil'),
    ('El Tesoro Perdido', 'Encuentra el tesoro escondido en una isla desierta.', 'Medio'),
    ('El Laboratorio Secreto', 'Descubre los secretos de un laboratorio abandonado.', 'Fácil')
]

cursor.executemany('''
INSERT INTO escape_rooms (name, description, difficulty) VALUES (?, ?, ?)
''', escape_rooms)

conn.commit()
conn.close()