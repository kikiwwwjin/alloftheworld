import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from flask import Flask, render_template


server = Flask(__name__)

#
# @server.route('/name')
# def name():
#     return render_template('index.html')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


layout = """
<!DOCTYPE html>
<html lang="en">
<title>{%title%}</title>
{%favicon%}
{%metas%}
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
{%css%}
<style>
body,h1,h2,h3,h4,h5,h6 {font-family: "Lato", sans-serif}
.w3-bar,h1,button {font-family: "Montserrat", sans-serif}
.fa-anchor,.fa-coffee {font-size:200px}
</style>
<body>

<!-- Navbar -->
<div class="w3-top">
  <div class="w3-bar w3-red w3-card w3-left-align w3-large">
    <a class="w3-bar-item w3-button w3-hide-medium w3-hide-large w3-right w3-padding-large w3-hover-white w3-large w3-red" href="javascript:void(0);" onclick="myFunction()" title="Toggle Navigation Menu"><i class="fa fa-bars"></i></a>
    <a href="#" class="w3-bar-item w3-button w3-padding-large w3-white">Home</a>
    <a href="#" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">Link 1</a>
    <a href="#" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">Link 2</a>
    <a href="#" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">Link 3</a>
    <a href="#" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">Link 4</a>
  </div>

  <!-- Navbar on small screens -->
  <div id="navDemo" class="w3-bar-block w3-white w3-hide w3-hide-large w3-hide-medium w3-large">
    <a href="#" class="w3-bar-item w3-button w3-padding-large">Link 1</a>
    <a href="#" class="w3-bar-item w3-button w3-padding-large">Link 2</a>
    <a href="#" class="w3-bar-item w3-button w3-padding-large">Link 3</a>
    <a href="#" class="w3-bar-item w3-button w3-padding-large">Link 4</a>
  </div>
</div>

<!-- Header -->
<header class="w3-container w3-red w3-center" style="padding:128px 16px">
  <h1 class="w3-margin w3-jumbo">START PAGE</h1>
  <p class="w3-xlarge">Template by w3.css</p>
  <button class="w3-button w3-black w3-padding-large w3-large w3-margin-top">Get Started</button>
</header>

<!-- First Grid -->
<div class="w3-row-padding w3-padding-64 w3-container">
  <div class="w3-content">
    <div class="w3-twothird">
      <h1>Bar Chart</h1>

        <h2>Insert bar chart here</h2>
        {%app_entry%}
  </div>
</div>
  {%config%}
  {%scripts%}
  {%renderer%}
</body>
</html>
"""

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, server=server, index_string=layout)

# 스코어 테이블 가져오기
f_nm = 'C:\\Users\\wai\\Desktop\\프로젝트\\암호화폐\\score_af_20210625.csv'
score_df = pd.read_csv(f_nm, encoding='cp949')
key_list = list(score_df['코인명'])
p_index_list = list(score_df['스코어_긍정_decenter'])
n_index_list = list(score_df['스코어_부정_decenter'])

app.layout = html.Div(children=[
    dcc.Graph(
        id='coin_index_graph',
        figure={
            'data': [
                {'x':key_list, 'y':p_index_list, 'type': 'bar', 'name': '긍정'},
                {'x':key_list, 'y':n_index_list, 'type': 'bar', 'name': '부정'},
                # {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': '부정'},
            ],
            'layout': {
                'title': '코인별 긍부정 지수'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)