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
- Przechowywanie tweetów przez określoną przez użytkownika ilość dni  
- Analiza sentymentu na przestrzeni czasu   
- Losowanie przykładowych tweetów o różnym poziomie sentymentu dla danego hasztagu  
- Zrobienie wykresów ogólnego sentymentu i sentymentu w przedziale czasowym  
- Prezentacja wykresów dla wielu hasztagów w aplikacji webowej  

## Stos technologiczny:
- Python (Flask)  
- mysql  
- Azure  
- HTML, CSS, JS

## Architektura
![Diagram architektury](Diagram_architektury.png)

## Instrukcja reprodukcji rozwiązania

### Harmonogram:
•	Pobieranie i przetwarzanie danych z Twitter API, baza danych - 21.12  
•	Połączenie modelu analizy sentymentu ( cognitive services sentiment text analysis ) z bazą danych - 4.01  
•	Generowanie wykresów, prezentacja wyników analizy - 14.01  
•	Gotowa Aplikacja webowa  - 27.01  
