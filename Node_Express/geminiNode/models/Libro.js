const mongoose = require('mongoose');

const libroSchema = new mongoose.Schema({
  titulo: String,
  autor: String,
  anioPublicacion: Number
});

module.exports = mongoose.model('Libro', libroSchema);