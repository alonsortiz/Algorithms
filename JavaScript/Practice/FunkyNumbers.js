/*
 * By: Alonso Ortiz - 08/Nov/2019
 * From: https://codeforces.com/problemset/problem/192/A
 *
 * As you very well know, this year's funkiest numbers are so called triangular numbers 
 * (that is, integers that are representable as k(k+1) / 2, where k is some positive integer), 
 * and the coolest numbers are those that are representable as a sum of two triangular numbers.
 * 
 * A well-known hipster Andrew adores everything funky and cool but unfortunately, 
 * he isn't good at maths. Given number n, help him define whether this number can be represented 
 * by a sum of two triangular numbers (not necessarily different)!
 */
function funkyNumbers(n) { 

    var funkyNumber = 'NO';

    var maxTriangle = maxTrianglePossible(n);

    for(let i = maxTriangle; i > 0; i--) {
        var firstTriangle = triangleNumbers(i);
        var rem = n - firstTriangle;

        if(rem === 0) continue;

        var secFactor = maxTrianglePossible(rem);
        var secTriangle = triangleNumbers(secFactor);

        var triangles = firstTriangle + secTriangle;

        if(triangles == n) {
            funkyNumber = 'YES';
            break;
        } 
        
    }
    
    return funkyNumber;       
} 

function maxTrianglePossible(n) {
    //k(k+1) / 2 = n where n is an integer
    //k(k+1) = n*2
    //k^2 + k - n*2 = 0 -> factors

    var k = Math.floor( Math.sqrt(n*2) );

    return k;

}

function triangleNumbers(x) {
    
    var f = ( x * (x + 1) ) / 2;

    return f;
}

//stdin → stdout
const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});
 
readline.on('line', n => {
    readline.close();
    
    let res = funkyNumbers(n);
    console.log('Is ' + n + ' a Funky Number? -> ' + res);
});
