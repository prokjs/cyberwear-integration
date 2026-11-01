"""Explicitly synthetic HR wire example; not a sensor driver. Python 3.9+."""

import argparse
import math
import socket
import struct
import time


PREFIX = "/avatar/parameters/"


def osc_string(value):
    data = value.encode("utf-8") + b"\0"
    return data + b"\0" * (-len(data) % 4)


def encode(parameter, value):
    address = osc_string(PREFIX + parameter)
    if isinstance(value, bool):
        return address + osc_string(",T" if value else ",F")
    if isinstance(value, float):
        return address + osc_string(",f") + struct.pack(">f", value)
    raise TypeError("This HR example accepts only OSC bool and float values")


def send(sock, destination, parameter, value):
    sock.sendto(encode(parameter, value), destination)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bpm", type=int, required=True, help="SYNTHETIC BPM, 1-200")
    parser.add_argument("--seconds", type=float, default=3, help="Demo duration, positive seconds")
    parser.add_argument("--port", type=int, default=9000, help="Local OSC UDP port")
    args = parser.parse_args()
    if not 1 <= args.bpm <= 200:
        parser.error("--bpm must be 1-200")
    if not math.isfinite(args.seconds) or args.seconds <= 0:
        parser.error("--seconds must be finite and positive")
    if not 1 <= args.port <= 65535:
        parser.error("--port must be 1-65535")

    destination = ("127.0.0.1", args.port)
    print(f"SYNTHETIC demo: {args.bpm} BPM -> {destination}; stop other HR senders first.")
    heartbeat = False
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        deadline = time.monotonic() + args.seconds
        try:
            while time.monotonic() < deadline:
                heartbeat = not heartbeat
                send(sock, destination, "hr_percent", args.bpm / 200.0)
                send(sock, destination, "hr_connected", True)
                send(sock, destination, "PersonalLink/Heartbeat", heartbeat)
                time.sleep(min(1.0, max(0.0, deadline - time.monotonic())))
        except KeyboardInterrupt:
            pass
        finally:
            send(sock, destination, "hr_connected", False)
            send(sock, destination, "hr_percent", 0.0)
    print("Demo stopped; sent HR unavailable/zero. UDP delivery is not guaranteed.")


if __name__ == "__main__":
    main()
