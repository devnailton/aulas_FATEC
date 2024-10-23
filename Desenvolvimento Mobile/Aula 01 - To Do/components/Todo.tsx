//Arquivo Todo.tsx

import React from 'react';
import { View, Text, StyleSheet, ViewStyle } from 'react-native';

interface TodoProps {
  name: string;
  style?: ViewStyle;
}

export default function Todo({ name, style }: TodoProps) {
  return (
    <View style={[styles.container, style]}>
      <Text>{name}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    padding: 5
  },
});