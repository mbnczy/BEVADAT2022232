# %%
import numpy as np

# %%
#FONTOS!!!

# CSAK OTT LEHET HASZNÁLNI FOR LOOP-OT AHOL A FELADAT KÜLÖN KÉRI!
# [1,2,3,4] --> ezek az értékek np.array-ek. Ahol listát kérek paraméterként ott külön ki fogom emelni!
# Ha végeztél a feladatokkal, akkor notebook-ot alakítsd át .py.
# A FÁJLBAN CSAK A FÜGGVÉNYEK LEGYENEK! (KOMMENTEK MARADHATNAK)

# %%
# Írj egy olyan fügvényt, ami megfordítja egy 2d array oszlopait. Bemenetként egy array-t vár.
# Be: [[1,2],[3,4]]
# Ki: [[2,1],[4,3]]
# column_swap()

# %%
def column_swap(arr : np.array) -> np.array:
    return np.array(arr)[:,::-1]

# %%
# Készíts egy olyan függvényt ami összehasonlít két array-t és adjon vissza egy array-ben, hogy hol egyenlőek 
# Pl Be: [7,8,9], [9,8,7] 
# Ki: [1]
# compare_two_array()
# egyenlő elemszámúakra kell csak hogy működjön

# %%
def compare_two_array(arr1 : np.array,arr2 : np.array) -> np.array:
    return np.flatnonzero(np.equal(np.array(arr1),np.array(arr2)).astype(int))

# %%
# Készíts egy olyan függvényt, ami vissza adja string-ként a megadott array dimenzióit:
# Be: [[1,2,3], [4,5,6]]
# Ki: "sor: 2, oszlop: 3, melyseg: 1"
# get_array_shape()
# 3D-vel még műküdnie kell!, 

# %%
def get_array_shape(arr) -> str:
    try:
        melyseg=len(arr[0][0]) 
    except: 
        melyseg=1
    return f"sor: {len(arr)}, oszlop: {len(arr[0])}, melyseg: {melyseg}"
#print(get_array_shape([[1,2,3], [4,5,6]]))

# %%
# Készíts egy olyan függvényt, aminek segítségével elő tudod állítani egy neurális hálózat tanításához szükséges pred-et egy numpy array-ből. 
# Bementként add meg az array-t, illetve hogy mennyi class-od van. Kimenetként pedig adjon vissza egy 2d array-t, ahol a sorok az egyes elemek. 
# Minden nullákkal teli legyen és csak ott álljon egyes, ahol a bementi tömb megjelöli. 
# Pl. ha 1 van a bemeneten és 4 classod van, akkor az adott sorban az array-ban a [1] helyen álljon egy 1-es, a többi helyen pedig 0.
# Be: [1, 2, 0, 3], 4
# Ki: [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# encode_Y()

# %%
def encode_Y(arr: np.array,cl : int) -> np.array:
    shape = np.array(arr).shape[0]
    pred =np.zeros((shape,cl),int)
    pred[np.arange(shape),arr]=1
    return pred
#print(encode_Y([1, 2, 0, 3], 4))

# %%
# A fenti feladatnak valósítsd meg a kiértékelését. Adj meg a 2d array-t és adj vissza a decodolt változatát
# Be:  [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# Ki:  [1, 2, 0, 3]
# decode_Y()

# %%
def decode_Y(pred : np.array) -> np.array:
    return np.argmax(pred,axis=1)
#print(decode_Y([[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]))

# %%
# Készíts egy olyan függvényt, ami képes kiértékelni egy neurális háló eredményét! 
# Bemenetként egy listát és egy array-t és adja vissza azt az elemet, aminek a legnagyobb a valószínüsége(értéke) a listából.
# Be: ['alma', 'körte', 'szilva'], [0.2, 0.2, 0.6]. # Az ['alma', 'körte', 'szilva'] egy lista!
# Ki: 'szilva'
# eval_classification()

# %%
def eval_classification(arr : np.array, lst : list) -> str:
    return arr[np.argmax(lst)]
#print(eval_classification(['alma', 'körte', 'szilva'], [0.2, 0.2, 0.6]))

# %%
# Készíts egy olyan függvényt, ahol az 1D array-ben a páratlan számokat -1-re cseréli
# Be: [1,2,3,4,5,6]
# Ki: [-1,2,-1,4,-1,6]
# repalce_odd_numbers()

