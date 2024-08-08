""" 
バイナリーサーチ
真ん中をまず見る。真ん中から大きい・小さいで区別してから見ていく
 """

from typing import List,NewType

IndexNum = NewType('IndexNum',int)

def liner_search(numbers:List[int],value:int) -> int:
  for i in range(0,len(numbers)):
    if numbers[i] == value:
      return i
  return -1


def binary_search(numbers:List[int],value:int) -> IndexNum:
  left,right = 0,len(numbers)-1
  while left <= right:
    # 真ん中を求める
    mid = (left + right) // 2
    if numbers[mid] == value:
      return mid
    elif numbers[mid] < value:
      left = mid + 1
    else:
      right = mid -1

  return -1


if __name__ == '__main__':
  nums = [0,1,5,7,8,11,15,20,24]
  print(binary_search(nums,20))
