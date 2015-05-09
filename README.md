scrumblr-box
============

Vagrant box for [scrumblr](https://github.com/aliasaria/scrumblr)

Includes a Python script to dump board contents as text file in Markdown format:

    vagrant@precise32:~$ ./shared/print-board.py http://localhost:8080/demo

    Board as of 2015-05-09
    ======================

    Not Started
    -----------
    - Hello this is fun
    - Hello this is fun

    Started
    -------
    - .
    - .

    Testing
    -------
    - .
    - Hello this is a new card.
    - Hello this is a new story.
    - .

    Review
    ------

    Complete
    --------

    Other
    -----

