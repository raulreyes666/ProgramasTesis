const mongoose = require('mongoose');

const bookSchema = new mongoose.Schema({
  title: {
    type: String,
    required: [true, 'El título es obligatorio']
  },
  author: {
    type: String,
    required: [true, 'El autor es obligatorio']
  },
  publishYear: {
    type: Number,
    required: [true, 'El año de publicación es obligatorio']
  },
  createdAt: {
    type: Date,
    default: Date.now
  }
});

module.exports = mongoose.model('Book', bookSchema);