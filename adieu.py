def main():

    names = []              # initializes empty list of names

    while True:
        try:
            names.append(input("Name: "))                                       # takes user input of names and adds them to our list, names
        except EOFError:                                                        # exits when user presses ctrl-d
            list(names)

            if len(names) == 1:                                                 # special format if user inputs only one name
                print(f"Adieu, adieu, to " +  names[0])
                break

            if len(names) == 2:                                                 # special format if user inputs only two names
                print(f"Adieu, adieu, to " +  names[0] + " and " + names[1])
                break

            if len(names) > 2:                                                  # very difficult to read, but if user enters 3 or more names
                print("Adieu, adieu, to ", end="")                              # prints, e.g., "Adieu, adieu, to Doug, Erin, and Finn"
                i = 0                                                           # prints blank line and breaks when done
                for name in names[0:-1]:
                    print(names[i] + ", ", end ="")
                    i += 1
                print("and " + names[-1])
                print("")
                break

main()
