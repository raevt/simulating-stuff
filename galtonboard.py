"""
    Simulate a Galton board!
"""
import random

# Settings
num_rows = 12 # Set the number of rows on either side of the starting peg
num_balls = 200 # Set the number of balls on the board

def simulate():
    # Create list
    positions = []
    for n in range(num_balls):
        positions.append(0)
    # For num rows, run simulations
    for i in range(num_rows):
        for n in range(num_balls):
            positions[n] += random.choice([-1,1])
    return positions

def output(positions):
    freqs = {}
    for n in range(-1*num_rows,num_rows+1):
        freqs[n] = 0
    for n in positions:
        freqs[n] += 1
    print("Frequencies")
    for i in range(-1*num_rows,num_rows+1):
        print(f"{i}:",end="")
        for n in range(freqs[i]):
            print("*",end="")
        print()

def main():
    output(simulate())

if __name__ == "__main__":
    main()
