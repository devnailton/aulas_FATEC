const express = require('express');
const mysql = require('mysql2');
const cors = require('cors');

const app = express(); // Inicializando o app Express
app.use(cors());
app.use(express.json());

const db = mysql.createConnection({
    host: 'localhost', // Ex: localhost ou IP do servidor
    user: 'root',
    password: 'Nlt@@123',
    database: 'tarefas_db'
});

// Rota para obter todas as tarefas
app.get('/tarefas', (req, res) => {
    db.query('SELECT * FROM tarefas', (err, results) => {
        if (err) return res.status(500).send(err);
        res.json(results);
    });
});

// Rota para adicionar uma nova tarefa
app.post('/tarefas', (req, res) => {
    const { nome } = req.body;
    db.query('INSERT INTO tarefas (nome) VALUES (?)', [nome], (err, results) => {
        if (err) return res.status(500).send(err);
        res.status(201).json({ id: results.insertId, nome });
    });
});

// Rota para remover uma tarefa
app.delete('/tarefas/:id', (req, res) => {
    const { id } = req.params;
    db.query('DELETE FROM tarefas WHERE id = ?', [id], (err) => {
        if (err) return res.status(500).send(err);
        res.status(200).json({ message: 'Tarefa removida com sucesso!' });
    });
});

// Iniciar o servidor
app.listen(3000, () => {
    console.log('Servidor rodando na porta 3000');
});