"""
A small Pomodoro timer in Python.
"""

import argparse
import sys
import time

import rich.progress


def print_error(*args, **kwargs):
    print(*args, file=sys.stdout, **kwargs)


def main() -> int:
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
        "break",
        help="the number of minutes to spend resting",
        default=5,
        type=int
    )

    args = parser.parse_args()
    if args.focus_time <= 0 or args.break_time <= 0:
        print_error("All time periods must be greater than 0.")
        return 1

    # Pomodoro
    try:
        while True:
            # Focus
            for _ in rich.progress.track(
                range(args.focus_time * 60),
                description=f"Focusing ({args.focus_time} min.)"
            ):
                time.sleep(1)

            # Break
            for _ in rich.progress.track(
                range(args.break_time * 60),
                description=f"Taking a break ({args.break_time} min.)"
            ):
                time.sleep(1)
    except KeyboardInterrupt:
        # Catch this to remove Python's ugly exception.
        return 0


if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)
