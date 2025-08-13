# Thyroid Cancer Recurrence Predictor

This project provides two interfaces for predicting thyroid cancer recurrence:
- **Desktop App**: Built with PyQt6
- **Web App**: Built with Streamlit

## Features
- Input form for patient data with all required features
- Data preprocessing to match model requirements
- Prediction display with recurrence probability
- Error handling for invalid inputs

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ShubhamMallick/Thyroid_Cancer_Detector.git
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv thyroid_env
   source thyroid_env/bin/activate  # Linux/Mac
   thyroid_env\Scripts\activate    # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
### Desktop Application
Run the desktop app:
```bash
python app.py
```

### Web Application
Run the web app:
```bash
streamlit run web_app.py
```

## Project Structure
```
Thyroid_Cancer_Detector/
├── app.py                     # Desktop application (PyQt6)
├── web_app.py                 # Web application (Streamlit)
├── thyroid_recurrence_model.pkl  # Trained machine learning model
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── .gitignore                 # Specifies files to ignore in version control
├── thyroid_icon.ico           # Application icon
├── thyroid_icon_*.png         # Icon images in various sizes
├── create_icon.py             # Script to create the icon
└── train.ipynb                # Jupyter notebook for model training
```

## Dependencies
- Python 3.9+
- scikit-learn
- pandas
- numpy
- joblib
- PyQt6
- streamlit
- Pillow

## Contributing
Contributions are welcome! Please fork the repository and create a pull request.

## License
[MIT](LICENSE)
