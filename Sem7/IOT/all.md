This response extracts the code snippets found within the source material covering Topic 6.2 ("Installing Python") up to Topic 6.11 ("Python Packages of Interest for IoT") in Chapter 6: "IoT Systems - Logical Design using Python".

---

### 6.2 Installing Python

**Box 6.1: Installing Python on Ubuntu Linux**

```bash
#Install Dependencies
sudo apt-get install build-essential
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev \
libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

#Download Python
wget http://python.org/ftp/python/2.7.5/Python-2.7.5.tgz
tar -xvf Python-2.7.5.tgz
cd Python-2.7.5

#Install Python
./configure
make
sudo make install
```

### 6.3 Python Data Types & Data Structures

#### 6.3.1 Numbers

**Box 6.2: Working with Numbers in Python**

```python
#Integer
>>>a=5
>>>type(a)
<type 'int'>

#Floating Point
>>>b=2.5
>>>type(b)
<type 'float'>

#Long
>>>c=9898787676L
>>>type(c)
<type 'long'>

#Complex
>>>y=2+5j
>>>y
(2+5j)
>>>type(y)
<type 'complex'>
>>>y.real
2.0
>>>y.imag
5.0

#Addition
>>>c=a+b
>>>c
7.5
>>>type(c)
<type 'float'>

#Subtraction
>>>d=a-b
>>>d
2.5
>>>type(d)
<type 'float'>

#Multiplication
>>>e=a*b
>>>e
12.5
>>>type(e)
<type 'float'>

#Division
>>>f=b/a
>>>f
0.5
>>>type(f)
<type 'float'>

#Power
>>>g=a**2
>>>g
25
```

#### 6.3.2 Strings

**Box 6.3: Working with Strings in Python**

```python
#Create string
>>>s="Hello World!"
>>>type(s)
<type 'str'>

#String concatenation
>>>t="This is " + "sample program."
>>>t
'This is sample program.'

#Get length of string
>>>len(s)
12

#Convert string to integer
>>>x="100"
>>>type(x)
<type 'str'>
>>>y=int(x)
>>>y
100

#Print string
>>>print s
Hello World!

#Formatting output
>>>print "The string (%s) has %d characters" % (s,len(s))
The string (Hello World!) has 12 characters

#Convert to upper/lower case
>>>s.upper()
'HELLO WORLD!'
>>>s.lower()
'hello world!'

#Accessing sub-strings
>>>s
'H'
>>>s[6:]
'World!'
>>>s[:6]
'Hello '
>>>s[:-1]
'World'

#strip: Returns a copy of the string with 
#the leading and trailing characters removed.
>>>s.strip('!*')
'Hello World'
```

#### 6.3.3 Lists

**Box 6.4: Working with Lists in Python**

```python
>>>fruits=["apple", 'orange', 'banana', 'mango']
>>>type(fruits)
<type 'list'>
>>>len(fruits)
4
>>>fruits
'orange'
>>>fruits[1:3]
['orange', 'banana']
>>>fruits[1:]
['orange', 'banana', 'mango']

#Appending an item to a list
>>>fruits.append('pear')
>>>fruits
['apple', 'orange', 'banana', 'mango', 'pear']

#Removing an item from a list
>>>fruits.remove('mango')
>>>fruits
['apple', 'orange', 'banana', 'pear']

#Inserting an item to a list
>>>fruits.insert(1, 'mango')
>>>fruits
['apple', 'mango', 'orange', 'banana', 'pear']

#Combining lists
>>>vegetables=['potato', 'carrot', 'onion', 'beans', 'radish']
>>>vegetables
['potato', 'carrot', 'onion', 'beans', 'radish']
>>>eatables=fruits+vegetables
>>>eatables
['apple', 'mango', 'orange', 'banana', 'pear', 'potato', 'carrot', 'onion', 'beans', 'radish']

#Mixed data types in a list
>>>mixed=['data', 5,100.1,8287398L]
>>>type(mixed)
<type 'list'>
>>>type(mixed)
<type 'str'>
>>>type(mixed)
<type 'int'>
>>>type(mixed)
<type 'float'>
>>>type(mixed)
<type 'long'>

#It is possible to change individual elements of a list
>>>mixed=mixed 'items'
>>>mixed=0.05
>>>mixed=mixed+0.05
>>>mixed
['data items', 6, 100.14999999999999, 8287398L]

#Lists can be nested
>>>nested=[fruits, vegetables]
>>>nested
[['apple', 'mango', 'orange', 'banana', 'pear'], ['potato', 'carrot', 'onion', 'beans', 'radish']]
```

