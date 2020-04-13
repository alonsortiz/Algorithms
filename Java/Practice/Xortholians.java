/*
 * By: Alonso Ortiz - 12/Apr/2020
 * From: Microsoft
 *
 * Xortholians are a proud race and have a rich history of rainbow-inspired art. One Xortholian artist from the last 
 * century made a particularly beautiful series of paintings using only the colors in the rainbow.
 *
 * Each of these paintings consists of two rows of paint. The first row is a series of equally sized squares, 
 * each of them being a primary color or blank, i.e. each is one of the following: "red", "yellow", "blue", "blank". 
 * No two neighboring spaces in the first row will ever have the same color (including blank).
 *
 * To be clear, possible colors are "red", "orange", "yellow", "green", "blue", and "purple". Xortholians do not 
 * recognize indigo or violet.
 *
 * Your goal as an aspiring young Xortholian Art and Mathematics dual-major is to determine what some paintings' first 
 * row is based on the corresponding second row.
 *
 * Example input:
 * red purple green orange purple purple orange yellow yellow yellow
 *
 * Example output
 * [red, blue, yellow, red, blue, red, yellow, blank, yellow]
 */

import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;
import java.util.stream.*;

public class Xortholians {

    public static String[] findFirstRow(String secRow) { 
              
        String[] secArr = secRow.split(" ");
        String[] firstRow = new String[secArr.length-1];
        firstRow[0] = secArr[0];

        HashMap<String, String> yellowCombinations = new HashMap<String, String>();
        yellowCombinations.put("green", "blue");
        yellowCombinations.put("orange", "red");
        yellowCombinations.put("yellow", "blank");

        HashMap<String, String> blueCombinations = new HashMap<String, String>();
        blueCombinations.put("purple", "red");
        blueCombinations.put("green", "yellow");
        blueCombinations.put("blue", "blank");

        HashMap<String, String> redCombinations = new HashMap<String, String>();
        redCombinations.put("purple", "blue");
        redCombinations.put("orange", "yellow");
        redCombinations.put("red", "blank");

        HashMap<String, HashMap<String, String>> colors = new HashMap<String, HashMap<String, String>>();
        colors.put("yellow", yellowCombinations);
        colors.put("blue", blueCombinations);
        colors.put("red", redCombinations);

        for(int i = 1; i < secArr.length-1; i++) {
            if(colors.containsKey(firstRow[i-1])) {
                firstRow[i] = colors.get(firstRow[i-1]).get(secArr[i]);
            } else {
                firstRow[i] = secArr[i];
            }
        }

        return firstRow;
        
    }

}