# %%
def replace_odd_numbers(arr : np.array)->np.array:
    arr=np.array(arr)
    return np.where(arr%2==1,-1,arr)
    #arr[arr % 2 == 1] = -1
    #return arr
#print(repalce_odd_numbers([1,2,3,4,5,6]))

# %%
# Készíts egy olyan függvényt, ami egy array értékeit -1 és 1-re változtatja, attól függően, hogy az adott elem nagyobb vagy kisebb a paraméterként megadott számnál.
# Ha a szám kisebb mint a megadott érték, akkor -1, ha nagyobb vagy egyenlő, akkor pedig 1.
# Be: [1, 2, 5, 0], 2
# Ki: [-1, 1, 1, -1]
# replace_by_value()

# %%
def replace_by_value(arr : np.array,num : int)->np.array:
    arr=np.array(arr)
    return np.where(arr>num,1,-1)
#print(replace_by_value([1, 2, 5, 0], 2))

# %%
# Készíts egy olyan függvényt, ami egy array értékeit összeszorozza és az eredményt visszaadja
# Be: [1,2,3,4]
# Ki: 24
# array_multi()
# Ha több dimenziós a tömb, akkor az egész tömb elemeinek szorzatával térjen vissza

# %%
def array_multi(arr : np.array)->int:
    arr=np.array(arr,int)
    return np.prod(arr)
#print(array_multi([1,2,3,4]))

# %%
# Készíts egy olyan függvényt, ami egy 2D array értékeit összeszorozza és egy olyan array-el tér vissza, aminek az elemei a soroknak a szorzata
# Be: [[1, 2], [3, 4]]
# Ki: [2, 12]
# array_multi_2d()

# %%
def array_multi_2d(arr : np.array)->np.array:
    return np.prod(arr,axis=1)
#print(array_multi_2d([[1, 2], [3, 4]]))

# %%
# Készíts egy olyan függvényt, amit egy meglévő numpy array-hez készít egy bordert nullásokkal. Bementként egy array-t várjon és kimenetként egy array jelenjen meg aminek van border-je
# Be: [[1,2],[3,4]]
# Ki: [[0,0,0,0],[0,1,2,0],[0,3,4,0],[0,0,0,0]]
# add_border()


# %%
def add_border(arr : np.array) -> np.array:
    arr=np.array(arr)
    padded=np.zeros(np.array(arr.shape)+2)
    padded[1:-1,1:-1]=arr
    return padded
#print(add_border([[1,2],[3,4]]))

# %%
# A KÖTVETKEZŐ FELADATOKHOZ NÉZZÉTEK MEG A NUMPY DATA TYPE-JÁT!

# %%
from datetime import datetime, timedelta, date

# %%
# Készíts egy olyan függvényt ami két dátum között felsorolja az összes napot és ezt adja vissza egy numpy array-ben. A fgv ként str vár paraméterként 'YYYY-MM' formában.
# Be: '2023-03', '2023-04'  # mind a kettő paraméter str.
# Ki: ['2023-03-01', '2023-03-02', .. , '2023-03-31',]
# list_days()

# %%
def list_days(start_date:str, end_date:str)->np.array:
  start_date = datetime.strptime(start_date, '%Y-%m')
  end_date = datetime.strptime(end_date, '%Y-%m')
  return np.arange(start_date,end_date,dtype = 'datetime64[D]')
#print(list_days('2023-03', '2023-04'))

# %%
# Írj egy függvényt ami vissza adja az aktuális dátumot az alábbi formában: YYYY-MM-DD. Térjen vissza egy 'numpy.datetime64' típussal.
# Be:
# Ki: 2017-03-24


# %%

import datetime
def datenow()->str:
    return date.today()
#print(datenow())

# %%
# Írj egy olyan függvényt ami visszadja, hogy mennyi másodperc telt el 1970 január 01. 00:02:00 óta. Int-el térjen vissza
# Be: 
# Ki: másodpercben az idó, int-é kasztolva
# sec_from_1970()

# %%
def sec_from_1970()->int:
    a=np.datetime64('1970-01-01T00:02:00')
    now=np.datetime64('now')
    return (now-a).astype('timedelta64[s]').astype(int)
#print(sec_from_1970())


