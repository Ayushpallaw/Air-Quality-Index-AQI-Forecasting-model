


# import streamlit as st
# import pickle
# import pandas as pd
# import matplotlib.pyplot as plt

# # Custom CSS for styling
# st.markdown(""" 
#     <style>
#         body {
#             background: linear-gradient(to bottom, #e3f2fd, #ffffff);
#             color: #333333;
#             font-family: 'Arial', sans-serif;
#         }
#         .stButton>button {
#             background: linear-gradient(to right, #42a5f5, #1e88e5);
#             color: white;
#             border: none;
#             border-radius: 8px;
#             padding: 0.6em 1.5em;
#             font-size: 1em;
#             font-weight: bold;
#             cursor: pointer;
#             box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#             transition: all 0.3s ease;
#         }
#         .stButton>button:hover {
#             background: linear-gradient(to right, #1e88e5, #1565c0);
#             transform: translateY(-2px);
#         }
#         .header-style {
#             font-size: 3em;
#             font-weight: bold;
#             text-align: center;
#             color: #1565c0;
#             margin-bottom: 0.5em;
#         }
#         .subheader-style {
#             font-size: 1.8em;
#             font-weight: bold;
#             color: white;
#             margin-bottom: 0.5em;
#         }
#         .large-text {
#             font-size: 1.8em;
#             font-weight: bold;
#             color: #1565c0;
#             text-align: center;
#             margin-top: 1em;
#             margin-bottom: 1em;
#         }
#         .stSelectbox label {
#             font-weight: bold;
#             font-size: 1.2em;
#             color: #1e88e5;
#         }
#         .stSlider label {
#             font-weight: bold;
#             font-size: 1.2em;
#             color: #1565c0;
#         }
#         .stMarkdown h3 {
#             font-size: 1.5em;
#             color: #333;
#             font-weight: bold;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Load the trained model
# model_path = "C:/Users/divya/DATASETS/aqi_rf_reg_model.pkl"
# with open(model_path, 'rb') as file:
#     model = pickle.load(file)

# # Load the dataset
# data = pd.read_csv("C:/Users/divya/DATASETS/AQIdata1.csv")

# # Features
# features_to_keep = ["PM-2.5 conc", "PM-10 conc", "NO2 conc", "SO2 conc", "CO conc", "Ozone conc"]

# # Initialize session state for Scenario Analysis toggle
# if "show_analysis" not in st.session_state:
#     st.session_state["show_analysis"] = False

# # Title
# st.markdown('<div class="header-style">AQI Predictor</div>', unsafe_allow_html=True)
# st.write("Analyze air quality data and predict AQI levels.")


# # Sidebar input form
# st.sidebar.header("Enter AQI Inputs")
# pm25 = st.sidebar.number_input("PM-2.5 conc (µg/m³)", min_value=0.0, max_value=1000.0, value=10.0)
# pm10 = st.sidebar.number_input("PM-10 conc (µg/m³)", min_value=0.0, max_value=1000.0, value=10.0)
# no2 = st.sidebar.number_input("NO2 conc (µg/m³)", min_value=0.0, max_value=1000.0, value=10.0)
# so2 = st.sidebar.number_input("SO2 conc (µg/m³)", min_value=0.0, max_value=1000.0, value=10.0)
# co = st.sidebar.number_input("CO conc (mg/m³)", min_value=0.0, max_value=10.0, value=0.5)
# ozone = st.sidebar.number_input("Ozone conc (µg/m³)", min_value=0.0, max_value=10.0, value=0.05)

# # Prediction in the Sidebar
# if st.sidebar.button("Predict AQI"):
#     input_data = pd.DataFrame([[pm25, pm10, no2, so2, co, ozone]], columns=features_to_keep)
#     prediction = model.predict(input_data)
#     aqi_value = prediction[0]

#     # AQI categories
#     if aqi_value <= 50:
#         category = "Good"
#         color = "#2ecc71"
#     elif aqi_value <= 99:
#         category = "Moderate"
#         color = "#f1c40f"
#     elif aqi_value <= 130:
#         category = "Unhealthy for Sensitive Groups"
#         color = "#e67e22"
#     elif aqi_value <= 200:
#         category = "Unhealthy"
#         color = "#e74c3c"
#     elif aqi_value <= 250:
#         category = "Very Unhealthy"
#         color = "#9b59b6"
#     else:
#         category = "Hazardous"
#         color = "#7f0000"

