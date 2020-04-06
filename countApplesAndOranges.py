def countApplesAndOranges(s, t, a, b, apples, oranges):

    apple_locations = [a + i for i in apples]
    orange_locations = [b + i for i in oranges]
    num_apples = 0
    num_oranges = 0

    for fruit in apple_locations:
        if fruit >= s:
            num_apples +=1
    for fruit in orange_locations:
        if fruit <= t:
            num_oranges +=1
    print(num_apples)
    print(num_oranges)


def breakingRecords(scores):
    recordbig = 0
    recordmin = 0
    current_max = scores[0]
    current_min = scores[0]

    for game in range(len(scores)-1):
        if scores[game+1] > current_max:
            recordbig += 1
            current_max = scores[game+1]

        elif scores[game+1] < current_min:
            recordmin += 1
            current_min = scores[game+1]

    print(current_max)


breakingRecords([1,2,3,1,2,5])