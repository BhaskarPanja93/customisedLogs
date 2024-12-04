# customisedLogs v2.0.1

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
from customisedLogs import CustomisedLogs
logger = CustomisedLogs()

logger.log(logger.Colors.blue, "Blue", "This is", "blue")
logger.log(logger.Colors.red_100_accent, "Red", "This is", "red-100-accent")
logger.log(logger.Colors.green_300, "Green", "This is green-300")
logger.log(logger.Colors.cyan_700, "Cyan", "This is cyan-700")
logger.log(logger.Colors.green_300, "Green", "This is green-300")
logger.log(logger.Colors.black, "Black", "This is black")
logger.log(logger.Colors.white, "White", "This is white")
```
And it would look like:<br>
![output-readme.png](https://raw.githubusercontent.com/BhaskarPanja93/customisedLogs/master/output-readme.png?raw=True)

The package contains all colours combinations from https://davidpiesse.github.io/tailwind-md-colours

### Future implementations:
* Let user change the default RGB values.
* Different formats. Compatible to render on HTML or any other stdout method.


###### <br>This project is always open to suggestions and feature requests.