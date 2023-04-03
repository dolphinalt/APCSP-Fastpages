---
toc: true
layout: post
description: Big Idea 4 Quiz Corrections
categories: [markdown]
title: Big Idea 4 Quiz Corrections
---

# APCSP Big Idea 4 Quiz Corrections
## Total score: 38/50

### Q2:

Which of the following is a characteristic of the fault-tolerant nature of routing on the Internet?

(A) The ability to use a hierarchical naming system to avoid naming conflicts

(B) The ability to provide data transmission even when some connections have failed

(C) The ability to resolve errors in domain name system (DNS) lookups

(D) The ability to use multiple protocols such as hypertext transfer protocol (HTTP), Internet protocol (IP), and simple mail transfer protocol (SMTP) to transfer data

**My answer**: D

**Correct answer**: B

The correct answer is B because routers on the Internet are able to move packets through various paths to reach their final destination, even when some connections have failed. This characterizes the fault-tolerant nature of routing.

### Q17:

A large data set contains information about all students majoring in computer science in colleges across the United States. The data set contains the following information about each student.

The student’s gender

The state in which the student attends college

The student’s grade point average on a 4.0 scale

Which of the following questions could be answered by analyzing only information in the data set?

(A) Do students majoring in computer science tend to have higher grade point averages than students majoring in other subjects?

(B) How many states have a higher percentage of female computer science majors than male computer science majors attending college in that state?

(C) What percent of students attending college in a certain state are majoring in computer science?

(D) Which college has the highest number of students majoring in computer science?

**My answer**: C

**Correct answer**: B

The correct answer is B because the data set stores information about an individual student’s gender and state. This information can be aggregated to extract information about the percentage of female majors in each state.

### Q19:

A retailer that sells footwear maintains a single database containing records with the following information about each item for sale in the retailer’s store.

 - Item identification number

 - Footwear type (sneakers, boots, sandals, etc.)

 - Selling price (in dollars)

 - Size

 - Color

 - Quantity available

Using only the database, which of the following can be determined?

(A) Which items listed in the database are not currently in the store

(B) Which colors are more popular among men than women

(C) Which type of footwear is most popular among adults

(D) The total number of shoes sold in a particular month

**My answer**: D

**Correct answer**: A

The correct answer is A because the database stores information on item identification numbers and quantities available, the retailer can search for all item identification numbers that have a quantity of 0.

### Q20:

When a cellular telephone user places a call, the carrier transmits the caller’s voice as well as the voice of the person who is called. The encoded voices are the data of the call. In addition to transmitting the data, the carrier also stores metadata. The metadata of the call include information such as the time the call is placed and the phone numbers of both participants. For which of the following goals would it be more useful to computationally analyze the metadata instead of the data?

I. To determine if a caller frequently uses a specific word

II. To estimate the number of phone calls that will be placed next Monday between 10:30 A.M. and noon.

III. To generate a list of criminal suspects when given the telephone number of a known criminal

(A) I only

(B) II only

(C) II and III only

(D) I, II, and III

**My answer**: B

**Correct answer**: C

The correct answer is C because both II and III are correct choices. II is correct because the repository of stored metadata includes time, so information about the time of calls can be analyzed to make predictions about future calls. In addition, III is correct because the metadata stores the phone numbers of the two parties of a call. Given one phone number, the metadata can be processed to provide all phone numbers that were called by or placed to that person.

### Q27:

**Directions: The question or incomplete statement below is followed by four suggested answers or completions. Select the one that is best in each case.**

Digital images are often represented by the red, green, and blue values (an RGB triplet) of each individual pixel in the image. A photographer is manipulating a digital image and overwriting the original image. Which of the following describes a lossless transformation of the digital image?

(A) Compressing the image in a way that may lose information but will suffer only a small loss of image quality.

(B) Creating the gray scale of an image by averaging the amounts of red, green, and blue in each pixel and assigning this new value to the corresponding pixel in the new image. The new value of each pixel represents a shade of gray, ranging from white to black.

(C) Creating the negative of an image by creating a new RGB triplet for each pixel in which each value is calculated by subtracting the original value from 255. The negative of an image is reversed from the original; light areas appear dark, and colors are reversed.

(D) Modifying part of the image by taking the pixels in one part of the picture and copying them to the pixels in another part of the picture.

**My answer**: B

**Correct answer**: C

The correct answer is C because if a negative of the original image is made, each RGB triplet value will be computed by subtracting the original value from 255. The original value can then be restored by subtracting the new value from 255. This process is lossless because the exact original can be restored.

### Q28:

A video-streaming Web site uses 32-bit integers to count the number of times each video has been played. In anticipation of some videos being played more times than can be represented with 32 bits, the Web site is planning to change to 64-bit integers for the counter. Which of the following best describes the result of using 64-bit integers instead of 32-bit integers?

(A) 2 times as many values can be represented.

