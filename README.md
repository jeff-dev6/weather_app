# Daily Weather Automation Script

## Overview
This Python project fetches daily weather data for a single city using the OpenWeather API and sends a simple daily weather report via email. 
It demonstrates Python backend skills, API integration, and automation.

## Features
- Fetch weather data for a single city
- Generate daily weather report with timestamp
- Send reports via email automatically
- Save report locally for reference
- Configurable via `config.json`

## Installation & Setup
1. Clone the repository:
2. Move into the project folder: cd weather app
3. Install the required Python packages: pip install -r requirements.txt
4. Open the config.json file and update it with your details: {
    "api_key": "YOUR_OPENWEATHER_API_KEY",
    "sender_email": "your_email",
    "receiver_email": "receiver_email",
    "app_password": "YOUR_APP_PASSWORD",
    "city": "Any City"
}
5. Run the script manually: python weather.py
6. Schedule automatic daily reports:
   On Windows, use Task Scheduler to run weather.py every day.
   On Mac/Linux, use cron jobs.
7. When the script runs, it generates a report like this: "2025-09-24 10:15:00 | Abuja | 29°C | clear sky"

Notes:
Make sure 2-Step Verification is enabled on your Gmail account to use App Password.
The project is easily extendable to multiple cities, HTML emails, or multiple recipients in the future.
config.json is ignored in Git (using .gitignore) so your credentials remain private.






