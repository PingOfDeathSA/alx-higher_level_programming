#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    newNames = dir(hidden_4)
    for newName in newNames:
        if newName[:2] != "__":
            print(newName)
