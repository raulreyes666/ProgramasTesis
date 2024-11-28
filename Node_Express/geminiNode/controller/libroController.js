// controllers/libroController.js
const Libro = require('../models/Libro');

// Obtener todos los libros
const getAllLibros = async (req, res) => {
  const libros = await Libro.find();
  res.json(libros);
};

// Crear un nuevo libro
const createLibro = async (req, res) => {
  const libro = new Libro(req.body);
  await libro.save();
  res.status(201).json(libro);
};

// Obtener un libro por ID
const getLibroById = async (req, res) => {
  const libro = await Libro.findById(req.params.id);
  if (!libro) {
    return res.status(404).json({ message: 'Libro no encontrado' });
  }
  res.json(libro);
};

// Actualizar un libro por ID
const updateLibro = async (req, res) => {
  const libro = await Libro.findByIdAndUpdate(req.params.id, req.body, { new: true });
  if (!libro) {
    return res.status(404).json({ message: 'Libro no encontrado' });
  }
  res.json(libro);
};

// Eliminar un libro por ID
const deleteLibro = async (req, res) => {
  const libro = await Libro.findByIdAndDelete(req.params.id);
  if (!libro) {
    return res.status(404).json({ message: 'Libro no encontrado' });
  }
  res.json({ message: 'Libro eliminado' });
};

module.exports = {
  getAllLibros,
  createLibro,
  getLibroById,
  updateLibro,
  deleteLibro
};