#### 6.3.4 Tuples

**Box 6.5: Working with Tuples in Python**

```python
>>>fruits=("apple", 'mango', "banana", "pineapple")
>>>type(fruits)
<type 'tuple'>

#Get length of tuple
>>>len(fruits)
4

#Get an element from a tuple
>>>fruits
'apple'
>>>fruits[2:]
('banana', 'pineapple')

#Combining tuples
>>>vegetables=('potato', 'carrot', 'onion', 'radish')
>>>eatables=fruits+vegetables
>>>eatables
('apple', 'mango', 'banana', 'pineapple', 'potato', 'carrot', 'onion', 'radish')
```

#### 6.3.5 Dictionaries

**Box 6.6: Working with Dictionaries in Python**

```python
>>>student={'name':'Mary', 'id':'8776', 'major':'CS'}
>>>student
{'major': 'CS', 'name': 'Mary', 'id': '8776'}
>>>type(student)
<type 'dict'>

#Get length of a dictionary
>>>len(student)
3

#Get the value of a key in dictionary
>>>student['name']
'Mary'

#Get all items in a dictionary
>>>student.items()
[('major', 'CS'), ('name', 'Mary'), ('id', '8776')]

#Get all keys in a dictionary
>>>student.keys()
['major', 'name', 'id']

#Get all values in a dictionary
>>>student.values()
['CS', 'Mary', '8776']

#Add a value in a dictionary can be another dictionary
>>>student1={'name':'David','id':'9876','major':'ECE'}
>>>students={'1': student, '2':student1}
>>>students
{'1': {'major': 'CS', 'name': 'Mary', 'id': '8776'}, '2': {'major': 'ECE', 'name': 'David', 'id': '9876'}}

#Check if dictionary has a key
>>>student.has_key('name')
True
>>>student.has_key('grade')
False
```

#### 6.3.6 Type Conversions

**Box 6.7: Type conversion examples**

```python
#Convert to string
>>>a=10000
>>>str(a)
'10000'

#Convert to int
>>>b="2013"
>>>int(b)
2013

#Convert to float
>>>float(b)
2013.0

#Convert to long
>>>long(b)
2013L

#Convert to list
>>>s="aeiou"
>>>list(s)
['a', 'e', 'i', 'o', 'u']

#Convert to set
>>>x=['mango','apple','banana','mango','apple','banana']
>>>set(x)
set(['mango', 'apple', 'banana'])

#Convert to tuple
>>>tuple(x)
('mango', 'apple', 'banana', 'mango', 'apple', 'banana')
```

### 6.4 Control Flow

#### 6.4.1 if

**Box 6.8: if statement examples**

```python
>>>a = 25*5
>>>if a > 10000:
... print "More"
... else:
... print "Less"
... 
Less

>>>if a < 1000000:
... print "Between 10K and 100K"
... elif a==10000:
... print "More than 10K"
... elif a==1000:
... print "Equal to 10K"
... else:
... print "Less than 10K"
...
More than 100K

>>>s="Hello World"
>>>if "World" in s:
... print s
... 
Hello World!

>>>student={'name':'Mary', 'id':'8776', 'major':'CS'}
>>>if not student.has_key('major'):
... print "no major"
... else:
... print student['major']
...
CS
```

#### 6.4.2 for

**Box 6.9: for statement examples**

```python
helloString = "Hello World"
fruits = ['apple', 'orange', 'banana', 'mango']
student = {'name': 'Mary', 'id': '8776', 'major': 'CS'}

#Looping over characters in a string
for c in helloString:
  print c
  
#Looping over items in a list
i=0
for item in fruits:
  print "Fruit-%d: %s" % (i,item)
  i=i+1
  
#Looping over keys in a dictionary
for key in student:
  print "Key: %s %s" % (key, student[key])
```

