import subprocess
import time

def vpndisconnect_command():
    disconnect_command = "protonvpn-cli d -r -p tcp 2>/dev/null"
    subprocess.run(disconnect_command, shell=True)
# Function to change the ProtonVPN connection
def change_protonvpn_connection():

    # Connect to a random ProtonVPN server
    connect_command = "protonvpn-cli c -r -p tcp 2>/dev/null"
    subprocess.run(connect_command, shell=True)

# Function to parse user input for the time interval
def parse_time_interval(interval_str):
    if interval_str.endswith("s"):
        return int(interval_str[:-1])
    elif interval_str.endswith("m"):
        return int(interval_str[:-1]) * 60  # Convert minutes to seconds
    else:
        raise ValueError("Invalid time format. Use 'Ns' or 'Nm'.")

# Get user input for the time interval
user_input = input("Enter the time interval (Ex, 30s for seconds or 2m for minutes): ")
try:
    change_interval_seconds = parse_time_interval(user_input)
except ValueError as e:
    print(e)
    exit()

try:
    while True:
        change_protonvpn_connection()
        time.sleep(change_interval_seconds)
except KeyboardInterrupt:
    print("Terminated by user.")
    vpndisconnect_command()