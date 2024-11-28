// routes/libros.js
const express = require('express');
// routes/libros.js
const librosController = require('../controllers/librosController');
const router = express.Router();

router.route('/libros')
  .get(librosController.getLibros)
  .post(librosController.createLibro);

router.route('/libros/:id')
  .get(librosController.getLibroById)
  .put(librosController.updateLibro)
  .delete(librosController.deleteLibro);

module.exports = router;