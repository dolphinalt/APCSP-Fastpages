---
toc: true
layout: post
description: Scoring 4 APCSP performance task submissions
categories: [markdown]
title: APCSP rubric scoring
---
## Scoring:

### **Submission 1**

| Reporting Category | My Score | Reasoning | College Board Scoring |
| --- | --- | --- | --- |
| Program Purpose and Function | 1 | The student has a clear purpose for the function of the program (meets all 6 requirements) | 1 |
| Data Abstraction | 0 | The student has a code segment which uses data abstraction but does not meet all 3 requriements (data is not accessed). | 0 |
| Managing Complexity | 0 | The list doesn't manage compelxity, but provides an example for how the program would be different without the lists. (does not meet all 2 requirements) | 0 |
| Procedural Abstraction | 0 | The list is used within the procedure, however, it does not state a purpose as to how it contributes. (does not meet all 2 requirements) | 0 |
| Algorithm Implementation | 1 | The procedure includes an algorithm which gives an output given an input, as well as a detailed writeup for replication. (meets all 2 requirements) | 1 |
| Testing | 1 | The writeup clearly shows the user testing their program thuroughly. (meets all 3 requirements) | 1 |
| Total | 3 | Reasoning as shown above | 3 |

### **Submission 2**

| Reporting Category | My Score | Reasoning | College Board Scoring |
| --- | --- | --- | --- |
| Program Purpose and Function | 1 | The student has a clear purpose for the function of the program (meets all 6 requirements) | 1 |
| Data Abstraction | 1 | The student has a code segment which uses data abstraction (meets all 3 requirements) | 1 |
| Managing Complexity | 1 | The list manages compelxity, and provides an example for how the program would be different without the lists. (meets all 2 requirements) | 1 |
| Procedural Abstraction | 1 | The list is used within the procedure and states a purpose as to how it contributes. (meets all 2 requirements) | 1 |
| Algorithm Implementation | 1 | The procedure includes an algorithm which gives an output given an input, as well as a detailed writeup for replication. (meets all 2 requirements) | 1 |
| Testing | 1 | The writeup clearly shows the user testing their program thuroughly. (meets all 3 requirements) | 1 |
| Total | 6 | Reasoning as shown above | 6 |

### **Submission 3**

<table>
  <tr>
    <th>Row</th>
    <th>Score</th>
    <th>Explaintation</th>
    <th>Notes/Discrepancies</th>
  </tr>
  <tr>
    <td><strong>Program Function and Purpose</strong></td>
    <td>1/1</td>
    <td>The video response does a good job of showing the input, functionality, and output of the program, which had the user input a state and then select different pieces of information to display on the screen. Moreover, the written response also clear documented the purpose (function) of the program was to provide the user with information on a us state, and that the actual purpose was to help with memorization and to learn new things.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Data Abstraction</strong></td>
    <td>0/1</td>
    <td>The program and response does include the usage of a list, it's name (<code>statelist</code>), and the purpose it serves. However, it does not show how the data is stored within the list. As such, it does not earn the point for this row of the rubric.
    <td>Moreover, the description in the written response for the list was also inaccurate as the list statelist only represents the name of the states.</td>
  </tr>
  <tr>
    <td><strong>Managing Complexity</strong></td>
    <td>1/1</td>
    <td>The written response does an good job at stating how the usage of the list serves to reduce complexity. The student responds that without the usage of a list, they would likely have to code each peice of data independently from each other, resulting in greater code complexity. </td>
    <td>Collegeboard says that the written response does not go a good job of explaining in detail on how the operation would be more complex to store.</td>
  </tr>
  <tr>
    <td><strong>Procedural Abstraction</strong></td>
    <td>0/1</td>
    <td>Although the written reponse demonstrates the usage of a function <code>updatescreen</code> in order to assign an index to each state. This function does not contain any parameters that are passed to it. Thus the program does not earn the point in this row.</td>
    <td>Collegeboard decided that the written response also inaccurately described the main function of the procedure</td>
  </tr>
  <tr>
    <td><strong>Algorithm Implementation</strong></td>
    <td>0/1</td>
    <td>The algorithm indicates the proper use of many if statements to implement sequencing and selection. However, the program does not indicate the use of any form of a loop or anything similar to denote a use of iteration in the program.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Testing</strong></td>
    <td>1/1</td>
    <td>The written response shows the results and scenario of the both proceudres to identify that their program works as expected according to the set purpose and function</td>
    <td>The written reponse does not properly show different parameters that are plugged into the procedures. Additionally, it does not describe the result in detail, instead, it only gives a breif overview of what happens on screen instead.</td>
  </tr>
