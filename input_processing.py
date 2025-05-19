# input_processing.py
# Jason Chiu, ENSF 692 Spring 2025
# A terminal-based program for processing computer vision changes detected by a car.

# No global variables are permitted

# Sensor Class: 
# Represents a sensor with foundations for a sensor one might use for obstacle detection.
# Has 4 attributes, 3 for object types being sensed i.e. traffic light, pedestrian, and vehicular presense.
# Has method update_status to call for input information that can be typed in the terminal.
class Sensor:
    """A class used to create Sensor object
    
        Attributes:
            light (str): String that represents the sensed traffic light color
            pedestrian (str): String that represents a pedestrian being present or not
            vehicle (str): String that represents a vehicle being present or not
            status (integer)): Integer to indicate Sensor Response Capability: 0 for off and no
                               response, 1 for on and normal reponse, 2 for on and no response
    """

    # Constructor with default attribute settings for no obstacles and status on
    def __init__(self, light = "green", pedestrian = "no", vehicle = "no", status = 1):
        self.light = light
        self.pedestrian = pedestrian
        self.vehicle = vehicle
        self.status = 1

    # Method for updating the information and status of the sensor object using input type objects and conditions
    def update_status(self):
        print("Are any changes detected in the vision input?")

        # First input to determine what kind of data should be updated using 1, 2, 3, or 0 condition otherwise Invalid
        inputVal = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ")
        if (inputVal == "1"):
            # Keep status to on and normal response
            self.status = 1
            # Second stage input for exact change to the data chosen
            inputLight = input("What change has been identified for the light?: ")
            if (inputLight == "green"):
                self.light = "green"
            elif (inputLight == "yellow"):
                self.light = "yellow"
            elif (inputLight == "red"):
                self.light = "red"
            else:
                print("Invalid vision change")
        elif (inputVal == "2"):
            # Keep status to on and normal response
            self.status = 1
            # Second stage input for exact change to the data chosen
            inputPedes = input("What change has been identified for the status of pedestrian?: ")
            if (inputPedes == "yes"):
                self.pedestrian = "yes"
            elif (inputPedes == "no"):
                self.pedestrian = "no"
            else:
                print("Invalid vision change")
        elif (inputVal == "3"):
            # Keep status to on and normal response
            self.status = 1
            # Second stage input for exact change to the data chosen
            inputVehic = input("What change has been identified for the status of vehicle?: ")
            if (inputVehic == "yes"):
                self.vehicle = "yes"
            elif (inputVehic == "no"):
                self.vehicle = "no"
            else:
                print("Invalid vision change")
        elif (inputVal == "0"):
            # Turn sensor status to off no response
            self.status = 0
            print("Update to sensor changes will now be terminated.")
        else:
            # Keep status to on but no response
            self.status = 2
            print("You must select either 1, 2, 3 or 0. \n")

# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting

# Function with sensor object as input type. Depending on sensor.status condition, either returns without printing sensor data, or
# prints out approprate action based on sensor values and then prints the values of the data itself
def print_message(sensor):
    if (sensor.status == 0 or sensor.status == 2):
        return
    print()
    if (sensor.light == "green" and sensor.pedestrian == "no" and sensor.vehicle == "no"):
        print("Proceed\n")
    elif (sensor.light == "yellow" and sensor.pedestrian == "no" and sensor.vehicle == "no"):
        print("Caution\n")
    else:
        print("STOP\n")
    
    print("Light = " + sensor.light + " , Pedestrian = " + sensor.pedestrian + " , Vehicle = " + sensor.vehicle + "\n")


# Main for testing of Sensor object and methods and update_status functionality
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n ---------------------------------------------------\n")
    # Creating object of class sensor for testing
    test = Sensor()
    
    # loop to continously prompt sensing updates unless certain conditions otherwise i.e. sensor.status is set turn "off" as defined previously
    while (test.status != 0):
        test.update_status()
        print_message(test)


# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()
