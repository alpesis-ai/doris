from os import system

def parse_file(filepath):
    contents = []

    with open(filepath, "r") as f:
        for line in f.readlines():
            this_line = line.strip().replace("\n", "")
            if len(this_line) != 0:
                contents.append(this_line)
    f.close()

    return contents


def main():
    book = raw_input("Which book would you pick?\nBook: ")
    contents = parse_file(book)
    
    for content in contents:
        system('say %s' % content)


if __name__ == "__main__":

    main()
