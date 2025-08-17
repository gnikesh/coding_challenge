# There are N gas stations along a circular route, where the amount of gas at station i is gas[i]. You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations. Return the starting gas station's index if you can travel around the circuit once, otherwise return -1. Note: The solution is guaranteed to be unique.


def canCompleteCircuit(gas, cost):
    # Time complexity: O(N), where N is the number of gas stations
    # Space complexity: O(1), as we are using a constant amount of space
    total_gas = 0
    total_cost = 0
    tank = 0
    start = 0

    for i in range(len(gas)):
        total_gas += gas[i]
        total_cost += cost[i]
        tank += gas[i] - cost[i]

        if tank < 0:
            start = i + 1
            tank = 0

    if total_gas < total_cost:
        return -1
    else:
        return start

def main():
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    print(canCompleteCircuit(gas, cost))

if __name__ == "__main__":
    main()
