from flask import Flask, request, render_template
import pandas as pd
import pickle

app = Flask(__name__)

file = open("./Random_Forest_regressor_model_2.pickle", 'rb')
model = pickle.load(file)

data = pd.read_csv("./clean_data.csv")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = int(request.form.get('age'))
        sex = request.form.get('sex')
        bmi = float(request.form.get('bmi'))
        children = int(request.form.get('children'))
        smoker = request.form.get('smoker')
        region = request.form.get('region')

        prediction = model.predict(pd.DataFrame([[age, sex, bmi, children, smoker, region]],
                                                columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region']))

        pred = prediction[0]

        pred_final = round(pred, 2)

        return render_template('result.html', prediction_final="$ " + str(pred_final))

    except Exception as e:
        return render_template('error.html')


if __name__ == "__main__":
    app.run(debug=True)