#     # Display results in the sidebar
#     st.sidebar.markdown(f"### Predicted AQI: **{aqi_value:.2f}**")
#     st.sidebar.markdown(f"<div style='font-size:1.2em; color:{color}; font-weight:bold;'>Category: {category}</div>", unsafe_allow_html=True)

# # Checkbox for displaying data sample
# if st.checkbox("Show data sample"):
#     st.markdown('<div class="subheader-style">Data Sample</div>', unsafe_allow_html=True)
#     st.write(data[features_to_keep].head())  # Display the first few rows of the dataset

# # Scenario Analysis Button
# if st.button("Show Scenario Analysis"):
#     st.session_state["show_analysis"] = True

# # Scenario Analysis Section
# if st.session_state["show_analysis"]:
#     st.markdown('<div class="large-text">Adjust Parameters and Predict AQI</div>', unsafe_allow_html=True)

#     # Sliders for input adjustments
#     new_pm25 = st.slider("PM-2.5 concentration (µg/m³)", 0.0, 1000.0, 50.0, step=10.0)
#     new_pm10 = st.slider("PM-10 concentration (µg/m³)", 0.0, 1000.0, 50.0, step=10.0)
#     new_no2 = st.slider("NO2 concentration (µg/m³)", 0.0, 1000.0, 50.0, step=10.0)
#     new_so2 = st.slider("SO2 concentration (µg/m³)", 0.0, 1000.0, 50.0, step=10.0)
#     new_co = st.slider("CO concentration (mg/m³)", 0.0, 10.0, 0.5, step=0.1)
#     new_ozone = st.slider("Ozone concentration (µg/m³)", 0.0, 10.0, 0.5, step=0.1)

#     # Predict AQI for updated inputs
#     scenario_data = pd.DataFrame([[new_pm25, new_pm10, new_no2, new_so2, new_co, new_ozone]], columns=features_to_keep)
#     scenario_prediction = model.predict(scenario_data)
#     scenario_aqi = scenario_prediction[0]

#     st.success(f"Scenario Predicted AQI: {scenario_aqi:.2f}")

#     # Display category
#     if scenario_aqi <= 50:
#         scenario_category = "Good"
#         scenario_color = "#2ecc71"
#     elif scenario_aqi <= 99:
#         scenario_category = "Moderate"
#         scenario_color = "#f1c40f"
#     elif scenario_aqi <= 130:
#         scenario_category = "Unhealthy for Sensitive Groups"
#         scenario_color = "#e67e22"
#     elif scenario_aqi <= 200:
#         scenario_category = "Unhealthy"
#         scenario_color = "#e74c3c"
#     elif scenario_aqi <= 250:
#         scenario_category = "Very Unhealthy"
#         scenario_color = "#9b59b6"
#     else:
#         scenario_category = "Hazardous"
#         scenario_color = "#7f0000"

#     st.markdown(f"<div style='font-size:1.5em; color:{scenario_color}; font-weight:bold;'>Scenario Category: {scenario_category}</div>", unsafe_allow_html=True)

#     # Visualization for scenario AQI
#     fig, ax = plt.subplots(figsize=(6, 2))
#     ax.barh(["Scenario AQI"], [scenario_aqi], color=scenario_color)
#     ax.set_xlim(0, 300)
#     ax.set_xlabel("AQI Value")
#     st.pyplot(fig)































