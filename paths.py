from random import choice

max_range = 70

factors = [2, 5, 7, 10] # 9/8, 4/3, 3/2, 16/9

def find_path(factors):
    # copy to temp list
    temp_factors = factors[:]
    # starting pitch
    pitch = 0
    # initialize paths list with starting pitch
    pitches = [pitch]

    # loop until path is complete or until 'bad path' determination
    while True:
        # select random interval
        interval = choice(temp_factors)
        # check to see if interval has exceeded max_range
        if pitch + interval > max_range:
            # remove bad interval
            temp_factors.remove(interval)
            # if no more intervals to try, break
            if len(temp_factors) == 0:
                #print("bad path")
                break
            else:
                # try another interval
                continue
        # add interval and get new pitch
        pitch += interval
        # add pitch to path list
        pitches.append(pitch)
        # check for exit critirion
        if pitch == max_range:
            #print("path found")
            return pitches

total_tests = 100
testing = True
searching = True
while testing:
    paths = []
    
    while searching:
        path = find_path(factors)
        if path:
            # check for duplicates
            if path in paths:
                continue
            # append path
            paths.append(path)
        if len(paths) >= total_tests:
            searching = False

    print(len(paths))
    if len(paths) == 0:
        testing = False
    total_tests += 1


#for path in paths:
#    print(path)
