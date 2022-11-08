# Import serialPy library and pynput keyboard library
import serial
from pynput.keyboard import Key, Controller

# Establish Serial Port, Baud Rate, and # data bits, and initialize keyboard 
ser = serial.Serial('COM5', 1200, 7)
keyboard = Controller()

# Kaypro 2000 Keyboard has an ID for each key, 
# this dictionary tells us what letter or function
# is on that key and whether it is being pressed.
keyTranslation = {
    # Function Row
    '59': [Key.f1, False], '60': [Key.f2, False], '61': [Key.f3, False], '62': [Key.f4, False], '63': [Key.f5, False], '64': [Key.f6, False],
    '65': [Key.f7, False], '66': [Key.f8, False], '67': [Key.f9, False], '68': [Key.f10, False], '69': [Key.num_lock, False], '70': [Key.scroll_lock, False],
    # First Row
    '1': [Key.esc, False], '2': ['1', False], '3': ['2', False], '4': ['3', False], '5': ['4', False],
    '6': ['5', False], '7': ['6', False], '8': ['7', False], '9': ['8', False], '10': ['9', False], '11': ['0', False], 
    '12': ['-', False], '13': ['=', False], '41': ['`', False], '14': [Key.backspace, False], 
    # Second Row
    '15': [Key.tab, False], '16': ['q', False], '17': ['w', False], '18': ['e', False], '19': ['r', False], '20': ['t', False],
    '21': ['y', False], '22': ['u', False], '23': ['i', False], '24': ['o', False], '25': ['p', False], '26': ['[', False],
    '27': [']', False], '28': [Key.enter, False], '71': [Key.insert, False],
    # Third Row
    '29': [Key.ctrl_l, False], '30': ['a', False], '31': ['s', False], '32': ['d', False], '33': ['f', False], '34': ['g', False],
    '35': ['h', False], '36': ['j', False], '37': ['k', False], '38': ['l', False], '39': [';', False], '40': ["'", False], '72': [Key.delete, False],
    # Fourth Row
    '42': [Key.shift_l, False], '44': ['z', False], '45': ['x', False], '46': ['c', False], '47': ['v', False], '48': ['b', False],
    '49': ['n', False], '50': ['m', False], '51': [',', False], '52': ['.', False], '53': ['/', False], '54': [Key.shift_r, False], 
    '73': [Key.up, False], '55': [Key.print_screen, False],
    # Fifth Row
    '56': [Key.alt, False], '58': [Key.caps_lock, False], '43': ['\\', False], '57': [Key.space, False], '77': [Key.cmd, False],
    '74': [Key.left, False], '75': [Key.down, False], '76': [Key.right, False],
    # specially reassigned keys, comment out for normal behavior. These override earlier definitions.
    
    }

while True:
    # looks at the first byte in the serial buffer
    key = ord(ser.read())

    # this if/else conditional updates whether the button is currently pressed 
    # and presses or releases that key accordingly.
    if not keyTranslation[f'{key}'][1]:
        keyTranslation[f'{key}'][1] = True
        keyboard.press(keyTranslation[f'{key}'][0])
    else:
        keyTranslation[f'{key}'][1] = False
        keyboard.release(keyTranslation[f'{key}'][0])
    print(keyTranslation[f'{key}'])
    

