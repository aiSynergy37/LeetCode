"""
1710. Maximum Units on a Truck

"""

def maximumUnits(boxTypes, truckSize):
    boxTypes.sort(key = lambda x : x[1])
    boxTypes = boxTypes[::-1]
    n = len(boxTypes)
    t_c = 0
    wt = 0
    arr = []

    for j in boxTypes:
        arr.append(j[0])

    for i in range(n):
        t_c += boxTypes[i][0]
        if t_c > truckSize:
            diff = truckSize -  sum([x for x in arr[:i]])
            wt += boxTypes[i][1] * diff
            break
        wt += boxTypes[i][0] * boxTypes[i][1]
    print(wt)
    return wt


def main():
    boxTypes = [[5,10],[2,5],[4,7],[3,9]]
    truckSize = 10
    #res = 
    print(maximumUnits(boxTypes, truckSize))
    #print(res)
    return res



if __name__ == "main":
    main()
