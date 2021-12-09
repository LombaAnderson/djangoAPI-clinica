# djangoAPI-clinica
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/LombaAnderson/djangoAPI-clinica/blob/main/LICENSE)

# Sobre o projeto
O projeto clínica é uma API de cadastro e gerenciamento de pacientes onde há a preocupação de disponibilizar uma plataforma de agendamentos e históricos de pacientes. Minha mãe trabalhou muitos anos em clínicas e hospitais e algumas vezes acompanhava seu trabalho, sei o quanto é importante ter um software semelhante ao que foi desenvolvido aqui com o poderoso Framework Django REST que permite a construção de APIs Rest utilizando o Django e nos coloca na "cara do gol" em relação à APIs. Inicialmente, para criar djangoAPI-clinica se configurou tudo o que foi implementado em um terminal. Nele é instalado o ambiente virtual Python e em seguida o Django.
Houve a preocupação em organizar os 'apps' na criação das pastas e demais funcionalidades de agendamentos, pacientes e histórico. O 'app' pacientes tem a funcionalidade de editar, cadastrar,incluir e apagar novo paciente. Dentro de pacientes é preciso criar uma pasta chamada api onde são incluídos mais dois arquivos: serializers.py e viewsets.py onde foi desenvolvida a API em si. Em todos além de seguir o mesmo que foi explicado sobre o 'app' anterior, é necessário a estruturação do 'models.py'.
Houve essencialmente a preocupação de testar tudo o que foi feito em três tipos de testes diferentes. O primeiro foi o teste manual, depois com a utilização do software Insomnia e por último foram realizados testes unitários.

## Imagem da página API com as três funcionalidades prontas 
<div align="center">
<img src="https://user-images.githubusercontent.com/60937513/145337203-c923f54d-0dd9-48ff-bcc3-54910d9c6743.png" width="600" />
</div>

## Exemplo do cadastro de pacientes 
<div align="center">
<img src="https://user-images.githubusercontent.com/60937513/145336879-89b72deb-fb00-474b-9c18-f5156b6e9c84.png" width="800" />
</div>

## Imagem que mostra o que é pedido no cadastro histórico
<div align="center">
<img src="https://user-images.githubusercontent.com/60937513/145337328-c604027a-4b1c-4dd6-867c-a635bc0c242d.png" width="800" />
</div>

# Tecnologias utilizadas

- Python
- API Django Rest
- asgiref==3.4.1
- autopep8==1.6.0
- djangorestframework==3.12.4
- pycodestyle==2.8.0
- python-decouple==3.5
- pytz==2021.3
- sqlparse==0.4.2
- toml==0.10.2
- tzdata==2021.5

# Testes unitários e manual
- Python
- Insomnia

# Instruções para compilar, testar e rodar o projeto

```bash
# Clonar repositório
git clone https://github.com/LombaAnderson/djangoAPI-clinica

# Criação e acesso da pasta do projeto
-mkdir clinica
-cd clinica

# Criação do ambiente de desenvolvimento do Python
-python -m venv venv

# Ativar o ambiente de desenvolvimento(venv)
-source venv/Scripts/activate

# Instalação do Django (Atenção: instalar somente após a ativação da venv)
-pip install django

# Instalação do pacote do Django Rest Framework
-pip install django djangorestframework
 
# Comando de criação do projeto
-django-admin startproject clinica .

# Criação do servidor
-python manage.py runserver

# Instalação do pytz(timezone)
pip install pytz

# Acesso ao servidor Django
http://127.0.0.1:8000/

# Apps 
-django-admin startapp pacientes
-django-admin startapp historicos
-django-admin startapp agendamentos

```

# Autor

Anderson Lomba de Oliveira

Linkedin

https://www.linkedin.com/in/anderson-lomba-140279142/

Portfólio

https://www.lombanderson.epizy.com

# Agradecimentos

Agradeço ao meu Deus que está sempre comigo e a minha esposa, minha companheira que amo muito! Agradeço também meus professores e desenvolvedores que me aturam às vezes em todas minhas perguntas curiosas sobre programação.



