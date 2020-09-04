# Ganga-Documentation
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
4. Memory Management Exercise.
    

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

Then you can use the `j.peek('stdout')` to check the output. Which is will show "Hello World".

## Creating a job in Ganga that demonstrates splitting a job into multiple pieces and then collates the results at the end.
### Splitting 'CERN.pdf' into individual pages using python.

The file 'fileSplit.py' was used to split the file 'CERN.pdf'. It was split into 12 parts since 'CERN.pdf' has 12 pages.

### Counting the number of occurences of the word “the” in the text of the PDF file 'CERN.pdf'

A job was created and the python script 'count.py' to count the number of the occurances of the word "the" was attached to the job. 
So that the job will execute the python scipt when it gets submitted.
The following lines were executed.

```
j=Job()
j.application.exe='/home/dark/GSoC/Ganga/gangaenv/bin/pyFiles/count.py'
j.application.args='/home/dark/GSoC/Ganga/gangaenv/bin/pyFiles/CERN.pdf'
j.outputfiles = [LocalFile('ans.txt')]
j.submit()
```
Then the number of the occurences can be seen by using `j.peek('ans.txt')`.

### Counting the occurences of each individual file as subjobs using ArgSplitter.
The following lines were executed to get the occurences of each file by creating subjobs and getting an output file for each subjob.

```
j=Job()
j.application.exe='/home/dark/GSoC/Ganga/gangaenv/bin/pyFiles/count.py'
args=[["/home/dark/GSoC/Ganga/gangaenv/bin/pyFiles/document-page0.pdf"],["/home/dark/GSoC/Ganga/gangaenv/bin/pyFiles/document-page1.pdf"],["/home/dark/GSoC/Ganga/gangaenv/bin/pyFiles/document-page2.pdf"],["/home/dark/GSoC/Ganga/gangaenv/bin/pyFiles/document-page3.pdf"],["/home/dark/GSoC/Ganga/gangaenv/bin/pyFiles/document-page4.pdf"],["/home/dark/GSoC/Ganga/gangaenv/bin/pyFiles/document-page5.pdf"],["/home/dark/GSoC/Ganga/gangaenv/bin/pyFiles/document-page6.pdf"],["/home/dark/GSoC/Ganga/gangaenv/bin/pyFiles/document-page7.pdf"],["/home/dark/GSoC/Ganga/gangaenv/bin/pyFiles/document-page8.pdf"],["/home/dark/GSoC/Ganga/gangaenv/bin/pyFiles/document-page9.pdf"],["/home/dark/GSoC/Ganga/gangaenv/bin/pyFiles/document-page10.pdf"],["/home/dark/GSoC/Ganga/gangaenv/bin/pyFiles/document-page11.pdf"]]
splitter=ArgSplitter(args=args)
j.splitter=splitter
j.outputfiles = [LocalFile('ans.txt')]
j.submit()
```
Then all the occurences will have being calculated for each subjob. To check each output we can use the code `j.subjobs(0).peek('ans.txt')`,`j.subjobs(1).peek('ans.txt')` and so on..

### Adding up the total number of occurences using CustomMerger
First a merger.py should be created. The the following code was executed just before the `j.submit()` line. 
`j.postprocessors=CustomMerger(files=['ans.txt'],module=File('/home/dark/GSoC/Ganga/gangaenv/bin/pyFiles/mymerger.py'))`
Then it will merge all the number of occurences into one output file. Then the code `j.peek('ans.txt')` can be used to check the final value.
The job done above is jobs(25). The folder '25' is uploaded here. The  output files can be seen above.

## Memory Management Exercise

1. A simple python programme that creates a configurable number of simple objects where each is a deep copy of the previous one was created. The objects were created in a delay loop.
2. Then the memory usage of the programme was monitored by using Pympler , `pympler.asizeof()`. The increase in memory was observed. Deepcopy creates a complete new copy of another object. So if the value of the copied object is changed the previous object doesn't get changed.
3. Then the references to the objects were released and the memory was monitored. The decrease in allocated memory was observed.
4. The same was implemented using Shallow Copy. Shallow Copy creates a reference to the same object. It doesn't create a new copy of the object.
5. A simple `copyOnModify()` method was made the memory efficient. So at first the shallow copies will exist. But if a copy is to be modified then that copy is changed to a deepcopy and then modified. So memory is saved. 

All the above functions can be observed by the python script 'memoryTest.py'

