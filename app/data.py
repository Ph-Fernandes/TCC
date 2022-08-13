import pandas as pd
import pymysql
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split, KFold, cross_val_score,cross_validate
from sklearn.neural_network import MLPClassifier

df = pd.read_sql_table('cliente','mysql+pymysql://root:123456@localhost:3306/TCC')
df = df.drop(["id"], axis=1)

def startNN():

    #Datas
    datas = [df.copy(deep=True),df.copy(deep=True)]
    X_resampled, y_resampled = SMOTE(random_state=1,k_neighbors=4).fit_resample(datas[0].drop('payment',axis=1),datas[0]['payment'])
    dataSM = X_resampled.assign(payment = y_resampled)
    datas[1] = dataSM


    #escalagem dos dados
    cols = range(0,23)
    scaler = MinMaxScaler()

    for data in datas:
        for i in cols:
            data[data.columns[i]] = scaler.fit_transform(data[data.columns[i]].values.reshape(-1, 1))



    #classificador
    result = [0,0]
    i=0   

    for data in datas:
        features = data.drop('payment',axis=1)
        label = data['payment']
        X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.3, random_state=1)
        model = MLPClassifier(alpha=0.05,hidden_layer_sizes=(12,6,2),activation='tanh', max_iter=250, random_state=1)
        model.fit(X_train.values,y_train.values)
        result[i] = model.score(X_test.values,y_test.values)
        i+=1

    return result


import dash
from dash import dcc, html
from django_plotly_dash import DjangoDash
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go

def newLegend(fig, newNames):
    novovet = list(map(str,fig.data[0].labels))
    for item in newNames:
        for i, elem in enumerate(fig.data[0].labels):
            if str(elem) == item:
                novovet[i] = newNames[item]
    fig.data[0].labels=novovet
    return(fig)

def dashboard():
    
    app = DjangoDash('dashboard')   # replaces dash.Dash

    fig0 = go.Figure(data=[go.Pie(labels=df['sex'])])
    fig0.update_traces(hoverinfo='label+value',textposition='inside', textinfo='percent',textfont_size=20)
    fig0.update_layout(title_text="Gênero")
    fig0 = newLegend(fig0,{"1": "Feminino", "2": "Masculino"})

    fig1 = go.Figure(data=[go.Pie(labels=df['education'])])
    fig1.update_traces(hoverinfo='label+value',textposition='inside', textinfo='percent',textfont_size=20)
    fig1.update_layout(title_text="Educação")
    fig1 = newLegend(fig1,{"1": "Pós Graduado", "2": "Graduado","3": "Ensino Médio","4": "Outros"})


    app.layout = html.Div([html.H1(children='Hello Dash'),dcc.Graph(figure = fig0),dcc.Graph(figure = fig1)])
    
    #app.run_server(debug=True)

    # @app.callback(
    #     dash.dependencies.Output('output-color', 'children'),
    #     [dash.dependencies.Input('dropdown-color', 'value')])
    # def callback_color(dropdown_value):
    #     return "The selected color is %s." % dropdown_value

    # @app.callback(
    #     dash.dependencies.Output('output-size', 'children'),
    #     [dash.dependencies.Input('dropdown-color', 'value'),
    #     dash.dependencies.Input('dropdown-size', 'value')])
    # def callback_size(dropdown_color, dropdown_size):
    #     return "The chosen T-shirt is a %s %s one." %(dropdown_size,
    #                                                 dropdown_color)