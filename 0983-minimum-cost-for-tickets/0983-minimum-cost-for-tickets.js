/**
 * @param {number[]} days
 * @param {number[]} costs
 * @return {number}
 */
var mincostTickets = function(days, costs) {
    let last_day = days[days.length -1];
    let days_set = new Set(days);
    
    let dp = new Array(last_day + 1).fill(0);
    
    for( let i = 1 ; i <= last_day ; ++i){
        if (days_set.has(i) == false)
            dp[i] = dp[i-1];
        else{
            const cost_day = costs[0] + dp[i-1];
            const cost_week = costs[1] + dp[Math.max(i-7 , 0)];
            const cost_month = costs[2] + dp[Math.max(i-30 , 0)];
            
            dp[i] = Math.min(cost_day , cost_week , cost_month);
        }
    }
    return dp[last_day];
};