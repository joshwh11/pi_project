# pi_project

### Summary:

Simple project that correlates the AppDynamics Controller, a Raspberry Pi w/ circuit, and GitHub API to give you a physical alert when a health rule is violated in
AppD (we used synthetic job health as the policy). AppDynamics will send a HTTP request via GitHub API, updating a file in a repo. The Raspberry Pi will pick this
change up via the checkHealth.py script, which in turn will turn on/off LED pins on the circuit depending on what the GitHub file is populated with.

### Steps to reproduce:

1. Set up Raspberry Pi with headless Raspian. There are lots of resources online to accomplish this.
2. SSH into RPi.
3. Download libraries to RPi:

     * ```sudo apt update -y && sudo apt upgrade -y```
     * ```sudo apt install python3```
     * ```sudo apt install python3-pip```
     * ```sudo apt install git vim -y```
     * ```pip3 install RPi.GPIO```
     * ```pip3 install requests```
     * ```pip3 install json```
     * ```pip3 install base64```

    Note: JSON and Base64 might already be downloaded via the base Python. If you run into errors installing these, just ignore.

4. This repository includes schematics for your RPi, the script your RPi will run to update the LEDs, and some supplemental files. Clone this git repository to your
   RPi using:

    ```git clone https://github.com/joshwh11/pi_project```

5. Set up breadboard circuit with Raspberry Pi. Requires:

    * Breadboard
    * 3x Female-to-Male wires
    * 2x LED Pins (1 red, 1 yellow)
    * 2x 220Ω Resistors 

    Super rough diagrams for reference are in the "schematic" folder. If you are going for a single light approach, then 2x FTM wires, 1x LED pin, and 1x resistor 
    is needed. Just ignore one of the lights and its connections when you are setting up the breadboard.

6. Test out pins by running the ledTest.py file on your RPi after changing directory to the pi_project folder:

    ```cd pi_project```
    
    ```python3 ledTest.py```
    
7. Now that the lights are working, let's set up a GitHub repository to hold the file that AppDynamics will update when a policy is triggered. Create an account if
   you do not already have one and create a repo with one file named "syntheticHealth.txt" that contains simply a 0 (0 will be the default "off" state of the LED). 
   If a policy is triggered, AppDynamics will update the file to a 1, or "on" state for one of the pins.
   
   Also, you will need a token to authenticate any request to update a GitHub file. To generate a token, click on the icon drop-down at the top right of GitHub page 
   after logging in -> Click "Settings" -> Click "Developer settings" -> Click "Personal access tokens" -> Click "Generate new token"

8. Time to set up an AppDynamics HTTP request action. From the controller, navigate to the Alert & Respond tab, then to HTTP Request Templates, then create a new
   template. Fill in the template like this and MAKE SURE TO READ CAREFULLY AND CONFIGURE WITH YOUR VALUES.
   
   * Method: PUT
   * Raw URL: https://<span></span>api.github.com/repos/\<your username\>/\<your repo\>/contents/syntheticHealth.txt
   * Custom Request Header (everything before the colon goes in the left box, everything after goes in the right box): 
       * Authorization: token \<your token\>
   * Payload:
       * MIME Type: application/json
       * Message: 

    ```
    {
     "message": "update syntheticHealth.txt from AppD",
     "committer": {
      "name": "<your name>",
      "email": "<your email>"
     },
     "content": "MQ==",
     "sha": "<syntheticHealth.txt SHA>"
    }
    ```

    The "committer" values will be your information linked to your GitHub account. The "content" value is the number 1 in Base64 code (Another request
    template should be made with the same parameters, but replace MQ== with MA== for 0 in Base64. This will turn off the light.). The sha value should be the unique 
    SHA identifier given to your syntheticHealth.txt file. This changes sometimes, but you can run the getSHA.py script provided in this repo to find it. Save and
    test this HTTP Request Template.
   
    Note: I went further personally and created a third request, one that passes "Mg==" as the content. This is Base64 for 2 and will turn on a second light.
    Currently, if the text file contains a 2, the RPi app will turn on the red light signifying a critical error. If the text file contains a 1, the RPi will light
    a yellow light signifying a warning. Finally, a 0 will turn off all lights. You can configure to include any number of lights and requests.
    
9. To update the LED pins, the RPi will be continuously running the checkHealth.py application as AppDynamics updates the syntheticHealth.txt file via policy 
   triggers. On your RPi, navigate to pi_project, edit checkHealth.py to have your URL, then run checkHealth.py via:
   
   ```python3 checkHealth.py```
   
   Now the RPi will constantly check the contents of your syntheticHealth.txt file hosted on your GitHub repo and will update the LED pin state given the content
   of the file. Test the app by running an HTTP request test from the AppDynamcis UI. Don't forget to check the SHA via getSHA.py and update the HTTP Request
   Template. You have to save and then reclick the template for the save to go through, then you can use the "test" button.
   
   GitHub has a limited number of requests for each user, so make sure to close out the checkHealth.py script when you are not using it.
   
   ledTest.py can be used to reset the LEDs when needed.
