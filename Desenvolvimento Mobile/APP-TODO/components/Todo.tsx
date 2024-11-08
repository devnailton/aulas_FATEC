//Arquivo Todo.tsx

import React from 'react';
import { Text, View, StyleSheet, TouchableOpacity, ViewStyle } from 'react-native';

interface TodoProps {
  name: string;
  onDelete: () => void; // Adicionei uma função para deletar a tarefa
  style?: ViewStyle;
}

export default function Todo({ name, onDelete, style }: TodoProps) {
  return (
    <View style={[styles.container, style]}>
      <Text style={styles.text}>{name}</Text>
      <TouchableOpacity onPress={onDelete} style={styles.deleteButton}>
        <Text style={styles.deleteText}>X</Text> {/* Botão de deletar */}
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    padding: 5,
    backgroundColor: '#f0f0f0',
    borderRadius: 5,
    flexDirection: 'row', // Para alinhar texto e botão na mesma linha
    justifyContent: 'space-between', // Espaçamento entre texto e botão
    alignItems: 'center', // Alinhar verticalmente
  },
  text: {
    color: '#000',
    fontSize: 18,
    flex: 1, // Permite que o texto ocupe o espaço restante
  },
  deleteButton: {
    padding: 5,
    marginLeft: 10,
  },
  deleteText: {
    color: 'black', // Cor do texto do botão de deletar
    fontWeight: 'bold',
  },
});