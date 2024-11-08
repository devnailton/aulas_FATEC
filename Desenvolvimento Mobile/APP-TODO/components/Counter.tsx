import React from 'react';
import{View, Text, StyleSheet, ViewStyle} from 'react-native';


interface CounterProps{
  name: string;
  value:number;
  style?:ViewStyle;
}


const Counter:React.FC<CounterProps>=({name,value,style}) =>{
  return(
    <View style={[styles.container,style]}>
      <Text>{name}: {value}</Text>
    </View>
  );
};


const styles = StyleSheet.create({
  container:{
    padding:10,
    backgroundColor: '#b0d7d0',
    borderRadius:5,
    borderWidth:1,
    borderColor:'#ccc',
    marginTop:10,
    alignItems:'center'
  },
});


export default Counter;