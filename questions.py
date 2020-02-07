'''
questions.py: questions to be used by tweet.py for @CodeQBot
21 January 2020
Vicki Langer (@vicki_langer)
'''

# TODO: add more questions
# NOTE: please add the question, then comment the expected answer

QUESTIONS = [
    'What questions would you like us to ask? Or what kinds of questions would you like to see?',  # Open-ended, no right answer
    'It would be cool if @CodeQBot could _______________________ \nfill in the blank',  # Open-ended, no right answer
    'Who has been called the worlds first computer programmer?',  # Ada Lovelace
    'Who popularized the idea of machine-independent programming languages?',  # Grace Hopper
    'What is "!" used for in "!=" ?',  # Not
    'What is required in the HTML <head>?',  # charset, viewport, title https://htmlhead.dev
    'What’s difference between The Internet and The Web?',  # hardware vs software
    'What characters do you use to comment your code? What language are you using?',  # Depends on the language
    'Why does List, the language,  use () instead of []?',  # The keyboard used to develop had issues with the [ key
    'What does Wi-Fi stand for?',  # nothing https://www.webopedia.com/DidYouKnow/Computer_Science/wifi_explained.asp
    'What is 0.1 + 0.2 in your language? Why?',  # https://0.30000000000000004.com/
    'ELI5: What is the DOM?',  # https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model
    'ELI5: What are the APIs?',  # https://developer.mozilla.org/en-US/docs/Web/API
    'What was the first song ever sung by a computer?',  # "Daisy Bell" was composed by Harry Dacre in 1892. In 1961, the IBM 7094 became the first computer to sing, singing the song Daisy Bell
    'What is polymorphism?',  # A programming language feature that allows the values of different data types to be handled using a uniform interface.
    'What is the name of the Java mascot?',  # Duke
    'What\'s the story behind the first computer virus?',  # http://web.eecs.umich.edu/~aprakash/eecs588/handouts/cohen-viruses.html
    'What was the first computer bug?',  # an actual bug
    'In a tree, where is the root?',  # The top
    'In terms of coding: when may a parent kill a child?',  # if the task assigned to them is no longer needed
    'Who recorded the first computer bug? What were they doing?',  # Grace Hopper recorded the first computer ‘bug’ in the book as she was working for the MARK II computer. https://www.nationalgeographic.org/thisday/sep9/worlds-first-computer-bug/
    'What is a commit?',  #
    'ELI5: What is Git?',  #
    'What is recursion?',  #
    'What is a viewport?',  #
    'What is a component?',  #
    'ELI5: What is cache?',  #
    'ELI5: What is an IDE?',  #
    'What is a code smell?',  #
    'ELI5: What is cookies?',  #
    'What are comments for?',  #
    'What is a pull request?',  #
    'What is the "black box?"',  #
    'ELI5: What is debugging?',  #
    'ELI5: "=" != "==" != "==="',  #
    'What does back end refer to?',  #
    'What does database refer to?',  #
    'How do you name git branches?',  #
    'What is JSON? What is it for?',  #
    'What does front end refer to?',  #
    'What is Alan Turing known for?',  #
    'What is Open Source Software (OSS)?',  #
    'ELI5: What is Regular Expression (RegEx)?',  #
    'What does it mean to be "Turing complete"?',  #
    'What is the difference between merge and rebase',  #
    'What day is celebrated as Programmer\'s day? Why?',  #
    'When would you use WET principles instead of DRY?',  #
    'When would you use DRY principles instead of WET?',  #
    'Whats the difference between an editor and an IDE?',  #
    'What is the difference between Java and JavaScript?',  #
    'What is the difference between a <div> and a <span>?',  #
    'What is the difference between a framework and library?',  #
    'What is the difference between a "grid" and a "flexbox"',  #
    'What\'s the difference between a web app and a website?,'  #
    'In CSS, what\'s the difference between flexbox and grid?',  #
    'What can back end devs do to make things more accessible?',  #
    'What can database devs do to make things more accessible?',  #
    'What is an instance and what does it mean to instantiate?',  #
    'What can front end devs do to make things more accessible?',  #
    'In CSS, what\'s the difference between a grid and a table?',  #
    'What is clean code? How do you make sure you code is clean?',  #
    'What is the difference between computer science and programming?',  #
    'What is the difference between front end, back end, and database?',  #
    'What is the difference between high-level and low-level languages?',  #
    'What makes a good commit message?',  # tells why you made a change https://dev.to/yvonnickfrin/a-guide-on-commit-messages-d8n
    'When would using the HTML <style> tag could be useful? \ncredit @bramleylmao',  # https://webwide.io/threads/usage-of-style-tag-in-html-but-why.646/
    'What does "++++++++++[>+++++++>++++++++++>+++>+<<<<-] >++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>." mean? What language is it in?',  # Hello World, Brainfuck
    'There is a language written with no letters , no numbers just 8 characters : > < + - . , [ ] \nWhat is it?',  # Brainfuckhttps://docs.google.com/document/d/1M51AYmDR1Q9UBsoTrGysvuzar2_Hx69Hz14tsQXWV6M/edit
    'What percentage of programming jobs are in industries outside of tech?',  # Currently around 70%
    'What languages are used to creat a website?',  # HTML, CSS, JavaScript
    'In JavaScript used for front end or back end?',  # Both
    'What language was created for orangutans?',  # Ook
    'What are the three syntax elements of the language created for orangutans?',  # Ook. Ook! Ook?
    'What language is made of only spaces, tabs and newlines?',  # Whitespace
    'How would you print "Hello World" in LOLCODE',  # https://github.com/justinmeza/lolcode-spec/blob/master/v1.2/lolcode-spec-v1.2.md
    'What was the first mouse made of?',  # wood
    'Who invented the Internet?',  # @timberners_lee Tim Burner Lee
    'Where did they source or get the parts for the first Apple computer?',  # made using old parts they collected from their staff for free
    'What does CAPTCHA stand for? \nBonus Points: Share a ridiculous CAPTCHA pic',  # Completely Automated Public Turing test to tell Computers and Humans Apart
    'What happens when you try to `import braces` in Python?',  # SyntaxError: not a chance
    'Emojis. Recipes. Music notes. LOLCATS. \nWhich of these is used to create a programming language?',  # All of the above
    'What should be in your git commit messages? What should not?',  # why you made a change
    'What is the purpose of testing code?',  #
    'How should I make a list without bullets?',  #
    'How do you conect the front end with the back end?',  #
    'What is a headless CMS? Why would I need this?',  # https://dev.to/defman/whats-headless-cms-2fek
    'What is recursion?',  # https://dev.to/rahatch/chocolate-chip-cookies-and-recursion-566k
    'What is a font-family and why would it have a fallback?\nShould it have a fallback?',  #
    'What are @keyframes for?',  # specifies the animation code
    'What is a z-index?',  # specifies the stack order of an element
    'Why would you use @media queries?',  # https://www.w3schools.com/cssref/css3_pr_mediaquery.asp
    'In CSS, what is @import used for and why would you use it?',  # allows you to import a style sheet into another style sheet
    'In CSS, what is @charset used for and why would you use it?',  # specifies the character encoding used in the style sheet
    'What is a computer?',  #
    'What is a compiler? Why would one use it?',  #
    'What is blockchain? Why would one use it?',  #
    'What are cron jobs? What are they for?',  #
    'What are Service Workers? What are they for?',  #
    'What is an dev environment?',  #
    'What are containers?',  # https://dev.to/ashleemboyer/explain-containers-like-i-m-five-4cbo
    'What are closures?',  # https://dev.to/rahatch/learning-closures-with-pokemon-teams-4109
    'What is documentation? \nIs it important? \nWhy?',

    # on the job stuff?
    'What is a code review?',  #
    'What is pair programming?',  #

    # Job Titles
    'What is a developer advocate?',  # https://dev.to/simo97/what-is-a-developer-advocate--1jei
    'What is a developer?',  #
    'What is a software engineer?',  #
    'What is a full stack developer?',  #
    'What is the difference between a software engineer and a developer?',  #
    'What is the difference between a software engineer and a software architecht?',  #

    # Language Creation
    'What languages influenced the design of JavaScript?',  # AWK, C, HyperTalk, Java, Lua, Perl, Python, Scheme, and Self
    'How was the language Java invented?',  # James Gosling, at Sun Labs, around 1992; the group was building a set-top box and started by “cleaning up” C++ and wound up with a new language and runtime.
    'What was PHP initially created for?',  # Lerdorf had created the language, or interface at the time, for the purpose of managing his personal website.
    'What was Java initally design for?',  # Java was designed with the primary aim for use in Interactive television
    'Where did the language "C" get it\'s name?',  # C language succeeds B language
    'Who is the creator of JavaScript?',  # Brendan Eich
    'What was Java called before it was Java? \nextra points: why was it changed?',  # Oak. Thename was ruled out by Sun's trademark lawyers since the name was used by the company Oak Technologies
    'What programming language did Bjarne Stroustrup create?',  # C++
    'Where did the language "Python" get it\'s name?',  # creator liked the movie Monty Python

    # Movies and TV
    'In "Ralph Breaks the Internet", what language was on Arthur\'s Heads Up Display (HUD)?',  # https://www.reddit.com/r/Python/comments/ariypt/just_noticed_that_the_code_in_ralph_breaks_the/
    'In "Stranger Things" Season 2, what language was used?',  # BASIC https://moviecode.tumblr.com/post/166870949505/at-least-they-tried-basic-from-stranger-things
    'In "Doctor Who" Season 7 Episode 2, what code is guiding the missiles?',  # In Doctor Who S07E02, missiles are being guided by the power of SVGs.
    'In "Silicon Valley" Season 3 Episode 1, what language is being used?',  # https://www.reddit.com/r/SiliconValleyHBO/comments/4gbra7/i_got_the_silicon_valley_s03e01_code_to_compile/)

    # Alphabet Soup aka Acronyms
    'What do WET and DRY stand for? When would you use these?',  # Write Everything Twice, Dont Repeat Yourself
    'What does CRUD stand for? When would you use it?',  # Create Read Update Delete
    'What does API stand for? What is it?',  # Application Program Interface
    'What does ASCII stand for? What is it?',  # American Standard Code For Information Interchange
    'What does A11Y stand for? What is it?',  # Accessibility
    'What does BLOB stand for? What is it?',  # Binary Large Object
    'What does 2FA stand for? What is it?',  # 2 factor Auth
    'What does IDE stand for? What is it?',  # Integrate Development Environment
    'What does DOM stand for? What is it?',  # Document Object Model
    'What does HTML stand for? What is it?',  # Hyper-Text Markup Language
    'What does CSS stand for? What is it?',  # Cascading Style Sheets
    'What does HTTP stand for? What is it?',  # HyperText Transfer Protocol
    'What does HTTPS stand for? What is it?',  # HyperText Transfer Protocol Secure
    'What does GUI stand for? What is it?',  # Graphical User Interface
    'What does OOP stand for? What is it?',  # Object Oriented Programming
    'What does FP stand for? What is it?',  # Funtional Programming
    'What does SOAP stand for? What is it?',  # Simple Object Access Protocol
    'What does SSL stand for? What is it?',  # Secure Sockets Layer
    'What does VPN stand for? What is it?',  # Virtual Private Network
    'What does XML stand for? What is it?',  # Extensible Markup Language
    'What does SOLID stand for? What is it?',  # Single responsibility, Open–closed, Liskov substitution, Interface segregation, Dependency inversion https://en.wikipedia.org/wiki/SOLID
    'What does PWA stand for? What is it?',  # Progressive Web App
    'What does WYSIWYG stand for? What is it?',  # What you see is what you get; in reference to editors
    'What does CMS stand for? What is it?',  # Content Management System (like wordpress and many many others)
    'What does TLD stand for? What is it?',  # Top Level Domain
    'What does XML stand for? What is it?',  #
    'What does SVG stand for? What is it?',  #
    'What does JSON stand for? What is it?',  #

    # HTTP Statuses
    'Answer with a GIF. \nWhat is HTTP status 100?',  # Continue https://httpstatuses.com
    'Answer with a GIF. \nWhat is HTTP status 101?',  # Switching Protocols https://httpstatuses.com
    'Answer with a GIF. \nWhat is HTTP status 102?',  # Processing https://httpstatuses.com
    'Answer with a GIF. \nWhat is HTTP status 200?',  # Okay https://httpstatuses.com
    'Answer with a GIF. \nWhat is HTTP status 201?',  # Created https://httpstatuses.com
    'Answer with a GIF. \nWhat is HTTP status 202?',  # Accepted https://httpstatuses.com
    'Answer with a GIF. \nWhat is HTTP status 300?',  # Multiple Choices https://httpstatuses.com
    'Answer with a GIF. \nWhat is HTTP status 301?',  # Moved Permanently https://httpstatuses.com
    'Answer with a GIF. \nWhat is HTTP status 302?',  # Found https://httpstatuses.com
    'Answer with a GIF. \nWhat is HTTP status 305?',  # Use proxy https://httpstatuses.com
    'Answer with a GIF. \nWhat is HTTP status 307?',  # Temporary Redirect https://httpstatuses.com
    'Answer with a GIF. \nWhat is HTTP status 308?',  # Permanent Redirect https://httpstatuses.com
    'Answer with a GIF. \nWhat is HTTP status 400?',  # Bad Request https://httpstatuses.com
    'Answer with a GIF. \nWhat is HTTP status 401?',  # Unauthorized https://httpstatuses.com
    'Answer with a GIF. \nWhat is HTTP status 402?',  # Payment Required https://httpstatuses.com
    'Answer with a GIF. \nWhat is HTTP status 403?',  # Forbidden https://httpstatuses.com
    'Answer with a GIF. \nWhat is HTTP status 404?',  # Not Found https://httpstatuses.com
    'Answer with a GIF. \nWhat is HTTP status 417?',  # Expectation Failed https://httpstatuses.com
    'Answer with a GIF. \nWhat is HTTP status 418?',  # I'm a teapot https://httpstatuses.com
    'Give an example of HTTP status 418, in the wild. Screenshots encouraged',  # google has one
    'Where did HTTP status 418 come from?',  # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/418
    'Answer with a GIF. \nWhat is HTTP status 500?',  # Internal Server Error https://httpstatuses.com
    'Answer with a GIF. \nWhat is HTTP status 503?',  # Service Not Available https://httpstatuses.com
    'Answer with a GIF. \nWhat is HTTP status 508?',  # Loop Detected https://httpstatuses.com

    # Opinions Welcome Here
    'What is the single best code/programming book you\'ve read?',
    'Tabs, Spaces, tabs as spaces, or spaces as tabs?',
    'Light mode or dark mode? Why?',
    'What\'s the best learning resource you\'ve used? Why?',
    'What editor or IDE do you use? Any special reason?',
    'Answer with a GIF. \nHow are you feeling about your code, right now?',
    'How did you get into coding/programming?',
    'What badass ladies are you following that everyone else should follow? \nWhy? \nTag \'em',
    # 'What badass dudes are you following that everyone else should follow? \nWhy? \nTag \'em',
    # 'What badass trans* peeps are you following that everyone else should follow? \nWhy? \nTag \'em \nnote: do not out someone who isn't out',
    # 'What badass POC are you following that everyone else should follow? \nWhy? \nTag \'em',
    # 'What badass underrepresented peeps are you following that everyone else should follow? \nWhy? \nTag \'em',
    'What badass folks you are following that everyone else should follow? \nWhy? \nTag \'em',
    'Do you have a portfolio? Why or why not? \nShare a link'
    'Do you write on dev.to? \nShare a link to your favorite article \n#DEVcommunity @ThePracticalDev',
    'What\'s the weirdest bug you\'ve dealt with? \nTell us about it.',
    'What\'s your go to framework? Why?',
    'What was your latest win?',
    # 'What do you need help with? \nor \nWhat can you help someone with?',
    'What are your goals for the next few days?',
    'What\'s your browser of choice? Why?',
    'Explain to a 5-year-old, what do you do for work?',
    'Do you work with Open Source? What project(s)?',
    # 'Do you have an open source project you would like help with? \nWhat help is needed? \nShare a link',
    ]
