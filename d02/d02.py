with open("d02/d02_data.txt") as f:
    data = f.readlines()
assert len(data) == 1000

data = [ [ int(x) for x in datum.split() ] for datum in data ] # for every report, split all the numbers and turn into ints


# Part 1
# First, throw out all reports not stricly ascending or descending
def ascending_check(report):
        valid = True 
        if report[0] < report[1]: # checks whether list is ascending or descending
            ascending = True
        else:
            ascending = False

        for x in range(len(report)): # for x, where x is number of items in list
            if x + 1 == len(report): # is it the last element, if so continue, this part is valid
                continue

            if (ascending and report[x] < report[x+1]) or (not ascending and report[x] > report[x+1]):
                continue
            else:
                valid = False
                break
        return valid



def change_check(report, upperLimit=3,lowerLimit=1):
    valid = True

    for x in range(len(report)):
        if x + 1 == len(report): # is it the last element, if so continue, this part is valid
            continue
          
        diff = abs(report[x] - report[x+1])
        if diff >= lowerLimit and diff <= upperLimit:
           continue
        else:
            valid = False
            break
    return valid


safe_reports = [report for report in data if ascending_check(report) and change_check(report)]

print("# Safe Reports:", len(safe_reports))

# Part 2

unsafe_reports = [report for report in data if not (ascending_check(report) and change_check(report)) ]
def check_with_damping(report):
    for x in range(len(report)):
        rep:list = report[:]

        rep.pop(x)

        if ascending_check(rep) and change_check(rep):
            return True
    return False

safe_with_damping = [report for report in unsafe_reports if check_with_damping(report)]

print("# Safe Damped Reports:", len(safe_with_damping))
print("Total Safe Reports: ", len(safe_reports) + len(safe_with_damping))