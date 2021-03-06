def WriteToFile(text):
    with open("log.txt", "a") as logFile:
        logFile.write(text + "\n")