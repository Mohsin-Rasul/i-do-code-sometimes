def findMinX(nums, rems):
    x = 1
    while True:
        for j in range(len(nums)):
            if x % nums[j] != rems[j]:
                break
        else:
            return x
        x += 1

ns = [3, 4, 5]
rs = [2, 3, 1]

res = findMinX(ns, rs)
print(f"The minimum x is: {res}")