#### 6.4.3 while

**Box 6.10: while statement examples**

```python
#Prints even numbers upto 100
>>>i=0
>>>while i<=100:
... if i%2 == 0:
... print i
... i=i+1
... 
0
2
4
...
98
100
```

#### 6.4.4 range

**Box 6.11: range examples**

```python
#Generate a list of numbers from 0 - 9
>>>range(10)


#Generate a list of numbers from 10 - 100 with increments of 10
>>>range(10,110,10)

```

#### 6.4.5 break/continue

**Box 6.12: break/continue examples**

```python
#break statement example
>>>for x in range(4,256,4):
... y = 1 + x
... if y > 512:
... break
... print y
... 
4
32
384

#continue statement example
>>>fruits=['apple','orange','banana','mango']
>>>for item in fruits:
... if item == "banana":
... continue
... else:
... print item
...
apple
orange
mango
```

#### 6.4.6 pass

**Box 6.13: pass statement example**

```python
fruits=['apple','orange','banana','mango']
for item in fruits:
  if item == "banana":
    pass
  else:
    print item
    
apple
orange
mango
```

### 6.5 Functions

**Box 6.14: Example of a function in Python**

```python
students = {'1': {'name': 'Bob', 'grade': 2.5}, 
            '2': {'name': 'Mary', 'grade': 3.5}, 
            '3': {'name': 'David', 'grade': 4.2}, 
            '4': {'name': 'John', 'grade': 4.1}, 
            '5': {'name': 'Alex', 'grade': 3.8}}

def averageGrade(students):
    "This function computes the average grade"
    sum = 0.0
    for key in students:
        sum = sum + students[key]['grade']
    average = sum/len(students)
    return average

avg = averageGrade(students)
print "The average garde is: %.2f" % (avg)
```

**Box 6.15: Example of function with default arguments**

```python
>>>def displayFruits(fruits=['apple','orange']):
... print "There are %d fruits in the list" % (len(fruits))
... for item in fruits:
... print item
...
#Using default arguments
>>>displayFruits()
There are 2 fruits in the list
apple
orange

>>>fruits = ['banana', 'pear', 'mango']
>>>displayFruits(fruits)
There are 3 fruits in the list
banana
pear
mango
```

**Box 6.16: Example of parameter passing by reference**

```python
>>>def displayFruits(fruits):
... print "There are %d fruits in the list" % (len(fruits))
... for item in fruits:
... print item
... print "Adding one more fruit"
... fruits.append('mango')
... 
>>>fruits = ['banana', 'pear', 'apple']
>>>displayFruits(fruits)
There are 3 fruits in the list
banana
pear
apple
Adding one more fruit

>>>fruits
['banana', 'pear', 'apple', 'mango']
>>>displayFruits(fruits)
There are 4 fruits in the list
banana
pear
apple
mango
Adding one more fruit
```

**Box 6.17: Examples of keyword arguments**

```python
>>>def printStudentRecords(name, age=20, major='CS'):
... print "Name: " + name
... print "Age: " + str(age)
... print "Major: " + major
... 

#This will give error as name is required argument
>>>printStudentRecords()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: printStudentRecords() takes at least 1 argument (0 given)

>>>printStudentRecords(name='Alex')
Name: Alex
Age: 20
Major: CS

>>>printStudentRecords(name='Bob', age=22, major='ECE')
Name: Bob
Age: 22
Major: ECE

>>>printStudentRecords(name='Alan', major='ECE')
Name: Alan
Age: 20
Major: ECE

#name is a formal argument.
#**kwargs accepts the formal argument as a dictionary.
>>>def student (name, **kwargs):
... print "Student Name: " + name
... for key in kwargs:
... print key + ': ' + kwargs[key]
...

>>>student(name='Bob', age='20', major = 'CS')
Student Name: Bob
Age: 20
Major: CS
```

**Box 6.18: Example of variable length arguments**

```python
def student (name, *varargs):
  print "Student Name: " + name
  for item in varargs:
    print item
    
>>>student('Nav')
Student Name: Nav

>>>student('Amy', 'Age: 24')
Student Name: Amy
Age: 24

>>>student('Bob', 'Age: 20', 'Major: CS')
Student Name: Bob
Age: 20
Major: CS
```

