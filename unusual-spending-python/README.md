Unusual Spending Kata in Python
===============================

This repository is a boilerplate code for the Unusual Spending Kata in Python

### Getting Started

In order to use it, we must install [docker](https://docs.docker.com/engine/installation/) to run it with a container, or install a standard python development environment and run it in your local machine.

To run the project with docker, we can do the following:

First we can build the docker image by issuing:

    $ docker-compose build

Then in order to start the app:

    $ docker-compose up -d

If we want to execute a file of the app:
    
    $ docker-compose exec app python <filepath>

or if we want to run the tests:
    
    $ docker-compose exec app pytest src/tests/test_app.py


## Requirements

You work at a credit card company and as a value-add they want to start providing alerts to users when their spending in any particular category is higher than usual.

* A `Payment` is a simple value object with a `price`, `description`, and `category`
* A `Category` is an enumerable type of a collection of things like "entertainment", "restaurants", and "golf"
* For a given `userId`, fetch the payments for the current month and the previous month
* Compare the total amount paid for each month, grouped by category; filter down to the categories for which the user spent at least 50% more this month than last month
* Compose an e-mail message to the user that lists the categories for which spending was unusually high, with a subject like "Unusual spending of $1076 detected!" and this body:
```
Hello card user!

We have detected unusually high spending on your card in these categories:

* You spent $148 on groceries
* You spent $928 on travel

Love,

The Credit Card Company
```

## Caveats

Like most applications that developers are paid to write, this kata tasks the programmer to implement just one layer of
an overall solution, meaning there are a number of important facets we can't control:

* We don't control who invokes our entry point, or when; nor can we change its method signature, as it represents a public interface that something else (maybe a job scheduler system) is depending on
* We don't control how payments are fetched, that's Somebody Else's Job; all we have is an agreed-upon contract: `get_payments`
* We don't control how e-mails are sent, all we know is that it's specified by the interface `email(userId, subject, body)`

## Extra Credit

Once you've completed the kata, if you'd like to test your approach for how easy it is to change, try these requested requirement changes:

* Load three months of payment history and compare the current month to their average totals by category (you're guaranteed to have the most recent month, but either of the two prior months might come back as empty sets, as if the user lacks the payment history)
* Update the e-mail to report what the usual spending amount was, in addition to the unusual spending amount
