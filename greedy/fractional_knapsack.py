# Uses python3
import sys
import random

def second_get_optimal_value(capacity, weights, values):
        density = compute_density(values, weights)
        indexes = density_index(density)
        value = 0.
        capacity_max = capacity

        for i in range(len(density)):
                if(capacity_max <= 0):
                        break

                if(weights[indexes[i]] > capacity_max):
                        weight = (capacity_max - capacity) + capacity
                        value = value + (density[indexes[i]] * capacity)
                else:
                        weight = weights[indexes[i]]
                        value = value + values[indexes[i]]

                capacity_max = capacity_max - weight

        return value

def density_index(density):
        a = []
        indexes = []

        for i in range(len(density)):
                a.append(i)

        indexes = [x for (y,x) in sorted(zip(density, a), reverse=True)]

        return indexes

def compute_density(values, weights):
        density = []

        for i in range(len(values)):
                density.append(values[i] / weights[i])

        return density

def get_optimal_value(capacity, weights, values):
    value = 0.

    valuePerWeight = valuePerWeight = sorted([[v / w, w] for v,w in zip(values,weights)], reverse=True)
    while capacity > 0 and valuePerWeight:
        maxi = 0
        idx = None
        for i,item in enumerate(valuePerWeight):
            if item [1] > 0 and maxi < item [0]:
                maxi = item [0]
                idx = i

        if idx is None:
            return 0.

        v = valuePerWeight[idx][0]
        w = valuePerWeight[idx][1]

        if w <= capacity:
            value += v*w
            capacity -= w
        else:
            if w > 0:
                value += capacity * v
                return value
        valuePerWeight.pop(idx)

    return value

def test_cases():
        while True:
                length = random.randint(1, 1000)
                capacity = random.randint(1, 2000000)
                values = []
                weights = []

                for i in range(length):
                        values.append(random.randint(1, 2000000))
                        weights.append(random.randint(1, 2000000))
                
                if (second_option(capacity, weights, values) == get_optimal_value(capacity, weights, values)):
                        print("OK")
                else:
                        print(get_optimal_value(capacity, weights, values), "<<<<< mine output")
                        print(get_optimal_value(capacity, weights, values), "<<<<< their output")        

#test_cases()

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
