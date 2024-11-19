from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

# Página sobre nosotros
@app.route('/about')
def about():
    return render_template('about.html')

# Página de contacto
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        # Aquí puedes agregar la lógica para enviar un correo electrónico o almacenar los datos en la base de datos
        return redirect(url_for('index'))
    return render_template('contact.html')

# Página de reseñas
@app.route('/reviews')
def reviews():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reviews")
    reviews = cursor.fetchall()
    conn.close()
    return render_template('reviews.html', reviews=reviews)

# Añadir una reseña
@app.route('/add_review', methods=['POST'])
def add_review():
    data = request.form
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reviews (name, review, rating) VALUES (?, ?, ?)", 
                   (data['name'], data['review'], data['rating']))
    conn.commit()
    conn.close()
    return redirect(url_for('reviews'))

# Eliminar una reseña
@app.route('/delete_review/<int:review_id>', methods=['POST'])
def delete_review(review_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reviews WHERE id = ?", (review_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('reviews'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)