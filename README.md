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
* Create a new task in Windows Task Scheduler and in "Action" tab set it to start the notify.py script. You will see two fields, in the "Program/Script" field give the path to "pythonw.exe" (Normally located in your python installation directory. If you are using a Virtual environment(VE) the path should be from the VE.) and for "arguments" field give the path to the "notify.py" script. The argument field should be in quotations. This feature has been tested only on Windows 7.
