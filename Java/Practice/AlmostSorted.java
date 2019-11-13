//Alonso Ortiz - 24/Sep/2019

import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;
import java.util.stream.*;

public class AlmostSorted {

    /*
     * From: https://www.geeksforgeeks.org/sort-an-almost-sorted-array-where-only-two-elements-are-swapped/
     *
     * Sort an almost sorted array where only two elements are swapped, how to sort the array efficiently?
     *
     * Input:  arr[] = {10, 20, 60, 40, 50, 30}  
     * // 30 and 60 are swapped
     * Output: arr[] = {10, 20, 30, 40, 50, 60}
     *
     * Input:  arr[] = {10, 20, 40, 30, 50, 60}  
     * // 30 and 40 are swapped
     * Output: arr[] = {10, 20, 30, 40, 50, 60}
     *
     * Input:   arr[] = {1, 5, 3}
     * // 3 and 5 are swapped
     * Output:  arr[] = {1, 3, 5}
     *
     */
    public static void almostSorted(int[] arr) {

        int temp, pos;
        temp = pos = 0;
        boolean found = false;

        for(int i = 0; i < arr.length; i++) {
            if(!found) { 
                if(arr[i] > arr[i+1]) {
                    temp = arr[i];
                    pos = i;
                    found = true;
                }
            } else {
                if(i == arr.length-1 || arr[i+1] > temp) {
                    arr[pos] = arr[i];
                    arr[i] = temp;
                    break;
                }
            } 
        }
        
    }

    public static void main(String[] args) throws IOException {
        
        int[] arr = {10, 20, 60, 40, 50, 30};
        System.out.println("Almost sorted array -> " + Arrays.toString(arr));
        almostSorted(arr);
        System.out.println("Sorted array        -> " + Arrays.toString(arr));

        int[] arr2 = {10, 20, 40, 30, 50, 60};
        System.out.println("\nAlmost sorted array -> " + Arrays.toString(arr2));
        almostSorted(arr2);
        System.out.println("Sorted array        -> " + Arrays.toString(arr2));

        int[] arr3 = {1, 5, 3};
        System.out.println("\nAlmost sorted array -> " + Arrays.toString(arr3));
        almostSorted(arr3);
        System.out.println("Sorted array        -> " + Arrays.toString(arr3));

        int[] arr4 = {50, 20, 30, 40, 10, 60};
        System.out.println("\nAlmost sorted array -> " + Arrays.toString(arr4));
        almostSorted(arr4);
        System.out.println("Sorted array        -> " + Arrays.toString(arr4));
  
        int[] arr5 = {20, 10};
        System.out.println("\nAlmost sorted array -> " + Arrays.toString(arr5));
        almostSorted(arr5);
        System.out.println("Sorted array        -> " + Arrays.toString(arr5));

    }
}
