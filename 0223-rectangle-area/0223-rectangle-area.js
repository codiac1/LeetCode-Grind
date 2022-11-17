/**
 * @param {number} ax1
 * @param {number} ay1
 * @param {number} ax2
 * @param {number} ay2
 * @param {number} bx1
 * @param {number} by1
 * @param {number} bx2
 * @param {number} by2
 * @return {number}
 */
var computeArea = function(a, b, c, d, e, f, g, h) {
    function intersection(){
        const top = Math.min(d , h);
        const bottom = Math.max(b , f);
        
        const left = Math.max(a , e);
        const right  = Math.min(c , g);
        
        if (right > left && top > bottom){
            return (right - left) * (top - bottom);  
        }
        return 0;
        
    }
    
    const l1 = Math.abs(a - c);
    const w1 = Math.abs(b - d);
    
    const l2 = Math.abs(e - g);
    const w2 = Math.abs(f - h);
    
    const total_area = (l1 * w1) + (l2 * w2) - intersection();
    return total_area ;
};