(B) 32 times as many values can be represented.

(C) 232 times as many values can be represented.

(D) 322 times as many values can be represented.

**My answer**: B

**Correct answer**: C

The correct answer is C because when you go from 32 bits to 64 bits you are increacing by a factor of 32, therefore 2^32 means 232 times as many values can be represented.

### Q29:

An online store uses 6-bit binary sequences to identify each unique item for sale. The store plans to increase the number of items it sells and is considering using 7-bit binary sequences. Which of the following best describes the result of using 7-bit sequences instead of 6-bit sequences?

(A) 2 more items can be uniquely identified.

(B) 10 more items can be uniquely identified.

(C) 2 times as many items can be uniquely identified.

(D) 10 times as many items can be uniquely identified.

**My answer**: B

**Correct answer**: C

The correct answer is C because Using 6-bit binary sequences allows for 26 or 64 different items to be identified. Using 7-bit binary sequences allows for 27 or 128 different items to be identified. Thus there are two times as many items that can be uniquely identified.

### Q30:

Each student that enrolls at a school is assigned a unique ID number, which is stored as a binary number. The ID numbers increase sequentially by 1 with each newly enrolled student. If the ID number assigned to the last student who enrolled was the binary number 1001 0011, what binary number will be assigned to the next student who enrolls?

(A) 1001 0100

(B) 1001 0111

(C) 1101 0100

(D) 1101 0111

**My answer**: C

**Correct answer**: A

The correct answer is A because when you add one, you need to shift every bit over by 1, 1001 0100 is the correct answer.

### Q36:

For which of the following situations would it be best to use a heuristic in order to find a solution that runs in a reasonable amount of time?

(A) Appending a value to a list of n elements, which requires no list elements be examined.

(B) Finding the fastest route that visits every location among n locations, which requires n! possible routes be examined.

(C) Performing a binary search for a score in a sorted list of n scores, which requires that fewer than n scores be examined.

(D) Performing a linear search for a name in an unsorted database of n people, which requires that up to n entries be examined.

**My answer**: D

**Correct answer**: B

The correct answer is B because if an algorithm has a factorial efficiency, it does not run in a reasonable amount of time. A heuristic approach can be used to find an approximate solution than can run in a reasonable amount of time.

### Q37:

A graphic artist uses a program to draw geometric shapes in a given pattern. The program uses an algorithm that draws the shapes based on input from the artist. The table shows the approximate number of steps the algorithm takes to draw different numbers of shapes.

| Number of Shapes Drawn | Number of Steps |
|:----------------------:|:---------------:|
| 4	| 17 |
| 5 | 24 |
| 6 | 35 |
| 7 | 50 |

Based on the values in the table, which of the following best characterizes the algorithm for drawing n shapes, where n is a very large number?

(A) The algorithm runs in a reasonable amount of time because it will use approximately n steps to draw n shapes.

(B) The algorithm runs in a reasonable amount of time because it will use approximately n2 steps to draw n shapes.

(C) The algorithm runs in an unreasonable amount of time because it will use approximately n steps to draw n shapes.

(D) The algorithm runs in an unreasonable amount of time because it will use approximately n2 steps to draw n shapes.

**My answer**: A

**Correct answer**: B

The correct answer is B because as n increases, the number of steps is approximately equal to n2, which would make the algorithm polynomial. An algorithm with an efficiency that approximates n2 is said to run in a reasonable amount of time.

### Q41:

A student is writing a program that is intended to replace each negative value in a particular column of a spreadsheet with the value 0. Which of the following procedures is most likely to be useful in the student’s program?

(A) A procedure containsNegatives, which returns true if any negative values appear in the column and returns false otherwise.

(B) A procedure countNegatives, which returns the number of negative values that appear in the column.

(C) A procedure findNegative, which returns the row number of the first negative value that appears in the column or -1 if there are no negative values.

(D) A procedure minimum, which returns the minimum value that appears in the column.

**My answer**: A

**Correct answer**: C

The correct answer is C because using this procedure would allow the student to identify the location where a negative value occurs, and then change that value to 0. This process can continue with repeated calls to the procedure until there are no more negative values.

### Q49:

A teacher stores the most recent quiz scores for her class in the list scores. The first element in the list holds the maximum possible number of points that can be awarded on the quiz, and each remaining element holds one student’s quiz score. Assume that scores contains at least two elements. Which of the following code segments will set the variable found to true if at least one student scored the maximum possible number of points on the quiz and will set found to false otherwise?

(A)

(B)

(C)

(D)

**My answer**: A

**Correct answer**: C

The correct answer is C because the code segment traverses the list beginning with the second element, so it is correctly comparing only student scores to the maximum possible score, which is found by accessing scores[1]. The variable found will only be set to true when a student’s score equals the maximum possible score. The code also sets the number of iterations to LENGTH(scores) - 1 to reflect that the first list element (maximum score) is skipped.