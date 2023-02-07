# International Standard Book Numbers

When analysing the ISBN code in the *isbn.py* source file the following definitions were used:
* **Time Complexity** is the computational complexity that describes the amount of computer time it takes to run an algorithm.
* The **Space Complexity** of an algorithm is the total space taken by the algorithm with respect to the input size. Space complexity includes both Auxiliary space and space used by input.

## Validation

The Time Complexity is *O(N + 3)* in the case where a string of valid length is provided. The *3* is for checking the object type and lengths done, these run in constant time, while *N* iterations are needed to check and validate an ISBN number in the correct format.

Space Complexity *O(11)* which relates to the list of valid characters stored for checking that only valid characters are used in the input string.

## ISBN-10 Validity Check

The Time Complexity is *O(N + 4)* where the *4* relates to the assignment statements and the modulus operation. The *N* relates to the number of iterations executed to process the entire ISBN number.

Space Complexity is constant at *O(3)*, as only 3 variables are used by this function. Here I kept it simple as readability is everything for me when I know someone is going to read my code. Readability means the code will be easier to understand.

## ISBN-13 Validity Check

The Time Complexity is *O(N + 3)* where the *3* relates to the assignment statements and the modulus operation. The *N* relates to the number of times the loop is run to process the ISBN number.

Space Complexity is constant at *O(2)*, as only 2 variables are used by this function. Here once again I just kept it simple as readability is everything for me when I know someone is going to read my code.

## Converting ISBN-10 numbers to ISBN-13

The Time Complexity is *O(N + 5)* where the *5* relates to the assignment statements, modulus operation, and concatenation. The *N* relates to the number of times the loop is run to process the ISBN number.

Where a string counts as *N + 3*, the Space Complexity is constant at *O(N + 7)*. I have counted the final variable formed by concatenation in line 97. In an attempt to reduce the space complexity list comprehension and the enumeration operator could have been applied but at the cost of readability. I believe this is a fair performance trade-off that I am making in this case to maintain readability.

## Main ISBN function

In the case where a valid ISBN-10 number is provided then the Time Complexity is *O(N + 3 + N + 4 + N + 5 = O(3N + 12)*. This accounts for validation, checking the ISBN-10 for validity, and conversion to an ISBN-13 number.

In the case where a valid ISBN-13 number is provided then the Time Complexity is *O(N + 3 + N + 4 + N + 3 = O(3N + 10)*. This accounts for validation and checking the ISBN-13 number for validity. The N + 4 is encountered because the number is checked for ISBN-10 validity first before it is checked for ISBN-13 validity.

Following the same logic the Space Complexity for a valid ISBN-10 number is *O(N + 21 + 5) = O(N + 26)* while its *O(16 + 5) = O(21)* for a valid ISBN-13 number. The *5* is for the string value for 'Valid'.

The worst case, in terms of time and space, remains in dealing with an ISBN-10 number as the number, has to be validated, checked, and then converted. When an invalid ISBN number is provided and validated, ISBN-10 and ISBN-13 checks are run, the Time Complexity of *O(3N + 10)*(the same as that of a valid ISBN-13 number), is less than that of dealing with an ISBN-10 number by 2. The Space Complexity is also less by 3 at *O(21)*. If you count the last statement(line 122) as *1* then technically executing the function with an invalid string is more expensive than executing it with a valid ISBN-13 by *1*.

## Summary

Function                    | Time Complexity | Space Complexity |
----------------------------|-----------------|------------------|
Validation                  | O(N + 3)        | O(11)            |
ISBN-10 Validity Check      | O(N + 4)        | O(3)             |
ISBN-13 Validity Check      | O(N + 3)        | O(2)             |
ISBN-10 Conversion          | O(N + 5)        | O(N + 7)         |
Main ISBN function(ISBN-10) | O(3N + 12)      | O(N + 26)        |
Main ISBN function(ISBN-13) | O(3N + 10)      | O(21)            |
Main ISBN function(Invalid) | O(3N + 11)      | O(24)            |

<span style="color:red; font-weight: bold;">Note</span>: For precision purposes, the *1* has been added to the complexities of the *Invalid* case for the main ISBN function.

All the Time Complexities are *linear* while some the Space Complexities are constant and some *linear*.
