for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')

result = [x*y for x in range(2, 10) for y in range(1, 10)]
print(result)

a = "Life is too short, you need python"

if "wife" in a:
    print("wife")
elif "python" in a and "you" not in a:
    print("python")
elif "shirt" not in a:
    print("shirt")
elif "need" in a:
    print("need")
else:
    print("none")
