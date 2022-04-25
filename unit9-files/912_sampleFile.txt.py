
def file_prog():
    filePath = input("Enter file path: ")
    command = input("Enter command: ")
    with open(filePath, 'r') as inputFile:
        if (command == "sort"):
            l = list()
            for line in inputFile:
                line = line.split()
                for word in line:
                    if (word not in l):
                        l.append(word)
            l.sort()
            print(l)
        elif (command == "rev"):
            for line in inputFile:
                print(line[-2::-1])
        elif (command == "last"):
            fileData = inputFile.read()
            l = fileData.split('\n')
            num = int(input("Enter real number: "))
            for i in range(num):
                print(l[-num + i])
    return



def main():
    file_prog()

if __name__ == "__main__":
    main()



