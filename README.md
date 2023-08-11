# Fastapi - Arduino Project

This was a small project to play around with arduino using python - fastapi and pyfirmata.

The project provides a web interface where you can interact with the arduino board.
Currently, you can only turn on amber LED or green LED, for a specified amount of seconds (default = 5 seconds)

## Getting Started
1. clone the repo
```shell
git clone https://github.com/Anthony-Asamoah/fastapi-arduino-led.git
```

This project **requires** an arduino Uno board loaded with the Standard Firmata Interface and connected to your pc through the 'COM5' port.

If you have an arduino board but haven't loaded firmata, do so using the standard/default arduino IDE (google arduino IDE, download and install if you do not have it). 

In the Arduino IDE, search in the library manager for "FIRMATA" and click install. once that is done, goto File > Examples >
Firmata > StandardFirmata. Then Upload the code onto the selected board.

Check the port through which the arduino board is connected. If the port is not **COM5** then lets modify the repo;
```
open the config.py file using and text editor or IDE
navigate to the "Defaults" class
Modify the "arduino_default" value from "COM5" to whatever port your arduino board is connected through.  
Note that the value should alwyas be a string
```

Once the above conditions are met, you may proceed.

This setup assumes you already have python3 and pipenv installed. If you do not; simply google how to install python and how to install pipenv.
Once those two are available, we proceed.

2. install dependencies (using pipenv)
```shell
pipenv install
```

3. run main.py script
```shell
python main.py
```

4. launch any web browser and enter the project url:
```
127.0.0.1:8080 or localhost:8080
```

### Make available to the public internet
The project creates a local server that interfaces with the arduino board, therefore you can make this local server available to the public internet and access it from anywhere!
visit [ngrok](https://ngrok.com/) for all the details.