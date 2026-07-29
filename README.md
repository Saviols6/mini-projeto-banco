
# Mini-Projeto 2 - Aplicação Full-Stack de Sistema Bancário em Python com Programação Orientada a Objetos

# Estrutura do Projeto
### Vamos organizar nosso projeto na seguinte estrutura de pastas e arquivos:
```
Mini-Projeto2/
├── dsaentidades/
│   ├── __init__.py
│   ├── sgcliente.py
│   └── sgconta.py
├── dsaoperacoes/
│   ├── __init__.py
│   └── banco.py
├── dsautilitarios/
│   ├── __init__.py
│   └── sgexceptions.py
└── sg_mini_projeto2.py
```

# Descrição:

sgentidades/: Contém as classes que representam as entidades de dados do nosso sistema (Cliente, Conta).

sgoperacoes/: Contém a lógica de negócio e as operações principais (a classe Banco que gerencia tudo).

sgutilitarios/: Contém utilitários, como exceções customizadas.

sg_mini_projeto2.py: É o ponto de entrada da nossa aplicação, responsável pela interface com o usuário (CLI - Command Line Interface).

Lembre-se todas as pastas com os módulos precisam ter um arquivo vazio nomeado "__init__.py", para que sejam reconhecidas como módulos python.

# Execução:

### Abra o terminal ou prompt de comando, navegue até a pasta com os arquivos do Mini-Projeto e execute o comando abaixo:

python sg_mini_projeto2.py
