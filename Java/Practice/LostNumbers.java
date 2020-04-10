/*
 * By: Alonso Ortiz - 09/Apr/2020
 *
 * Given a set of arrays of scrambled integers, your goal is to find which numbers were lost from each of the sequences.
 * 
 * Numbers are only lost from the middle of a (properly ordered) sequence: the first integer in the sequence l and
 * last integer r are never lost. For this problem, a properly ordered sequence of numbers is to be in strictly 
 * increasing order: [l, l + 1, l + 2, ... , r - 2, r - 1, r].
 *
 * Your task, for each of the given arrays, is to print a string containing all of the missing numbers from 
 * the sequence in increasing order.
 */

import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;
import java.util.stream.*;

public class LostNumbers {

    public static String missingNumbers(int[] arr) { 
        
        String missingNums = "";
        Set<Integer> incompleteSet = new HashSet<Integer>();
        int min, max;
        min = max = arr[0];

        //Arrays.sort(arr);

        for(int i = 0; i < arr.length; i++) {
            if(arr[i] > max) {
                max = arr[i];
            } 

            if(arr[i] < min) {
                min = arr[i];
            }

            incompleteSet.add(arr[i]);
        }

        while(min < max) {
            if(!incompleteSet.contains(min)) {
                if(missingNums == "") {
                    missingNums += min;
                } else {
                    missingNums += " " + min;
                }
            }

            min++;
        }

        return missingNums;
    }

}
