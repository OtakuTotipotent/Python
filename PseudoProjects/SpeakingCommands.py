import os

if __name__ == "__main__":
    while True:
        message = input("Hi, Enter something to speak : ")
        if message == "Q":
            os.system('say "Goodbye"')
            break
        command = f"say {message}"
        os.system(command)
