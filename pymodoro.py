#!/usr/bin/env python3
"""
A small Pomodoro timer in Python.
"""

"""
I am trying to add a bit more functionality to the program by allowing the user to exit the infinite pomodoro loop with a 'q' keystroke.  This way I can count the number of focus/break cycles the user did and append the data in a txt file with so I can do some simple data analysis like number of cycles completed per week or number of minutes worked per week.

But I am having trouble working with the rich.progress bar. I'm not sure if it's having trouble due to the terminal being occupied by the timer and not letting the process read and process keyboard input while the bar is working.

Ctrl-c would kill the program and not be incredibly user friendly than a quick 'q' for quit, but I suppose still operational if the keyboard interrupt error is caught and ignored.

Still working on it.
"""
import argparse
import sys
import signal
import time
from typing import NoReturn

import rich.progress


def print_error(*args, **kwargs):
    print(*args, file=sys.stdout, **kwargs)


def sleep_and_track(seconds: int, description: str) -> None:
    """
    Sleep for a given number of seconds and display a progress bar.
    """
    if seconds < 0:
        raise ValueError

    with rich.progress.Progress(transient=True) as progress:
        task = progress.add_task(description, total=seconds)

        while not progress.finished:
            progress.update(
                task,
                advance=1,
            )
            time.sleep(1)


def main() -> int:
    # Exit quietly upon SIGINT.
    def handle_SIGINT(*_) -> NoReturn:
        quit()
    signal.signal(signal.SIGINT, handle_SIGINT)

    # Parse arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "focus_time",
        metavar="focus",
        help="the number of minutes to spend focused",
        default=25,
        type=int
    )
    parser.add_argument(
        "break_time",
        metavar="break",
        help="the number of minutes to spend resting",
        default=5,
        type=int
    )

    args = parser.parse_args()
    if args.focus_time <= 0 or args.break_time <= 0:
        print_error("All time periods must be greater than 0.")
        return 1

    # Pomodoro
    while True:
        # Focus
        description = "Focusing ({} min{})".format(args.focus_time, "s" if args.focus_time > 1 else "")
        sleep_and_track(args.focus_time * 60, description)
        # Break

        description = "Focusing ({} min{})".format(args.break_time, "s" if args.break_time > 1 else "")
        sleep_and_track(args.break_time * 60, description)


if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)
