#!/usr/bin/python3
import subprocess
import time
import argparse

def vpndisconnect_command():
    disconnect_command = "protonvpn-cli d -r -p tcp 2>/dev/null"
    subprocess.run(disconnect_command, shell=True)

def change_protonvpn_connection(use_faster, use_random, use_tor, protocol):
    # Use '-f' or '--faster' option if 'use_faster' is True
    faster_option = "-f" if use_faster else ""
    
    # Use '-r' or '--random' option if 'use_random' is True
    random_option = "-r" if use_random else ""
    
    # Use '--tor' option if 'use_tor' is True
    tor_option = "--tor" if use_tor else ""
    
    # Use '-p' or '--protocol' option to specify the protocol
    protocol_option = f"-p {protocol}" if protocol else ""
    
    connect_command = f"protonvpn-cli c {faster_option} {random_option} {tor_option} {protocol_option} 2>/dev/null"
    subprocess.run(connect_command, shell=True)

def parse_time_interval(interval_str):
    if interval_str.endswith("s"):
        return int(interval_str[:-1])
    elif interval_str.endswith("m"):
        return int(interval_str[:-1]) * 60  # Convert minutes to seconds
    else:
        raise ValueError("Invalid time format. Use 'Ns' or 'Nm, replace N with Number.")

def main():
    parser = argparse.ArgumentParser(description="Change ProtonVPN connection at specified intervals.")
    parser.add_argument(
        "interval",
        help="Time interval in the format 'Ns' for seconds or 'Nm' for minutes.",
    )
    parser.add_argument(
        "protocol",
        choices=["tcp", "udp"],
        help="Specify the protocol (TCP or UDP) to use.",
    )
    parser.add_argument(
        "-f", "--faster",
        action="store_true",
        help="Use the faster server option (-f or --faster).",
    )
    parser.add_argument(
        "-r", "--random",
        action="store_true",
        help="Use the random server option (-r or --random).",
    )
    parser.add_argument(
        "-t","--tor",
        action="store_true",
        help="Use the Tor connection option (-t or --tor) with ProtonVPN.",
    )
    args = parser.parse_args()
    
    try:
        change_interval_seconds = parse_time_interval(args.interval)
    except ValueError as e:
        print(e)
        exit()
    
    if not (args.faster or args.random or args.tor):
        print("At least one of -f, -r, or -t options must be specified.")
        exit()
    
    try:
        while True:
            change_protonvpn_connection(args.faster, args.random, args.tor, args.protocol)
            time.sleep(change_interval_seconds)
    except KeyboardInterrupt:
        print("Terminated by the user.")
    finally:
        vpndisconnect_command()

if __name__ == "__main__":
    main()
