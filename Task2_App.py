from flask import Flask, render_template, request
# Importing required libraries
import pandas as pd
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Frontend_App.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """
        Compute Daily and Annualized Volatility.

        Endpoint: /upload

        Parameters:
        - 'file': CSV file containing financial data (chosen).
          File Headers:
            - 'Date ': Name of the column containing Dates .
            - 'Close ': Name of the column containing Closing value for the particular Date.

        Returns:
        Calculated values of Daily Volatility and Annualized Volatility
        """
    # Check if the POST request has the file part
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    # If the user does not select a file, the browser submits an empty file without a filename
    if file.filename == '':
        return 'No selected file'

    # Process the uploaded file (e.g., read CSV data using Pandas)
    try:
        nifty_df = pd.read_csv(file)
        # Calculate daily returns using a loop
        daily_returns_list = []

        # First Previous close value assumed to be current close value for calculation simplicity
        previous_close = nifty_df['Close '][0]

        # Iterate over the 'Close' column
        for current_close in nifty_df['Close ']:
            # Calculate daily returns using the specified formula
            ret = (current_close / previous_close) - 1

            # Append the result to the list
            daily_returns_list.append(ret)

        # Create a Series for daily returns with the 'Date' column as the index
        daily_returns_Series = pd.Series(daily_returns_list, index=nifty_df['Date '])

        # Calculate daily volatility
        daily_volatility = daily_returns_Series.std()

        # Get the length of the Series
        length_Series = daily_returns_Series.size

        # Calculate annualized volatility
        Annualized_Volatility = daily_volatility * math.sqrt(length_Series)

        result = {
            'Daily_Volatility': daily_volatility,
            'Annualized_Volatility': Annualized_Volatility
        }
        return (result)
    except Exception as e:
        return f'Error processing file: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)
