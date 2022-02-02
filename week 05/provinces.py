def main():

    read_text("provinces.txt")


def read_text(filename):
    text_list = []

    with open(filename, "rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)
    
    print(text_list)

    text_list.remove("Alberta")
    text_list.pop()

    for x, province in enumerate(text_list):
        if province == "AB":
            text_list[x] = "Alberta"

    count = text_list.count("Alberta")
    print("")
    print(f"Alberta occurs {count} times in the modified list.")

if __name__ == "__main__":
    main()