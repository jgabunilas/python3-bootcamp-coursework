colors = ["purple", "teal", "magenta", "crimson", "emerald green"]

index = 0

while index < len(colors):
    print(colors[index])
    # Remember to increment the index with each pass through the loop. Otherwise you'll just print the first element over and over again
    index += 1

# direct use of the index to print the color at a particular index

index = 0
while index < len(colors):
    print(f"{index}: {colors[index]}")
    index += 1

