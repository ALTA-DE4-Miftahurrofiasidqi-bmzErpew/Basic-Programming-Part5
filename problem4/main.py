def muncul_sekali(angka):
    freq = {}
    for i in angka:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    result = []
    for i in freq:
        if freq[i] == 1:
            result.append(int(i))

    return result


if __name__ == "__main__":
    print(muncul_sekali("1234123"))  # [4]
    print(muncul_sekali("76523752"))  # [6, 3]
    print(muncul_sekali("12345"))  # [1, 2, 3, 4, 5]
    print(muncul_sekali("1122334455"))  # []
    print(muncul_sekali("0872504"))  # [8, 7, 2, 5, 4]
