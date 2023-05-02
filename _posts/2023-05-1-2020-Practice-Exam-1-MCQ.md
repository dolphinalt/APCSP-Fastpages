---
toc: true
layout: post
description: 2020 Practice Exam 1 MCQ
categories: [markdown]
title: 2020 Practice Exam 1 MCQ
---

# 2020 Practice Exam 1 MCQ
## Total score: 60/67

### Q12
A color in a computing application is represented by an RGB triplet that describes the amount of red, green, and blue, respectively, used to create the desired color. A selection of colors and their corresponding RGB triplets are shown in the following table. Each value is represented in decimal (base 10).

| Color Name | RGB Triplet |
| --- | --- |
| indigo | (75,   0, 130) |
| ivory | (255, 255, 240) |
| light pink | (255, 182, 193)​ |
| light yellow | (255, 255, 224) |
| magenta | (255,   0, 255) |
| neutral gray | (127, 127, 112) |
| pale yellow | (255, 255, 160) |
| vivid yellow | (255, 255,  14) |

What is the binary RGB triplet for the color indigo?

(A) (00100101, 00000000, 10000010)

(B) (00100101, 00000000, 01000001)

(C) (01001011, 00000000, 10000010)

(D) (01001011, 00000000, 01000001)

**My answer**: D

**Correct answer**: C

The correct answer is C because the RGB triplet for indigo is (75, 0, 130). 75 is 01001011 in binary, 0 is 00000000 in binary, and 130 is 10000010 in binary. I got this wrong because I looked for only the last triplet for the color ivory because I read the question wrong.

### Q15
Consider the two programs below.
```
Program A:
i <- 1
repeat until i > 10
    display i
    i <- i + 1
```
```
Program B:
i <- 0
repeat until i >= 10
    i <- i + 1
    display i
```

(A) Program A and program B display identical values in the same order.

(B) Program A and program B display the same values in different orders.

(C) Program A and program B display the same number of values, but the values differ.

(D) Program B displays one more value than program A.

**My answer**: B

**Correct answer**: A

The correct answer is A because both programs display the same values in the same order. Program A will start with 1 and print until 10, while program B will start with 0, add one, and print until 10. I got this wrong because I thought that the first program would display 1-10 and the second program would display 2-11. This stemmed from reading program Bs initial value wrong.

### Q16
A student wrote the following program to remove all occurrences of the strings "the" and "a" from the list wordList.
```
Line 1: index <- LENGTH (wordList)

Line 2: REPEAT UNTIL (index < 1)

Line 3: {

Line 4:    IF ((wordList[index] = "the") OR (wordList[index] = "a"))

Line 5:    {

Line 6:       REMOVE (wordList, index)

Line 7:    }

Line 8: }
```
While debugging the program, the student realizes that the loop never terminates. Which of the following changes can be made so that the program works as intended?

(A) Inserting index <- index + 1 between lines 6 and 7

(B) Inserting index <- index + 1 between lines 7 and 8

(C) Inserting index <- index - 1 between lines 6 and 7

(D) Inserting index <- index - 1 between lines 7 and 8

**My answer**: C

**Correct answer**: D

The correct answer is D because the index needs to be decremented by 1 after the word is removed from the list. I got this wrong because I read the code wrong and assumed that just inserting an `index <- index - 1` would work between lines 6 and 7, but instead it would only activate if the word is "the" or "a".

### Q22
Consider the following spinner, which is used to determine how pieces are to be moved on a game board. The region labeled "Move 1 space" is six times as large as each of the other two regions.

```
|                                Move 1 space                             |lose a turn|  move 2   |
```

Which of the following code segments can be used to simulate the behavior of the spinner?

(A)

(B)

(C)

(D)

**My answer**: B

**Correct answer**: D

The correct answer is D because the spinner has a 6/8 chance of moving 1 space, a 1/8 chance of losing a turn, and a 1/8 chance of moving 2 spaces. I got this wrong because I thought the spinner was split into 6ths instead of 8ths.

### Q50
Consider the following algorithms. Each algorithm operates on a list containing n elements, where n is a very large integer.

  I An algorithm that accesses each element in the list twice
 II An algorithm that accesses each element in the list n times
III An algorithm that accesses only the first 10 elements in the list, regardless of the size of the list

Which of the algorithms run in reasonable time?

(A) I only

(B) III only

(C) I and II only

(D) I, II, and III

**My answer**: B

**Correct answer**: D

The correct answer is D because I runs in 2n time, II runs in n^2 time and III runs in 10 time. I got this wrong because I thought calculated the time complexity of I wrong and didn't realize that n^2 was reasonable time.

### Q58
The following procedure is intended to return true if at least two of the three parameters are equal in value and is intended to return false otherwise.

```
PROCEDURE AnyPairs (x, y, z)

    {

        IF (x = y)

        {

            RETURN (true)

        }

        ELSE

        {

    RETURN (y = z)

    }

}
```

For which of the following procedure calls does the procedure NOT return the intended value?

(A) AnyPairs ("bat", "cat", "rat")

(B) AnyPairs ("bat", "bat", "rat")

(C) AnyPairs ("bat", "cat", "bat")

(D) AnyPairs ("bat", "cat", "cat")

**My answer**: D

**Correct answer**: C

The correct answer is C because in C, even though there is a pair, the program will not return true because it never checks if X is equal to Z. D is wrong because it still checks if Y is equal to Z.

### Q66
In mathematics, a perfect number is a type of integer. The procedure IsPerfect (num) returns true if num is a perfect number and returns false otherwise.

The following program is intended to count and display the number of perfect numbers between the integers start and end, inclusive. Assume that start is less than end. The program does not work as intended.

```
Line 1:  currentNum <- start

Line 2:  count <- 0

Line 3:  REPEAT UNTIL (currentNum > end)

Line 4:  {

Line 5:     count <- count + 1

Line 6:     IF (IsPerfect (currentNum))

Line 7:     {

Line 8:        count <- count + 1

Line 9:        currentNum <- currentNum + 1

Line 10:    }

Line 11:    currentNum <- currentNum + 1

Line 12: }

Line 13: DISPLAY (count)
```

Which two lines of code should be removed so that the program will work as intended?

Select two answers.

[A] Line 5

[B] Line 8

[C] Line 9

[D] Line 11

**My answer**: A, D

**Correct answer**: A, C

The choice D is wrong because we still need to increment the amount of numbers that have been checked. C is correct because we should not increment twice if a perfect number is found. The mistake I made was assuming that the program would only increment once even if a perfect number was found.