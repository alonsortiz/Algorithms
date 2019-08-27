//Alonso Ortiz - 25/Aug/2019

import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;
import java.util.stream.*;

public class QuickSort {

    /*
     * 1. Implementing my version of the Quicksort Algorithm.
     */
    public static List<Integer> myQuicksort(List<Integer> ar) {
        if(ar.size() < 2) {
            return ar;
        } else {
            List<Integer> less = new ArrayList<Integer>();
            List<Integer> more = new ArrayList<Integer>();
            List<Integer> subList = new ArrayList<Integer>();
            Random ran = new Random();
            
            int indexPivot = ran.nextInt(ar.size());
            Integer pivot = ar.get(indexPivot);
            ar.remove(indexPivot);

            for(Integer element : ar) {
                if(element.compareTo(pivot) < 0) {
                    less.add(element);
                } else {
                    more.add(element);
                }
            }

            subList.addAll(myQuicksort(less));
            subList.add(pivot);
            subList.addAll(myQuicksort(more));
            return subList;
        }
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        List<Integer> unordered = new ArrayList<Integer>();


        for(int i = 0; i<=10; i++) {
            Random ran = new Random();
            int randomInt = ran.nextInt(20) + 1;
            unordered.add(randomInt);
        }

        System.out.println(unordered);

        List<Integer> ordered = myQuicksort(unordered);

        System.out.println(ordered);
        
    }
}