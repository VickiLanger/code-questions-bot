'''
questions_misc.py: miscellaneous questions for @CodeQBot
11 February 2020
Vicki Langer (@vicki_langer)
'''

# TODO: add more questions
# NOTE: please add the question, then comment the expected answer

misc_questions = [
    'What’s difference between The Internet and The Web?',  # hardware vs software
    'What characters do you use to comment your code? What language are you using?',  # Depends on the language
    'ELI5: What is the DOM?',  # https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model
    'ELI5: What are the APIs?',  # https://developer.mozilla.org/en-US/docs/Web/API
    'What is the name of the Java mascot?',  # Duke
    'In a tree, where is the root?',  # The top
    'In terms of coding: when may a parent kill a child?',  # if the task assigned to them is no longer needed
    'What is a DDoS attack?',  #
    'ELI5: What is cache?',  #
    #'ELI5: What is an IDE?',  #
    'What is a code smell?',  #
    'ELI5: What is cookies?',  #
    'What are comments for?',  #
    'ELI5: What is the cloud?',  #
    'What is the "black box?"',  #
    'ELI5: What is debugging?',  #
    'ELI5: "=" != "==" != "==="',  # https://twitter.com/amdev83/status/1234529491604705281?s=20
    'What does back end refer to?',  #
    'What does database refer to?',  #
    'What is a global variable?',  #
    'What is JSON? What is it for?',  #
    'What does front end refer to?',  #
    'What is Open Source Software (OSS)?',  #
    'What is pseudocode? Why would you use it',  #
    #'Whats the difference between an editor and an IDE?',  #
    'What is the difference between Java and JavaScript?',  #
    'What is the difference between a framework and library?',  #
    'What can database devs do to make things more accessible?',  #
    'What is clean code? How do you make sure you code is clean?',  #
    'What is the difference between computer science and programming?',  #
    'What is the difference between front end, back end, and database?',  #
    'What is the difference between high-level and low-level languages?',  #
    'Who are the "Big 4"? Would you work for them?',  # some combination of Google, Microsoft, Facebook, Amazon, and Apple
    'What percentage of programming jobs are in industries outside of tech?',  # Currently around 70%
    'Is JavaScript used for front end or back end?',  # Both
    'How do you conect the front end with the back end?',  #
    'What is a headless CMS? Why would I need this?',  # https://dev.to/defman/whats-headless-cms-2fek
    'What is recursion?',  # https://dev.to/rahatch/chocolate-chip-cookies-and-recursion-566k
    'What is a computer?',  #
    'What are cron jobs? What are they for?',  #
    'What is a compiler? Why would one use it?',  #
    'What is blockchain? Why would one use it?',  #
    'What are Service Workers? What are they for?',  #
    'What are containers?',  # https://dev.to/ashleemboyer/explain-containers-like-i-m-five-4cbo
    'What are closures?',  # https://dev.to/rahatch/learning-closures-with-pokemon-teams-4109
    'What is documentation? \nIs it important? \nWhy?',
    'What is nesting',  #
    'How do we know if an algorithm is efficient?',  #
    'What is Big O Notation?',  # expression of overall efficiency, factoring in both the time and space complexities
    'When evaluating complexity, what factors should you consider?',  # runtime and space
    'What is an algorithm? What are they used for?',  # process or set of rules that computers follow in order to make things happen; Algorithms are most often used to manipulate data
    'What is the best way to organize methods/functions within a file?',  # https://dev.to/ben/what-is-the-best-way-to-organize-methods-functions-within-a-file-11ih
    'Why is JPG the most performant file type for photos?',  # https://twitter.com/EmmaBostian/status/1231997438346612736
    'What does DevOps have to do with feedback?',  # from the slides "feedback === faster and better enhancements/updates/repairs"
    'What do you call monkeys that share an @Amazon account?  \n\ninspired by JS Jeopardy at a @moderndotweb meetup w/ @ladyleet',  # Prime-ates
    'What type of function includes let const and var?',  # function expression
    'What React hook fires synchronously after all DOM mutations?',  # useLayout Effect
    'What does Vue call their version of React hooks?',  # composition API
    'What JavaScript convention allows you to use a function before it\'s defined?',  # hoisting
    'As a variable, what is "i"? What is it used for?',  # index; https://twitter.com/laurieontech/status/1235028860506275841?s=20
    'What is a ternary? Why shouldn\'t there be more than one per line?',  # https://twitter.com/laurieontech/status/1235026481819992066?s=20
    'What is "self documenting code"?',  # https://twitter.com/laurieontech/status/1235025020763533312?s=20
    'How many things should a single function do?',  # 1
    'What is mapping used for?',  # takes each element from an original array, transforms it with a function that you specify, and adds the result to a new array in the same order
    'When would you use a map instead of a loop?',  # https://blog.codeanalogies.com/2018/02/20/javascript-map-method-explained-by-going-on-a-hike/
    'When would you use a loop instead of a map?',  # https://blog.codeanalogies.com/2018/02/20/javascript-map-method-explained-by-going-on-a-hike/
    'When should you use a for loop?',  # tell computer what to do with each element
    'When should you use a while loop?',  # wanted do do something as long as certain condition is true
    'When should you use a loop?',  # repeated actions
    'When should you use a switch statements instead of if-else statements',  #

    # on the job stuff?
    'What is a code review?',  #
    'What should you be looking at in a code review?',  # https://twitter.com/techgirl1908/status/1235287138478018561?s=20
    'What is pair programming?',  #
    'What is Agile?',  #
    'What is scrum?',  #

    # Job Titles
    'What is a developer advocate?',  # https://dev.to/simo97/what-is-a-developer-advocate--1jei
    'What is a developer?',  #
    'What is a software engineer?',  #
    'What is a full stack developer?',  #
    'What is the difference between a software engineer and a developer?',  #
    'What is the difference between a software engineer and a software architecht?',  #
    'What is DevOps?',  #
    'What is DevRel?',  #
    'What\'s the difference between Computer Engineering and Computer Science',  #

    # Ergonomics
    'In terms of ergonomics, what angle should your screen be at?',  # 20 degrees
    'In terms of ergonomics, what angle should your elbows be at?',  # 90 degrees
    'In terms of ergonomics, how far away from your screen should you be?',  # something like 20-22 inches

    # Real World Examples
    'What is a real life analogy of "file directories"?',  # memories, stores, relationships, https://blog.codeanalogies.com/2018/06/24/file-directories-explained-by-getting-dressed-in-the-morning/
    'What is a real life example of "browser dev tools"?',  # https://blog.codeanalogies.com/2018/07/21/browser-developer-tools-explained-by-training-to-become-a-chef/
    'What is a real life metaphor of "back end development"?',  #
    'What is a real life metaphor of "front end development"?',  #
    'What is a real life metaphor of "front end vs back end"?',  # https://blog.codeanalogies.com/2018/04/07/front-end-v-back-end-explained-by-waiting-tables-at-a-restaurant/
    'What is a real life analogy of "localhost"?',  # https://blog.codeanalogies.com/2018/02/02/localhost-explained-by-trying-to-start-a-microbrewery/
    'What is a real life example of "web servers"?',  # https://blog.codeanalogies.com/2018/04/26/web-servers-explained-by-running-a-microbrewery/
    'What is a real life metaphor of "caching"?',  # https://blog.codeanalogies.com/2018/06/11/web-caching-explained-by-buying-milk-at-the-supermarket/
    'What is a real life analogy of "APIs"?',  # https://blog.codeanalogies.com/2018/02/27/web-apis-explained-by-selling-goods-from-your-farm/
    'What is a real life example of "Amazon Web Services (AWS) \n@awscloud"?',  # https://blog.codeanalogies.com/2018/07/31/amazon-web-services-aws-explained-by-operating-a-brewery/
    'What is a real life metaphor of "webhooks"?',  # https://blog.codeanalogies.com/2018/03/05/the-difference-between-apis-and-webhooks-explained/
    'What is a real life analogy of "blockchain"?',  # https://blog.codeanalogies.com/2018/04/18/blockchain-explained-by-trying-to-pass-high-school-math-class/
    'What is a real life example of "cookies"?',  # https://blog.codeanalogies.com/2018/06/02/internet-cookies-explained-by-taking-your-kids-to-the-doctors-office/
    'What is a real life analogy of a "repository"?',  #
    'What is a real life example of "SQL tables"?',  # https://medium.com/@kevink/sql-tables-explained-by-voting-in-the-infamous-2016-election-de638dd9db7#.16pkuy69p
    'What is a real life metaphor of "JavaScript AJAX"? \n#JavaScript',  # https://blog.codeanalogies.com/2018/01/15/ajax-basics-explained-by-working-at-a-fast-food-restaurant/
    'What is a real life analogy of "JavaScript closures"? \n#JavaScript',  # https://blog.codeanalogies.com/2018/10/19/javascript-closures-explained-by-mailing-a-package/
    'What is a real life example of "JavaScript scoping"? \n#JavaScript',  # https://blog.codeanalogies.com/2017/11/22/how-javascript-variable-scoping-is-just-like-multiple-levels-of-government/
    'What is a real life metaphor of "JavaScript promises"? \n#JavaScript',  # https://blog.codeanalogies.com/2018/08/26/javascript-promises-explained-by-gambling-at-a-casino/
    'What is a real life analogy of "JavaScript map()"? \n#JavaScript',  # https://blog.codeanalogies.com/2018/02/20/javascript-map-method-explained-by-going-on-a-hike/
    'What is a real life example of "JavaScript filter()"? \n#JavaScript',  # https://blog.codeanalogies.com/2018/05/14/javascripts-filter-function-explained-by-applying-to-college/
    'What is a real life metaphor of "JavaScript this"? \n#JavaScript',  # https://blog.codeanalogies.com/2018/03/12/javascripts-this-explained-by-starting-a-high-school-band/
    'What is a real life analogy of "JavaScript reduce()"? \n#JavaScript',  # https://blog.codeanalogies.com/2018/07/24/javascripts-reduce-method-explained-by-going-on-a-diet/
    'What is a real life example of "React.js props/state "? \n#JavaScript #react',  # https://blog.codeanalogies.com/2016/10/04/react-props-state-explained-through-darth-vaders-hunt-for-the-rebels/
    'What is a real life metaphor of "Docker containers"? \n@Docker',  # https://dev.to/kbk0125/docker-containers-explained-by-renting-office-space-p0o
    'What is a real life analogy of "JavaScript Async/Await"? \n#JavaScript',  # https://blog.codeanalogies.com/2019/12/22/async-await-explained-by-doing-your-morning-routine/
    'What is a real life example of "JavaScript merge sort"? \n#JavaScript',  # https://dev.to/kbk0125/recursion-and-the-call-stack-explained-by-reading-a-book-a1
    'What is a real life metaphor of "JavaScript recursion"? \n#JavaScript',  # https://dev.to/kbk0125/recursion-and-the-call-stack-explained-by-reading-a-book-4khm
    'What is a real life analogy of "JavaScript arrow function"? \n#JavaScript',  # https://dev.to/kbk0125/javascript-s-arrow-functions-explained-by-going-down-a-slide-1ebm
    'What is a real life example of "NPM"? \n@npmjs #JavaScript',  # https://dev.to/kbk0125/node-package-manager-npm-explained-by-directing-a-movie-359
    'What is a real life metaphor of "code smell"?',  #
    'What is a real life analogy of "mapping"?',  #
    'What is a real life example of "a function"?',  # any action that has repeatable steps
    #'What is a real life example of " "? \n#',  #
    #'What is a real life example of " "? \n#',  #
    #'What is a real life example of " "? \n#',  #
    ]
