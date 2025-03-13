import sort_package as sp

nums = [4, 1, 3, 1, 5, 2]
sp.bubble_sort(nums)
print("冒泡排序完成后 nums =", nums)
nums = [4, 1, 3, 1, 5, 2]
sp.selection_sort(nums)
print("选择排序完成后 nums =", nums)
nums = [4, 1, 3, 1, 5, 2]
sp.insertion_sort(nums)
print("插入排序完成后 nums =", nums)
nums = [4, 1, 3, 1, 5, 2]
sp.shell_sort(nums)
print("希尔排序完成后 nums =", nums)
nums = [4, 1, 3, 1, 5, 2]
sp.merge_sort(nums, 0, len(nums) - 1)
print("归并排序完成后 nums =", nums)
nums = [4, 1, 3, 1, 5, 2]
sp.quick_sort(nums, 0, len(nums) - 1)
print("快速排序完成后 nums =", nums)
nums = [4, 1, 3, 1, 5, 2]
sp.heap_sort(nums)
print("堆排序完成后 nums =", nums)
nums = [4, 1, 3, 1, 5, 2]
sp.counting_sort(nums)
print("计数排序完成后 nums =", nums)
nums = [0.49, 0.96, 0.82, 0.09, 0.57, 0.43, 0.91, 0.75, 0.15, 0.37]
sp.bucket_sort(nums)
print("桶排序完成后 nums =", nums)
nums = [10546151,35663510,42865989,34862445,81883077,88906420,72429244,30524779,82060337,63832996]
sp.radix_sort(nums)
print("基数排序完成后 nums =", nums)