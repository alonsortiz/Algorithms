/*
 * By: Alonso Ortiz - 06/Apr/2020
 *
 * Given a set of lines each containing multiple random strings, your task for each line is to find the characters 
 * that are common to all of its strings. In other words, you should output one string for each line that contains 
 * all of the distinct characters that the given strings on that line have in common.
 *
 * Characters include [A-Z, a-z, 0-9]. Characters with different cases (e.g. 'a' vs 'A') count as distinct characters.
 *
 * The order of characters in the output string should appear as follows:
 *
 * In order of numbers 0-9.
 * In order of uppercase characters A-Z.
 * In order of lowercase characters a-z.
 */

import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;
import java.util.stream.*;

public class CommonString {

    public static String commonString(String line) { 
                
        char[] charArr = line.toCharArray();
        String common = "";
        int wordNum = 1;
        Map<Character, HashSet<Integer>> charMap = new HashMap<Character, HashSet<Integer>>();
        Set<Integer> numOfWords = new HashSet<Integer>();

        for(int i = 0; i < charArr.length; i++) {
            if(charArr[i] == ' ') { 
                wordNum++;
            } else {
                charMap.computeIfAbsent(charArr[i], k -> new HashSet<>()).add(wordNum);

                numOfWords.add(wordNum);
            }
        }

        for(Character key : charMap.keySet()) {
            if(charMap.get(key).equals(numOfWords)) {
                common += key;
            }
        }

        char[] commonArr = common.toCharArray();
        Arrays.sort(commonArr);
        
        return new String(commonArr);

    }

}
