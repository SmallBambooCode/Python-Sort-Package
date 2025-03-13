def shell_sort(nums: list[int]):
    # 指定增量序列（希尔排序的核心思想）
    # 这里使用的是一个固定的增量序列 [5, 2, 1]（即逐步缩小间隔）
    gaps = [5, 2, 1]

    # 遍历每一个增量（gap）
    for gap in gaps:
        # 从 gap 位置开始，对每个元素进行插入排序
        for i in range(gap, len(nums)):
            temp = nums[i]  # 当前待插入的元素
            j = i  # 记录当前位置

            # 进行“间隔为 gap”的插入排序
            while j >= gap and nums[j - gap] > temp:
                nums[j] = nums[j - gap]  # 向右移动较大的元素
                j -= gap  # 向前寻找合适的插入位置

            # 找到合适的位置后插入当前元素
            nums[j] = temp

# 测试代码
if __name__ == '__main__':
    arr = [10, 3, 7, 15, 2, 9, 1, 6, 14, 8]  # 定义待排序数组
    shell_sort(arr)  # 调用希尔排序算法
    print(arr)  # 输出排序结果
