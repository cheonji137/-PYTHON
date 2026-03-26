score = int(input("Enter a score: "))

match score//10:
    case 10:
        print("A")
    case 9:
        print("B")
    case 8:
        print("C")
    case 7:
        print("D")
    case _:
        print("F")