from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+mariadbconnector://root:pandur%40tE01@localhost:3307/biblioteca'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Librox(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_libro = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    anio_publicacion = db.Column(db.Integer)

    def __repr__(self):
        return f'<Librox {self.nombre_libro}>'

    def to_json(self):
        return {
            'id': self.id,
            'nombre_libro': self.nombre_libro,
            'autor': self.autor,
            'anio_publicacion': self.anio_publicacion
        }

# Rutas
@app.route('/libros', methods=['GET', 'POST'])
def libros():
    if request.method == 'POST':
        libro = Librox(nombre_libro=request.json['nombre_libro'],
                      autor=request.json['autor'],
                      anio_publicacion=request.json['anio_publicacion'])
        db.session.add(libro)
        db.session.commit()
        return jsonify({'mensaje': 'Libro creado exitosamente'}), 201
    else:
        libros = Librox.query.all()
        return jsonify([libro.to_json() for libro in libros])

@app.route('/libros/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def libro_por_id(id):
    libro = Librox.query.get(id)
    if not libro:
        return jsonify({'mensaje': 'Libro no encontrado'}), 404

    if request.method == 'GET':
        return jsonify(libro.to_json())

    elif request.method == 'PUT':
        data = request.get_json()
        if 'nombre_libro' in data:
            libro.nombre_libro = data['nombre_libro']
        if 'autor' in data:
            libro.autor = data['autor']
        if 'anio_publicacion' in data:
            libro.anio_publicacion = data['anio_publicacion']
        db.session.commit()
        return jsonify({'mensaje': 'Libro actualizado exitosamente'}), 200

    elif request.method == 'DELETE':
        db.session.delete(libro)
        db.session.commit()
        return jsonify({'mensaje': 'Libro eliminado exitosamente'}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)