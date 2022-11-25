/**
 * @param {number[]} arr
 * @return {number}
 */
var sumSubarrayMin = function(arr) {
    // Bruteforce
    const n = arr.length;
    let s = 0;
    
    for (let i =0 ; i < n ; i++){
        let m = arr[i]; 
        for (let j = i ; j < n ; j++ ){
            m = Math.min(arr[j] , m)
            s += m;  
        }
    }
    return s;
}; // will give TLE



var sumSubarrayMins = function(arr){
    const n = arr.length;    
    
    let left = new Array(n).fill(-1);
    let right  = new Array(n).fill(n);
    
    function leftSmaller(){
        stack = [];
        for (let i = 0 ; i < n ; i++){
            while(stack.length > 0 && arr[stack[stack.length -1]] >= arr[i] )
                stack.pop();
            
            if (stack.length > 0 )
                left[i] = stack[stack.length -1];
            
            stack.push(i);
        }
    }

    function rightSmaller(){
        let stack = [];
        for(let i = n - 1 ; i >= 0 ; i--){
            while(stack.length > 0 &&  arr[stack[stack.length -1]] > arr[i])
                stack.pop();
            
            if (stack.length > 0)
                right[i] = stack[stack.length -1];
            
            stack.push(i);
        }
    }
    
    leftSmaller();
    rightSmaller();
    
    let sum  = 0 ;
    let MOD = Math.pow(10, 9) + 7;        
        
    for (i = 0 ; i < n ; i++)
        sum = (sum + (i - left[i]) * (right[i] - i) * arr[i] ) % MOD;
    
    return sum;
};
