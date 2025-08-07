import ctypes
import time
import argparse
import sys

# Constants from the Windows API
KEYEVENTF_KEYUP = 0x0002
VK_NUMLOCK = 0x90  # Virtual-Key code for the NumLock key

def press_numlock():
    """
    Simulates a quick tap of the NumLock key to keep the system active.
    """
    ctypes.windll.user32.keybd_event(VK_NUMLOCK, 0, 0, 0)  # Press
    ctypes.windll.user32.keybd_event(VK_NUMLOCK, 0, KEYEVENTF_KEYUP, 0)  # Release

def keep_active(interval=47):
    try:
        print(f"Keeping system active. Pressing 'NumLock' key every {interval} seconds.")
        while True:
            press_numlock()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nScript terminated by user. Exiting...")
        sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A script to keep your system active by simulating key presses."
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=47,
        help="Interval in seconds between key presses. Default is 47 seconds.",
    )
    args = parser.parse_args()
    keep_active(interval=args.interval)
