# routes.py
from flask import Blueprint, request, jsonify
from models import db, Book

bp = Blueprint('librox2', __name__)

@bp.route('/librox2', methods=['GET'])
def get_books():
    try:
        books = Book.query.all()
        return jsonify({
            'success': True,
            'data': [book.to_dict() for book in books]
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@bp.route('/librox2/<int:id>', methods=['GET'])
def get_book(id):
    try:
        book = Book.query.get_or_404(id)
        return jsonify({
            'success': True,
            'data': book.to_dict()
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 404

@bp.route('/librox2', methods=['POST'])
def create_book():
    try:
        data = request.get_json()
        
        # Validar campos requeridos
        required_fields = ['nombre', 'autor', 'anio_creacion']
        if not all(field in data for field in required_fields):
            return jsonify({
                'success': False,
                'error': 'Faltan campos requeridos. Se necesitan: nombre, autor, anio_creacion'
            }), 400
        
        new_book = Book(
            nombre=data['nombre'],
            autor=data['autor'],
            anio_creacion=data['anio_creacion']
        )
        
        db.session.add(new_book)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Libro creado exitosamente',
            'data': new_book.to_dict()
        }), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@bp.route('/librox2/<int:id>', methods=['PUT'])
def update_book(id):
    try:
        book = Book.query.get_or_404(id)
        data = request.get_json()
        
        if 'nombre' in data:
            book.nombre = data['nombre']
        if 'autor' in data:
            book.autor = data['autor']
        if 'anio_creacion' in data:
            book.anio_creacion = data['anio_creacion']
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Libro actualizado exitosamente',
            'data': book.to_dict()
        }), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@bp.route('/librox2/<int:id>', methods=['DELETE'])
def delete_book(id):
    try:
        book = Book.query.get_or_404(id)
        db.session.delete(book)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Libro eliminado exitosamente'
        }), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