</table>

### **Submission 4**

<table>
  <tr>
    <th>Row</th>
    <th>Score</th>
    <th>Explaintation</th>
    <th>Notes/Discrepancies</th>
  </tr>
  <tr>
    <td><strong>Program Function and Purpose</strong></td>
    <td>1/1</td>
    <td>The video response does a good job of showing the input and output of the program, which was to use certain keyboard keys such as a and d to move the boat, and eventually add to a total count of fish if the hook comes into contact with a fish. THe function and purpose were also stated explicity, with the purpose being to reduce boredom, and the function being to simulate a fishing game.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Data Abstraction</strong></td>
    <td>1/1</td>
    <td>The program and response does include the usage of a list, it's name (<code>fishtypes</code>), and the purpose it serves. The list is in the form of an array that stores the total amount of fish caught by the user. Later, the list is also shown to be used to output the total number of fish of each type caught.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Managing Complexity</strong></td>
    <td>1/1</td>
    <td>The written response does an good job at stating how the usage of the list serves to reduce complexity. The student responds that without the usage of a list, they would likely have to resort to the use of individual variables to store each fish and the number of that fish caught, which would not only be cumbersome and produce clutter, but would also be hard to add new fish types in the future. The student also address and refutes the possibility of using individual variables for each type of fish and it's total.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Procedural Abstraction</strong></td>
    <td>1/1</td>
    <td>The written reponse demonstrates usage of a function <code>clone movement</code> in order to determine the spawning of the fishes including their location, distance, and final position. This function consists of 5 arguments serving to define the range and speed of the fish. The student also explains how this specific helps the functionality of the program as a whole, as it serves to randomly spawn fishes with different attributes to increase the difficulty of the game.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Algorithm Implementation</strong></td>
    <td>1/1</td>
    <td>The algorithm indicates the proper use of a loop to implement iteration to move the fish clone until it eithe reaches the end of the screen, or is touched by the hook. Sequencing could also be observed in the function as it creates a clone of a fish first before executing the loop and it's following logic. Moreover, the algorithm also uses an if statement to implement selection in the code to determine whether of not if the clone is touching the edge of the screen.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Testing</strong></td>
    <td>1/1</td>
    <td>The written response clearly shows the inputting of two different inputs, one where the clone is touching the right edge of the screen, and another one where it doesn't. Moreover, the response clearly details the results of each procedure. The end results of the program are also the expected results.</td>
    <td>According to collegeboard, this student did not earn the point for this row because they only tested for the alternate code segments, rather than actual arguments, parameters, and inputs into the function itself.</td>
  </tr>
</table>




## Reflection:

### **on any discrepancies in your scoring versus the ap scoring**
I was consistantly grading much more leinently than college board did, might be because I am still not very familiar for every single one of the requirements to be met.

### **on what your program will need to fulfill all requirements**
On my program, I need to make sure that I have detailed testing in order to fulfill all requirements for the performance task.

### **on the criteria and why a submission may have failed to meet the standard**
The submissions that failed to meet the standerds failed due to them not being able to meet every single sub-requirement, while I was not checking each sub-requirement in very much detail.
