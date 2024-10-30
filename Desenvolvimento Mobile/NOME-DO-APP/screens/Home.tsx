//Arquivo Home.tsx

import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { AddNewTodo } from '../components/AddNewTodo';
import Todo from '../components/Todo';
import Counter from '../components/Counter';
import axios from 'axios';

export default function Home() {
  const [tasks, setTasks] = useState<{ id: number; nome: string; concluida: boolean }[]>([]);
  const [newTask, setNewTask] = useState<string>('');

  const fetchTasks = async () => {
    try {
      const response = await axios.get('http://localhost:3000/tarefas');
      console.log('Tarefas recebidas:', response.data);
      setTasks(response.data);
    } catch (error) {
      console.error('Erro ao buscar tarefas:', error);
    }
  };

  const handleTodoAdd = async () => {
    if (!newTask.trim()) return;

    try {
      const response = await axios.post('http://localhost:3000/tarefas', { nome: newTask });
      setTasks(prevState => [...prevState, { ...response.data, concluida: false }]);
      setNewTask('');
    } catch (error) {
      console.error('Erro ao adicionar tarefa:', error);
    }
  };

  const handleTodoRemove = async (id: number) => {
    try {
      await axios.delete(`http://localhost:3000/tarefas/${id}`);
      setTasks(prevState => prevState.filter(task => task.id !== id));
    } catch (error) {
      console.error('Erro ao remover tarefa:', error);
    }
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Lista de Tarefas Nailton</Text>
      <AddNewTodo onPress={handleTodoAdd} onChange={setNewTask} value={newTask} />
      
      {tasks.map((task) => (
        task.nome ? (
          <Todo 
            key={task.id} 
            name={task.nome} 
            onDelete={() => handleTodoRemove(task.id)} // Passa a função de remover
          />
        ) : null
      ))}
      
      <Counter style={{ margin: 10 }} name='Criadas' value={tasks.length} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
    textAlign: 'center',
    color: '#000',
  },
});