# Synthetic Data Generator Engine

A web-based tool for generating synthetic data with customizable columns and realistic noise patterns.

## Features

- **Multiple Data Types**: Name, Email, Address, Phone Number, Company Name, Date, Integer, Float, Text/Job Title, Country
- **Real-World Noise**: Adjustable slider (0-50%) to introduce data imperfections
- **Flexible Row Count**: Generate from 1 to 10,000 rows
- **CSV Export**: Direct download of generated datasets
- **Dynamic Columns**: Add/remove columns as needed

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to `http://localhost:5000`

## Usage

1. **Define Columns**: Add one or more columns with names and select data types
2. **Set Parameters**: Specify row count and noise level
3. **Generate Data**: Click "Generate Data" to create the dataset
4. **Download**: Click "Download CSV" to save the file

## Noise Implementation

The noise feature introduces realistic data imperfections:
- **NULL Values**: Randomly converts valid data to missing values
- **Typos**: Introduces character substitutions in text fields
- **Percentage Based**: Applies noise to the specified percentage of total data points

## Technical Stack

- **Backend**: Flask (Python web framework)
- **Data Generation**: Faker library for realistic dummy data
- **Data Processing**: Pandas for CSV generation
- **Frontend**: HTML, CSS, JavaScript (no external frameworks)

## File Structure

```
synthetic-data-generator/
├── app.py              # Flask web application
├── data_generator.py   # Core data generation logic
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Web interface
└── README.md          # This file
```