### 6.6 Modules

**Box 6.19: Module student**

```python
def averageGrade(students):
  sum = 0.0
  for key in students:
    sum = sum + students[key]['grade']
  average = sum/len(students)
  return average

def printRecords(students):
  print "There are %d students" % (len(students))
  i=1
  for key in students:
    print "Student-%d:" % i
    print "Name: %s" % students[key]['name']
    print "Grade: %s" % str(students[key]['grade'])
    i=i+1
```

**Box 6.20: Using module student**

```python
>>>import student

>>>students = {'1': {'name': 'Bob', 'grade': 2.5}, 
            '2': {'name': 'Mary', 'grade': 3.5}, 
            '3': {'name': 'David', 'grade': 4.2}, 
            '4': {'name': 'John', 'grade': 4.1}, 
            '5': {'name': 'Alex', 'grade': 3.8}}

>>>student.printRecords(students)
There are 5 students
Student-1:
Name: Bob
Grade: 2.5
Student-2:
Name: Mary
Grade: 3.5
Student-3:
Name: David
Grade: 4.2
Student-4:
Name: John
Grade: 4.1
Student-5:
Name: Alex
Grade: 3.8

>>>avg= student.averageGrade(students)
>>>print "THe average garde is: %.2f" % (avg)
3.62
```

**Box 6.21: Importing a specific function from a module**

```python
>>>from student import averageGrade

>>>students = {'1': {'name': 'Bob', 'grade': 2.5}, 
            '3': {'name': 'Mary', 'grade': 3.5}, 
            '4': {'name': 'David', 'grade': 4.2}, 
            '5': {'name': 'John', 'grade': 4.1}, 
            '6': {'name': 'Alex', 'grade': 3.8}}

>>>avg= averageGrade(students)
>>>print "The average garde is: %.2f" % (avg)
3.62
```

**Box 6.22: Listing all names defined in a module**

```python
>>>import email
>>>dir(email)
['Charset', 'Encoders', 'Errors', 'FeedParser', 'Generator', 'Header', 'Iterators', 'LazyImporter', 'MIMEAudio', 'MIMEBase', 'MIMEImage', 'MIMEMessage', 'MIMEMultipart', 'MIMENonMultipart', 'MIMEText', 'Message', 'Parser', 'Utils', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '__path__', '__version__', '_name_', 'base64mime', 'email', 'import', 'message_from_file', 'message_from_string', 'mime', 'quopriMIME', 'sys']
```

### 6.7 Packages

**Box 6.23: skimage package listing**

```
skimage/
__init__.py
color/
__init__.py
colorconv.py
colorlabel.py
rgb_colors.py
draw/
__init__.py
draw.py
setup.py
exposure/
__init__.py
adjust.py
exposure.py
feature/
__init__.py
brief.py
daisy.py
...
```

### 6.8 File Handling

**Box 6.24: Example of reading an entire file**

```python
>>>fp = open('file.txt','r')
>>>content = fp.read()
>>>print content
Python supports more than one programming paradigms 
including object-oriented programming and structured 
programming
Python is an interpreted language and does 
not require an explicit compilation 
step.
>>>fp.close()
```

**Box 6.25: Example of reading line by line**

```python
>>>fp.close()
>>>fp = open('file.txt','r')
>>>print "Line-1: " + fp.readline()
Line-1: Python supports more than one programming paradigms 
including object-oriented programming and structured 
programming
>>>print "Line-2: " + fp.readline()
Line-2: Python is an interpreted language and does not 
require an explicit compilation step.
>>>fp.close()
```

**Box 6.26: Example of reading lines in a loop**

```python
>>>fp = open('file.txt','r')
>>>lines = fp.readlines()
>>>for line in lines:
... print line
...
Python supports more than one programming paradigms including 
object-oriented programming and structured programming
```

**Box 6.27: Example of reading a certain number of bytes**

```python
>>>fp = open('file.txt','r')
>>>fp.read(10)
'Python sup'
>>>fp.close()
```

