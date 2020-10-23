'''
questions_version_control.py: version control questions for @CodeQBot
11 February 2020
Vicki Langer (@vicki_langer)
'''

# TODO: add more questions
# NOTE: please add the question, then comment the expected answer

version_control_questions = [
    'What should be in your git commit messages? What should not?',  # why you made a change
    'What is the purpose of testing code?',  #
    'What is a commit?',  # a snapshot of the repository at one point in time
    'What does it mean to stage changes?',  # to stage changes means to finally prepare them for a commit i.e git knows about the change but they are not permanent in repository
    'Why would you stage changes?',  #
    'Why would you squash commits?',  #
    'What do it mean to rebase?',  #
    'ELI5: What is Git?',  #
    'ELI5: What is version control?',  #
    'What is a pull request?',  # Pull requests let you tell others about changes you've pushed to a branch in a repository.
    'How do you name git branches?',  #
    'What is a .gitignore file used for?',  # It specifies intentionally untracked files that Git should ignore
    'What is the difference between merge and rebase',  # https://www.atlassian.com/git/tutorials/merging-vs-rebasing
    'What makes a good commit message?',  # tells why you made a change https://dev.to/yvonnickfrin/a-guide-on-commit-messages-d8n
    'What are examples of software that can be used for version control other than git?',  # SVN, Mercurial, Bazaar
    'What is a real life example of version control?',  #
    'What is the difference between a fix and a hotfix?',  #
    'What is a master branch?',  # 
    'What is head in git and how many heads can be created in a repository?', # Head is simply a reference to a commit object.Default head is "Master".There can be multiple heads in a repository.
    'What is a branch? Why do you need to make a branch?',  #  A branch is a separate development path (in the same repository) that is frequently used to contribute new features without interfering with the main project.  Contributos need to make branches because it allows each developer to branch out from the original code base and isolate their work from others without affecting the original code.
    'Are GUI available for git version control systems?',  # Yes, you can use Gitkraken or Sourcetree, which removes the need to type git commands in terminal
    ]
