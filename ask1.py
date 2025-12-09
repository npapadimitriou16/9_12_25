class UpperString:
    def get_String():
        x = input()
        word = x.upper()
        return word

    def print_String(upper):
        print(upper)

print("give me something :")
UpperString.print_String(UpperString.get_String())