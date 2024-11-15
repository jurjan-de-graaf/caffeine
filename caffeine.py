import pyautogui
import time
import argparse
import sys


def keep_active(interval=47):
    """
    Keeps the system active by pressing a harmless key every 'interval' seconds.

    :param interval: Wait time between key presses in seconds.
    """
    try:
        print(f"Keeping system active. Pressing 'Shift' key every {interval} seconds.")
        while True:
            pyautogui.press('shift')  
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
