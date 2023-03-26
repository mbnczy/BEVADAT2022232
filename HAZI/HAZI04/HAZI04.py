# %%
from tabulate import tabulate
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# %%
'''
FONTOS: Az első feladatáltal visszaadott DataFrame-et kell használni a további feladatokhoz. 
A függvényeken belül mindig készíts egy másolatot a bemenő df-ről, (new_df = df.copy() és ezzel dolgozz tovább.)
'''

# %%
'''
Készíts egy függvényt, ami egy string útvonalat vár paraméterként, és egy DataFrame ad visszatérési értékként.

Egy példa a bemenetre: 'test_data.csv'
Egy példa a kimenetre: df_data
return type: pandas.core.frame.DataFrame
függvény neve: csv_to_df
'''

# %%
def csv_to_df(path: str) -> pd.core.frame.DataFrame:
    return pd.read_csv(path)
#df = csv_to_df('/Users/banoczymartin/Library/Mobile Documents/com~apple~CloudDocs/OE/4/bevadat/lab/BEVADAT2022232/HAZI/HAZI04/StudentsPerformance.csv')
#print(df)

# %%
'''
Készíts egy függvényt, ami egy DataFrame-et vár paraméterként, 
és átalakítja azoknak az oszlopoknak a nevét nagybetűsre amelyiknek neve nem tartalmaz 'e' betüt.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_capitalized
return type: pandas.core.frame.DataFrame
függvény neve: capitalize_columns
'''

# %%
def capitalize_columns(df_data: pd.DataFrame) -> pd.core.frame.DataFrame:
    newdf=df_data.copy()
    newdf.columns = [col.upper() if 'e' not in col else col for col in newdf.columns]
    return newdf
#print(capitalize_columns(df).to_markdown())

# %%
'''
Készíts egy függvényt, ahol egy szám formájában vissza adjuk, hogy hány darab diáknak sikerült teljesíteni a matek vizsgát.
(legyen az átmenő ponthatár 50).

Egy példa a bemenetre: df_data
Egy példa a kimenetre: 5
return type: int
függvény neve: math_passed_count
'''

# %%
def math_passed_count(df_data) -> int:
    newdf=df_data.copy()
    return (newdf.loc[np.where(newdf['math score']>=50)]).shape[0]
#print(math_passed_count(df))

# %%
'''
Készíts egy függvényt, ahol Dataframe ként vissza adjuk azoknak a diákoknak az adatait (sorokat), akik végeztek előzetes gyakorló kurzust.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_did_pre_course
return type: pandas.core.frame.DataFrame
függvény neve: did_pre_course
'''

# %%
def did_pre_course(df_data) -> pd.core.frame.DataFrame:
    newdf=df_data.copy()
    return newdf[newdf['test preparation course'] != 'none']
#print(did_pre_course(df).to_markdown())

# %%
'''
Készíts egy függvényt, ahol a bemeneti Dataframet a diákok szülei végzettségi szintjei alapján csoportosításra kerül,
majd aggregációként vegyük, hogy átlagosan milyen pontszámot értek el a diákok a vizsgákon.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_average_scores
return type: pandas.core.frame.DataFrame
függvény neve: average_scores
'''

# %%
def average_scores(df_data) -> pd.core.frame.DataFrame:
    return pd.DataFrame(df_data.copy()).groupby(['parental level of education']).mean()
    # df[['math score', 'reading score','writing score']].mean(axis=1)
#print(average_scores(df).to_markdown())

