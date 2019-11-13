//Alonso Ortiz - 18/Sep/2019

import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;
import java.util.stream.*;

public class MoveZeroes {

    /*
     * From: https://leetcode.com/problems/move-zeroes/
     *
     * 283. Given an array nums, write a function to move all 0's to the end of it while maintaining
     * the relative order of the non-zero elements.
     *
     * 1. You must do this in-place without making a copy of the array.
     * 2. Minimize the total number of operations.
     */
    public static void moveZeroes(int[] arr) {

        int pos = 0;
        boolean firstZero = true;

        for(int i = 0; i < arr.length; i++) {
            if(arr[i] !=  0) {
                if(!firstZero) {
                    arr[pos++] = arr[i];
                    arr[i] = 0;
                } 
            } else {
                if(firstZero) {
                    pos = i;
                    firstZero = false;
                }
            }
        }
        
    }

    public static void main(String[] args) throws IOException {
        
        int[] arr = {0,1,0,3,12};
        System.out.println("Array             -> " + Arrays.toString(arr));
        moveZeroes(arr);
        System.out.println("Zeroes at the end -> " + Arrays.toString(arr));

        int[] arr2 = {2,9,7,0,0,0,4,0,8};
        System.out.println("\nArray           -> " + Arrays.toString(arr2));
        moveZeroes(arr2);
        System.out.println("Zeroes at the end -> " + Arrays.toString(arr2));

        int[] arr3 = {0,0,0,0,1};
        System.out.println("\nArray           -> " + Arrays.toString(arr3));
        moveZeroes(arr3);
        System.out.println("Zeroes at the end -> " + Arrays.toString(arr3));

        int[] arr4 = {0,1,0};
        System.out.println("\nArray           -> " + Arrays.toString(arr4));
        moveZeroes(arr4);
        System.out.println("Zeroes at the end -> " + Arrays.toString(arr4));

        Random ran = new Random();
        int[] randomArr = new int[10];
        for (int i = 0; i < randomArr.length; i++) {
            randomArr[i] = ran.nextInt(5);;
        }

        System.out.println("\nArray           -> " + Arrays.toString(randomArr));
        moveZeroes(randomArr);
        System.out.println("Zeroes at the end -> " + Arrays.toString(randomArr));

    }
}
