# RaspberryPi5_DHT11
A method to interface dht11 sensor to Raspberry Pi 5

---

Some sensor may not work with the new Raspberry Pi 5 because they change the chip relating to input control. So, most low-level library for gpio pin control wont work. 

To solve this issue, we can use the rpi-lgpio library because this GPIO library is compatible with  Raspberry Pi 5 (and Raspberry Pi 3, Raspberry Pi 4 too). 
refer this for installation step: https://rpi-lgpio.readthedocs.io/en/latest/install.html

So now, your raspberry pi can run codes importing RPi.GPIO or rpi-lgpio library

After that, for the dht11 library, The library I used are "dht11" from Dave Jones https://github.com/szazo/DHT11_Python. 
This is a pure python library that uses RPi.GPIO library, thus compatible for our Raspberry Pi 5, and also easy to understand@troubleshoot.

To run this, you can run the "basicDHT11.py"

BUT
the library have some inaccuraries that cause the communication error between sensor and Raspberry Pi. This make the program have issue on Pi 4 and Pi 3.

So, I edited the "dht11" library (the "__init__.py" file) and save it as another name ("dht11new"). [I only editted the sleep function in the code.]

So, to run this new improved version, you can run the "dht11code.py" in "Improved version" folder.


Credit to Dave Jones https://github.com/szazo/DHT11_Python for the library that are easy to understand.
