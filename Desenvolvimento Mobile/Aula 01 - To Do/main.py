from fpdf import FPDF

# Criar o documento PDF
pdf = FPDF()

# Adicionar uma página
pdf.add_page()

# Definir título
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Explicação do Código React Native", ln=True, align='C')

# Adicionar subtítulo
pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, txt="Código de Componente Home", ln=True, align='L')

# Adicionar explicação do código
pdf.set_font("Arial", size=11)
texto = """
Este código implementa a tela inicial (`Home`) de uma aplicação de tarefas em React Native. A tela permite adicionar 
novas tarefas, exibir a lista de tarefas e contar quantas tarefas foram criadas.

- **Imports**: O código importa React e o hook `useState` para gerenciar o estado local da aplicação, além de componentes 
  visuais do React Native como `View` e `Text`. Também importa três componentes customizados: `AddNewTodo`, `Todo` e `Counter`.

- **Estado**:
  1. `tasks`: Um array de objetos que contém as tarefas, onde cada objeto tem um nome (`name`) e um status (`checked`).
  2. `newTask`: Armazena o valor da nova tarefa que o usuário está digitando.

- **Função handleTodoAdd**: Esta função é responsável por adicionar uma nova tarefa à lista de tarefas:
  - Verifica se o campo da nova tarefa está vazio. Caso esteja, a função retorna sem adicionar nada.
  - Verifica se já existe uma tarefa com o mesmo nome na lista. Se existir, exibe um alerta.
  - Caso contrário, adiciona a nova tarefa ao estado `tasks` e limpa o campo de entrada (`setNewTask('')`).

- **Renderização**:
  1. O componente renderiza um título "Lista de Tarefas" no topo da página.
  2. O componente `AddNewTodo` é utilizado para capturar o input do usuário e o botão para adicionar a tarefa.
  3. A lista de tarefas é renderizada dinamicamente utilizando o método `map`, onde cada tarefa é exibida através do componente `Todo`.
  4. O componente `Counter` exibe a quantidade de tarefas criadas, baseado no comprimento do array `tasks`.

- **Conclusão**: Este componente é a tela principal de uma aplicação de lista de tarefas. Ele permite adicionar novas 
  tarefas, visualizá-las na tela e manter um contador simples de quantas tarefas foram criadas.
"""

# Escrever o texto no PDF
pdf.multi_cell(0, 10, txt=texto)

# Salvar o PDF
output_path = "/mnt/data/explicacao_home_component.pdf"
pdf.output(output_path)

output_path
