def cabbage_check(cabbage):
    cabbage_list = ["green cabbage", "red cabbage", "purple cabbage", "savoy cabbage", "napa cabbage", "cabbage"]
    for val in cabbage_list:
        if val == cabbage.lower():
            cab = f"{cabbage} is a cabbage!!!!"
            return cab
    return f"I don't think that {cabbage} is a cabbage..."

test = cabbage_check("Ed")

test2 = cabbage_check("Red Cabbage")

print(test)
print(test2)

