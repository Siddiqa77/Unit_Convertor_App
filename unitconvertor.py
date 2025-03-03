

# import streamlit as st
# import streamlit.components.v1 as components
# import pyttsx3
# import speech_recognition as sr
# import re

# conversion_factors = {
#     "Length": {
#         "Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Mile": 0.000621371,
#         "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701, "Nanometer": 1e9, "Micrometer": 1e6
#     },
#     "Weight": {
#         "Kilogram": 1, "Gram": 1000, "Pound": 2.20462, "Ounce": 35.274, "Ton": 0.001, "Milligram": 1e6
#     },
#     "Temperature": {
#         "Celsius": lambda c: c, "Fahrenheit": lambda c: (c * 9/5) + 32, "Kelvin": lambda c: c + 273.15
#     },
#     "Speed": {
#         "Meters per second": 1, "Kilometers per hour": 3.6, "Miles per hour": 2.23694, "Knots": 1.94384
#     },
#     "Time": {
#         "Second": 1, "Minute": 1/60, "Hour": 1/3600, "Day": 1/86400
#     }
# }

# unit_aliases = {
#     "m": "Meter", "km": "Kilometer", "cm": "Centimeter", "mm": "Millimeter", "mi": "Mile",
#     "yd": "Yard", "ft": "Foot", "in": "Inch", "nm": "Nanometer", "um": "Micrometer",
#     "kg": "Kilogram", "g": "Gram", "lb": "Pound", "oz": "Ounce", "mg": "Milligram", "t": "Ton",
#     "c": "Celsius", "f": "Fahrenheit", "k": "Kelvin", "mps": "Meters per second",
#     "kph": "Kilometers per hour", "mph": "Miles per hour", "kt": "Knots",
#     "s": "Second", "min": "Minute", "h": "Hour", "d": "Day"
# }

# def convert_units(value, from_unit, to_unit, unit_type):
#     if unit_type == "Temperature":
#         temp_in_celsius = value if from_unit == "Celsius" else (value - 32) * 5/9 if from_unit == "Fahrenheit" else value - 273.15
#         return conversion_factors[unit_type][to_unit](temp_in_celsius)
#     else:
#         return value * (conversion_factors[unit_type][to_unit] / conversion_factors[unit_type][from_unit])

# def speak(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()

# def listen():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.write("🎤 Listening...")
#         try:
#             audio = recognizer.listen(source)
#             command = recognizer.recognize_google(audio)
#             return command.lower()
#         except sr.UnknownValueError:
#             return "Sorry, I didn't understand."
#         except sr.RequestError:
#             return "Speech recognition service unavailable."

# def process_voice_command(command):
#     pattern = r"convert (\d+(\.\d+)?)\s*([a-zA-Z]+)\s*(to|into)\s*([a-zA-Z]+)"
#     match = re.search(pattern, command)
#     if match:
#         try:
#             value = float(match.group(1))
#             from_unit = unit_aliases.get(match.group(3).lower(), match.group(3).capitalize())
#             to_unit = unit_aliases.get(match.group(5).lower(), match.group(5).capitalize())
            
#             for unit_type, units in conversion_factors.items():
#                 if from_unit in units and to_unit in units:
#                     result = convert_units(value, from_unit, to_unit, unit_type)
#                     response = f"{value} {from_unit} is equal to {result:.4f} {to_unit}."
#                     st.write(response)
#                     speak(response)
#                     return
#             st.write("Invalid conversion units.")
#             speak("Invalid conversion units.")
#         except ValueError:
#             st.write("Could not process the conversion command correctly.")
#             speak("Could not process the conversion command correctly.")
#     else:
#         st.write("Command not recognized.")
#         speak("Command not recognized.")

# # Streamlit UI
# st.set_page_config(page_title="Unit Converter App", page_icon="🔄", layout="wide")
# st.markdown("""
#     <style>
#         body {
#             background-color: #f4f4f4;
#             background: linear-gradient(to right, #1e3c72, #2a5298);
#             font-family: Arial, sans-serif;
#         }
#         .container {
#             max-width: 600px;
#             margin: auto;
#             padding: 20px;
#             background: white;
#             border-radius: 10px;
#             box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
#             text-align: center;
#         }
#         h1 {
#             color: #2a5298;
#             font-size: 28px;
#             font-weight: bold;
#             padding: 10px;
#         }
#     </style>
# """, unsafe_allow_html=True)

# st.markdown("<div class='container'><h1>🔄 Unit Converter</h1>", unsafe_allow_html=True)

# unit_types = ["Length", "Weight", "Temperature", "Speed", "Time", "Voice Command"]
# selected_type = st.selectbox("Select Unit Type:", unit_types)

# if selected_type == "Voice Command":
#     st.write("🤖 Speak your conversion command (e.g., Convert 10 m to ft)")
#     if st.button("🎤 Speak Command"):
#         user_command = listen()
#         st.write(f"You said: {user_command}")
#         process_voice_command(user_command)
# else:
#     unit_options = list(conversion_factors[selected_type].keys())
#     from_unit = st.selectbox("From Unit:", unit_options)
#     to_unit = st.selectbox("To Unit:", unit_options)

