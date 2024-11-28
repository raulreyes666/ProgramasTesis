const express = require('express');
const mongoose = require('mongoose');

const Libro = require('./models/Libro');

const app = express();
const port = 3000;

// Conexión a MongoDB
mongoose.connect('mongodb://localhost:27017/biblioteca', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Conectado a MongoDB'))
  .catch(err => console.error(err));

app.use(express.json());

// Rutas
app.get('/libros', async (req, res) => {
  const libros = await Libro.find();
  res.json(libros);
});

app.post('/libros', async (req, res) => {
  const libro = new Libro(req.body);
  await libro.save();
  res.status(201).json(libro);
});

app.get('/libros/:id', async (req, res) => {
  const libro = await Libro.findById(req.params.id);
  if (!libro) {
    return res.status(404).json({ message: 'Libro no encontrado' });
  }
  res.json(libro);
});

app.put('/libros/:id', async (req, res) => {
  const libro = await Libro.findByIdAndUpdate(req.params.id, req.body, { new: true });
  if (!libro) {
    return res.status(404).json({ message: 'Libro no encontrado' });
  }
  res.json(libro);
});

app.delete('/libros/:id', async (req, res) => {
  const libro = await Libro.findByIdAndDelete(req.params.id);
  if (!libro) {
    return res.status(404).json({ message: 'Libro no encontrado' });
  }
  res.json({ message: 'Libro eliminado' });
});

app.listen(port, () => {
  console.log(`Servidor escuchando en el puerto ${port}`);
});