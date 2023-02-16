from paramiko import SSHClient
import paramiko

def main():
    print("Creating ssh connection to RPi")
    client = SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('10.242.215.212', username='stephen', password='4thyearproject2022!')
    
    print("Setting up MAVProxy")
    transport = client.get_transport()
    channel = transport.open_session()
    channel.exec_command('python /home/stephen/Desktop/mavproxy.py --out=tcpin:0.0.0.0:14550')
    input("Press enter to stop the mavproxy process...")
    
if __name__ == "__main__":      
    main()