// routes/bookRoutes.js
const express = require('express');
const Book = require('../models/Book');
const router = express.Router();

// Crear un libro
router.post('/books', async (req, res) => {
  try {
    const book = new Book(req.body);
    await book.save();
    res.status(201).send(book);
  } catch (error) {
    res.status(400).send(error);
  }
});

// Leer todos los libros
router.get('/books', async (req, res) => {
    try {
      const books = await Book.find();
      res.status(200).send(books);
    } catch (error) {
      res.status(500).send(error);
    }
});

  

// Leer un libro por ID
router.get('/books/:id', async (req, res) => {
  try {
    const book = await Book.findById(req.params.id);
    if (!book) return res.status(404).send('Libro no encontrado');
    res.status(200).send(book);
  } catch (error) {
    res.status(500).send(error);
  }
});

// Actualizar un libro
router.put('/books/:id', async (req, res) => {
  try {
    const book = await Book.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });
    if (!book) return res.status(404).send('Libro no encontrado');
    res.status(200).send(book);
  } catch (error) {
    res.status(400).send(error);
  }
});

// Eliminar un libro
router.delete('/books/:id', async (req, res) => {
  try {
    const book = await Book.findByIdAndDelete(req.params.id);
    if (!book) return res.status(404).send('Libro no encontrado');
    res.status(200).send('Libro eliminado');
  } catch (error) {
    res.status(500).send(error);
  }
});

module.exports = router;
