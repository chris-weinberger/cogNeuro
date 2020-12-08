# cogNeuro

This repo was created by Christopher Weinberger for computational neuroscience research directed by Dr. Chad Marsolek, at the University of Minnesota-Twin Cities.

The files contained in this repository can be broken down into code and data:
1) Code
generate_input_vectors.py
The code here is written to generate vectors. The nature of the vectors generated is as follows: the code will generate n vectors, each with n units. 
All the vectors are mutually orthogonal to each other with respect to the Pearson Correlation, and n-1 of the vectors have (n/2) units "on" and (n/2) units "off" (on = 1, off = 0).
For example, if n = 16, then generate_input_vectors.py will create 16 vectors total. 15 of these vectors will have 8 ones and 8 zeroes, and the last vector will be all ones. They 
will all be mutually orthogonal.

generate_abstract_pairs.py
creates a text file containing random pairs of numbers between 0 and n. For example, if n = 32, it will create a .txt file with the something like the following:
[(0, 22), (17, 6), (27, 21), (4, 8), (28, 7), (24, 32), (5, 2), (16, 12), (18, 30), (23, 11), (29, 26), (19, 13), (1, 31), (20, 3), (9, 10), (25, 14)]

generate_specific_exemplars.py
This code will open a file of n input vectors, and for each vector in the file, it will generate two new vectors. The new vectors will be exactly the same as the old vectors except that
two of the units in these vectors are "flipped" (ones become zeroes and vice versa), such that thes new vectors have a Pearson Correlation of 0.75. It will then save these 2n new vectors 
into a file called "specific exemplars.csv".

2) Data files
Most of these are self-explanatory, but to make things clear, I've used to following convention when naming things: If the name has the word "old" in it, it just refers to vectors that 
contain -1 instead of 0. These were previously used. "excel" and "csv" simply refer to the file type. 

