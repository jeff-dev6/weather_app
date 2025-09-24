import requests
import smtplib 
from email.mime.text import MIMEText
from datetime import datetime
import json

with open("config.json") as file:
    config = json.load(file)

# ---------CONFIGURATION-----------
API_KEY = config["api_key"]
CITY = config["city"]
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
sender_email = config["sender_email"]
receiver_email = config["receiver_email"]
app_password = config["app_password"]

# -------- FETCH WEATHER DATA ---------
response = requests.get(URL)
if response.status_code == 200:
    data = response.json()
    city = data["name"]
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    report = f"{now} - City: {city}, Temp: {temp}°C, Weather: {weather}\n" 
else:
     print("Error fetching weather data:", response.status_code) 

# --------- SAVE TO FILE ---------
with open("weather_report.txt", "a") as file:
    file.write(report) 
    print("Weather report saved")

# --------- SEND EMAIL ---------
msg = MIMEText(report)
msg["Subject"] = f"Weather Report for Abuja - {now}"
msg["From"] = sender_email
msg["To"] = receiver_email

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receiver_email, msg.as_string()) 

    print("Email sent successfully!")
 
    


