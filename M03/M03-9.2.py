def get_odds():
    #gets a rangfe in a for loop
    for num in range(10):
        if num % 2 != 0:
            #yeild to return number
            yield num



count = 0
for num in get_odds():
    if count == 2:
        print (num)
        break
    count +=1