**Box 6.28: Example of getting the current position of read**

```python
>>>fp = open('file.txt','r')
>>>fp.read(10)
'Python sup'
>>>currentpos = fp.tell()
>>>print currentpos
10
>>>print currentpos
<built-in method tell of file object at 0x0000000002391390>
>>>fp.close()
```

**Box 6.29: Example of seeking to a certain position in a file**

```python
>>>fp = open('file.txt','r')
>>>fp.seek(10,0)
10
>>>content = fp.read(10)
>>>print content
ports more
>>>fp.close()
```

**Box 6.30: Example of writing to a file**

```python
>>>fo = open('file1.txt','w')
>>>content="This is an example of writing to a file in Python."
>>>fo.write(content)
49
>>>fo.close()
```

### 6.9 Date/Time Operations

**Box 6.31: Examples of manipulating with date**

```python
>>>from datetime import date
>>>now = date.today()
>>>print "Date: " + now.strftime("%m-%d-%y")
Date: 07-24-13
>>>print "Day of Week: " + now.strftime("%A")
Day of Week: Wednesday
>>>print "Month: " + now.strftime("%B")
Month: July

>>>then = date(2013, 6, 7)
>>>timediff = now - then
>>>timediff.days
47
```

**Box 6.32: Examples of manipulating with time**

```python
>>>import time
>>>nowtime = time.time()
>>>time.localtime(nowtime)
time.struct_time(tm_year=2013, tm_mon=7, tm_mday=24, tm_hour=16, tm_min=14, tm_sec=51, tm_wday=2, tm_yday=205, tm_isdst=0)
>>>time.asctime(time.localtime(nowtime))
'Wed Jul 24 16:14:51 2013'

>>>time.strftime("The date is %d-%m-%y. \
Today is a %A. It is %H hours, %M minutes and %S seconds now.")
'The date is 24-07-13. Today is a Wednesday. It is 16 hours, 
15 minutes and 14 seconds now.'
```

### 6.10 Classes

**Box 6.33: Examples of a class**

```python
>>>class Student:
... studentCount = 0
... def __init__(self, name, id):
... print "Constructor called"
... self.name = name
... self.id = id
... Student.studentCount = Student.studentCount + 1
... self.grades={}
... 
... def __del__(self):
... print "Destructor called"
... 
... def getStudentCount(self):
... return Student.studentCount
... 
... def addGrade(self, key, value):
... self.grades[key]=value
... 
... def getGrade(self, key):
... return self.grades[key]
... 
... def printGrades(self):
... for key in self.grades:
... print key + ': ' + self.grades[key]
... 
>>>s = Student('Steve','98928')
Constructor called
>>>s.addGrade('Math','90')
>>>s.addGrade('Physics','85')
>>>s.printGrades()
Physics: 85
Math: 90
>>>mathgrade = s.getGrade('Math')
>>>print mathgrade
90
>>>count = s.getStudentCount()
>>>print count
1
>>>del s
Destructor called
```

**Box 6.34: Examples of class inheritance**

*(Note: The definition for the `Point` class is required for the code execution shown below, and appears across page 156)*:
```python
>>>class Point:
... def __init__(self, x, y):
... self.xCoordinate = x
... self.yCoordinate = y
... 
... def getXCoordinate(self,self,x):
... return self.xCoordinate
... def getYCoordinate(self,self,y):
... return self.yCoordinate
... 
... def setXCoordinate(self,self,x):
... self.xCoordinate = x
... def setYCoordinate(self,self,y):
... self.yCoordinate = y
... 
```

*(Continuation of Box 6.34)*:
```python
>>>class Shape:
... def __init__(self, color='Green'):
... print "Base class constructor"
... self.color = color
... self.lineWidth = 10.0
... def draw(self):
... print "Draw needs to be implemented"
... def getColor(self):
... return self.color
... def getLineWidth(self):
... return self.lineWidth
... def setColor(self, c):
... self.color = c
... def setLineWidth(self, lwt):
... self.lineWidth = lwt
... 
>>>class Circle(Shape):
... def __init__(self, c, r):
... print "Child class constructor"
... self.center = c
... self.radius = r
... self.color = 'Green'
... self.lineWidth = 10.0
... self.__label = 'Hidden circle label'
... def getCenter(self):
... return self.center
... def getRadius(self):
... return selfcirc.radius
7
>>>circ._label
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'Circle' instance has no attribute '_label'

>>>circ._Circle__label
'Hidden circle label'
```

