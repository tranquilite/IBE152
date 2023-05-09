# IBE152 Deleksamen 2
Oppgaver fra Deleksamen 2 i HiMoldes IBE152 for vårsemesteret 2023.
Med forbehold om skrivefeil.


## Question 1
Write a function that recives a text *text* and an integer *size*, searches for the first occurrence of a word with size *size*, and *returns the word found or the empty string* if there is none.
The words are separated by spaces and punctuation marks (only dots, parenthesis and commas are present).
Spaces and punctuation marks are not part of a word.

### Sample parameters
*text* = "The Python String split() method splits all words in a string separated by a specified separator. This separator is a delimiter string, and can be a comma, full stop, space character or any other character used to separare strings. Usually, if multiple separators are grouped together, the method treats it as an empty string. But if the separator is not specified or is None, and the string consists for consecutive whitespaces, they are regarded as a single separator, and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace. Consequently, splitting an empty string or a string consisting of just whitespace with a None separator results in an empty string."

| Sample parameters | Sample return   |
|-------------------|-----------------|
| text, 30          | ""              |
| text, 7           | "strings"       |

## Question 2
A school uses a dictionary to keep track of its courses. Each key is the name of a course and the value is a list with the name of the students of the course. No student is enrolled in more than once course.

Write a function that gets a dictionary as a parameter representing the courses and returns a tuple with the name of all female students in the school. All students whose name ends in 'a' are female (In Spanish that is often the case.) All the names end in lowercase.

__Example:__

courses = {
    'IBE152': ['Juan', 'Ana', 'Claudia'],
    'IBE500': ['Pedro', 'Linda', 'Maria'],
    'HIST01': ['David', 'Laura']
}

__Returns:__
('Ana', 'Claudia', 'Linda', 'Maria', 'Laura')


## Question 3
Write a function that recives a list *cities* with the name of the cities that an airline flights from, a list of lists *direct_flights* that indicates which cities are connected by direct flights, and the name of a *city*, and returns a list with the name of the cities connected by direct flights (in either direction) to the city.

Each list in *direct_flights* correspond to a city in list *cities*, and contains 1's and 0's. Each element in *direct_flights[i][j]* with value 1 indicates that tehre is a direct flight from the city at index i in the *cities* list to the city at index *j* in the *cities* list.

### Sample parameters
* cities = ['Seattle', 'Denver' 'New York', 'Chicago']

| direct_flights                                           | city       | Sample return           |
|----------------------------------------------------------|------------|-------------------------|
| [1, 0, 1, 1], [0, 1, 1, 0], [1, 1, 1, 1], [0, 0, 1, 1] ] | 'Seattle'  | ['New York', 'Chicago'] |
| [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1] ] | 'Chicago'  | []                      |


## Question 4
Write a function that takes two lists of integers as input and returns a dictionary that maps each integer present in both lists to a tuple containing *the last index* where the number appears in each of the lists.
__Using break or continue is forbidden in this question__

Header:
def find_last_common(list1: list[int], list2: list[int]) -> dict[int, tuple[int, int]]


### Sample parameteres
| list1              | list2        | Sample return                     |
|--------------------|--------------|-----------------------------------|
| [1, 0, 3, 4, 5, 3] | [3, 4, 5]    | {3: (5, 0), 4: (3, 1), 5: (4, 2)} |
| [1, 0, 3, 4, 5]    | [30, 40, 50] | {}