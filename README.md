# SafeWalkDrone
Github for the Carleton University Safe Walk Drone Capstone project. 
By Graham Kendall, Stephen Batterton, Bailey Lyster and Conor Johnson Martin.

Setup:

pip install paramiko
pip install dronekit
pip install dronekit-sitl

Startup:

Ensure the ground station machine is connected to the project zerotier network.

python rpi_station/main.py
python ground_station/main.py

The script should start MAVProxy on RPi and then start the automated control of the drone.