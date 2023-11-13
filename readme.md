# How to use

This folder contians all the necessary components to run scripts against the QRadar API

### Components
- Logging: logger.py, logger.yaml, logger_utility.py
- Authentication: creds.py
- API definitions: qradar_functions.py
- Scripts: everything else

The logger files need no changes unless you want to change the directory you want to output the log file to. For that go to logger.yml and change the value on line 17. Note that the directory must already exist as stated in the comment for that line. 

## Using the logger
> logger.info('oh no!')


> logger.error('I've slipped on my beans!')

## Authentication
Go to the creds.py and enter the values for the Console and the API token
> console = 'IP or FQDN of Console'

> token = 'Your API Token'

## API Definitions
The qradar_functions.py simply defines the GET, POST, and PUT functions laying out the URL, data, headers etc to be reused in your future scripts. One thing to note is that all calls require an input for params and the GET call requires a range. If no params are desired simply pass a blank variable of ''.
