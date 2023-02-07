/**
 * This file contains recursive functions to do the following operations:
 *     - reverse a string
 *     - print the first n numbers in the Fibonacci Series.
 * 
 * @author Ibrahim Sheriff Sururu
 * @bugs no known bugs
 */
public class Recursion {
    public static void main(String[] args) {
        String result1 = reverseString("food");
        String result2 = reverseString("madam");
        String result3 = reverseString("union");
        String result4 = reverseString("ballon");
        System.out.println(result1);
        System.out.println(result2);
        System.out.println(result3);
        System.out.println(result4);
        fibonacciSeries(5);
        fibonacciSeries(6);
        fibonacciSeries(7);
    }

    /**
     * Processes the given string and reverses it and returns the result.
     * 
     * @param myStr the input string to reverse
     * @return a string holding the reversed version of the given String
     **/
    public static String reverseString(String myStr) {
        // base case
        if (myStr.isEmpty())
            return myStr;
        // recursive case
        return reverseString(myStr.substring(1)) + myStr.charAt(0);
    }

    public static int FIBONACCI_VERSION = 2;  // can be 1(multiple calls of recursive function) or 2(print as we go)

    /**
     * Given the number n, this method prints out the first n Fibonacci numbers.
     * Fibonacci numbers are a sequence where each number is the sum of the previous
     * two - 0 1 1 2 3 5 8 ...
     * 
     * @param n the number of Fibonacci numbers to print
     */
    public static void fibonacciSeries(int n) {
        if (FIBONACCI_VERSION == 1) {
            for (int i = 0; i < n; i++) {
                System.out.print(fibonacciSeriesHelper(i) + " ");
            }
            System.out.println();
        } else {
            // n1=0, n2=1, n3=0
            if (n == 1) {
                System.out.print("0");  // print 0
            } else if (n == 2) {
                System.out.print("0 1");  // print the first 2 values - 0 and 1
            } else {
                System.out.print("0 1 ");  // print the first 2 values - 0 and 1
                fibonacciSeries2(n - 2, 0, 1, 0);
                System.out.println();
            }
        }
    }

    // computes the nth number of the Fibonacci series
    private static int fibonacciSeriesHelper(int n) {
        // Base Case
        if (n <= 1) return n;

        // Recursive call
        return fibonacciSeriesHelper(n - 1) + fibonacciSeriesHelper(n - 2);
    }

    // Prints the m Fibonacci numbers after the first 2 values - 0 and 1
    private static void fibonacciSeries2(int n, int n1, int n2, int n3) {    
        if(n > 0) {    
             n3 = n1 + n2;    
             n1 = n2;    
             n2 = n3;    
             System.out.print(n3 + " ");   
             fibonacciSeries2(n-1, n1, n2, n3);    
         }    
     }   
}