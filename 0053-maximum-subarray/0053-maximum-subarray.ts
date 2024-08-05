function maxSubArray(nums: number[]): number {
    let current_sum = 0
    let max_sum = nums[0] 

    for (let num of nums){
        current_sum += num;
        max_sum = Math.max(max_sum , current_sum);
        if (current_sum < 0){
            current_sum = 0;
        } 
        
    }
    return max_sum;
};