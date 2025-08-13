import sys
import joblib
import pandas as pd
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, 
                             QLineEdit, QComboBox, QPushButton, 
                             QVBoxLayout, QWidget, QMessageBox, 
                             QHBoxLayout, QGroupBox, QScrollArea, QGridLayout)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon, QPixmap

class ThyroidApp(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('🏥 Thyroid Cancer Recurrence Predictor')
        self.setGeometry(200, 200, 800, 700)
        self.setWindowIcon(QIcon('thyroid_icon.ico'))
        
        # Set application style
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QGroupBox {
                font-weight: bold;
                border: 2px solid #cccccc;
                border-radius: 5px;
                margin-top: 1ex;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
            QPushButton {
                background-color: #4CAF50;
                border: none;
                color: white;
                padding: 10px;
                text-align: center;
                font-size: 14px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QLabel {
                font-size: 12px;
                margin: 2px;
            }
        """)
        
        # Create scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_widget = QWidget()
        scroll.setWidget(scroll_widget)
        self.setCentralWidget(scroll)
        
        main_layout = QVBoxLayout(scroll_widget)
        
        # Title
        title = QLabel('Thyroid Cancer Recurrence Predictor')
        title.setFont(QFont('Arial', 16, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet('color: #2c3e50; margin: 20px;')
        main_layout.addWidget(title)
        
        # Create input fields in two columns
        self.fields = {}
        features = [
            'Age', 'Gender', 'Smoking', 'Hx Smoking', 'Hx Radiotherapy',
            'Thyroid Function', 'Physical Examination', 'Adenopathy',
            'Pathology', 'Focality', 'Risk', 'T', 'N', 'M', 'Stage', 'Response'
        ]
        
        # Split features into two columns
        half = len(features) // 2
        col1_features = features[:half]
        col2_features = features[half:]
        
        # Create a horizontal layout for the two columns
        columns_layout = QHBoxLayout()
        
        # Column 1
        col1_widget = QWidget()
        col1_layout = QVBoxLayout(col1_widget)
        for feature in col1_features:
            col1_layout.addWidget(QLabel(feature))
            if feature in ['Age', 'T', 'N', 'M']:
                self.fields[feature] = QLineEdit()
            else:
                self.fields[feature] = QComboBox()
                if feature == 'Gender':
                    self.fields[feature].addItems(['Select...', 'male', 'female'])
                elif feature == 'Smoking':
                    self.fields[feature].addItems(['Select...', 'yes', 'no'])
                elif feature == 'Hx Smoking':
                    self.fields[feature].addItems(['Select...', 'yes', 'no'])
                elif feature == 'Hx Radiotherapy':
                    self.fields[feature].addItems(['Select...', 'yes', 'no'])
                elif feature == 'Thyroid Function':
                    self.fields[feature].addItems(['Select...', 'normal', 'abnormal'])
                elif feature == 'Physical Examination':
                    self.fields[feature].addItems(['Select...', 'normal', 'abnormal'])
                elif feature == 'Adenopathy':
                    self.fields[feature].addItems(['Select...', 'yes', 'no'])
                elif feature == 'Pathology':
                    self.fields[feature].addItems(['Select...', 'papillary', 'follicular'])
                elif feature == 'Focality':
                    self.fields[feature].addItems(['Select...', 'unifocal', 'multifocal'])
                elif feature == 'Risk':
                    self.fields[feature].addItems(['Select...', 'low', 'high'])
                elif feature == 'Stage':
                    self.fields[feature].addItems(['Select...', 'I', 'II', 'III', 'IV'])
                elif feature == 'Response':
                    self.fields[feature].addItems(['Select...', 'complete', 'incomplete'])
            col1_layout.addWidget(self.fields[feature])
        
        # Column 2
        col2_widget = QWidget()
        col2_layout = QVBoxLayout(col2_widget)
        for feature in col2_features:
            col2_layout.addWidget(QLabel(feature))
            if feature in ['Age', 'T', 'N', 'M']:
                self.fields[feature] = QLineEdit()
            else:
                self.fields[feature] = QComboBox()
                if feature == 'Gender':
                    self.fields[feature].addItems(['Select...', 'male', 'female'])
                elif feature == 'Smoking':
                    self.fields[feature].addItems(['Select...', 'yes', 'no'])
                elif feature == 'Hx Smoking':
                    self.fields[feature].addItems(['Select...', 'yes', 'no'])
                elif feature == 'Hx Radiotherapy':
                    self.fields[feature].addItems(['Select...', 'yes', 'no'])
                elif feature == 'Thyroid Function':
                    self.fields[feature].addItems(['Select...', 'normal', 'abnormal'])
                elif feature == 'Physical Examination':
                    self.fields[feature].addItems(['Select...', 'normal', 'abnormal'])
                elif feature == 'Adenopathy':
                    self.fields[feature].addItems(['Select...', 'yes', 'no'])
                elif feature == 'Pathology':
                    self.fields[feature].addItems(['Select...', 'papillary', 'follicular'])
                elif feature == 'Focality':
                    self.fields[feature].addItems(['Select...', 'unifocal', 'multifocal'])
                elif feature == 'Risk':
                    self.fields[feature].addItems(['Select...', 'low', 'high'])
                elif feature == 'Stage':
                    self.fields[feature].addItems(['Select...', 'I', 'II', 'III', 'IV'])
                elif feature == 'Response':
                    self.fields[feature].addItems(['Select...', 'complete', 'incomplete'])
            col2_layout.addWidget(self.fields[feature])
        
        columns_layout.addWidget(col1_widget)
        columns_layout.addWidget(col2_widget)
        main_layout.addLayout(columns_layout)
        
        # Predict button
        self.predict_btn = QPushButton('Predict Recurrence')
        self.predict_btn.clicked.connect(self.predict)
        main_layout.addWidget(self.predict_btn)
        
        # Result display
        self.result_label = QLabel('')
        self.result_label.setStyleSheet('font-size: 16px; font-weight: bold; margin: 20px;')
        main_layout.addWidget(self.result_label)
    
    def predict(self):
        try:
            # Prepare input data
            input_data = {}
            for feature, widget in self.fields.items():
                if isinstance(widget, QLineEdit):
                    input_data[feature] = [float(widget.text()) if widget.text() else 0]
                else:
                    text = widget.currentText()
                    if text == 'Select...':
                        # Skip if not selected
                        continue
                    input_data[feature] = [text]
            
            # Check if all fields are filled
            if len(input_data) != len(self.fields):
                raise ValueError("Please fill all fields")
            
            df = pd.DataFrame(input_data)
            
            # Preprocess data
            df['Gender'] = df['Gender'].map({'male': 0, 'female': 1})
            df['Smoking'] = df['Smoking'].map({'yes': 1, 'no': 0})
            df['Hx Smoking'] = df['Hx Smoking'].map({'yes': 1, 'no': 0})
            df['Hx Radiotherapy'] = df['Hx Radiotherapy'].map({'yes': 1, 'no': 0})
            df['Thyroid Function'] = df['Thyroid Function'].map({'normal': 0, 'abnormal': 1})
            df['Physical Examination'] = df['Physical Examination'].map({'normal': 0, 'abnormal': 1})
            df['Adenopathy'] = df['Adenopathy'].map({'yes': 1, 'no': 0})
            df['Pathology'] = df['Pathology'].map({'papillary': 0, 'follicular': 1})
            df['Focality'] = df['Focality'].map({'unifocal': 0, 'multifocal': 1})
            df['Risk'] = df['Risk'].map({'low': 0, 'high': 1})
            df['Stage'] = df['Stage'].map({'I': 1, 'II': 2, 'III': 3, 'IV': 4})
            df['Response'] = df['Response'].map({'complete': 0, 'incomplete': 1})
            
            # Make prediction
            prediction = self.model.predict(df)[0]
            probability = self.model.predict_proba(df)[0][1]
            
            # Display results
            result = "HIGH RISK OF RECURRENCE" if prediction == 1 else "LOW RISK OF RECURRENCE"
            self.result_label.setText(
                f"Prediction: {result}\n"
                f"Recurrence Probability: {probability:.2%}\n"
                f"Confidence: {'High' if probability > 0.7 or probability < 0.3 else 'Medium'}"
            )
            
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Prediction failed: {str(e)}')

if __name__ == '__main__':
    # Load model
    model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'thyroid_recurrence_model.pkl')
    model = joblib.load(model_path)
    
    # Start app
    app = QApplication(sys.argv)
    window = ThyroidApp(model)
    window.show()
    sys.exit(app.exec())