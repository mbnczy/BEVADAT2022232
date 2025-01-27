"""
1.  Értelmezd az adatokat!!!
    A feladat megoldásához használd a NJ transit + Amtrack csv-t a moodle-ból.
    A NJ-60k az a megoldott. Azt fogom használni a modellek teszteléséhez, illetve össze tudod hasonlítani az eredményedet.    

2. Írj egy osztályt a következő feladatokra:  
     2.1 Neve legyen NJCleaner és mentsd el a NJCleaner.py-ba. Ebben a fájlban csak ez az osztály legyen.
     2.2 Konsturktorban kapja meg a csv elérési útvonalát és olvassa be pandas segítségével és mentsük el a data (self.data) osztályszintű változóba 
     2.3 Írj egy függvényt ami sorbarendezi a dataframe-et 'scheduled_time' szerint növekvőbe és visszatér a sorbarendezett df-el, a függvény neve legyen 'order_by_scheduled_time' és térjen vissza a df-el  
     2.4 Dobjuk el a from és a to oszlopokat, illetve azokat a sorokat ahol van nan és adjuk vissza a df-et. A függvény neve legyen 'drop_columns_and_nan' és térjen vissza a df-el  
     2.5 A date-et alakítsd át napokra, pl.: 2018-03-01 --> Thursday, ennek az oszlopnak legyen neve a 'day'. Ezután dobd el a 'date' oszlopot és térjen vissza a df-el. A függvény neve legyen 'convert_date_to_day' és térjen vissza a df-el   
     2.6 Hozz létre egy új oszlopot 'part_of_the_day' névvel. A 'scheduled_time' oszlopból számítsd ki az alábbi értékeit. A 'scheduled_time'-ot dobd el. A függvény neve legyen 'convert_scheduled_time_to_part_of_the_day' és térjen vissza a df-el  
         4:00-7:59 -- early_morning  
         8:00-11:59 -- morning  
         12:00-15:59 -- afternoon  
         16:00-19:59 -- evening  
         20:00-23:59 -- night  
         0:00-3:59 -- late_night  
    2.7 A késéseket jelöld az alábbiak szerint. Az új osztlop neve legyen 'delay'. A függvény neve legyen pedig 'convert_delay' és térjen vissza a df-el
         0min <= x < 5min   --> 0  
         5min <= x          --> 1  
    2.8 Dobd el a felesleges oszlopokat 'train_id' 'scheduled_time' 'actual_time' 'delay_minutes'. A függvény neve legyen 'drop_unnecessary_columns' és térjen vissza a df-el
    2.9 Írj egy olyan metódust, ami elmenti a dataframe első 60 000 sorát. A függvénynek egy string paramétere legyen, az pedig az, hogy hova mentse el a csv-t (pl.: 'data/NJ.csv'). A függvény neve legyen 'save_first_60k'. 
    2.10 Írj egy függvényt ami a fenti függvényeket összefogja és megvalósítja (sorbarendezés --> drop_columns_and_nan --> ... --> save_first_60k), a függvény neve legyen 'prep_df'. Egy paramnétert várjon, az pedig a csv-nek a mentési útvonala legyen. Ha default value-ja legyen 'data/NJ.csv'

3.  A feladatot a HAZI06.py-ban old meg.
    Az órán megírt DecisionTreeClassifier-t fit-eld fel az első feladatban lementett csv-re. 
    A feladat célja az, hogy határozzuk meg azt, hogy a vonatok késnek-e vagy sem. 0p <= x < 5p --> nem késik (0), ha 5p <= x --> késik (1).
    Az adatoknak a 20% legyen test és a splitelés random_state-je pedig 41 (mint órán)
    A testset-en 80% kell elérni. Ha megvan a minimum százalék, akkor azzal paraméterezd fel a decisiontree-t és azt kell leadni.

    A leadásnál csak egy fit kell, ezt azzal a paraméterre paraméterezd fel, amivel a legjobb accuracy-t elérted.

    A helyes paraméter megtalálásához használhatsz grid_search-öt.
    https://www.w3schools.com/python/python_ml_grid_search.asp 

4.  A tanításodat foglald össze 4-5 mondatban a HAZI06.py-ban a fájl legalján kommentben. Írd le a nehézségeket, mivel próbálkoztál, mi vált be és mi nem. Ezen kívül írd le 10 fitelésed eredményét is, hogy milyen paraméterekkel probáltad és milyen accuracy-t értél el. 
Ha ezt feladatot hiányzik, akkor nem fogadjuk el a házit!

HAZI-
    HAZI06-
        -NJCleaner.py
        -HAZI06.py

##################################################################
##                                                              ##
## A feladatok közül csak a NJCleaner javítom unit test-el      ##
## A decision tree-t majd manuálisan fogom lefuttatni           ##
## NJCleaner - 10p, Tanítás - acc-nál 10%-ként egy pont         ##
## Ha a 4. feladat hiányzik, akkor nem tudjuk elfogadni a házit ##
##                                                              ##
##################################################################
"""
import pandas as pd
from src.DecisionTreeClassifier import DecisionTreeClassifier
from NJCleaner import NJCleaner
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# train_id,stop_sequence,from_id,to_id,actual_time,delay_minutes,status,line,type,day,part_of_the_day,delay
col_name = [
    "stop_sequence",
    "from_id",
    "to_id",
    "status",
    "line",
    "type",
    "day",
    "part_of_the_day",
    "delay",
]
njc = NJCleaner("HAZI/HAZI06/2018_03.csv")
njc.prep_df("HAZI/HAZI06/data.csv")

