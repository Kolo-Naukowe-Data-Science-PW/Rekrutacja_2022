from flask import Flask, redirect, url_for, render_template, request
import pandas as pd
import numpy as np

####### Analiza danych #######
data = pd.read_csv('data.csv')
def Analiza_danych(df):
	df = pd.DataFrame(data[["Review Text", "Rating", "Class Name","Positive Feedback Count"]])
	df = df.reset_index(drop=True)
	df = df.where(df["Rating"]==1)
	df= df.dropna()
	return df
def ktore_ubranie(var,df):
	result = df.where(df["Class Name"]==var).drop(columns=["Rating","Class Name"]).dropna()
	result = result.sort_values(by="Positive Feedback Count", ascending = False)
	result.index = np.arange(1, len(result) + 1)
	return result
def statystyki(var, df, rating):
	result = pd.DataFrame(data[["Class Name","Rating","Positive Feedback Count","Age"]]).dropna()
	result = result.where(df["Rating"]==rating).groupby(["Class Name"]).count()
	result["Positive Feedback Count"] = df["Class Name"].value_counts()
	result["Age"] = round(df["Age"].groupby(df["Class Name"]).mean() -10,1)
	result = result.set_axis([f"Ile ocen {rating}/5:","Stosunek oceny do wszystkich (w procentach):","Średni wiek kupujących:"],axis=1,inplace=False)
	result["Stosunek oceny do wszystkich (w procentach):"] = round((result[f"Ile ocen {rating}/5:"] / result["Stosunek oceny do wszystkich (w procentach):"]) * 100,1) 
	return result

df = Analiza_danych(data)
df1,df2,df3,df4,df5,df6,df7,df8 = ktore_ubranie("Dresses",df),ktore_ubranie("Blouses",df),\
ktore_ubranie("Pants",df),ktore_ubranie("Jackets",df),ktore_ubranie("Sleep",df), \
ktore_ubranie("Intimates",df), ktore_ubranie("Swim",df), ktore_ubranie("Sweaters",df)

stat1 = statystyki("Statistics",data,1)
stat2 = statystyki("Statistics",data,2)
stat3 = statystyki("Statistics",data,3)
stat4 = statystyki("Statistics",data,4)
stat5 = statystyki("Statistics",data,5)

####### Web app ########
app = Flask(__name__)
@app.route('/', methods=["POST","GET"]) # menu główne
def main():
	if request.method=="POST":
		var = request.form.get("operator")
		return redirect(url_for(f"{var}"))
	else: return render_template("index.html")

#stronka odpowiedzialna za sukienki
@app.route('/Dresses', methods=("POST", "GET"))
def Dresses():
    return render_template('Dresses.html',  tables=[df1.to_html(classes='data')], titles=None)

#stronka odpowiedzialna za Bluzki
@app.route('/Blouses', methods=("POST", "GET"))
def Blouses():
    return render_template('Blouses.html',  tables=[df2.to_html(classes='data')], titles=None)

#stronka odpowiedzialna za spodnie
@app.route('/Pants', methods=("POST", "GET"))
def Pants():
    return render_template('Pants.html',  tables=[df3.to_html(classes='data')], titles=None)

#stronka odpowiedzialna za kurtki
@app.route('/Jackets', methods=("POST", "GET"))
def Jackets():
    return render_template('Jackets.html',  tables=[df4.to_html(classes='data')], titles=None)

#stronka odpowiedzialna za piżame
@app.route('/Sleep', methods=("POST", "GET")) 
def Sleep():
    return render_template('Sleep.html',  tables=[df5.to_html(classes='data')], titles=None)

#stronka odpowiedzialna za intymne
@app.route('/Intimates', methods=("POST", "GET"))
def Intimates():
    return render_template('Intimates.html',  tables=[df6.to_html(classes='data')], titles=None)

#stronka odpowiedzialna za do pływania
@app.route('/Swim', methods=("POST", "GET")) 
def Swim():
    return render_template('Swim.html',  tables=[df7.to_html(classes='data')], titles=None)

#stronka odpowiedzialna za swetry
@app.route('/Sweaters', methods=("POST", "GET")) 
def Sweaters():
    return render_template('Sweaters.html',  tables=[df8.to_html(classes='data')], titles=None)

#stronka odpowiedzialna za statystyke
@app.route('/Statistics', methods=("POST", "GET")) 
def Statistics():
    return render_template('Statistics.html',  tables=[stat1.to_html(classes='data'),stat2.to_html(classes='data'), stat3.to_html(classes='data'),stat4.to_html(classes='data'),stat5.to_html(classes='data')], titles=None)

if __name__ == "__main__":
    app.run(debug=True)
