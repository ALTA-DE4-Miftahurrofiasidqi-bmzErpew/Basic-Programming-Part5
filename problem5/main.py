def pair_sum(arr, target):
    lookup = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]

        lookup[num] = i


if __name__ == "__main__":
    print(pair_sum([1, 2, 3, 4, 6], 6))  # [1, 3]
    print(pair_sum([2, 5, 9, 11], 11))  # [0, 2]
    print(pair_sum([1, 3, 5, 7], 12))  # [2, 3]
    print(pair_sum([1, 4, 6, 8], 10))  # [1, 2]
    print(pair_sum([1, 5, 6, 7], 6))  # [0, 1]
