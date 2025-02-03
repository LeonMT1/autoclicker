# Autoclicker
A simple autoclicker made in python using the pyautogui library. See requirements.txt for all dependencies.

## Features
- Adjustable click speed
- Hotkey to stop clicking
- Multiple click positions
- Fast and easy to use
- Lightweight

## Planned Features
- Makro support
- Customizable hotkeys
- Save and load settings
- Better Performance

## Comparison
In this Comparison, I will compare this Autoclicker with the "OP Auto Clicker" by https://www.opautoclicker.com/.

|                  | CPS (100cps was desired) | Ram at Idle | CPU at usage | Storage |
|------------------|--------------------------|-------------|--------------|---------|
| OP Auto Clicker  | 48.6 CPS                 | 12.2mb      | 0-5%         | 0.9mb   |
| This Autoclicker | 93.4 CPS                 | 22.9mb      | 0-1%         | 13.7mb  |

## How to Compile the Source Code
1. Run `git clone https://github.com/LeonMT1/autoclicker.git` in your terminal
2. Run `cd autoclicker` in your terminal
3. Run `pip install -r requirements.txt` in your terminal
4. Run `python -m PyInstaller --onefile --name "Autoclicker by LeonMT1" --icon=icon.ico main.py` in your terminal
5. The compiled file is located in the `dist` folder

Or simply download the compiled file from the [releases](https://github.com/LeonMT1/autoclicker/releases)