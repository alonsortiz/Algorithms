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

const funkyNumbers = n => {
    let funkyNumber = 'NO';

    let maxTriangle = maxTrianglePossible(n);

    for(let i = maxTriangle; i > 0; i--) {
        let firstTriangle = triangleNumbers(i);
        let rem = n - firstTriangle;

        if(rem === 0) continue;

        let secFactor = maxTrianglePossible(rem);
        let secTriangle = triangleNumbers(secFactor);

        let triangles = firstTriangle + secTriangle;

        if(triangles == n) {
            funkyNumber = 'YES';
            break;
        } 
        
    }
    
    return funkyNumber; 
}

const maxTrianglePossible = n => Math.floor( Math.sqrt(n*2) );

const triangleNumbers = x => ( x * (x + 1) ) / 2;

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
