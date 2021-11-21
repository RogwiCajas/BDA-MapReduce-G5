// Constantes
const express = require('express');
const mongoose = require('mongoose');
const taxiRoutes = require('./routes/taxi');  
require('dotenv').config();

const app = express();
const port = process.env.port || 9000;

// Middlewares
app.use(express.json());
app.use('/api', taxiRoutes);

// Rutas
app.get('/', (req, res) => {
    res.send('Bienvenido a la aplicacion de taxis de Chicago!');
});

// Conexion a MongoDB
mongoose
    .connect(process.env.MONGODB_URI)
    .then(() => console.log('Conectado a la base de datos en MongoDB Atlas!'))
    .catch((error) => console.log('Uy, algo salió mal! ', error));

app.listen(port, () => console.log('El servidor funciona en el puerto ', port));