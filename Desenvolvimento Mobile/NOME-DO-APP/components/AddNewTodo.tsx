import React from 'react';
import{TextInput, TouchableOpacity, View, Text} from 'react-native';
import{styles} from './styles';


interface AddNewTodoProps {
    onChange: (text: string)=> void;
    onPress: ()=> void;
    value:string;
}

export const AddNewTodo: React.FC<AddNewTodoProps>=({onPress, onChange, value})=>{
    return(
     <View style={styles.container}>
      <TextInput
       style={styles.inputField}
       placeholder='Adicione uma nova tareefa'
       placeholderTextColor='#808080'
       onChangeText={onChange}
       value={value}
       />
     <TouchableOpacity onPress={onPress} style={styles.button}>
      <View style={styles.iconButton}>
       <Text style={styles.textButton}>+</Text>
      </View>
     </TouchableOpacity>
    </View>
    );
};