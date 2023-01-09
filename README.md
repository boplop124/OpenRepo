# Telegram printing service bot PrintMe03

tasks:
- setup logging module to log
- find a way to launch both python files at the same time

## Introduction

PrintMe03 is a Telegram bot, a part of PrintMe service, desighned to act as an intermediate between printer service provider and customer.
It's primary function is to automate the process of pinging printer service provider, job receiving, handling out payment forwarding options. Which includes:

Minimum

- Providing customer with printing stantion's online status and price
- Printable files management
- Downloading and sending printable files to the serve
- Displaying current totals (price, number of pages etc)(probably going to pop up after file upload)
- Providing customer with payment options
- Allowing to print a quee by call
- Notifying customer when the printing is finished

Secondatry functions(not implemented):

- paper available
- Providing printing options(colour, orientation)
- Bonus system for customer
- Providing example of a test page at the beginning of each business day

## Used tech

Pyrogram is a Telegram bot framework build with Telegram Call API, used as a core. Very high level, but has a lot of functionality, has a configurable proxy, operates of TgCrypto, so plenty fast for small scale needs. Build for true async, but it isn't used because of unnecessary coplexity.

## Setup quide

- Programm structure:
    1. apps directory with apps
    2. DBs directory with databases
    3. config.ini - configuration file
    4. main.py - main executable file that deploys every app 

