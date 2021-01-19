def display_names(first, second, third):
    # print(kwargs)
    print(f"{first} says hello to {second}")

names = {"first": "Colt", "second": "Rusty", "third": "Mitch"}

# display_names(names) # nope..
display_names(**names)  # yup!

def add_and_multiply_numbers(a,b,c,**kwargs):
    print(a + b * c)
    print("OTHER STUFF....")
    print(kwargs)

data = dict(a=1,b=2,c=3,d=55,name="Tony")

add_and_multiply_numbers(**data) # 7
