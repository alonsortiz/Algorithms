/*
 * Name: Two Number Sum
 * By: Alonso Ortiz - 11/Mar/2021
 * From: AlgoExpert
 */

const twoNumberSum = (arr, target) => {
    let mySet = new Set();

    for(let el of arr) {
        if(mySet.has((target-el))) {
            return [el,(target-el)];
        } else {
            mySet.add(el);
        }
    }

    return [];
};