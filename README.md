# EY_aspect_based_sentiment_analysis

[Live site](https://mango-sea-00caa9c03.azurestaticapps.net)

[Front-end repository](https://github.com/damaneks/sentimentAnalysis)

## Zespół
**Kamil Kowieski**  
Bartłomiej Łukasik  
Damian Wróblewski  

## Funkcjonalności:
- Wczytywanie tweetów z api twittera do bazy danych 
- aktualizacja bazy danych dla hasztagów codziennie o 4:30  
- Przechowywanie tweetów z zanalizowanym sentymentem w bazie
- Analiza sentymentu na przestrzeni czasu   
- Losowanie przykładowych tweetów o różnym poziomie sentymentu dla danego hasztagu  
- Zrobienie wykresów ogólnego sentymentu i sentymentu w przedziale czasowym  
- Prezentacja wykresów dla wielu hasztagów w aplikacji webowej  

## Stos technologiczny:
- Python (Flask)  
- Transact-sql  
- Azure  
- React

## Architektura
![Diagram architektury](Diagram_architektury.png)

## Instrukcja reprodukcji rozwiązania
- stworzenie bazy danych i tabel z kolumnami: (tekst, data, sentyment) dla każdego hashtagu
- pobieranie danych z twitter api
- analiza snetymentu przez TextAnalitics w Azure
- wgranie wyników do bazy
- stworzenie aplikacji webowej i backendu pobierającego dane z bazy i wyzwalającego update wyników

### Harmonogram:
- [x]	Pobieranie i przetwarzanie danych z Twitter API, baza danych - 21.12  
- [x]	Połączenie modelu analizy sentymentu ( cognitive services sentiment text analysis ) z bazą danych - 4.01  
- [x]	Generowanie wykresów, prezentacja wyników analizy - 14.01  
- [x]	Gotowa Aplikacja webowa  - 27.01  
