/**
 * @param {number[]} rec1
 * @param {number[]} rec2
 * @return {boolean}
 */
var isRectangleOverlap = function(rec1, rec2) {
        let a , b , c, d, e, f, g, h;
        [a , b , c, d, e, f, g, h] = [...rec1 , ...rec2];
    
        const top = Math.min(d , h);
        const bottom = Math.max(b , f);
        
        const left = Math.max(a , e);
        const right  = Math.min(c , g);
        
        if (right > left && top > bottom){
            return true;  
        }
        return false;
};