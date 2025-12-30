class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(arr,low,mid,high):
            left = low
            right = mid+1
            temp = []

            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    right += 1
            while left <= mid:
                temp.append(arr[left])
                left += 1
            while right <= high:
                temp.append(arr[right])
                right += 1

            for i in range(len(temp)):
                arr[i+low] = temp[i]


        def countpairs(arr,low,mid,high):
            right = mid +1
            cnt = 0

            #the left side array...
            for i in range(low,mid+1):
                # comparing with right side
                while right <= high and arr[i] > 2*arr[right]:
                    right +=1
                    #gives the number of elemtns present in 
                    # the right side of the arr
                cnt += (right - (mid+1)) 
            return cnt


        def mergesort(arr,low,high):
            cnt = 0
            if low >= high:
                return cnt 
            mid = (low + high) // 2
            cnt += mergesort(arr,low,mid)
            cnt += mergesort(arr,mid+1,high)
            cnt += countpairs(arr,low,mid,high)
            merge(arr,low,mid,high)
            return cnt

        n = len(nums)
        return mergesort(nums,0,n-1)                    