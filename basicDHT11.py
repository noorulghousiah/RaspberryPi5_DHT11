import RPi.GPIO as GPIO
import dht11
import time
import datetime

# Initialize GPIO settings
GPIO.setwarnings(True) # Enable GPIO warnings
GPIO.setmode(GPIO.BCM) # Use BCM (Broadcom) numbering for GPIO pins

# Initialize DHT11 sensor instance on GPIO pin 4
instance = dht11.DHT11(pin=4)

try:
    while True:
        # Read data from the DHT11 sensor
        result = instance.read()

        # Check if the reading is valid
        if result.is_valid():
            # Print the current timestamp, temperature, and humidity
            print("Last valid input: " + str(datetime.datetime.now()))
            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)
        else:
            # Print the error code if the reading is invalid
            # comment out this line for troubleshooting purposes
            print("Error: %d" % result.error_code)

            #add a small delay before retrying to read sensor
            time.sleep(0.001) 
            

        # Wait for 2 seconds before the next reading
        #(DHT11 requires at least 1 second between reads)
        # comment out this line if use Pi 3
        time.sleep(2)  

except KeyboardInterrupt:
    # Cleanup GPIO settings before exiting the program
    print("Cleanup")
    GPIO.cleanup()
