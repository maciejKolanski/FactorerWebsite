Skip to content
This repository  
Search
Pull requests
Issues
Gist
 @maciejKolanski
 Unwatch 4
  Star 0
  Fork 0 maciejKolanski/AIiR_CZ1115_FaktoryzacjaLiczby
 Code  Issues 0  Pull requests 0  Wiki  Pulse  Graphs  Settings
Branch: master Find file Copy pathAIiR_CZ1115_FaktoryzacjaLiczby/README.md
fc792ab  2 days ago
@BartoszJanusz BartoszJanusz Update README.md
4 contributors @maciejKolanski @BartoszJanusz @piotrDowgiallo @DurajR
RawBlameHistory     118 lines (74 sloc)  8.18 KB
Faktoryzacja dużej liczby z użyciem obliczeń rozproszonych (AIiR_CZ1115)
1. Temat projektu

W dzisiejszych czasach, gdy właściwie wszystko co robimy w jakiś sposób połączone jest z Internetem bezpieczeństwo jest bardzo ważnym tematem.

Faktoryzacja jest to proces podczas którego dla zadanego obiektu odnajduje się inne obiekty, które spełniają to, że ich iloczyn równy jest oryginalnemu obiektowi, w związku z czym te znalezione czynniki są w pewnym sensie od niego prostsze.

Podstawowy algorytm faktoryzacji bazuje na próbowaniu podziału liczby do faktoryzacji n przez wszystkie liczby pierwsze od 2 do √n. Tego typu algorytm bardzo dobrze radzi sobie z początkiem faktoryzacji liczby, bo dowolna liczba ma czynnik zarówno małe jak i duże. Jak wiadomo połowa wszystkich liczb dzieli się przez dwa, jedna trzecia licz przez trzy i tak dalej, a więc z dużym prawdopodobieństwem można pozbyć się w prosty sposób niskich czynników.

RSA jest to jeden z pierwszych i też obecnie najpopularniejszych asymetrycznych algorytmów kryptograficznych gdzie klucz jest publiczny. Bezpieczeństwo szyfrowania przy pomocy tego algorytmu jest związane z trudnością faktoryzacji dużych liczb.

2. Zakres projektu

Cel

Celem projektu jest umożliwienie zlecenia zadania faktoryzacji dużej liczby (większych od 2^64 -1). Jednym z głównych założeń jest udostępnienie prostego w obsłudze interfejsu użytkownika i zmaksymalizowanie elastyczności – system powinień być zdolny do współpracy z zadanymi komputerami, a instalacja wymaganego oprogramowania musi być prosta.

Funkcjonalność

Podstawa:

Udostępnienie mechanizmów rejestracji i logowania (konta użytkowników)
Zarządzanie zadaniami z poziomu interfejsu webowego
zlecanie zadań
przegląd historii
Możliwość rozbudowy klastra bez ingerencji w kod
Faktoryzacja metodą „brutalnej siły”
Faktoryzacja metodą CFRAC
Zachowywanie wyników pomyślanie wykonanych faktoryzacji
Rozszerzenie:

Łamanie szyfru RSA
Faktoryzacja metodą sita kwadratowego
Forma graficznej prezentacji wyników pomiarów
3. Narzędzia i technologie zastosowane w projekcie

alt tag

Zastosowane technologie:

Strona klienta - HTML5, CSS

Interfejs z którego bedzie korzystal klient projektowanego systemu bedzie napisany w jezyku skryptowym HTML5 z użyciem stylów CSS. HTML5 jest obecnie standardem przy tworzeniu stron internetowych i w wiekszosci wyparl HTML4, w którego specyfikacji bylo duzo niescislosci. Uzycie CSS z kolei pozwoli ujednolicic prezentacje zawartosci w różnych przegladarkach, oraz uprosci organizacje samego kodu.

Aplikacja Webowa - Python 3.4 + Django 1.8.7

Python jest jezykiem wysokiego poziomu ogólnego przeznaczenia, z kolei Django to framework webowy dla tego jezyka. Wybralismy ten zestaw z powodu wielu ulatwień przy tworzeniu aplikacji webowych, które sa przezeń oferowane, np. dynamiczny interfejs bazy danych, automatyczny interfejst administracyjny. Dodatkowo czesc naszej grupy jest zaznajomiona z tymi technologiami, wiec nie ma potrzeby poznawania ich od zera. Istotne sa tutaj wersje srodowisk - najnowsze dystrybucje nie obsluguja MySQL, w zwiazku z tym wybralismy poprzednie.

Baza danych - MySQL

SZBD rozwijany przez firme Oracle. Charakteryzuje sie wszystkimi najwazniejszymi funkcjonalnosciami bazy danych oraz prostota tworzenia takiej bazy. Rozważalismy zastosowanie systemu Oracle Database, jednakże jest on zbyt rozbudowany jak na nasze potrzeby, a co za tym idzie trudny w obsudze. Mamy również doswiadczenie w integracji bazy MySQL z aplikacjami napisanymi w Pythonie (Django).

Klaster obliczeniowy - standard MPI, implementacja MPICH2