# finalcode for the presentation
# Required modules
import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background: linear-gradient(to bottom, #e3f2fd, #ffffff);
            color: #333333;
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background: linear-gradient(to right, #42a5f5, #1e88e5);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.6em 1.5em;
            font-size: 1em;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background: linear-gradient(to right, #1e88e5, #1565c0);
            transform: translateY(-2px);
        }
        .header-style {
            font-size: 4.5em;
            font-weight: bold;
            text-align: center;
            color: #1565c0;
            margin-bottom: 0.5em;
        }
        .header-style1{
            font-weight: bold;
            font-size: 2.5em;
        }
        .subheader-style {
            font-size: 1.8em;
            font-weight: bold;
            color: #1565c0;
            margin-bottom: 0.5em;
        }
    </style>
""", unsafe_allow_html=True)
# unsafe_allow_html=True:Allows the usage of raw HTML and CSS for better customization.


# Load the trained model
model_path = "C:/Users/divya/DATASETS/aqi_rf_reg_model.pkl"
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Load the dataset
data = pd.read_csv("C:/Users/divya/DATASETS/AQIdata1.csv")

# Features
features_to_keep = ["PM-2.5 conc", "PM-10 conc", "NO2 conc", "SO2 conc", "CO conc", "Ozone conc"]

# Title
st.markdown('<div class="header-style">AQI Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="header-style1">Analyze air quality data and predict AQI levels.</div>', unsafe_allow_html=True)


# displaying data sample
if st.checkbox("Show data sample"):
    st.markdown('<div class="subheader-style">Data Sample</div>', unsafe_allow_html=True)
    st.write(data[features_to_keep].head())  # Display the first few rows of the dataset


# Sidebar input form
st.sidebar.header("Enter AQI Inputs")
pm25 = st.sidebar.number_input("PM-2.5 conc (µg/m³)", min_value=0.0, max_value=1000.0, value=10.0)
pm10 = st.sidebar.number_input("PM-10 conc (µg/m³)", min_value=0.0, max_value=1000.0, value=10.0)
no2 = st.sidebar.number_input("NO2 conc (µg/m³)", min_value=0.0, max_value=1000.0, value=10.0)
so2 = st.sidebar.number_input("SO2 conc (µg/m³)", min_value=0.0, max_value=1000.0, value=10.0)
co = st.sidebar.number_input("CO conc (µg/m³)", min_value=0.0, max_value=10.0, value=0.5)
ozone = st.sidebar.number_input("Ozone conc (µg/m³)", min_value=0.0, max_value=10.0, value=0.05)

# Initialize session state for sliders
if "slider_values" not in st.session_state:
    st.session_state.slider_values = {
        "PM-2.5": 50.0,
        "PM-10": 50.0,
        "NO2": 50.0,
        "SO2": 50.0,
        "CO": 1.0,
        "Ozone": 0.1
    }
if "scenario_active" not in st.session_state:
    st.session_state.scenario_active = False

# Function for prediction and category
def predict_aqi(inputs):
    prediction = model.predict(inputs)[0]
    if prediction <= 50:
        category = "Good"
        color = "#2ecc71"
    elif prediction <= 99:
        category = "Moderate"
        color = "#f1c40f"
    elif prediction <= 130:
        category = "Unhealthy for Sensitive Groups"
        color = "#e67e22"
    elif prediction <= 200:
        category = "Unhealthy"
        color = "#e74c3c"
    elif prediction <= 250:
        category = "Very Unhealthy"
        color = "#9b59b6"
    else:
        category = "Hazardous"
        color = "#7f0000"
    return prediction, category, color

# Sidebar prediction button
if st.sidebar.button("Predict AQI"):
    input_data = pd.DataFrame([[pm25, pm10, no2, so2, co, ozone]], columns=features_to_keep)
    aqi_value, category, color = predict_aqi(input_data)
    st.sidebar.success(f"Predicted AQI: {aqi_value:.2f}")
    st.sidebar.markdown(f"<div style='color:{color}; font-weight:bold;'>Index Category: {category}</div>", unsafe_allow_html=True)


# Button to toggle scenario analysis
if st.button("Start Scenario Analysis"):
    st.session_state.scenario_active = not st.session_state.scenario_active

# Scenario analysis section:-
if st.session_state.scenario_active:
    st.markdown('<div class="subheader-style">Adjust the values below:</div>', unsafe_allow_html=True)

    # Interactive sliders in an expander
    with st.expander("Adjust Parameters and Predict AQI", expanded=False):

        # Sliders for input adjustments
        new_pm25 = st.slider("PM-2.5 concentration (µg/m³)", 0.0, 300.00, 250.00, step=10.0)
        new_pm10 = st.slider("PM-10 concentration (µg/m³)", 0.0, 300.00, 250.00, step=10.0)
        new_no2 = st.slider("NO2 concentration (µg/m³)", 0.0, 300.00, 250.00, step=10.0)
        new_so2 = st.slider("SO2 concentration (µg/m³)", 0.0, 300.00, 250.00, step=10.0)
        new_co = st.slider("CO concentration (µg/m³)", 0.0, 10.00, 8.00, step=0.1)
        new_ozone = st.slider("Ozone concentration (µg/m³)", 0.0, 10.00, 8.00, step=0.1)

        # Predict AQI for updated inputs
        scenario_data = pd.DataFrame([[new_pm25, new_pm10, new_no2, new_so2, new_co, new_ozone]], columns=features_to_keep)
        scenario_prediction = model.predict(scenario_data)
        scenario_aqi = scenario_prediction[0]

        st.success(f"Scenario Predicted AQI: {scenario_aqi:.2f}")

        # Display category
        if scenario_aqi <= 50:
            scenario_category = "Good"
            scenario_color = "#2ecc71"
        elif scenario_aqi <= 99:
            scenario_category = "Moderate"
            scenario_color = "#f1c40f"
        elif scenario_aqi <= 130:
            scenario_category = "Unhealthy for Sensitive Groups"
            scenario_color = "#e67e22"
        elif scenario_aqi <= 200:
            scenario_category = "Unhealthy"
            scenario_color = "#e74c3c"
        elif scenario_aqi <= 250:
            scenario_category = "Very Unhealthy"
            scenario_color = "#9b59b6"
        else:
            scenario_category = "Hazardous"
            scenario_color = "#7f0000"

        st.markdown(f"<div style='font-size:1.5em; color:{scenario_color}; font-weight:bold;'>Scenario Category: {scenario_category}</div>", unsafe_allow_html=True)

        # Visualization for scenario AQI
        fig, ax = plt.subplots(figsize=(6, 2))
        ax.barh(["Scenario AQI"], [scenario_aqi], color=scenario_color)
        ax.set_xlim(0, 500)
        ax.set_title("Scenario AQI Level", fontsize=14)
        ax.set_xlabel("Air Quality Index")
        st.pyplot(fig)


# countinue nhi h
# # Comparative analysis section
# st.markdown('<div class="subheader-style">Comparative AQI Analysis</div>', unsafe_allow_html=True)

# # Number of locations to compare
# num_locations = st.number_input("Number of locations to compare:", min_value=1, max_value=5, value=2, step=1)

# location_data = []
# for i in range(int(num_locations)):
#     st.markdown(f"### Location {i+1}")
#     loc_pm25 = st.number_input(f"PM-2.5 for Location {i+1}", min_value=0.0, max_value=1000.0, value=50.0)
#     loc_pm10 = st.number_input(f"PM-10 for Location {i+1}", min_value=0.0, max_value=1000.0, value=50.0)
#     loc_no2 = st.number_input(f"NO2 for Location {i+1}", min_value=0.0, max_value=1000.0, value=50.0)
#     loc_so2 = st.number_input(f"SO2 for Location {i+1}", min_value=0.0, max_value=1000.0, value=50.0)
#     loc_co = st.number_input(f"CO for Location {i+1}", min_value=0.0, max_value=10.0, value=1.0)
#     loc_ozone = st.number_input(f"Ozone for Location {i+1}", min_value=0.0, max_value=10.0, value=0.1)
    
#     location_data.append([loc_pm25, loc_pm10, loc_no2, loc_so2, loc_co, loc_ozone])

# if st.button("Compare Locations"):
#     # Create DataFrame for all locations
#     location_df = pd.DataFrame(location_data, columns=features_to_keep)

#     # Predict AQI for all locations
#     location_predictions = model.predict(location_df)
    
#     # Display Results
#     results = []
#     for idx, pred in enumerate(location_predictions):
#         if pred <= 50:
#             category = "Good"
#             color = "#2ecc71"
#         elif pred <= 99:
#             category = "Moderate"
#             color = "#f1c40f"
#         elif pred <= 130:
#             category = "Unhealthy for Sensitive Groups"
#             color = "#e67e22"
#         elif pred <= 200:
#             category = "Unhealthy"
#             color = "#e74c3c"
#         elif pred <= 250:
#             category = "Very Unhealthy"
#             color = "#9b59b6"
#         else:
#             category = "Hazardous"
#             color = "#7f0000"

#         results.append((f"Location {idx+1}", pred, category, color))
    
#     # Display Table
#     st.markdown('<div class="subheader-style">Comparison Results</div>', unsafe_allow_html=True)
#     comparison_df = pd.DataFrame(results, columns=["Location", "AQI Value", "Category", "Color"])
#     st.dataframe(comparison_df[["Location", "AQI Value", "Category"]])

#     # Visualization
#     fig, ax = plt.subplots(figsize=(8, 4))
#     bars = ax.bar([res[0] for res in results], [res[1] for res in results], color=[res[3] for res in results])
#     ax.set_title("AQI Comparison Across Locations", fontsize=14)
#     ax.set_ylabel("AQI Value")
#     ax.set_xlabel("Locations")
#     ax.set_ylim(0, 500)
#     st.pyplot(fig)











# # Required modules
# import streamlit as st
# import pickle
# import pandas as pd
# import matplotlib.pyplot as plt

# # Custom CSS for styling
# st.markdown("""
#     <style>
#         body {
#             background: linear-gradient(to bottom, #e3f2fd, #ffffff);
#             color: #333333;
#             font-family: 'Arial', sans-serif;
#         }
#         .stButton>button {
#             background: linear-gradient(to right, #42a5f5, #1e88e5);
#             color: white;
#             border: none;
#             border-radius: 8px;
#             padding: 0.6em 1.5em;
#             font-size: 1em;
#             font-weight: bold;
#             cursor: pointer;
#             box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#             transition: all 0.3s ease;
#         }
#         .stButton>button:hover {
#             background: linear-gradient(to right, #1e88e5, #1565c0);
#             transform: translateY(-2px);
#         }
#         .header-style {
#             font-size: 4.5em;
#             font-weight: bold;
#             text-align: center;
#             color: #1565c0;
#             margin-bottom: 0.5em;
#         }
#         .header-style1{
#             font-weight: bold;
#             font-size: 2.5em;
#         }
#         .subheader-style {
#             font-size: 1.8em;
#             font-weight: bold;
#             color: #1565c0;
#             margin-bottom: 0.5em;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Load the trained model
# model_path = "C:/Users/divya/DATASETS/aqi_rf_reg_model.pkl"
# with open(model_path, 'rb') as file:
#     model = pickle.load(file)

# # Features
# features_to_keep = ["PM-2.5 conc", "PM-10 conc", "NO2 conc", "SO2 conc", "CO conc", "Ozone conc"]

# # Title
# st.markdown('<div class="header-style">AQI Predictor</div>', unsafe_allow_html=True)
# st.markdown('<div class="header-style1">Analyze air quality data and predict AQI levels.</div>', unsafe_allow_html=True)

# # Sidebar input form
# st.sidebar.header("Enter AQI Inputs")
# pm25 = st.sidebar.number_input("PM-2.5 conc (µg/m³)", min_value=0.0, max_value=1000.0, value=10.0)
# pm10 = st.sidebar.number_input("PM-10 conc (µg/m³)", min_value=0.0, max_value=1000.0, value=10.0)
# no2 = st.sidebar.number_input("NO2 conc (µg/m³)", min_value=0.0, max_value=1000.0, value=10.0)
# so2 = st.sidebar.number_input("SO2 conc (µg/m³)", min_value=0.0, max_value=1000.0, value=10.0)
# co = st.sidebar.number_input("CO conc (µg/m³)", min_value=0.0, max_value=10.0, value=0.5)
# ozone = st.sidebar.number_input("Ozone conc (µg/m³)", min_value=0.0, max_value=10.0, value=0.05)

# # Function for prediction and category
# def predict_aqi(inputs):
#     prediction = model.predict(inputs)[0]
#     if prediction <= 50:
#         category = "Good"
#         color = "#2ecc71"
#     elif prediction <= 99:
#         category = "Moderate"
#         color = "#f1c40f"
#     elif prediction <= 130:
#         category = "Unhealthy for Sensitive Groups"
#         color = "#e67e22"
#     elif prediction <= 200:
#         category = "Unhealthy"
#         color = "#e74c3c"
#     elif prediction <= 250:
#         category = "Very Unhealthy"
#         color = "#9b59b6"
#     else:
#         category = "Hazardous"
#         color = "#7f0000"
#     return prediction, category, color

# # Sidebar prediction button
# if st.sidebar.button("Predict AQI"):
#     input_data = pd.DataFrame([[pm25, pm10, no2, so2, co, ozone]], columns=features_to_keep)
#     aqi_value, category, color = predict_aqi(input_data)
#     st.sidebar.success(f"Predicted AQI: {aqi_value:.2f}")
#     st.sidebar.markdown(f"<div style='color:{color}; font-weight:bold;'>Index Category: {category}</div>", unsafe_allow_html=True)

# # Comparative analysis section
# st.markdown('<div class="subheader-style">Comparative AQI Analysis</div>', unsafe_allow_html=True)

# # Number of locations to compare
# num_locations = st.number_input("Number of locations to compare:", min_value=1, max_value=5, value=2, step=1)

# location_data = []
# for i in range(int(num_locations)):
#     st.markdown(f"### Location {i+1}")
#     loc_pm25 = st.number_input(f"PM-2.5 for Location {i+1}", min_value=0.0, max_value=1000.0, value=50.0)
#     loc_pm10 = st.number_input(f"PM-10 for Location {i+1}", min_value=0.0, max_value=1000.0, value=50.0)
#     loc_no2 = st.number_input(f"NO2 for Location {i+1}", min_value=0.0, max_value=1000.0, value=50.0)
#     loc_so2 = st.number_input(f"SO2 for Location {i+1}", min_value=0.0, max_value=1000.0, value=50.0)
#     loc_co = st.number_input(f"CO for Location {i+1}", min_value=0.0, max_value=10.0, value=1.0)
#     loc_ozone = st.number_input(f"Ozone for Location {i+1}", min_value=0.0, max_value=10.0, value=0.1)
#     location_data.append([loc_pm25, loc_pm10, loc_no2, loc_so2, loc_co, loc_ozone])

# if st.button("Compare Locations"):
#     # Create DataFrame for all locations
#     location_df = pd.DataFrame(location_data, columns=features_to_keep)

#     # Predict AQI for all locations
#     location_predictions = model.predict(location_df)
    
#     # Display Results
#     results = []
#     for idx, pred in enumerate(location_predictions):
#         if pred <= 50:
#             category = "Good"
#             color = "#2ecc71"
#         elif pred <= 99:
#             category = "Moderate"
#             color = "#f1c40f"
#         elif pred <= 130:
#             category = "Unhealthy for Sensitive Groups"
#             color = "#e67e22"
#         elif pred <= 200:
#             category = "Unhealthy"
#             color = "#e74c3c"
#         elif pred <= 250:
#             category = "Very Unhealthy"
#             color = "#9b59b6"
#         else:
#             category = "Hazardous"
#             color = "#7f0000"
#         results.append((f"Location {idx+1}", pred, category, color))
    
#     # Display Table
#     st.markdown('<div class="subheader-style">Comparison Results</div>', unsafe_allow_html=True)
#     comparison_df = pd.DataFrame(results, columns=["Location", "AQI Value", "Category", "Color"])
#     st.dataframe(comparison_df[["Location", "AQI Value", "Category"]])

#     # Visualization
#     fig, ax = plt.subplots(figsize=(8, 4))
#     bars = ax.bar([res[0] for res in results], [res[1] for res in results], color=[res[3] for res in results])
#     ax.set_title("AQI Comparison Across Locations", fontsize=14)
#     ax.set_ylabel("AQI Value")
#     ax.set_xlabel("Locations")
#     ax.set_ylim(0, 500)
#     st.pyplot(fig)



