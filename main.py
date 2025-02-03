import pyautogui
from pynput import mouse
import os
import time
import keyboard

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def display_menu():
    clear_console()
    print("\n" * 2)
    print("          █████╗ ██╗   ██╗████████╗ ██████╗  ██████╗██╗     ██╗ ██████╗██╗  ██╗███████╗██████╗ ")
    print("         ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗██╔════╝██║     ██║██╔════╝██║ ██╔╝██╔════╝██╔══██╗")
    print("         ███████║██║   ██║   ██║   ██║   ██║██║     ██║     ██║██║     █████╔╝ █████╗  ██████╔╝")
    print("         ██╔══██║██║   ██║   ██║   ██║   ██║██║     ██║     ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗")
    print("         ██║  ██║╚██████╔╝   ██║   ╚██████╔╝╚██████╗███████╗██║╚██████╗██║  ██╗███████╗██║  ██║")
    print("         ╚═╝  ╚═════╝    ╚═╝    ╚═════╝  ╚═════╝╚══════╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝")
    print("\n\n╔═[1] Autoclicker\n║\n╠══[2] Click a specific location\n║\n╠═══[3] Click on multiple locations\n║\n╚═╦══[4] Exit\n  ║")
    return int(input("  ╚═════> "))

def auto_clicker():
    cps = int(input("Enter the desired CPS: "))
    print("Press 'Ctrl + 1' to stop the Auto Clicker.")
    on = True

    while on:
        pyautogui.click()
        time.sleep(1 / cps)
        if keyboard.is_pressed('ctrl+1'):
            on = False
            print("Auto Clicker stopped.")

def click_specific_location():
    print("Click on the desired location...")
    position = get_mouse_click_position()
    if position:
        clicks = int(input("Enter the desired CPS: "))
        print("Press 'Ctrl + 1' to stop clicking.")
        auto_click_position([position], clicks)

def click_multiple_locations():
    amount = int(input("How many locations do you want to click? "))
    positions = []

    for i in range(amount):
        print(f"Click on the {i + 1} location...")
        positions.append(get_mouse_click_position())

    if positions:
        clicks = int(input("Enter the desired CPS: "))
        print("Press 'Ctrl + 1' to stop clicking.")
        auto_click_position(positions, clicks)

def get_mouse_click_position():
    position = None

    def on_click(x, y, button, pressed):
        nonlocal position
        if pressed:
            position = (x, y)
            print(f"The location is: {position}")
            listener.stop()

    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
    return position

def auto_click_position(positions, cps):
    on = True

    while on:
        for position in positions:
            pyautogui.click(position)
            time.sleep(1 / cps)
        if keyboard.is_pressed('ctrl+1'):
            on = False
            print("Clicking stopped.")

def main():
    while True:
        choice = display_menu()
        if choice == 1:
            auto_clicker()
        elif choice == 2:
            click_specific_location()
        elif choice == 3:
            click_multiple_locations()
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
