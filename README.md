# resmon-auth

Zanim zaczniesz pracować z repozytorium resmon-auth:
a) Wykonaj 'source ./resmon-auth-env.sh'

Generowanie Dokumentacji:
a) sh docgen.sh

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
