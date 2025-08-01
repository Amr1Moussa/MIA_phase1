import time
import os

# utility1: console cleaner 
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# user inputs gear number + input validation
def input_gear():
    while True:
        try:
            gear_number = int(input("Enter Gear (0-8): "))
            if 0 <= gear_number <= 8:
                return gear_number
            else:
                print("Invalid gear number. Please enter a number between 0 and 8.")   # handles invalid range 
        except ValueError:
            print("Invalid input. Please enter an integer between 0 and 8.")    # handles invalid data types, error while casting the input


def display_gear(gear_number):

    #initialize empty grid 
    grid = [[' ',' ',' ',' '],
            [' ',' ',' ',' '],
            [' ',' ',' ',' '],
            [' ',' ',' ',' '],
            [' ',' ',' ',' '],
            ]
    
    # each segment defination
    segments = {
        'a': [(0, 0), (0, 1), (0, 2), (0, 3)],
        'b': [(1, 3), (2, 3)],
        'c': [(3, 3), (4, 3)],
        'd': [(4, 0), (4, 1), (4, 2), (4, 3)],
        'e': [(3, 0), (4, 0)],
        'f': [(1, 0), (2, 0)],
        'g': [(2, 0), (2, 1), (2, 2), (2, 3)]
    }

    # 7-segment encoding for digits 0–8 (each value is a list of active segments)
    digits = {
        0: ['a', 'b', 'c', 'd', 'e', 'f'],
        1: ['b', 'c'],
        2: ['a', 'b', 'g', 'e', 'd'],
        3: ['a', 'b', 'g', 'c', 'd'],
        4: ['f', 'g', 'b', 'c'],
        5: ['a', 'f', 'g', 'c', 'd'],
        6: ['a', 'f', 'g', 'e', 'c', 'd'],
        7: ['a', 'b', 'c'],
        8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    }

    # filling corresponding segments with #
    for segment in digits[gear_number]: 
        for (x, y) in segments[segment]:
            grid[x][y] = '#'

    for row in grid:
        print(*row, sep='')    # unpack each 1D array 


def animate_shift(from_gear, to_gear):
    # Show from_gear for 10 seconds
    clear_console()
    print(f"Gear: {from_gear}")
    display_gear(from_gear)
    time.sleep(10)

    # Blank screen for 1 seconds
    clear_console()
    time.sleep(1)

    # Show to_gear
    print(f"Gear: {to_gear}")
    display_gear(to_gear)


def main():
    gear_number = input_gear()
    display_gear(gear_number)

    print("---"*30)
    print("Gear shifting(enter 2 gears)")
    from_gear = input_gear()
    to_gear = input_gear()
    animate_shift(from_gear, to_gear)


if __name__ == '__main__':
    main()

