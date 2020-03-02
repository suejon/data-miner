# Data-miner

#### Intro

This service provides the ability to scan tweets as input data and discover 
patterns in the dataset using machine learning.

#### Setup

Since this service uses your twitter feed, you will need to create an application as a developer on your twitter account.
This will allow you to access the twitter API using a set of tokens (these should never be checked into source code).
You can add these to an .env file which the service will pull the properties from.

To install the dependencies for the project using pipenv

```bash
pipenv install
```

Run the application:
```bash
pipenv run python auth.py
```