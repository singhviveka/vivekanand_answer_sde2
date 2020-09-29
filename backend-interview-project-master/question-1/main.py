import typing


def main(numbers: typing.List[int], target_sum: int):
    numbers.sort()
    arr_size = len(numbers)

    for i in range(0, arr_size - 2):
        l = i + 1
        r = arr_size - 1
        while l < r:
            if numbers[i] + numbers[l] + numbers[r] == target_sum:
                return True
            elif numbers[i] + numbers[l] + numbers[r] < target_sum:
                l += 1
            else:
                r -= 1

    return False


if __name__ == "__main__":
    assert (main([5, 4, 10, 7, 1, 9], 13) is True), "Triplet exists"
    assert (main([4, 2, 5, 9, 11, 23], 9) is False), "Triple does not exist"
