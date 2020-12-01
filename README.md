Lab4 PR: https://github.com/batoolmalkawii/madlib-cli/pull/1

This is MADLIB game, which includes three functions: 

* **read_template:** that takes in a path to text file and returns a stripped string of the file’s contents.

* **parse:** that takes in a template string and returns a string with language parts removed,
and a separate list of those language parts.

* **merge:** that takes in a “bare” template and a list of user entered language parts, 
and returns a string with the language parts inserted into the template.


***Note:*** the project includes User Acceptance Tests, with the following test cases: 

*read_template* test cases:

    "" -> ""

    "Hello there, this is Batool." -> "Hello there, this is Batool."

    "Hello there, this is {Name}, I am {Age} years old." -> "Hello there, this is {Name}, I am {Age} years old."


*parse* test cases:

    "" -> "", []
    
    "Hello there, this is Batool" -> "Hello there, this is Batool", []

    "Hello there, this is {Name}, I am {Age} years old." -> "Hello there, this is $, I am $ years old.", ["Name", "Age"]


*merge* test cases:

    Hello there, this is Batool" , [] -> "Hello there, this is Batool"
    
    "Hello there, this is $, I am $ years old", ["Batool", "24"] -> "Hello there, this is Batool, I am 24 years old"


