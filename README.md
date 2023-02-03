# Pytest Lab

In this lab you will walk through the basic procedure for creating and contributing to an open source project.
You will also walk through how to use the pytest framework for running test cases.

## Instructions

**DO NOT FORK THIS REPO!!!**

You will need a partner to complete this lab,
so introduce yourself to someone next to you.
A team of 3 is okay.

**Part 1:**

1. Create a new repository by clicking the "+" sign in the top right corner of the github webpage.
   
   It doesn't matter what you name your repo, except that it must be different than what your partner names their repo.
   
   Ensure the repository is public and that you are not creating any default files in the repo (like a README or LICENSE file).

1. On the lambda server, run the following commands:
    ```
    $ mkdir pytest-example
    $ cd pytest-example
    $ git init
    $ git remote add origin $YOUR_REPO_URL
    $ git remote add mikeizbicki https://github.com/mikeizbicki/pytest-example
    $ git pull mikeizbicki master
    $ git push origin master
    ```
    You should substitute your repo url for the variable `$YOUR_REPO_URL` above.

    If everything worked correctly, then you should have a copy of my repo in your repo on github.

1. Modify the README file to include a test cases badge.

    > **HINT:**
    > I'm not going to directly tell you how to do this.
    > Instead, you should look at a repo that already has a test cases badge and copy the format of that code.
    > In general, this type of copying from other people's projects to include features they have and you want is highly encouraged.

   Once you've completed this step, you should now have a RED badge because the test cases are failing.

1. At this point, you are not allowed to directly modify your repository at all.
    Instead, your partner will follow the steps in Part 2 below to fix your repo.
    (And you will follow the steps to fix theirs.)

**Part 2:**

1. Fork your partners repo.

1. On the lambda server, clone and enter your forked repo.

1. Run the following command:
    ```
    $ python3 -m pytest
    ```

    > **NOTE:**
    > The first time you run this command, you may get an error message saying that `No module named pytest`.
    > In that case, you need to run the command
    > ```
    > $ pip3 install pytest
    > ```
    > to download and install the library.

    You should see 5 failing test cases.
    These test cases are located in the file `tests/test_main.py`.
    You should open this file in vim and visually inspect it.

    Each function in the file is a single test case.
    The function `evens` being tested is the same function you had on the last homework assignment,
    I've just rewritten the tests to use the pytest framework instead of the doctests framework.
    In this new framework, a test case is "passed" whenever a function returns without an exception,
    and a test is "failed" whenever a function throws an exception.
    (Recall that `assert` throws an exception whenever the expression to the right evaluates to `False`.)

    Doctests are generally used for very simple tests,
    but soon in this class we will need more complicated tests that don't work well for doctests.
    The pytest framework is good for these complicated tests.

1. Modify the `Fixme.py` file so that all of the tests pass.

1. Submit a pull request with changes that you've made.

    > **NOTE:**
    > You should not be submitting a pull request to my repo,
    > but to your partner's repo.

1. When you receive your partner's pull request, you should see an option to run the github actions before accepting the merge.
    You should do this and check that the change fixes the test cases before accepting the pull request.

## Submission

Paste the URL to both your repo and your partner's repo into sakai.