data = pd.read_csv(
    "HAZI/HAZI06/data.csv",
    skiprows=1,
    header=None,
    names=col_name,
)

X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values.reshape(-1, 1)
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=41
)
print("splitted")

dtree = DecisionTreeClassifier(min_samples_split=120, max_depth=18)
print("dtc init")
dtree.fit(X_train, Y_train)
print("dtc fitted")
Y_pred = dtree.predict(X_test)
print("predicted")
print(accuracy_score(Y_test, Y_pred))

"""
A feltanítás paramétereinek először az órán használt értékeket adtam meg.
Számítottam arra, hogy nem lesz túl eredményes, az iris.csv 151 rekordból áll ami nagyon kevés 2018_03.csv-hez képest, 
illetve csak 4 független változóból áll a tábla, míg a most használt táblában dupla ennyi volt. 
A sokszoros rekordszám miatt jóval megnöveltem a min_samples_split értékét, 
a dupla adag független változóból adódóan pedig nem kisebb léptékben, de növeltem a max_depth értékét is.
Írtam egy test osztályt, amivel megnéztem, hogy különböző paraméterekkel mennyiben változik becslések pontossága.
Több mint egy óra futási idő után ezeket az eredményeket kaptam:

min_samples_split: 0, max_depth: 0, accuracy: 0.7765, time: 0.0055
min_samples_split: 0, max_depth: 6, accuracy: 0.7883, time: 0.0230
min_samples_split: 0, max_depth: 12, accuracy: 0.7907, time: 0.0426
min_samples_split: 0, max_depth: 18, accuracy: 0.7809, time: 0.0543
min_samples_split: 0, max_depth: 24, accuracy: 0.7658, time: 0.0615
min_samples_split: 0, max_depth: 30, accuracy: 0.7645, time: 0.0605
min_samples_split: 30, max_depth: 0, accuracy: 0.7765, time: 0.0054
min_samples_split: 30, max_depth: 6, accuracy: 0.7883, time: 0.0234
min_samples_split: 30, max_depth: 12, accuracy: 0.796, time: 0.0410
min_samples_split: 30, max_depth: 18, accuracy: 0.7966, time: 0.0514
min_samples_split: 30, max_depth: 24, accuracy: 0.7903, time: 0.0533
min_samples_split: 30, max_depth: 30, accuracy: 0.7901, time: 0.0528
min_samples_split: 60, max_depth: 0, accuracy: 0.7765, time: 0.0053
min_samples_split: 60, max_depth: 6, accuracy: 0.7883, time: 0.0232
min_samples_split: 60, max_depth: 12, accuracy: 0.7969, time: 0.0401
min_samples_split: 60, max_depth: 18, accuracy: 0.7973, time: 0.0477
min_samples_split: 60, max_depth: 24, accuracy: 0.7946, time: 0.0498
min_samples_split: 60, max_depth: 30, accuracy: 0.7945, time: 0.0492
min_samples_split: 90, max_depth: 0, accuracy: 0.7765, time: 0.0054
min_samples_split: 90, max_depth: 6, accuracy: 0.7886, time: 0.0226
min_samples_split: 90, max_depth: 12, accuracy: 0.798, time: 0.0387
min_samples_split: 90, max_depth: 18, accuracy: 0.7991, time: 0.0454
min_samples_split: 90, max_depth: 24, accuracy: 0.7969, time: 0.0474
min_samples_split: 90, max_depth: 30, accuracy: 0.7969, time: 0.0463
min_samples_split: 120, max_depth: 0, accuracy: 0.7765, time: 0.0053
min_samples_split: 120, max_depth: 6, accuracy: 0.7886, time: 0.0225
min_samples_split: 120, max_depth: 12, accuracy: 0.7994, time: 0.0385
min_samples_split: 120, max_depth: 18, accuracy: 0.8002, time: 0.0436
min_samples_split: 120, max_depth: 24, accuracy: 0.7994, time: 0.0448
min_samples_split: 120, max_depth: 30, accuracy: 0.7994, time: 0.0441

Ezek közül a 120-18-as kombináció adta a legpontosabb becsléseket,
habár futási idő szempontjából nem ez volt a legjobb. 
"""
