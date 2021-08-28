"""
A small Pomodoro timer in Python.
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
