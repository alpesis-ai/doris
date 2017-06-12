from os import system



if __name__ == "__main__":

    contents = []

    with open("joan_baez_diamonds_and_rust.txt", "r") as f:
        for line in f.readlines():
            this_line = line.strip().replace("\n", "")
            if len(this_line) != 0: 
                contents.append(this_line)
    f.close()   

    for content in contents:
        print content
        system('say %s' % content)

