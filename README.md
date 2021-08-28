# Overview

A simple Pomodoro timer in Python.

![A screenshot](./screenshot.png)

# Usage

The output of `$ python pymodoro --help` is:

```
usage: pymodoro.py [-h] focus break

positional arguments:
  focus       the number of minutes to spend focused
  break       the number of minutes to spend resting

optional arguments:
  -h, --help  show this help message and exit
```

For example,
```
$ python pymodoro.py 25 5
```

# Setup

There is one dependency, [rich](https://pypi.org/project/rich/). To install use

```
pip install -r ./requirements.txt
```
