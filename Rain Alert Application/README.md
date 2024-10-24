# Weather Alert Application

This Python code uses the OpenWeatherMap API to fetch the weather forecast for a specific location and sends a WhatsApp message if rain is expected. The message is sent via Twilio's API.

## Features

- Fetches weather data using OpenWeatherMap API.
- Detects if it will rain within the next 4 time periods.
- Sends a WhatsApp message alert using Twilio if rain is detected.

## Requirements

- Python 3.x
- A Twilio account with WhatsApp enabled
- An OpenWeatherMap API key



## Code Explanation

The Code performs the following steps:

1. **Imports**:
   - `requests`: Used to make API requests to OpenWeatherMap.
   - `twilio.rest.Client`: Used to send messages via Twilio's API.
   
2. **Weather API Request**:
   - A `GET` request is made to the OpenWeatherMap API using the specified latitude, longitude, and API key to get the weather forecast.
   
3. **Weather Condition Check**:
   - The response JSON is parsed, and the script checks each weather condition in the forecast.
   - If any of the conditions have a code less than 700 (indicating rain), the `will_rain` flag is set to `True`.

4. **Twilio Messaging**:
   - If rain is expected, the Twilio API sends a WhatsApp message to the specified number, notifying the user to carry an umbrella.

### Example Weather Conditions:
- Codes below 700 generally indicate rain, snow, or other forms of precipitation.
- The code checks for rain and sends a WhatsApp message if rain is detected in the forecast.
