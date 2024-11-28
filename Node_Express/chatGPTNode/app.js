// app.js
const express = require('express');
const mongoose = require('mongoose');
const bookRoutes = require('./routes/bookRoutes');  // Asegúrate de usar la ruta correcta

const app = express();
const PORT = 3000;

// Conecta a MongoDB
mongoose.connect('mongodb://localhost:27017/biblioteca')
  .then(() => console.log('Conectado a MongoDB'))
  .catch(error => console.log('Error de conexión:', error));

// Middleware
app.use(express.json());
app.use('/api', bookRoutes);  // Esto da el prefijo '/api' para las rutas de libros

// Inicia el servidor
app.listen(PORT, () => {
  console.log(`Servidor escuchando en http://localhost:${PORT}`);
});
