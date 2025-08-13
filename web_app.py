import streamlit as st
import joblib
import pandas as pd
import numpy as np
import os

# Load the model
@st.cache_resource
def load_model():
    model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'thyroid_recurrence_model.pkl')
    return joblib.load(model_path)

def preprocess_input_data(input_data):
    # Convert categorical variables to numerical variables
    input_data['Gender'] = input_data['Gender'].map({'Male': 0, 'Female': 1})
    input_data['Smoking'] = input_data['Smoking'].map({'No': 0, 'Yes': 1})
    input_data['Hx Smoking'] = input_data['Hx Smoking'].map({'No': 0, 'Yes': 1})
    input_data['Hx Radiotherapy'] = input_data['Hx Radiotherapy'].map({'No': 0, 'Yes': 1})
    input_data['Thyroid Function'] = input_data['Thyroid Function'].map({'Normal': 0, 'Abnormal': 1})
    input_data['Physical Examination'] = input_data['Physical Examination'].map({'Normal': 0, 'Abnormal': 1})
    input_data['Adenopathy'] = input_data['Adenopathy'].map({'No': 0, 'Yes': 1})
    input_data['Pathology'] = input_data['Pathology'].map({'Papillary': 0, 'Follicular': 1, 'Medullary': 2, 'Anaplastic': 3})
    input_data['Focality'] = input_data['Focality'].map({'Unifocal': 0, 'Multifocal': 1})
    input_data['Risk'] = input_data['Risk'].map({'Low': 0, 'Intermediate': 1, 'High': 2})
    input_data['T'] = input_data['T'].map({'T1': 1, 'T2': 2, 'T3': 3, 'T4': 4})
    input_data['N'] = input_data['N'].map({'N0': 0, 'N1': 1})
    input_data['M'] = input_data['M'].map({'M0': 0, 'M1': 1})
    input_data['Stage'] = input_data['Stage'].map({'I': 1, 'II': 2, 'III': 3, 'IV': 4})
    input_data['Response'] = input_data['Response'].map({'Excellent': 0, 'Biochemical Incomplete': 1, 'Structural Incomplete': 2})
    
    return input_data

def main():
    st.title('🏥 Thyroid Cancer Recurrence Predictor')
    st.write('Enter patient information to predict recurrence risk')
    
    # Load model
    model = load_model()
    
    # Create input form
    with st.form("prediction_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            age = st.number_input('Age', min_value=0, max_value=120, value=45)
            gender = st.selectbox('Gender', ['Male', 'Female'])
            smoking = st.selectbox('Smoking', ['No', 'Yes'])
            hx_smoking = st.selectbox('History of Smoking', ['No', 'Yes'])
            hx_radiotherapy = st.selectbox('History of Radiotherapy', ['No', 'Yes'])
            thyroid_function = st.selectbox('Thyroid Function', ['Normal', 'Abnormal'])
            physical_exam = st.selectbox('Physical Examination', ['Normal', 'Abnormal'])
            adenopathy = st.selectbox('Adenopathy', ['No', 'Yes'])
        
        with col2:
            pathology = st.selectbox('Pathology', ['Papillary', 'Follicular', 'Medullary', 'Anaplastic'])
            focality = st.selectbox('Focality', ['Unifocal', 'Multifocal'])
            risk = st.selectbox('Risk', ['Low', 'Intermediate', 'High'])
            t_stage = st.selectbox('T Stage', ['T1', 'T2', 'T3', 'T4'])
            n_stage = st.selectbox('N Stage', ['N0', 'N1'])
            m_stage = st.selectbox('M Stage', ['M0', 'M1'])
            stage = st.selectbox('Stage', ['I', 'II', 'III', 'IV'])
            response = st.selectbox('Response', ['Excellent', 'Biochemical Incomplete', 'Structural Incomplete'])
        
        submitted = st.form_submit_button("Predict Recurrence")
        
        if submitted:
            # Prepare input data
            input_data = {
                'Age': [age],
                'Gender': [gender],
                'Smoking': [smoking],
                'Hx Smoking': [hx_smoking],
                'Hx Radiotherapy': [hx_radiotherapy],
                'Thyroid Function': [thyroid_function],
                'Physical Examination': [physical_exam],
                'Adenopathy': [adenopathy],
                'Pathology': [pathology],
                'Focality': [focality],
                'Risk': [risk],
                'T': [t_stage],
                'N': [n_stage],
                'M': [m_stage],
                'Stage': [stage],
                'Response': [response]
            }
            
            try:
                df = pd.DataFrame(input_data)
                df = preprocess_input_data(df)
                
                # Make prediction
                prediction = model.predict(df)[0]
                probability = model.predict_proba(df)[0][1]
                
                # Display results
                st.subheader('Prediction Results')
                
                if prediction == 1:
                    st.error(f'🚨 HIGH RISK OF RECURRENCE')
                else:
                    st.success(f'✅ LOW RISK OF RECURRENCE')
                
                st.metric("Recurrence Probability", f"{probability:.1%}")
                
                # Confidence level
                if probability > 0.7 or probability < 0.3:
                    confidence = "High"
                    st.info(f"🎯 Confidence Level: {confidence}")
                else:
                    confidence = "Medium"
                    st.warning(f"⚠️ Confidence Level: {confidence}")
                
            except Exception as e:
                st.error(f'❌ Prediction failed: {str(e)}')
                st.write("Please check that all fields are filled correctly.")

if __name__ == '__main__':
    main()
