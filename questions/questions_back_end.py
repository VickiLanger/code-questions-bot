'''
questions_back_end.py: back end questions for @CodeQBot
11 February 2020
Vicki Langer (@vicki_langer)
'''

# TODO: add more questions
# NOTE: please add the question, then comment the expected answer

back_end_questions = [
    'What is a class?',  # https://www.geeksforgeeks.org/c-classes-and-objects/
    'What is a method?',  # https://en.wikipedia.org/wiki/Method_(computer_programming)#:~:text=A%20method%20in%20object%2Doriented,a%20message%20and%20an%20object.&text=This%20allows%20the%20sending%20objects,behavior%20of%20a%20class%20object
    'What is a module?',  #
    'What is a function?',  # A grouped set of instructions that are given a name so they can be called elsewhere
    'What is a codebase?',  #
    'What are data types?',  # data type or simply type is an attribute of data which tells the compiler or interpreter how the programmer intends to use the data
    'What are data structures?',  # data structure is a collection of data values, the relationships among them, and the functions or operations that can be applied to the data
    'What are lambda functions?',  # https://www.w3schools.com/python/python_lambda.asp
    'What does it mean to loop?',  # To repeat a certain set of instructions over and over (usually until some condition is met)
    'What does it mean to refactor?',  # improving the internal structure of an existing program's source code, while preserving its external behavior
    'What is an attribute of a class?',  # https://www.python-course.eu/python3_class_and_instance_attributes.php#:~:text=Class%20Attributes&text=Class%20attributes%20are%20attributes%20which,right%20below%20the%20class%20header
    'What does it mean to concatenate?',  # To add two things together (strings, arrays, maps, etc.)
    'What is exception handling? Why use it?',  # exception handling is the process of responding to the occurrence of exceptions – anomalous or exceptional conditions requiring special processing - during the execution of a program, https://en.wikipedia.org/wiki/Exception_handling
    'ELI5: What is Regular Expression (RegEx)?',  # https://www.geeksforgeeks.org/write-regular-expressions/
    'What does it mean to be "Turing complete"?',  #
    'What should you do when a line is too long?',  #
    'How is exception handling different from a loop?',  #
    'When would you use WET principles instead of DRY?',  #
    'When would you use DRY principles instead of WET?',  #
    'What can back end devs do to make things more accessible?',  #
    'What is an instance and what does it mean to instantiate?',  # an instance is a single member of a class. To instantiate means to create an instance.
    'What is the difference between a "for loop" and a "while loop"?',  # For loop is for when you know how many iterations you want to loop through, while loops are for when you want to loop until a certain condtion is met.
    'What are conditionals?',  # different for different languages; for python: if, elif, else https://dev.to/vickilanger/charming-the-python-conditionals-4e5f
    'What are logical operators?',  # and + or https://dev.to/vickilanger/charming-the-python-conditionals-4e5f
    'Why does List, the language,  use () instead of []?',  # The keyboard used to develop had issues with the [ key
    'What does "++++++++++[>+++++++>++++++++++>+++>+<<<<-] >++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>." mean? What language is it in?',  # Hello World, Brainfuck
    'There is a language written with no letters , no numbers just 8 characters : > < + - . , [ ] \nWhat is it?',  # Brainfuckhttps://docs.google.com/document/d/1M51AYmDR1Q9UBsoTrGysvuzar2_Hx69Hz14tsQXWV6M/edit
    'What language was created for orangutans?',  # Ook
    'What are the three syntax elements of the language created for orangutans?',  # Ook. Ook! Ook?
    'What language is made of only spaces, tabs and newlines?',  # Whitespace
    'How would you print "Hello World" in LOLCODE',  # https://github.com/justinmeza/lolcode-spec/blob/master/v1.2/lolcode-spec-v1.2.md
    'What happens when you try to `import braces` in Python?',  # SyntaxError: not a chance
    'Emojis. Recipes. Music notes. LOLCATS. \nWhich of these is used to create a programming language?',  # All of the above
    'What is "!" used for in "!=" ?',  # Not
    'What is 0.1 + 0.2 in your language? Why?',  # https://0.30000000000000004.com/
    'What is polymorphism?',  # A programming language feature that allows the values of different data types to be handled using a uniform interface.
    'What is the difference between "while loop" and "do-while loop"? \ncredit @in_skyacademy',  #
    'What is the difference between "for loop" and "while loop"?',  # https://techdifferences.com/differenece-between-for-and-while-loop.html#:~:text=In%20'for'%20loop%20the%20initialization,each%20time%20the%20loop%20iterate.&text=In%20'for'%20loop%20iteration%20statement,statements%20in%20loop%20are%20executed
    'Why should you push security keys to a public Github repo?  \n\ninspired by @cjtaylor2390',  # security
    'What is the best way to store passwords?  \n\ninspired by @cjtaylor2390',  # salt and hash
    'Stored passwords should be hashed. Why should they also be salted?  \n\ninspired by @cjtaylor2390',  # https://twitter.com/cjtaylor2390/status/1234519650026827778?s=20
    'What are rainbow tables?  \n\ninspired by @cjtaylor2390',  # https://twitter.com/cjtaylor2390/status/1234519650026827778?s=20
    'What does storing passwords have to do with breakfast?  \n\ninspired by @cjtaylor2390',  # https://twitter.com/cjtaylor2390/status/1234516501908115459?s=20
    'What are tests for?  \n\ninspired by @Treybastian',  #
    'Why is readability so important?  \n\ninspired by @Treybastian',  #
    'Why should you avoid single letter variables? \n\ninspired by @Treybastian @cjtaylor2390',  # readability
    'What is a model?',  #
    'What is abstraction?',  # https://stackify.com/oop-concept-abstraction/
    'What are the advanced functions in python?',  # map(), filter(), reduce()
    'What is python best at?',  #

    # Real life examples
    'What is a real life example of "exception handling"?',  #
    'What is a real life example of "logical operators"?',  # if raining and dog_is_napping: skip_playing_ball
    'What is a real life example of "conditionals"?',  # if nice_outside: play_ball_with_dog
    'What is a real life example of a "function"?',  # run: pick up right for, pick up left foot, propel forward, repeat
    'What is a real life example of a "class" and some "attributes"?',  # dog: name, colors, age, chipped https://dev.to/vickilanger/charming-the-python-data-structures-154i
    'What is a real life example of a "for loop"?',  # for each dirty dish, clean dish
    'What is a real life example of a "while loop"?',  # while not napping, play fetch with dog
    ]