### 6.11 Python Packages of Interest for IoT

#### 6.11.1 JSON

**Box 6.35: JSON Example - A Twitter tweet object**

```json
{
  "created_at":
  "Sat Oct 02 11:39:43 +0000 2013",
  "id":134073787059875841,
  "text":"What a bright and sunny day today!",
  "truncated":false,
  "in_reply_to_status_id":null,
  "user":{
    "id":203825039,
    "name":"Harry",
    "followers_count":316,
    "friends_count":29    "type":"Point",
    "coordinates":[75.78908449,26.92782727]
    },
  "place":null,
  "contributors":null,
  "retweet_count":0,
  "favorite_count":0,
  "entities":{
    "hashtags":[],
    "symbols":[],
    "urls":[],
    "user_mentions":[]
    },
  "favorited":false,
  "retweeted":false,
  "filter_level":"medium",
  "lang":"nl"
}
```

**Box 6.36: Encoding & Decoding JSON in Python**

```python
>>>import json

>>>message = {
  "created": "Wed Jun 31 2013",
  "id": "001",
  "text": "This is a test message.",
  }

>>>json.dumps(message)
'{"text": "This is a test message.", "id": "001", "created": "Wed Jun 31 2013"}'

>>>decodedMsg = json.loads('{"text": "This is a \
test message.", "id": "001", "created": "Wed Jun 31 2013"}')
>>>decodedMsg['id']
'001'
>>>decodedMsg['created']
'Wed Jun 31 2013'
>>>decodedMsg['text']
'This is a test message.'
```

#### 6.11.2 XML

**Box 6.37: XML example**

```xml
<?xml version="1.0"?>
<catalog>
  <plant id='1'>
    <common>Bloodroot</common>
    <botanical>Sanguinaria canadensis</botanical>
    <zone>4</zone>
    <light>Mostly Shady</light>
    <price>2.44</price>
    <availability>031599</availability>
  </plant>
  <plant id='2'>
    <common>Columbine</common>
    <botanical>Aquilegia canadensis</botanical>
    <zone>3</zone>
    <light>Mostly Shady</light>
    <price>3.98</price>
    <availability>030699</availability>
  </plant>
  <plant id='3'>
    <common>Marsh Marigold</common>
    <botanical>Caltha palustris</botanical>
    <zone>4</zone>
    <light>Mostly Sunny</light>
    <price>6.81</price>
    <availability>051799</availability>
  </plant>
</catalog>
```

**Box 6.38: Parsing an XML file in Python**

```python
from xml.dom.minidom import parse
dom = parse('test.xml')
for node in dom.getElementsByTagName('plant'):
  id=node.getAttribute('id')
  print "Plant ID:", id
  common = node.getElementsByTagName('common').childNodes.nodeValue
  print "Common:", common
  botanical=node.getElementsByTagName('botanical').childNodes.nodeValue
  print "Botanical:", botanical
  zone=node.getElementsByTagName('zone').childNodes.nodeValue
  print "Zone:", zone
```

**Box 6.39: Creating an XML file with Python**

```python
#Python example to create the following XML:
#<?xml version="1.0" ?> <Class> <Student> <Name>Alex</Name> <Major>ECE</Major> </Student> </Class>

from xml.dom.minidom import Document
doc = Document()

# create base element
base = doc.createElement('Class')
doc.appendChild(base)

# create an entry element
entry = doc.createElement('Student')
base.appendChild(entry)

# create an element and append to entry element
name = doc.createElement('Name')
nameContent = doc.createTextNode('Alex')
name.appendChild(nameContent)
entry.appendChild(name)

# create an element and append to entry element
major = doc.createElement('Major')
majorContent = doc.createTextNode('ECE')
major.appendChild(majorContent)
entry.appendChild(major)

fp = open('foo.xml','w')
doc.writexml( fp )
fp.close()
```

