# Write your solution here
def longest_series_of_neighbours(nums:list)->int:
    series=1
    longest=1
    for i in range(0,len(nums)-1):
        if abs((nums[i]-nums[i+1]))==1:
            series+=1
        else:
            series=1
        longest=max(longest,series)
    return longest


if __name__=="__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))