"""
In this Program track the current location of ISS(International Space Station) and then maps the location.
We will write a script that will display the current location of ISS along with onboarded crew names.
It works on API, it takes the current location of ISS in the form of latitude and longitude and then locates
that value onto the map. It takes the value from the website at every 5 sec and then updates the
value of latitude and longitude and thus also moves the ISS icon on the world map
"""
import requests
import webbrowser
import geocoder
import turtle
import time


def current_iss_location():
    check_iss = True

    screen = turtle.Screen()
    screen.setup(1280, 720)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic("images\map.gif")
    screen.register_shape("images\iss.gif")
    iss = turtle.Turtle()
    iss.shape("images\iss.gif")
    iss.setheading(45)
    iss.penup()
    time.sleep(5)

    while check_iss:
        try:
            # Open the url
            response = requests.get("http://api.open-notify.org/iss-now.json")

            response.raise_for_status()  # Raises an HTTPError for non-200 status codes

            # Process the response data here if needed
            if response.status_code == 200:
                resp_msg = response.json()

                IssPos = resp_msg['iss_position']
                Iss_Lat = IssPos['latitude']
                Iss_Lon = IssPos['longitude']

                print("\n Latitude: " + str(Iss_Lat))
                print("\n Longitude: " + str(Iss_Lon))

                # Update the ISS location on the map
                iss.goto(float(Iss_Lon), float(Iss_Lat))

                # Refresh each 5 seconds
                time.sleep(5)

            else:
                print(response.status_code)

        except requests.HTTPError as e:
            print(f"HTTP error occurred: {e}")

        except requests.RequestException as e:
            print(f"An error occurred: {e}")


def write_iss(iss_names, no_iss):
    g = geocoder.ip('me')
    with open('iss.txt', 'w') as iss_txt:
        iss_txt.write(f"There are currently {no_iss} astronauts on the ISS:\n\n")
        for astronaut in iss_names:
            iss_txt.write(f"{astronaut} - on board\n")

        iss_txt.write("\nYour current lat / long is: " + str(g.latlng))
    webbrowser.open("iss.txt")
    current_iss_location()


def main():
    try:
        # Open the url
        response = requests.get("http://api.open-notify.org/astros.json")

        response.raise_for_status()  # Raises an HTTPError for non-200 status codes

        # Process the response data here if needed
        if response.status_code == 200:
            resp_msg = response.json()

            write_iss(resp_msg['people'], resp_msg['number'])
        else:
            print(response.status_code)

    except requests.HTTPError as e:
        print(f"HTTP error occurred: {e}")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
