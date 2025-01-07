# Forest Fire Prediction Model

This project is a web application built using Flask and machine learning for predicting forest fire risks based on environmental factors. The model uses Ridge Regression and StandardScaler for preprocessing and prediction. The application allows users to input relevant environmental data and obtain forest fire risk predictions.

## Project Structure:
- **`application.py`**: Main file containing the Flask web application and Ridge Regression model for prediction.
- **`models/`**: Directory containing the pre-trained models (`ridge.pkl`) and scaler (`scalar.pkl`).
- **`templates/`**: Contains HTML templates for rendering the user interface.

## Parameters:
- **Month**: Month of the year (e.g., "jan" to "dec").
- **Day**: Day of the week (e.g., "mon" to "sun").
- **FFMC**: Fine Fuel Moisture Code (FFMC) index.
- **DMC**: Duff Moisture Code (DMC) index.
- **DC**: Drought Code (DC) index.
- **ISI**: Initial Spread Index (ISI).
- **Temp**: Temperature in Celsius.
- **RH**: Relative Humidity.
- **Wind**: Wind speed in km/h.
- **Rain**: Rainfall in mm/m².

## Output:
The model predicts the **FWI (Fire Weather Index)** value, which represents the fire risk based on the given environmental conditions. A higher FWI indicates a higher risk of forest fire occurrence.

## Requirements:
- Flask
- scikit-learn
- numpy
- pandas

## How to Run:
1. Clone the repository:

   ```
   git clone https://github.com/tejas-130704/ForestFire-Model/
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```
   python application.py
   ```
4. Access the app via `http://127.0.0.1:5000/` in your browser.

