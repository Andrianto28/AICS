# ===================================================
# file: app.py
# this file contains the main function to run the flask app
# how to run this file (must set FLASK_APP=app.py first):
# $ set FLASK_APP=app.py
# [$ python app.py] OR [$ flask run]
# ===================================================

# * Import Libraries
from libraries import *

# * Initialize Flask App
app = Flask(__name__)
app.config["APISPEC_FORMAT_RESPONSE"] = False


# * Initialize Routes
# * 1. Predict Route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        content_type = request.headers.get("Content-Type")
        if content_type == "application/json":
            # Get json data
            json_data = request.get_json()

            # Convert json to dataframe
            df_input = pd.DataFrame.from_dict(json_data, orient="index").T

            # Convert specific columns to numeric data type
            numeric_columns = [
                "domicile_lat",
                "domicile_lon",
                "now_lat",
                "now_lon",
                "last_1_week_lat",
                "last_1_week_lon",
                "last_2_week_lat",
                "last_2_week_lon",
                "last_3_week_lat",
                "last_3_week_lon",
                "last_4_week_lat",
                "last_4_week_lon",
            ]
            df_input[numeric_columns] = df_input[numeric_columns].apply(pd.to_numeric)

            # Preprocess Data
            preprocessed_data = data_preprocessing(df_input)
            print(preprocessed_data)

            reshaped_data = np.reshape(
                preprocessed_data, (preprocessed_data.shape[0], -1)
            )

            result = model.predict(reshaped_data)[0]

            return jsonify(
                {
                    "status": True,
                    "message": "success",
                    "input": json_data,
                    "result": result,
                }
            )
    except Exception as e:
        return jsonify(
            {"status": False, "message": "Data is not valid", "error": str(e)}
        )


# * Main Function
if __name__ == "__main__":
    app.run(debug=True)
