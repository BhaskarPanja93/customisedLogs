__version__ = "1.5.1"
__packagename__ = "customisedlogs"


def updatePackage():
    from time import sleep
    from json import loads
    import http.client
    print(f"Checking updates for Package {__packagename__}")
    try:
        host = "pypi.org"
        conn = http.client.HTTPSConnection(host, 443)
        conn.request("GET", f"/pypi/{__packagename__}/json")
        data = loads(conn.getresponse().read())
        latest = data['info']['version']
        if latest != __version__:
            try:
                import pip
                pip.main(["install", __packagename__, "--upgrade"])
                print(f"\nUpdated package {__packagename__} v{__version__} to v{latest}\nPlease restart the program for changes to take effect")
                sleep(3)
            except:
                print(f"\nFailed to update package {__packagename__} v{__version__} (Latest: v{latest})\nPlease consider using pip install {__packagename__} --upgrade")
                sleep(3)
        else:
            print(f"Package {__packagename__} already the latest version")
    except:
        print(f"Ignoring version check for {__packagename__} (Failed)")


class Manager:
    def __init__(self, verbosity:int=100, maxLogCount:int=1000):
        """
        Initialise the Manager and then use the public functions to display coloured logs
        :param verbosity: Integer value to set minimum threshold of log verbosity
        :param maxLogCount: Maximum number of logs to store in memory, Values available as list in `Manager().allLogs`
        """
        from colr import color as __color
        from time import ctime as __ctime
        self.__color = __color
        self.__ctime = __ctime
        self.allLogs = []
        self._verbosity = verbosity
        self._maxLogCount = maxLogCount

        self._fatal = [1, (255, 0, 0), (90, 0, 0)]
        self._failed = [2, (255, 182, 0), (127, 89, 0)]
        self._success = [3, (57, 202, 0), (23, 81, 0)]
        self._info = [4, (0, 140, 255), (0, 52, 95)]
        self._skip = [5, (0, 255, 195), (0, 100, 77)]


    def __log(self, string: str, back: tuple[int,int,int], fore: tuple[int,int,int]):
        """
        Private function to finally print the coloured text onto terminal and remove older logs if exceeds max count.
        :param string: The string to print
        :param back: RGB tuple specifying the background colour
        :param fore: RGB tuple specifying the foreground colour
        :return:
        """
        self.allLogs.append(string)
        if len(self.allLogs) > self._maxLogCount:
            self.allLogs.pop(0)
        print(self.__color(string, back=back, fore=fore))


    def __formString(self, category: str, *args:*list[str]):
        """
        Decorate the log string and all other arguments passed into a single string
        :param category: The string that gets decorated
        :param args: Other strings to join to fina log
        :return:
        """
        return f"[{self.__ctime()}] [{category}] {' '.join(args)}"


    def skip(self, category: str, *args):
        """
        Log with verbosity value 1
        :param category: The string that gets decorated
        :param args: Other strings to pass
        """
        string = self.__formString(category, *args)
        if self._skip[0] <= self._verbosity:
            self.__log(string, back=self._skip[1], fore=self._skip[2])
        return string


    def info(self, category: str, *args):
        """
        Log with verbosity value 2
        :param category: The string that gets decorated
        :param args: Other strings to pass
        """
        string = self.__formString(category, *args)
        if self._info[0] <= self._verbosity:
            self.__log(string, back=self._info[1], fore=self._info[2])
        return string


    def success(self, category: str, *args):
        """
        Log with verbosity value 3
        :param category: The string that gets decorated
        :param args: Other strings to pass
        """
        string = self.__formString(category, *args)
        if self._success[0] <= self._verbosity:
            self.__log(string, back=self._success[1], fore=self._success[2])
        return string


    def failed(self, category: str, *args):
        """
        Log with verbosity value 4
        :param category: The string that gets decorated
        :param args: Other strings to pass
        """
        string = self.__formString(category, *args)
        if self._failed[0] <= self._verbosity:
            self.__log(string, back=self._failed[1], fore=self._failed[2])
        return string


    def fatal(self, category: str, *args):
        """
        Log with verbosity value 5
        :param category: The string that gets decorated
        :param args: Other strings to pass
        """
        string = self.__formString(category, *args)
        if self._fatal[0] <= self._verbosity:
            self.__log(string, back=self._fatal[1], fore=self._fatal[2])
        return string

