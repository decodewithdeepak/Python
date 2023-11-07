for i in range(1, 15):
    print("5 x", i, "=", 5*i)
    if (i == 10):
        break

print("out of the loop")

for i in range(1, 15):
    if (i == 10):
        print("skip the iteration")
        continue

    print("5 x", i, "=", 5*i)

