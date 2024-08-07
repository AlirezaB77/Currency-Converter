# Currency Converter

## Description
This is an efficient currency converter program that allows users to convert between different currencies using up-to-date exchange rates. The application is built using Streamlit, providing a user-friendly web interface for easy currency conversion.

## Features
- Convert between a wide range of currencies
- Real-time exchange rates
- User-friendly interface
- Display of last update time for exchange rates

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/currency-converter.git
   ```

2. Navigate to the project directory:
   ```
   cd currency-converter
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit app:
```
streamlit run app.py
```

Then open your web browser and go to `http://localhost:8501`.

## Dependencies
- Python 3.7+
- Streamlit
- Humanize
- Datetime

## File Structure
- `app.py`: Main application file
- `currency.py`: Contains the list of supported currencies
- `currency_convert.py`: Contains functions for currency conversion and fetching exchange rates
