# customisedLogs v1.4.1

```pip install customisedlogs --upgrade```

###### <br>A well maintained program to have coloured logs on the terminal. This would help isolate errors and success messages from each other just by their colours.


<br>To install: 
```
pip install customisedlogs --upgrade
pip3 install customisedlogs --upgrade
python -m pip install customisedlogs --upgrade
python3 -m pip install customisedlogs --upgrade
```


#### <br><br>Using this program is as simple as:
```
from customisedLogs import Manager as LogManager

logger = LogManager()

logger.fatal("SERVER", "Unhandled Exception", "Overloaded")
logger.failed("SERVER", "Unable to connect..")
logger.success("NETWORK", "Successfully connected", "Bi-directional", "lat: 1ms")
logger.info("CLIENT", "Port reserved")
logger.skip("PROGRAM", "Started...")
```
And it would look like:
![output-readme.png](https://raw.githubusercontent.com/BhaskarPanja93/customisedLogs/master/output-readme.png?raw=True)


### Future implementations:
* Let user change the default RGB values.
* Add more verbose levels.
* Customised verbose levels.
* Skip same log if repeated within a time-frame.
* Different formats. Compatible to render on HTML or any other stdout method.


###### <br>This project is always open to suggestions and feature requests.