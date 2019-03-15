# Ganga-Exercise
The basic usage of Ganga 6. Of how to run jobs, subjobs, and merging. And an exercise regarding memory management using Python.

__What is done__
1. Installing Ganga
2. Running a “Hello World” job that executes on a “Local” backend.
3. A job was created in Ganga that demonstrates splitting a job into multiple pieces and then collates
the results at the end.
    1. A file 'CERN.pdf' was split into individual pages using python.
    2. A Ganga job was created to count the number of occurences of the word “the” in the text of the PDF file 'CERN.pdf'.
    3. Using the ArgSplitter subjobs were created that will each count the occurences for a single page.
    4. Then a merger(CustomMerger) was created to add up the number extracted from each page and the total number was placed into one file.

## Installing Ganga
The code below was executed to install ganga on a virtualenv.
1. 