#### 6.11.3 HTTPLib & URLLib

**Box 6.40: HTTP GET request example using HTTPLib**

```python
>>>import httplib
>>>import urllib
>>> h = httplib.HTTP('http://example.com')
>>> h.request("GET", "http://example.com", "")
>>> resp, content = h.getresponse()
>>>resp
( 'status', '200'), ('content-length', '1270'), ('content-location', '
http://example.com/'), ('cache-control', 'HIT'), ('accept-ranges', 
'bytes'), ('server', 'ECS
(cpa/FB5B)'), ('last-modified', 'Thu, 23 Jan 2013 16:11:44 GMT'), ('etag', 
'"780602-4fe-4db31b2978ec0"', 'date', 'Wed, 31 Jul 2013 12:36:05 GMT', 
('content-type', 'text/html; charset=UTF-8')
)

>>>content
'<!doctype html> \n<html>\n<head>\n<title>Domain Example</title>\n
<meta charset="utf-8" />\n'
```

**Box 6.41: HTTP request example using URLLib2**

```python
>>>import urllib2
>>>import urllib

>>>req = urllib2.Request('http://example.com')
>>>response = urllib2.urlopen(req)
>>>resp_code= response.getcode()
>>>response_page
'<!doctype html>\n<html>\n<head>\n<title>Domain \
Example</title>\n<meta charset="utf-8" />\n'
```

**Box 6.42: HTTP POST example using HTTPLib2**

```python
>>>import httplib2
>>>import urllib

>>>h = httplib2.Http()
>>>data = '{"title": "Cloud computing"}'
>>>headers = {'Content-Type': 'text/plain'}
>>>resp, content = \
h.request("http://www.htmlcodetutorial.com/cgi-bin/mycgi.pl", "POST", \
urllib.urlencode(data))

>>>resp
( 'status', '200'), ('transfer-encoding', 'chunked'), 
('server', 'Apache/2.2.6 (Unix) mod_ssl/2.2.6 OpenSSL/0.9.7a \
mod_auth_passthrough/2.1 mod_bwlimited/1.4 FrontPage/5.0.2.2635 \
PHP/5.3.10'), ('connection', 'close'), ('date', 'Wed, 31 Jul 2013 \
12:41:20 GMT'), ('content-type', 'text/html; charset=ISO-8859-1')
)

>>>content
'<html>\n<head><title>iDoze Guide to \
HTML, My CGI</title></head>\n'
```

**Box 6.43: Example of sending data to a URL**

```python
>>>import urllib
>>>import urllib2

>>>url = 'http://www.htmlcodetutorial.com/cgi-bin/mycgi.pl'
>>>values = {'title': 'Cloud Computing',
            'language' : 'Python'}

>>>data = urllib.urlencode(values)
>>>req = urllib2.Request(url, data)
>>>response = urllib2.urlopen(req)
>>>the_page = response.read()
>>>the_page
'<HTML>\n<HEAD><TITLE>iDoze Guide to \
HTML, My CGI</TITLE></HEAD>\n'
```

#### 6.11.4 SMTPLib

**Box 6.44: Python example of sending email**

```python
import smtplib

from_email = '<enter-gmail-address>'
recipient_list = ['<enter-sender-email>']
cc_list = []
subject = 'Hello'
message = 'This is a test message.'

username = '<enter-gmail-username>'
password = '<enter-gmail-password>'
server = 'smtp.gmail.com:587'

def sendemail(from_addr, to_addr_list, cc_addr_list, 
              subject, message, 
              login, password,
              smtpserver):
    
    header = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n' % subject
    message = header + message
    
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    
    
#send email
sendemail(from_email, recipients_list, cc_list, subject, 
          message, username, password, server)


#The following code block, which appears lower on page 164, demonstrates direct server interaction:
header = 'From: %s\n' % from_addr
header += 'To: %s\n' % ','.join(to_addr_list)
header += 'Cc: %s\n' % ','.join(cc_addr_list)
header += 'Subject: %s\n' % subject
message = header + message

server = smtplib.SMTP(smtpserver)
server.starttls()
server.login(login, password)
problems = server.sendmail(from_addr, to_addr_list, message)
server.quit()
```