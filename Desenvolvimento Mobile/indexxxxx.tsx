import React from 'react';
import { View, Text, Image, StyleSheet, ScrollView } from 'react-native';

const App = () => {
  return (
    <ScrollView contentContainerStyle={styles.container}>
      {/* Foto da pessoa */}
      <Image 
        source={require('./assets/images/foto.jpg')} 
        style={styles.photo} 
      />

      {/* Nome da pessoa */}
      <Text style={styles.name}>John Doe</Text>

      {/* Experiências */}
      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Experiências</Text>
        <Text style={styles.sectionContent}>- Desenvolvedor Backend na APEYY Sistemas</Text>
        <Text style={styles.sectionContent}>- Professor de Tecnologia da Informação e Business Intelligence</Text>
        <Text style={styles.sectionContent}>- Consultor em Segurança de Dados e Engenharia Social</Text>
      </View>

      {/* Qualificações */}
      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Qualificações</Text>
        <Text style={styles.sectionContent}>- Especialista em Django e React</Text>
        <Text style={styles.sectionContent}>- Experiência em desenvolvimento mobile com React Native</Text>
        <Text style={styles.sectionContent}>- Conhecimentos avançados em AWS e Blockchain</Text>
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flexGrow: 1,
    alignItems: 'center',
    padding: 20,
    backgroundColor: '#f0f0f0',
  },
  photo: {
    width: 150,
    height: 150,
    borderRadius: 75,
    marginBottom: 20,
  },
  name: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 20,
  },
  section: {
    width: '100%',
    marginBottom: 20,
    paddingHorizontal: 10,
    paddingVertical: 15,
    backgroundColor: '#ffffff',
    borderRadius: 8,
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowOffset: { width: 0, height: 2 },
    shadowRadius: 4,
    elevation: 3,
  },
  sectionTitle: {
    fontSize: 22,
    fontWeight: '600',
    color: '#444',
    marginBottom: 10,
  },
  sectionContent: {
    fontSize: 16,
    color: '#666',
    marginBottom: 5,
  },
  
});

export default App;