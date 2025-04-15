def compare(x, y):
    if x > y:
        print(f"{x} is greater")
    elif x == y:
        print(f"both equal")
    else:
        print(f"{y} is greater")


if __name__ == '__main__':
    def sh():
        print("ok")

# python has a special built in variable => __name__
# when executing the script it value is => "__main__"
# but when you import a script as a module then for 
# that module the __name__ becomes the name of the module

# so we are just adding a if statement to check the value
# value of the __name__

print(__name__)