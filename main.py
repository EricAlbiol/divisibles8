# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main():
    divisibles = list()
    for x in range (0,1001):
        if x % 8 == 0:
            divisibles.append(x)
    print(divisibles)
if __name__ == '__main__':
    main()
