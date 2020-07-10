# pi_project

Steps to reproduce:

1. Set up Raspberry Pi with headless Raspian
2. SSH into Pi
3. Download libraries to Pi:

* ```sudo apt update -y && sudo apt upgrade -y```
* ```sudo apt install python3```
* ```sudo apt install python3-pip```
* ```sudo apt install git vim -y```
* ```pip3 install RPi.GPIO```
* ```pip3 install requests```

4. Clone git repository to Pi:

    ```git clone https://github.com/joshwh11/pi_project```

5. Set up breadboard with Raspberry Pi. Requires:
* Breadboard
* 3x Female-to-Male wires
* 2x LED Pins (1 red, 1 yellow)
* 2x 220Ω Resistors 

    (Super rough diagrams for reference are in the "schematic" folder)

6. Test out pins by running the ledtest.py file after changing directory to the pi_project folder

    ```cd pi_project```
    
    ```python3 ledtest.py```