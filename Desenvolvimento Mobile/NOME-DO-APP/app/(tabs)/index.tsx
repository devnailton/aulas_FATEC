import React from 'react';
import{SafeAreaView} from 'react-native';
import Home from '../../screens/Home';


export default function App() {
  return(
    <SafeAreaView style={{flex:2}}> 
     <Home/>
    </SafeAreaView>
  );
}