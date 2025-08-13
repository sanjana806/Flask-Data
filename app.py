from flask import Flask, render_template, redirect, url_for
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Base directory for file paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def home():
    return render_template('Index.html')


@app.route('/sanjana')
def about():
    return render_template('About.html')


@app.route('/game')
def game():
    return render_template('Game.html')


@app.route('/File')
def file():
    file_path = os.path.join(BASE_DIR, 'airlines_flights_data.csv')
    data_df = pd.read_csv(file_path).head()
    df = data_df[["airline", "source_city", "arrival_time"]]
    return render_template(
        'File.html',
        title="flights",
        table=df.to_html(index=False, classes="table")
    )


@app.route('/file2')
def file2():
    file_path = os.path.join(BASE_DIR, 'spotify_data_dictionary Description.csv')
    df = pd.read_csv(file_path)
    return render_template(
        'file2.html',
        title="spotify",
        Table=df.head().to_html(index=False, classes="table")
    )


@app.route('/file3')
def file3():
    file_path = os.path.join(BASE_DIR, 'multilingual_mobile_app_reviews_2025.csv')
    df = pd.read_csv(file_path)
    return render_template(
        'file3.html',
        title="Mobile",
        Table=df.head().to_html(index=False, classes="table")
    )


@app.route('/file4')
def file4():
    file_path = os.path.join(BASE_DIR, 'BMW_Car_Sales_Classification.csv')
    df = pd.read_csv(file_path)
    return render_template(
        'file4.html',
        title="BMW",
        Table=df.head().to_html(index=False, classes="table")
    )


@app.route('/bar')
def bar():
    file_path = os.path.join(BASE_DIR, 'airlines_flights_data.csv')
    data_df = pd.read_csv(file_path).head()

    plt.figure(figsize=(10, 6))
    plt.bar(data_df["airline"], data_df["arrival_time"])
    plt.xlabel("Airlines")
    plt.ylabel("Time")
    plt.grid(False)

    chart_path = os.path.join(BASE_DIR, 'static', 'chart.png')
    plt.savefig(chart_path)
    plt.close()

    return render_template('bar.html', chart_url=url_for('static', filename='chart.png'))

@app.route('/hist')
def hist():
    file_path = os.path.join(BASE_DIR, 'airlines_flights_data.csv')
    data_df = pd.read_csv(file_path).head()

    plt.figure(figsize=(10, 6))
    plt.hist(data_df["arrival_time"], bins=5, color='skyblue', edgecolor='black')
    plt.xlabel("Arrival Time")
    plt.ylabel("Frequency")
    plt.title("Distribution of Arrival Times")
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    chart_path = os.path.join(BASE_DIR, 'static', 'hist_chart.png')
    plt.savefig(chart_path)
    plt.close()

    return render_template('hist.html', chart_url=url_for('static', filename='hist_chart.png'))


@app.route('/pie')
def pie():
    data_df = pd.read_csv('airlines_flights_data.csv').head()

    plt.figure(figsize=(8, 8))
    data=data_df["price"].value_counts()
    plt.pie(data.index,autopct='%1.1f%%', startangle=90)
    plt.title("Airline Distribution")
    chart_url = os.path.join('static', 'pie_chart.png')
    plt.savefig(chart_url)
    plt.close()
    return render_template('pie.html', chart_url=url_for('static', filename='pie_chart.png'))


if __name__ == '__main__':
    app.run(port=4000, debug=True)
