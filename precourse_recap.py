def is_cabbage(cabbage):
    testlist = ["green cabbage", "red cabbage", "purple cabbage", "savoy cabbage", "napa cabbage"]
    for val in testlist:
        if val == cabbage.lower() or val == "cabbage": 

            cab = "Thats a cabbage!!!!"
            break
        else:
            cab = "I don't think thats a cabbage..."
    return cab

    
            

test = is_cabbage("sAvoY cAbbage")


print(test)