#     value = st.number_input("Enter Value:", min_value=0.0, format="%.4f")

#     if st.button("Convert"):
#         result = convert_units(value, from_unit, to_unit, selected_type)
#         result_text = f"{value} {from_unit} is equal to {result:.4f} {to_unit}."
#         st.markdown(f"<h2>{result_text}</h2>", unsafe_allow_html=True)
#         speak(result_text)

# st.markdown("</div>", unsafe_allow_html=True)


import streamlit as st
import pyttsx3
import speech_recognition as sr
import re

# Conversion Factors
types = {
    "Length": {"Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Mile": 0.000621371,
                "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701, "Nanometer": 1e9, "Micrometer": 1e6},
    "Weight": {"Kilogram": 1, "Gram": 1000, "Pound": 2.20462, "Ounce": 35.274, "Ton": 0.001, "Milligram": 1e6},
    "Temperature": {"Celsius": lambda c: c, "Fahrenheit": lambda c: (c * 9/5) + 32, "Kelvin": lambda c: c + 273.15},
    "Speed": {"Meters per second": 1, "Kilometers per hour": 3.6, "Miles per hour": 2.23694, "Knots": 1.94384},
    "Time": {"Second": 1, "Minute": 1/60, "Hour": 1/3600, "Day": 1/86400}
}

# Unit Aliases
aliases = {"m": "Meter", "km": "Kilometer", "cm": "Centimeter", "mm": "Millimeter", "mi": "Mile",
           "yd": "Yard", "ft": "Foot", "in": "Inch", "nm": "Nanometer", "um": "Micrometer",
           "kg": "Kilogram", "g": "Gram", "lb": "Pound", "oz": "Ounce", "mg": "Milligram", "t": "Ton",
           "c": "Celsius", "f": "Fahrenheit", "k": "Kelvin", "mps": "Meters per second",
           "kph": "Kilometers per hour", "mph": "Miles per hour", "kt": "Knots",
           "s": "Second", "min": "Minute", "h": "Hour", "d": "Day"}

# Conversion Function
def convert(value, from_unit, to_unit, unit_type):
    if unit_type == "Temperature":
        temp = value if from_unit == "Celsius" else (value - 32) * 5/9 if from_unit == "Fahrenheit" else value - 273.15
        return types[unit_type][to_unit](temp)
    else:
        return value * (types[unit_type][to_unit] / types[unit_type][from_unit])

# Speech Functions
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("🎤 Listening...")
        try:
            audio = recognizer.listen(source)
            return recognizer.recognize_google(audio).lower()
        except sr.UnknownValueError:
            return "Sorry, I didn't understand."
        except sr.RequestError:
            return "Speech recognition service unavailable."

# Process Voice Command
def process_voice_command(command):
    pattern = r"convert (\d+(\.\d+)?)\s*([a-zA-Z]+)\s*(to|into)\s*([a-zA-Z]+)"
    match = re.search(pattern, command)
    if match:
        try:
            value = float(match.group(1))
            from_unit = aliases.get(match.group(3).lower(), match.group(3).capitalize())
            to_unit = aliases.get(match.group(5).lower(), match.group(5).capitalize())
            
            for unit_type, units in types.items():
                if from_unit in units and to_unit in units:
                    result = convert(value, from_unit, to_unit, unit_type)
                    response = f"{value} {from_unit} is equal to {result:.4f} {to_unit}."
                    st.write(response)
                    speak(response)
                    return
            
            st.write("Invalid conversion units.")
            speak("Invalid conversion units.")
        except ValueError:
            st.write("Could not process the conversion command correctly.")
            speak("Could not process the conversion command correctly.")
    else:
        st.write("Command not recognized.")
        speak("Command not recognized.")

# Streamlit UI
st.set_page_config(page_title="Unit Converter App", page_icon="🔄", layout="wide")
st.title("🔄 Unit Converter")

unit_types = list(types.keys()) + ["Voice Command"]
selected_type = st.selectbox("Select Unit Type:", unit_types)

if selected_type == "Voice Command":
    st.write("🤖 Speak your conversion command (e.g., Convert 10 m to ft)")
    if st.button("🎤 Speak Command"):
        user_command = listen()
        st.write(f"You said: {user_command}")
        process_voice_command(user_command)
else:
    unit_options = list(types[selected_type].keys())
    from_unit = st.selectbox("From Unit:", unit_options)
    to_unit = st.selectbox("To Unit:", unit_options)
    value = st.number_input("Enter Value:", min_value=0.0, format="%.4f")
    
    if st.button("Convert"):
        result = convert(value, from_unit, to_unit, selected_type)
        result_text = f"{value} {from_unit} is equal to {result:.4f} {to_unit}."
        st.success(result_text)
        speak(result_text)