def precourse_work(cabbage):
    cabbages = ["Green Cabbage", "Red Cabbage", "Purple Cabbage", "Savoy Cabbage", "Napa Cabbage"]
    for val in cabbages:
        if val == cabbage:
            cab = "Thats a cabbage!!"
        else:
            cab = "Not so sure about that one"
    return cab

    
            

test = precourse_work("Napa Cabbage")


print(test)