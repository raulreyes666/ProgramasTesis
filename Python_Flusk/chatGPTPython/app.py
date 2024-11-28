from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# Inicializar la app y configurar la base de datos
app = Flask(__name__)
app.config.from_object(Config)

# Inicializar las extensiones
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Definir el modelo de la entidad Libro
class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    autor = db.Column(db.String(255), nullable=False)
    año_publicacion = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Libro {self.titulo} de {self.autor}>"

# Rutas y controladores para las operaciones CRUD

# Crear un nuevo libro
@app.route('/api/libros', methods=['POST'])
def crear_libro():
    data = request.get_json()
    nuevo_libro = Libro(titulo=data['titulo'], autor=data['autor'], año_publicacion=data['año_publicacion'])
    db.session.add(nuevo_libro)
    db.session.commit()
    return jsonify({'message': 'Libro creado correctamente'}), 201

# Obtener todos los libros
@app.route('/api/libros', methods=['GET'])
def obtener_libros():
    libros = Libro.query.all()
    return jsonify([{'id': libro.id, 'titulo': libro.titulo, 'autor': libro.autor, 'año_publicacion': libro.año_publicacion} for libro in libros])

# Obtener un libro por ID
@app.route('/api/libros/<int:id>', methods=['GET'])
def obtener_libro(id):
    libro = Libro.query.get_or_404(id)
    return jsonify({'id': libro.id, 'titulo': libro.titulo, 'autor': libro.autor, 'año_publicacion': libro.año_publicacion})

# Actualizar un libro
@app.route('/api/libros/<int:id>', methods=['PUT'])
def actualizar_libro(id):
    libro = Libro.query.get_or_404(id)
    data = request.get_json()
    libro.titulo = data['titulo']
    libro.autor = data['autor']
    libro.año_publicacion = data['año_publicacion']
    db.session.commit()
    return jsonify({'message': 'Libro actualizado correctamente'})

# Eliminar un libro
@app.route('/api/libros/<int:id>', methods=['DELETE'])
def eliminar_libro(id):
    libro = Libro.query.get_or_404(id)
    db.session.delete(libro)
    db.session.commit()
    return jsonify({'message': 'Libro eliminado correctamente'})

if __name__ == '__main__':
    app.run(debug=True)



