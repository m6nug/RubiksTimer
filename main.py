from pynput import keyboard
import time
import sys
import os
import random

recording = False
solveTime = 0

currentScramble = ""

times = []

moves = ['f', "f'", 'b', "b'", 'r', "r'", 'l', "l'", 'd', "d'", 'u', "u'", 'f2', 'b2', 'r2', 'l2', 'd2', 'u2']

def scramble():
    scramble = ""
    move = ""
    prevMove = ""

    for i in range(10):
        move = random.choice(moves) + ' '

        while move[0] == prevMove:
            move = random.choice(moves) + ' '

        prevMove = move[0]
        scramble += move
    
    return scramble

currentScramble = scramble()
print("Scramble: " + currentScramble)

def on_press(key):
    pass

def on_release(key):
    global recording
    global solveTime
    global currentScramble

    if key == keyboard.Key.space:
        recording = not recording

        if not recording:
            os.system('cls')
            print(f"Solved in {solveTime} seconds")
            f = open("scrambles.txt", 'a')
            f.write(f"\nScamble: {currentScramble} Time: {solveTime}")
            f.close()
            currentScramble = scramble()
            print("New Scramble: " + currentScramble)
            times.append(solveTime)
            average = sum(times) / len(times)

            print("Times: ")

            for i in times: 
                print("  " + str(i))

            print("Average: " + str(average))
            solveTime = 0

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release
)

listener.start()

while True:
    if recording:
        solveTime += 1
        sys.stdout.write("\rTime: " + str(solveTime))
        sys.stdout.flush()
        time.sleep(1)