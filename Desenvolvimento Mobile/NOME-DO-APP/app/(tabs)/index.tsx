import React, { useState } from 'react';
import { ScrollView, View, Text, Image, StyleSheet, Button, Linking } from 'react-native';
import { TextInput } from 'react-native-gesture-handler';

export default function App() {
  const [name, setName] = useState('');
  const [emailAddress, setEmailAddress] = useState('');
  const [phone, setPhone] = useState('');

  // Função para abrir o WhatsApp
  const openWhatsApp = () => {
    const phoneNumber = '5566996555525';
    
    if (!name) {
      alert('Por favor, insira o seu nome');
      return;
    }
    
    const message = `Olá, meu nome é ${name}. Gostaria de saber mais sobre seus serviços.`;
    const url = `https://wa.me/${phoneNumber}?text=${encodeURIComponent(message)}`;

    Linking.canOpenURL(url)
      .then(supported => {
        if (supported) {
          return Linking.openURL(url);
        } else {
          alert("Não foi possível abrir o WhatsApp.");
        }
      })
      .catch(err => console.error('Erro ao abrir o WhatsApp:', err));
  };

  return (
    <ScrollView contentContainerStyle={styles.container}>
      {/* Foto */}
      <Image
        source={require('../../assets/images/foto.jpg')}
        style={styles.photo}
      />

      {/* Nome */}
      <Text style={styles.name}>Nailton Silva dos Santos</Text>

      {/* Experiências */}
      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Experiências</Text>
        <Text style={styles.sectionContent}>- Desenvolvedor Backend na Apey Sistemas</Text>
        <Text style={styles.sectionContent}>- Professor de Tecnologia da Informação e Business Intelligence</Text>
        <Text style={styles.sectionContent}>- Consultor em Segurança de Dados e Engenharia Social</Text>
      </View>

      {/* Qualificações */}
      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Qualificações</Text>
        <Text style={styles.sectionContent}>- Especialista em Django e React</Text>
        <Text style={styles.sectionContent}>- Experiência em desenvolvimento{"\n"}mobile com React Native</Text>
        <Text style={styles.sectionContent} numberOfLines={2}>- Conhecimentos avançados em AWS e Blockchain. Conhecimentos avançados em AWS e Blockchain. Conhecimentos avançados em AWS e Blockchain. Conhecimentos avançados em AWS e Blockchain. Conhecimentos avançados em AWS e Blockchain</Text>
      </View>

      {/* Formulário */}
      <View style={styles.container}>
        <TextInput
          style={styles.input}
          placeholder="Nome"
          value={name}
          onChangeText={setName}
        />
        <TextInput
          style={styles.input}
          placeholder="E-mail"   
          value={emailAddress}   
          onChangeText={setEmailAddress}
          keyboardType="email-address"
        />
        <TextInput
          style={styles.input}
          placeholder="Telefone"
          value={phone}
          onChangeText={setPhone}
          keyboardType="phone-pad"
        />
      </View>

      {/* Botão para abrir o WhatsApp */}
      <View style={styles.buttonContainer}>
        <Button
          title="Enviar pelo WhatsApp"
          color="#841584"
          onPress={openWhatsApp}
        />
      </View>
    </ScrollView>
  );
} 

const styles = StyleSheet.create({
  container: {
    flexGrow: 1,
    padding: 20,
    backgroundColor: '#f5f5f5',
  },
  photo: {
    width: 150,
    height: 150,
    borderRadius: 75,
    alignSelf: 'center',
    marginBottom: 20,
    marginTop: 20,
  },
  name: {
    fontSize: 24,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 20,
  },
  section: {
    marginBottom: 20,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 10,
  },
  sectionContent: {
    fontSize: 16,
    marginBottom: 5,
  },
  buttonContainer: {
    marginTop: 20,
    alignItems: 'center',
  },
  input: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 10,
    paddingHorizontal: 10,
  }
});
