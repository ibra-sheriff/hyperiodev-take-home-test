# Java Task Review
> "*To understand recursion, one must first understand recursion.*" - Stephen Hawking

I find that since *Recursion* means defining a problem in "terms of itself", this can make it both an interesting and tricky programming concept to implement correctly. With that said, I believe this is a good attempt. I will break down this review into:
* Housekeeping
* Comments on Recursion
* Reverse String Problem
* Fibonacci Series Problem
* Closing Remarks: Rose and Thorn

## Housekeeping
Before discussing the two methods I would like to start by going through the style elements of the program. I put a lot of weight on style because it's important for readability and consistency in a codebase. In fact, I once attended a talk from Facebook engineers that said that Facebook puts more emphasis on readability than performance now.

Styling in Java tends to follow the CamelCase naming convention unlike Python which favours an under_score approach so in line 11 you need to write  **reverse_string** as **reverseString**. Your class name must always start with a capital letter so just change **recursion**(in line 1) to **Recursion**. You have followed the general Java style conventions very well in the rest of the document.

The last comment on your naming convention is that using generic names like **function** does not say much about the method. Ensure the names of methods and classes are descriptive, they need to say something about what the method or class does. It increases the readability of your code. Instead of **function** you can call it **fibonacciSeries** or **fibonacciNumbers**.

