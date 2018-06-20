# ResMon-auth
Repository for authorization server, which is part of ResMon software.

**Very important!** The given key file (_./data/jwt.key_) is just used in test environment.
Please, don't use it in your production version!

**Info!** All path existing in this file are considered 
as being used in project/install root directory.

# Usage

```bash
./resmon-auth [-h] [-k KEY_PATH] [-p PORT]
```

**Info!** Key file has to be the same as in monitors 
which use this authorization server to confirm identity of users.
You have to generate key and to make sure that both this server and monitor 
use the same version of file.

### Options
| Option                                       | Default value  | Description                                |
| -------------------------------------------- |:--------------:| ------------------------------------------:|
| **-h**, **--help**                           | ---            | show help message and exit the application |
| **-k _KEY_PATH_**, **--key_path _KEY_PATH_** | ./data/jwt.key | Location where is stored secret key        |
| **-p _PORT_**, **--port _PORT_**             | 5000           | Port on which the server is listening      |

#Instalation
We provide single file `install-auth.sh` which is used to install this application. It's enough that you just run it as following:
```bash
./install-auth.sh [--quiet]
```
Later you have to accept unpacking files. It's automatically accepted if you choose option _--quiet_.
Application will be installed in the same place where script `install-auth.sh`

#For developers

You can run some scripts to make your developing process faster and more comfortable.
All scripts can be executed in this way:
```bash
./scripts.sh SCRIPT_NAME
```
where `SCRIPT_NAME` can be as following:
* `build` - it prepares file _install-auth.sh_ to use it later for installing this application
* `docgen` - it generates documentation and puts it into _./docs/_ directory
* `runtest` - it runs all tests available for this project in _./test/_ directory

**Info!** If you need to use environment file manually, it is located in `./data` directory.

## Deployment on Docker
You can develop this application on [Docker](https://docs.docker.com). It can be used to testing it in a clear environment. 
At start you can make yourself sure that the file `install-auth.sh` is created by _build_ script.

Then you can execute these two following commands:
```bash
docker build -t resmon-auth .
```
and:
```bash
docker run -p 5000:5000 -it resmon-auth
```
Then you can run there this application. 
Authorization server will be reachable on port 5000 (default).

1. jak działa serwer autoryzacji?

Serwer autoryzacji posiada dwie funkcje: logowanie i autoryzację. 
W przypadku rejestracji serwer dodaje do bazy danych użytkownika i zwraca token JWT (czyli użytkownik od razu jest zalogowany).
W przypadku logowania serwer sprawdza poprawność przesłanych danych (hasło jest zapisane w bazie w postaci zahasowanej).
Jest dodany także testowy endpoint /secret umożliwiający sprawdzenie czy token jest prawidłowy.

2. Jak go uruchomić?

python run.py

3. jaka jest jego struktura

run.py - skrypt uruchamiający serwer. Bardziej plik konfiguracyjny niż rzeczywisty kod.

model.py - plik zawierający klasę UserModel będącej modelem jedynej tabeli w bazie danych oraz funkcję do jego obsługi.
Na podstawie tej klasy tworzona i obsługiwana jest baza danych.

resources.py - plik zawierające klasy będące definicjami restowych zasobów. 

view.py - plik definiujący endpointy i łączący je z odpowiednimi zasobami restowymi.


4. Jak się go odpytuje?


REJESTRACJA:

POST /registration
{
    "username": "asd",
    "password": "asd"
}


LOGOWANIE:
POST /login
{
    "username": "asd",
    "password": "asd"
}

TEST:
GET /secret

Z tokenem w headerze w formie:

Authorization : Bearer {otrzymany token JWT}
np:
Authorization : Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1


5. Co dokładnie zwraca?

Endpoint /regiestration zwraca informację o dodaniu użytkownika do bazy danych i token JWT, lub informację, że użytkownik o takiej nazwie jest już w 
bazie danych.

Endpoint /login zwraca token JWT w przypadku otrzymanej prawidłowej nazwy użytkownika i hasła lub informację o nieprawidłowych otrzymanych danych.

Endpoint /secret zwraca json w postaci: {"valid":True} w przypadku przesłania zapytania z prawidłowym tokenem JWT


6. Jak tego użyć w monitorze?

Korzystając z biblioteki obsługującej JWT, skonfigurować ją tak aby korzystała z tego samego klucza prywatnego. 
Za jej pomocą sprawdzić czy otrzymany token JWT jest "valid" czy nie.

7. Użyte techologie.

Python 3.6
Flask 0.12.2
Flask-JWT-Extended 3.7.2
Flask-RESTful 0.3.6
Flask-SQLAlchemy 2.3.2
