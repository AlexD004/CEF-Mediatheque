# CEF Mediatheque

There is a project, designed and developped for my formation to become a fullstack developper.
It use Django with sqLite3 to structure and manage datas.
CEF Mediatheque permit to create, update and remove 'Livres', 'Cds', 'DVDs', 'Jeux' and 'Membres'.
You can also link one 'Membre' and one 'Media' (Livres, CDs or DVDs) to create one 'emprunt'.

## :magic_wand: Features

- ✨ Django
- ✨ CRUD for all items
- ✨ Create or Remove 'Emprunts'
- ✨ Restrictions for create a 'Emprunt' (3 max. and 1 week max)
- ✨ Logging operations
- ✨ Basics tests

## 🏗️ Getting Started

### 📄 Prerequisites

You'll need Python.

### 🔨 Installation

#### Create a virtuel environment for your mediatheque
From your command line :

```
py -m venv [environment-name]

# Exemple :
py -m venv CEF-Mediatheque
```

#### Clone this repository
From your command line, clone CEF-Mediatheque :

```sh
# Clone repository
$ git clone https://github.com/AlexD004/CEF-Mediatheque
```

### Running the Mediatheque

#### Return to the virtual environment root

```
cd ../
```

#### Going into the Scripts folder

```
cd Scripts
```

#### Activate the virtual environment

```
.\activate
```

#### Install Django
From your command line :

```
# Check if pip is installed
pip

# If not
py -m ensurepip --upgrade

# Then
pip install Django

```

#### Going into the app

```
cd CEF-Mediatheque
```

#### Run server

```
py manage.py runserver
```
