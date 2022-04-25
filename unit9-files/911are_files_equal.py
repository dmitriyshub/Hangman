def are_files_equal(file1, file2):
    '''
    This fucntion compare 2 files and return True if they are equal otherwise return False
    :param file1: file
    :param file2: file
    :return: True or False
    '''
    file1_open = open(file1, "r")
    file2_open = open(file2, "r")


    for line1 in file1_open:
        for line2 in file2_open:
            if line1 == line2:
                continue
            elif line1 != line2:
                file1_open.close()
                file2_open.close()
                return False
    file1_open.close()
    file2_open.close()
    return True


def main():
    print(are_files_equal("d:\\file1.txt", "d:\\file2.txt"))

if __name__ == "__main__":
    main()