# %%
'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'age' oszloppal, töltsük fel random 18-66 év közötti értékekkel.
A random.randint() függvényt használd, a random sorsolás legyen seedleve, ennek értéke legyen 42.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_age
return type: pandas.core.frame.DataFrame
függvény neve: add_age
'''

# %%
def add_age(df_data) -> pd.core.frame.DataFrame:
    newdf = df_data.copy()
    np.random.seed(42)
    newdf['age']=np.random.randint(18,67,size=newdf.shape[0])
    return newdf
#print(pd.DataFrame(add_age(df)).sort_values('age',ascending= False).to_markdown())

# %%
'''
Készíts egy függvényt, ami vissza adja a legjobb teljesítményt elérő női diák pontszámait.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: (99,99,99) #math score, reading score, writing score
return type: tuple
függvény neve: female_top_score
'''

# %%
def female_top_score(df_data) -> tuple:
    newdf=df_data.copy()
    ndf= newdf.loc[newdf["gender"] == "female"].sort_values(["math score", "writing score", "reading score"],ascending=[False,False,False]).iloc[0]
    return (ndf["math score"], ndf["writing score"], ndf["reading score"])
    #newdf=df.loc[np.where(newdf['gender']=='female')]
    #newdf['avg'] = newdf[['math score','reading score','writing score']].mean(axis=1)
    #return list((newdf.sort_values('avg',ascending=False).head(1))[['math score','reading score','writing score']].itertuples(index=False,name=None))[0]
#print(female_top_score(df)) 

# %%
'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'grade' oszloppal. 
Számoljuk ki hogy a diákok hány százalékot ((math+reading+writing)/300) értek el a vizsgán, és osztályozzuk őket az alábbi szempontok szerint:

90-100%: A
80-90%: B
70-80%: C
60-70%: D
<60%: F

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_grade
return type: pandas.core.frame.DataFrame
függvény neve: add_grade
'''

# %%
def add_grade(df_data) -> pd.core.frame.DataFrame:
    newdf=df_data.copy()
    grades=[]
    for i in range(len(newdf)):
        newcol = 100*(newdf['math score'][i]+
                      newdf['reading score'][i]+
                      newdf['writing score'][i])/300
        if newcol >= 90:
            grades.append('A')
        elif newcol >= 80:
            grades.append('B')
        elif newcol >= 70:
            grades.append('C')
        elif newcol >= 60:
            grades.append('D')
        else:
            grades.append('F')
    newdf['grade']=grades
    return newdf
#print(add_grade(df).to_markdown())

# %%
'''
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan oszlop diagrammot,
ami vizualizálja a nemek által elért átlagos matek pontszámot.

Oszlopdiagram címe legyen: 'Average Math Score by Gender'
Az x tengely címe legyen: 'Gender'
Az y tengely címe legyen: 'Math Score'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: math_bar_plot
'''

# %%
def math_bar_plot(df_data):
    newdf = df_data.copy().groupby(['gender'])['math score'].mean()
    fig, ax=plt.subplots()
    ax.bar(newdf.index,newdf.values)
    ax.set_title = 'Average Math Score by Gender'
    ax.set_xlabel = 'Gender'
    ax.set_ylabel = 'Math Score'
    return fig
#plt.show(math_bar_plot(df))

# %%
''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan histogramot,
ami vizualizálja az elért írásbeli pontszámokat.

A histogram címe legyen: 'Distribution of Writing Scores'
Az x tengely címe legyen: 'Writing Score'
Az y tengely címe legyen: 'Number of Students'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: writing_hist
'''

# %%
def writing_hist(df_data):
    newdf=df_data.copy()
    fig, ax = plt.subplots()
    ax.hist(newdf['writing score'])
    ax.set_xlabel('Writing Score')
    ax.set_ylabel('Number of Students')
    ax.set_title('Distribution of Writing Scores')
    return fig
#plt.show(writing_hist(df))

# %%
''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan kördiagramot,
ami vizualizálja a diákok etnikum csoportok szerinti eloszlását százalékosan.

Érdemes megszámolni a diákok számát, etnikum csoportonként,majd a százalékos kirajzolást az autopct='%1.1f%%' paraméterrel megadható.
Mindegyik kör szelethez tartozzon egy címke, ami a csoport nevét tartalmazza.
A diagram címe legyen: 'Proportion of Students by Race/Ethnicity'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: ethnicity_pie_chart
'''

# %%
def ethnicity_pie_chart(df_data):
    se = df_data.copy().groupby(['race/ethnicity'])['race/ethnicity'].count()
    fig, ax = plt.subplots()
    ax.set_title('Proportion of Students by Race/Ethnicity')
    ax.pie(se.values,labels=se.index, autopct='%1.1f%%')
    return fig
#print(ethnicity_pie_chart(df).to_markdown())
#plt.show(ethnicity_pie_chart(df))