For your comment, inline comments are more appropriate for explaining logic, steps, or helper methods, for your core methods use Javadoc comments. Usually, I ensure to use Javadoc for my methods with the *public* access modifier and inline comments for my *private* helper methods. These are great as they structure the comments into:
* A general description of the method outlining the output and workings of the method.
* A description of each parameter, its type, and its role.
* A description of the return type and the meaning of the return value.
If you are unfamiliar with Javadoc check out the blog post by [Baeldung](https://www.baeldung.com/javadoc) to get started and the complete documentation on [Oracle](https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html) to get the complete picture.

Your indentation and spacing are quite good, I would say this is me nitpicking
* Your **for** loop in line 29 is on the far left of the source file, indent it so that it is in line with the rest of your code.
* In your **for** loop(line 29) and **if** statement(line 13) ensure to use the same number of spaces when indenting the body of code as with the bodies of your methods. It looks like you were using a tab made up of 4 spaces for indenting code in your method but only 2 spaces for your **for** loop and **if** statement.
* After the **for** loop parenthesis in line 29 please leave a space between the parenthesis and curly brace, so **) {** not **){**.
I only nitpick to ensure that your code always has the best general impression at first glance, the human eye easily picks up misplacements or misalignments.

Continuing with the point of the human eye, consistency is another thing that is important to ensure smooth viewing of your source code. Consistency must be followed when defining, declaring, assigning, or commenting. I see you like to start comments with a capital letter, ensure this follows through in all your comment, the comment in line 5 is missing a capital letter. When defining methods you have chosen to put the opening curly brace on the same line after the closing parenthesis and the closing curly brace on the next line after the method. This though is not the case for the **reverse_string** method in line 11 where the opening curly brace is on the next line and the closing brace is on the same line as the last line of the body of the method. Please ensure the convention is applied as in the **main** and **function** method.

Once you are done with your code and you are happy with it, ensure to remove any unnecessary comments and print statements. The comments in line 3 and line 5 relate to self-explanatory statements, while the print statements in lines 14, 18, and 28 can be removed as they relate to testing. By the end of the day, ensure your core methods only output what is mentioned in the specification.

The last thing in housekeeping is, in most projects, it's preferred that your **main** method(in line 2) is at the bottom of your source file, so that the source file starts with the important methods and objects. Here we are more interested in your recursive methods rather than test statements.

## Comments on Recursion
As mentioned before, *Recursion* can be an awkward programming concept to learn but once you get it, you might find yourself making every method recursive like functional language programmers.

In general, you correctly applied Recursion in the **reverse_string** method. You clearly started with your *Base Case* and then wrote your *Recursive Step*. Unfortunately, the same cannot be said of the Fibonacci Series problem where the method **function** is not a recursive method. It does not break down the problem into cases with the two cases(*Base Case* and *Recursive Step*) but the big giveaway is that the method does not call itself.

## Reverse String Problem
As mentioned before the **reverse_string** method is a great attempt, the only issue is the method call in the *Recursive Step*. You had to call **reverse_string** instead of **reverseString** or in line with CamelCase convention, rename **reverse_string** as **reverseString**(preferred). In fact, the solution was so close to correct that my solution just involved fixing that issue.

The body of the method uses short and concise code, making it very readable. I love this application of the [KISS principle](https://www.freecodecamp.org/news/keep-it-simple-stupid-how-to-use-the-kiss-principle-in-design/). String concatenation can be expensive but by keeping it simple I find your solution quite efficient. To improve the performance, especially for large strings, you could incorporate *StringBuffer*.

In terms of testing, I am not sure what string values you used to test the method but it would be great to leave the reader a string value in the **main** method that demonstrates what the method does. In line 4 the string is empty, just place a value like *'food'* so that when someone runs the program they get *'doof'*.

## Fibonacci Series Problem
I see you struggled with this problem, but that's okay, let's talk about it. We have been tasked to code a recursive function that, given a number n, prints out the first n Fibonacci numbers. Let's get our method definition right:
```
public static void fibonacciSeries(int n)
```
There is no need to make use of [Java Generics](https://www.baeldung.com/java-generics) in line 22, let's stick to our primitive types and operate with what we know well. The problem does not require that objects are involved in the solution so [Java Generics](https://www.geeksforgeeks.org/generics-in-java/) offer no value and only over-complicate the solution. Notice how I have called the parameter **n** instead of **maxNumber**, I find it better to name my parameters according to the specification. It makes it easier to translate the specification of the question to the code. On this point of **maxNumber** there was a mistake, as the **maxNumber** is provided as a parameter and then declared in the method body again. Always make sure that each variable has its own unique name, method parameters are variables too in the method body, so we cannot use their names when declaring new variables in the method body. The last point on the **maxNumber** is that it is declared and assigned a value of 10 which is not desired, we want the caller of the method to be able to provide their own **maxNumber** i.e. n. This ensures we can print a Fibonacci Series of any length.

Now that we have defined our key variables: **n**, **previousNumber** and **nextNumber**, we can start working on the *Base Case* and *Recursive Step* of the recursive method. Our *Base Case* can relate to ensuring that **n > 0** for example, and our *Recursive Step* can involve using the variables **previousNumber** and **nextNumber** to calculate the next value in the Fibonacci Series. We then need to update the values of variables: **n**, **previousNumber** and **nextNumber**, then use the updated values in a recursive call, this means that we may need to change our method signature and include not just **n** but **previousNumber** and **nextNumber** too.

This is an efficient approach to obtaining the Fibonacci Series of n numbers with a time complexity of *O(N)* and a Space Complexity of *O(1)*. This is because we print the ith value in the Fibonacci Series as we compute it. If we computed each value in the Fibonacci Series using its own recursive method call, the time complexity becomes 2^N as we are making extra method calls.

## Closing Remarks: Rose and Thorn
I hope you found this review constructive, as I enjoyed reviewing your code. It's always great to see a programmer wrestling with *Recursion* and starting to understand it. In general, the Reverse String problem was well done, though it had one issue, the solution was well thought out and elegant. More work needs to be done on the Fibonacci Series problem especially in ensuring that the design of the answer is in line with the components of *Recursion*.

To improve on this, take care of your coding style and take your time with your final solution. I know there are course deadlines but at the minimum ensure you submit work that compiles and runs as I feel it's an important part of getting to a working solution. Very important in debugging. If it compiles and runs, you can at least experiment with it until you get to a working solution. This is why placing print statements to display variable values and map out branching remains a popular debugging technique.

Let me know if anything is unclear. Good luck with the next one!
