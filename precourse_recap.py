def is_cabbage(cabbage):
    cabbages = ["Green Cabbage", "Red Cabbage", "Purple Cabbage", "Savoy Cabbage", "Napa Cabbage"]
    for val in cabbages:
        if val == cabbage or val == "Cabbage" or val == "cabbage": 
            cab = "Thats a cabbage!!!!"
        else:
            cab = "I don't think thats a cabbage..."
    return cab

    
            

test = is_cabbage("Rory")


print(test)