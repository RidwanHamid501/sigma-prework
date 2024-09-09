def maxmin(arr):
    arr.sort()
    return [arr[0], arr[-1]]


def main():
    arr = input("Enter an array (numbers separated by comma): ")
    result = maxmin(list(map(int, arr.split(","))))

    print(f"The minimum and maximum are: {result}")


if __name__ == "__main__":
    main()
