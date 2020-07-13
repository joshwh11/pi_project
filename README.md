# pi_project

Steps to reproduce:

1. Set up Raspberry Pi with headless Raspian
2. SSH into RPi
3. Download libraries to RPi:

* ```sudo apt update -y && sudo apt upgrade -y```
* ```sudo apt install python3```
* ```sudo apt install python3-pip```
* ```sudo apt install git vim -y```
* ```pip3 install RPi.GPIO```
* ```pip3 install requests```

4. Clone git repository to RPi:

    ```git clone https://github.com/joshwh11/pi_project```

5. Set up breadboard with Raspberry Pi. Requires:
* Breadboard
* 3x Female-to-Male wires
* 2x LED Pins (1 red, 1 yellow)
* 2x 220Ω Resistors 

    (Super rough diagrams for reference are in the "schematic" folder)

6. Test out pins by running the ledtest.py file after changing directory to the pi_project folder:

    ```cd pi_project```
    
    ```python3 ledtest.py```
    
7. You can also test the app and the request. Install requirements and run the app.py file by executing commands
    
* ```pip3 install -r requirements.txt```
* ```python3 app.py```

    You should see the app running. This will stay running as it is the way the Raspberry Pi listens for requests to change the state of the pins.
    Now open another tab in terminal and SSH back into the RPi. Navigate again to the pi_project folder and run the requestscript.py file by passing the pin ID and 
    the new state of the pin as arguments in terminal. The format for the command should be: python3 requestscript.py \<pin id> \<new pin state>
    
    Example format:
    
    ```python3 requestscript.py 1 on```
    
    This should turn on the red pin. To turn off, replace "on" with "off".

8. Set up port forwarding on laptop/local machine. Open another terminal tab of your local machine, not the RPi. Run command:

    ```ssh -Nf -L localhost:9999:localhost:5000 pi@raspberrypi.local```
    
    Now any request made to the local machine on port 9999 will be routed to the RPi on port 5000. Test by running requestscript.py on your local machine.
    
    **NOTE: In the script, you must change the URL to be 'http://localhost:9999/pins/' since the app is now listening on port 9999**
    
    You can now control the lights via requests on your laptop. In order to stop the SSH port forward, from your local machine run
    
    ```ps aux | grep ssh```
    
    Which will give you a list of SSH processes. Find the port forward process and it's ID, then use
    
    ```kil <id>```
