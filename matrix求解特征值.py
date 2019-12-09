# import numpy as np
#
# A = np.mat("5 4 2; 4 10 1; 2 1 2")
#
# print("A\n", A)
#
# inverse = np.linalg.inv(A)
# print("inverse\n", inverse)
#
#
#
# eigenvalues = np.linalg.eigvals(A) #单纯的求解矩阵的特征值
# eigenvalues, eigenvectors = np.linalg.eig(A)
# print("eigenvalues: ", eigenvalues)   #特征值
# print("eigenvectors: ", eigenvectors) #特征向量

def sortColors(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # 最优的三个指针解法
    red, white, blue = 0, 0, len(nums) - 1

    while white <= blue:

        if nums[white] == 0:
            nums[red], nums[white] = nums[white], nums[red]
            red += 1
            white += 1
        elif nums[white] == 1:
            white += 1
        else:
            nums[blue], nums[white] = nums[white], nums[blue]
            blue -= 1
    return nums

a = [2,0,2,1,1,0]
print(sortColors(a))