MPICH2 to darmowa implementacja standardu MPI dla systemów Linux. Umożliwa proste tworzenie klastrów obliczeniowych, rozdzielania zadań miedzy poszczególne wezly i zbierania wyników. Oferuje interfejs dla jezyka C++. Jest wykorzystywany w wiekszosci topowych urzadzen wieloprocesorowych i ta popularnosc znaczaco wplynelo na jego wybór.

Aplikacaja rozproszona - C++ 11

Wybór padl na ten jezyk ze wzgledu na jego znajomosc przez czlonków grupy oraz interfejs udostepniany przez srodowisko MPICH2.

Narzedzia wykorzystane w projekcie:

Aplikacja webowa - PyCharm 5.0.4 - IDE do Pythona, obsuguje Django
Aplikacja rozproszona - CodeLite 9.1 IDE do C++, wersja na system Linux
Baza danych - developer do MySQL
Organizacja pracy - Trello (https://trello.com/)
Hosting plików - GitHub (https://github.com/)

4. Aktualny stan rynku

[jakie są podobne dostępne rozwiązania, co zostało w tej dziedzinie zrobione]

GGNFS (GPL'd implementation of General Number Field Sieve) - aktywny rozwój. faktoryzacja liczb do 180 znaków, srednio do 140. Kilka wiekszych liczb tez. W wiekszosci przypadkow program GGNFS jest stabilny dla liczb skladajacych sie do 150-160 znakow. Posiada bugi.Nie jest czarna skrzynka, trzeba miec odpowiednia wiedze zeby go uzywac

Opensource /\

tylko wartosc badawcza :

1.Cunningham Project Projekt faktoryzujacy liczby b^n +-1 dla b=2,3,5,6,7,10,11,12 i duze n.

http://homes.cerias.purdue.edu/~ssw/cun/

RSA Factoring Challenge - zawody zorganizowane przez RSA Security. Otwarte zawody dla wszystkich mające na celu zwiększyć zainteresowanie faktoryzacją liczb. Opublikowana została lista pseudopierwszych liczb (rozkładających się na dokładnie dwa czynniki), nazwanych liczbami RSA.Za rozłożenie niektórych z nich wyznaczono pieniężną nagrodę. Najmniejsza z nich, 100-cyfrowa liczba RSA-100 została rozłożona w ciągu kilku dni, ale większość do dziś pozostaje niezłamana.Zawody miały na celu śledzenie rozwoju możliwości komputerów w faktoryzacji. Jest to niezwykle istotne przy wyborze długości klucza w szyfrowaniu asymetrycznym metodą RSA. Postęp w łamaniu kolejnych liczb powinien zdradzać jakie długości klucza można jeszcze uznawać za bezpieczne. (wikipedia)
Poczatkowo, rekordy były bite za pomoca algorytmu CFRAC, który ustapił dopiero w latach 8XX w. algorytmowi sita kwadratowego. Za pomoca algorytmu QS sfaktoryzowano, miedzy innymi,liczby RSA-100, RSA-110, RSA-120 i RSA-129 [5]. Nast˛epnie na scen˛e wkroczył algorytm sita ciałliczbowego, który do dzis pozostaje najszybszym ze znanych algorytmów faktoryzacji i dzier ´ zy rekordy - najpierw RSA-640 (640 bitów, 193 cyfry) i RSA-200 (200 cyfr) w 2005 roku, a nast˛epnie RSA-768(232 cyfry) w 2009 roku, co pozostaje niepobitym rekordem do dzis [19, 20, 21].

praca mgr Mateusz Niezabitkowski http://ki.agh.edu.pl/sites/default/files/usefiles/172/theses/mateusz.niezabitowski.algorytmy.faktoryzacji.w.zastosowaniach.kryptograficznych.v1.0-final.pdf

Implementacje (eng wiki) : Some implementations focus on a certain smaller class of numbers. These are known as special number field sieve techniques, such as used in the Cunningham project. A project called NFSNET ran from 2002[6] through at least 2007. It used volunteer distributed computing on the Internet.[7] Paul Leyland of the United Kingdom and Richard Wackerbarth of Texas were involved.[8]

Until 2007, the gold-standard implementation was a suite of software developed and distributed by CWI in the Netherlands, which was available only under a relatively restrictive license. In 2007, Jason Papadopoulos developed a faster implementation of final processing as part of msieve, which is in the public domain. Both implementations feature the ability to be distributed among several nodes in a cluster with a sufficiently fast interconnect.

Polynomial selection is normally performed by GPL software written by Kleinjung, or by msieve, and lattice sieving by GPL software written by Franke and Kleinjung; these are distributed in GGNFS.

NFS@Home GGNFS pGNFS factor by gnfs CADO-NFS msieve, which contains excellent final-processing code, a good implementation of the polynomial selection which is very good for smaller numbers, and an implementation of the line sieve. kmGNFS

ElvenSmooth - projekt (... jeszcze nie doczytalem o nim dokladnie) http://home.earthlink.net/~elevensmooth/

Factorizations of Cyclotomic Numbers http://www.asahi-net.or.jp/~KC2H-MSM/cn/
Status API Training Shop Blog About Pricing
© 2016 GitHub, Inc. Terms Privacy Security Contact Help
