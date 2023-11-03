# Geolocation tracker using Public IP address
# Using Nominatim
import requests
from geopy.geocoders import Nominatim

# Fetch public IP address
def get_public_ip_address():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        data = response.json()
        public_ip = data["ip"]
        return public_ip
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

# Function for finding the current location
def get_location(locator, current_ip):
    try:
        # Use the locator to get the current location based on IP address
        location = locator.geocode(current_ip, exactly_one=True)

        # Extract latitude and longitude
        latitude = location.latitude
        longitude = location.longitude
        address = location.address

        return latitude, longitude, address

    except Exception as e:
        print(f"Error: {e}")
        return None

# Main
if __name__ == "__main__":
    # Call the function to get the public IP address
    current_ip = get_public_ip_address()
    print("Public IP address:", current_ip)

    if current_ip:
        # Using Nominatim geocoder
        locator = Nominatim(user_agent="geo_locator")
        current_location = get_location(locator, current_ip)

        if current_location:
            latitude, longitude, address = current_location
            print(f"Current Location: Latitude = {latitude}, Longitude = {longitude}")
            print(f"Current Address: {address}")
        else:
            print("Failed to get the current location.")
    else:
        print("Failed to get the public IP address.")
