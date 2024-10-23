//Arquivo Home.tsx

import React, { useState } from 'react';
import { View, Text } from 'react-native';
import { AddNewTodo } from '../components/AddNewTodo';
import Todo from '../components/Todo';
import Counter from '../components/Counter';

export default function Home() {
  const [tasks, setTasks] = useState<{ name: string; checked: boolean }[]>([]);
  const [newTask, setNewTask] = useState<string>('');

  const handleTodoAdd = () => {
    if (!newTask.trim()) return;
    const taskWithSameName = tasks.find(task => task.name === newTask);
    if (taskWithSameName) {
      alert('Tarefa já existe');
      return;
    }
    setTasks(prevState => [...prevState, { name: newTask, checked: false }]);
    setNewTask('');
  };

  return (
    <View>
      <Text style={{marginTop: 55, marginLeft: 20, fontWeight: 'bold', fontSize: 24}}>Lista de Tarefas</Text>
      <AddNewTodo onPress={handleTodoAdd} onChange={setNewTask} value={newTask} />
      {tasks.map((task, index) => (
        <Todo style={{ margin: 10 }} key={index} name={task.name} />
      ))}
      <Counter style={{ margin: 10 }} name="Criadas" value={tasks.length} />
    </View>
  );
}

const styles = {
  title: {
    fontSize: 24, 
    fontWeight: 'bold', 
    marginBottom: 20,
    textAlign: 'center', 
  },
};