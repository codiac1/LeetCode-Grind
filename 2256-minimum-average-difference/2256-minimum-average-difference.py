class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        
        pre = [0]*n
        post = [0]*n
        
        pre[0] = nums[0]
        post[n-1] = nums[n-1]
        
        for i in range(1,n):
            pre[i] = pre[i-1] + nums[i]
            post[n-i-1] = post[n-i] + nums[n-i-1]
        
        ans = 0
        mn = math.inf
        
        for i in range(n):
            x = pre[i]//(i+1) 
            
            if i == n-1:
                y = 0
            else:
                y = post[i+1]//(n-i-1)
                
            avg = abs( x - y )
            #print(avg)
            if avg < mn :
                mn = avg
                ans = i 
                
        return ans 
        