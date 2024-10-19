# Exercício de Fixação sobre o conteúdo de Django
Esse repositório foi criado com o intuito de apresentar o exercício proposto pela orientação da disciplina de Desenvolvolvimento de Aplicações Web, especificamente sobre o conteúdo
de Django, ministrado em sala.

A app criada como exemplo tem como escôpo um RPG genérico, o que inclui as seguintes entidades:

- Personagem
- Ocupação
- Item

As entidades foram descritas como classes e implementadas como models do app "rpg".

Para o funcionamento do projeto é necessário, primordialmente, instalar as dependências com o comando
```
pip install Django
```
Em seguida, deve-se rodar o servidor com o projeto através do seguinte comando e, então, abrir o endereço local
```
python3 manage.py runserver
```
Caso se tenha interesse em adcionar instâncias ou apenas verificar as entidades, deve ser realizado pela página de admin, adicionando "/admin" ao final do endereço local, no navegador, e realizando o login
com as informações do super usuário.
Para cadastrar um super usuário (admin) utilize do seguinte comando e digite as informações requisitadas:
```
python3 manage.py createsuperuser
```
