def join_array_remove_duplicate(arrayA, arrayB):
    # your code here
    combine_array = arrayA + arrayB
    arrayAB = []

    for _, v in enumerate(combine_array):
        if v not in arrayAB:
            arrayAB.append(v)

    return arrayAB


if __name__ == "__main__":
    # Test cases
    print(join_array_remove_duplicate(["apel", "anggur"], ["lemon", "leci", "nanas"]))
    # ["apel", "anggur", "lemon", "leci", "nanas"]

    print(
        join_array_remove_duplicate(["samsung", "apple"], ["apple", "sony", "xiaomi"])
    )
    # ["samsung", "apple", "sony", "xiaomi"]

    print(
        join_array_remove_duplicate(
            ["football", "basketball"], ["basketball", "football"]
        )
    )
    # ["football", "basketball"]
