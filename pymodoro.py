"""
A small Pomodoro timer in Python.
"""

import argparse
import sys
import time

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
    try:
        while True:
            # FOCUS
            if args.focus_time > 1:
                output = f"Focusing ({args.focus_time} mins)"
            else:
                output = f"Focusing ({args.focus_time} min)"

            sleep_and_track(
                args.focus_time * 60, output)

            # BREAK
            if args.break_time > 1:
                output = f"Resting ({args.break_time} mins)"
            else:
                output = f"Resting ({args.break_time} min)"

            sleep_and_track(args.break_time * 60, output)

    except KeyboardInterrupt:
        # Catch this to remove Python's ugly exception.
        return 0


if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)
