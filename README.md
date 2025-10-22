# SystemSonifier

**Hear your computer think.**

SystemSonifier is a Python tool that converts CPU, RAM, and disk usage into audible tones. The higher the usage, the higher the pitch, creating a real-time “machine orchestra” of your system’s activity.

---

## Features

* Converts **CPU, RAM, and Disk usage** into distinct sounds.
* Real-time monitoring with pitch reflecting system load.
* Lightweight and simple to run.
* Great for learning system monitoring and Python sound programming.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/surendrasonusep26/SystemSonifier
cd SystemSonifier
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the main script:

```bash
python src/main.py
```

* Open apps, stress CPU, or copy large files to hear the pitch change.
* CPU, RAM, and Disk usage will generate sequential beeps.

---

## Future Improvements

* Play CPU, RAM, and Disk sounds **simultaneously** for a richer experience.
* Add **volume or waveform variation**.
* Optional **GUI** to visualize system usage alongside sounds.
* Log usage data and save as audio file for analysis.

---

## Requirements

* Python 3.x
* [psutil](https://pypi.org/project/psutil/)

---

## License

MIT License
