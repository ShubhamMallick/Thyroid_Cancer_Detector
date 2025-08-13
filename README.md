# Thyroid Cancer Recurrence Predictor

This project provides two interfaces for predicting thyroid cancer recurrence:
- **Desktop App**: Built with PyQt6
- **Web App**: Built with Streamlit

## Features
- Input form for patient data
- Machine learning model for recurrence prediction
- Preprocessing of categorical inputs

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ShubhamMallick/Thyroid_Cancer_Detector.git
   ```
2. Create a virtual environment:
   ```bash
   python -m venv thyroid_env
   ```
3. Activate the environment:
   - Windows: `thyroid_env\Scripts\activate`
   - Unix: `source thyroid_env/bin/activate`
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
- **Desktop App**:
  ```bash
  python app.py
  ```
- **Web App**:
  ```bash
  streamlit run web_app.py
  ```

## Project Structure
```
thyroid_cancer/
├── app.py                # Desktop application
├── web_app.py            # Web application
├── thyroid_recurrence_model.pkl  # Trained model
├── requirements.txt      # Dependencies
├── README.md             # This file
└── ...                   # Other project files
```
