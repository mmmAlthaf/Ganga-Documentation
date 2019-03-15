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

The following was executed to install Ganga on a virutual env. 

```
virtualenv ./gangaenv
source ./gangaenv/bin/activate
pip install ganga
```
Then type `ganga` to run Ganga. 

## Running a “Hello World” job that executes on a “Local” backend.

To create a job this code was executed.

```
j=Job()
j.backend=Local()
j.submit()
```

Then you can use the `j.peek('stdout') to check the output. Which is will show "Hello World".

## Creating a job in Ganga that demonstrates splitting a job into multiple pieces and then collates the results at the end.
### Splitting 'CERN.pdf' into individual pages using python.

The file 'fileSplit.py' was used to split the file 'CERN.pdf'. It was split into 12 parts since 'CERN.pdf' has 12 pages.

### Counting the number of occurences of the word “the” in the text of the PDF file 'CERN.pdf'

First the text of 'CERN.pdf' was extracted and saved into a .txt file using a python script 'PDFtoTXT.py'.
Then a job was created and the python script 'count.py' to count the number of the occurances of the word "the" was attached to the job. 
So that the job will execute the python scipt when it gets submitted.
The following lines were executed.

```
j=Job()
j.application.exe='/home/dark/GSoC/Ganga/gangaenv/bin/pyFiles/count.py'
j.application.args='/home/dark/GSoC/Ganga/gangaenv/bin/pyFiles/CERN.txt'
j.outputfiles = [LocalFile('ans.txt')]
j.submit()
```
