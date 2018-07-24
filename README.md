## About

Search words and their meanings and store them in a table for faster access later. Also get pop up notification for randomly generated words you searched before. It helps you strengthen your vocabulary.

## Requirements
* Python 3.x is required
* Install mysqlclient
        
        pip install mysqlclient
* Install pywin32

        pip install pywin32
* MySQL 5.7

## Usage

* Get your Oxford Dictionary API key from https://developer.oxforddictionaries.com/
* You need to create a table to store words you search. Fields <...> are to be substituted as per user. 

        mysql> create database <database name>;
        mysql> create table words(word varchar(50),meaning varchar(500),example varchar(1000),type varchar(10),constraint pk_word primary key (word));
        
* Run script

        >python dictionary.py
