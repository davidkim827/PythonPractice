#!/usr/bin/env python3

def bSearchGuess(listInput):
    
    l = 0
    h = len(listInput)
    
    mid = (l + h) // 2
    print(f"Is it {mid}, y or n?")
    userBool = input()
    if userBool == 'y':
        return
    else:
        while userBool != 'r':
            print(f"Is it higher (h) or lower (l) or am I right (r)?")
            userBool = input()
            if userBool == "l":
                h = mid - 1
            elif userBool == "h":
                l = mid + 1
            elif userBool == "r":
                return
            else:
                print(f"That's not a valid response")
                print(f"Is it higher (h) or lower (l) or am I right (r)?")
                userBool = input()

            mid = (l + h) // 2
            print(f"{mid}")

    return False


numList = [i for i in range(0,101)]     #creates a list of numbers 0 to 100
print("Please think of a number that the computer will have to guess between 0 and 100")
print("\nIt\'s time to guess your number! Please follow the prompts") 

bSearchGuess(numList)

print("I guessed the right answer! Game is now over.")


