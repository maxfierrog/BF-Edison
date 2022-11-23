## BigFix to Edison Reference Tool

Python tool using the BigFix WebReports SOAP API to reconcile the contents of the Edison inventory system.

### Preliminaries

Make sure to use the virtual environment. 

### Usage

To make requests you will need a valid Berkeley Client Admininistrator account.

1. Create a file named `keys` under the `files` directory.
2. Write your username on the first line, and your password on the second line.
3. Write a valid [BigFix Session Relevance expression](https://developer.bigfix.com/relevance/guide/session/).
4. Paste the relevance expression into the `relevance` file in the `files` directory.
5. Make sure to save both `keys` and `relevance`.
6. Run `handler.py`.

This will place the results of the query in the `response` file under `files`, one object per line.

### Libraries

* [Zeep](https://docs.python-zeep.org/en/master/)
