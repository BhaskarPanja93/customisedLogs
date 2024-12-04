__version__ = "2.0.2"
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
                import subprocess
                from pip._internal.utils.entrypoints import (
                    get_best_invocation_for_this_pip,
                    get_best_invocation_for_this_python,
                )
                from pip._internal.utils.compat import WINDOWS
                if WINDOWS:
                    pip_cmd = f"{get_best_invocation_for_this_python()} -m pip"
                else:
                    pip_cmd = get_best_invocation_for_this_pip()
                subprocess.run(f"{pip_cmd} install {__packagename__} --upgrade")
                print(f"\nUpdated package {__packagename__} v{__version__} to v{latest}\nPlease restart the program for changes to take effect")
                sleep(3)
            except:
                print(f"\nFailed to update package {__packagename__} v{__version__} (Latest: v{latest})\nPlease consider using pip install {__packagename__} --upgrade")
                sleep(3)
        else:
            print(f"Package {__packagename__} already the latest version")
    except:
        print(f"Ignoring version check for {__packagename__} (Failed)")


class Imports:
    from enum import Enum
    class Colors(Enum):
        """
        colour-names to colour and priority dictionary
        mv: minimum verbosity required to output logs of that colour
        bg: background RGB tuple
        fg: foreground RGB tuple
        """
        red = {"mv": 15, "c": {"bg": (244, 67, 54), "fg": (255, 255, 255)}}
        red_50 = {"mv": 14, "c": {"bg": (255, 235, 238), "fg": (0, 0, 0)}}
        red_100 = {"mv": 13, "c": {"bg": (255, 205, 210), "fg": (0, 0, 0)}}
        red_200 = {"mv": 11, "c": {"bg": (239, 154, 154), "fg": (0, 0, 0)}}
        red_300 = {"mv": 9, "c": {"bg": (229, 115, 115), "fg": (0, 0, 0)}}
        red_400 = {"mv": 8, "c": {"bg": (239, 83, 80), "fg": (0, 0, 0)}}
        red_500 = {"mv": 6, "c": {"bg": (244, 67, 54), "fg": (255, 255, 255)}}
        red_600 = {"mv": 5, "c": {"bg": (229, 57, 53), "fg": (255, 255, 255)}}
        red_700 = {"mv": 4, "c": {"bg": (211, 47, 47), "fg": (255, 255, 255)}}
        red_800 = {"mv": 2, "c": {"bg": (198, 40, 40), "fg": (255, 255, 255)}}
        red_900 = {"mv": 1, "c": {"bg": (183, 28, 28), "fg": (255, 255, 255)}}
        red_100_accent = {"mv": 12, "c": {"bg": (255, 138, 128), "fg": (0, 0, 0)}}
        red_200_accent = {"mv": 10, "c": {"bg": (255, 82, 82), "fg": (255, 255, 255)}}
        red_400_accent = {"mv": 7, "c": {"bg": (255, 23, 68), "fg": (255, 255, 255)}}
        red_700_accent = {"mv": 3, "c": {"bg": (213, 0, 0), "fg": (255, 255, 255)}}
        deep_orange = {"mv": 15, "c": {"bg": (255, 87, 34), "fg": (255, 255, 255)}}
        deep_orange_50 = {"mv": 14, "c": {"bg": (251, 233, 231), "fg": (0, 0, 0)}}
        deep_orange_100 = {"mv": 13, "c": {"bg": (255, 204, 188), "fg": (0, 0, 0)}}
        deep_orange_200 = {"mv": 11, "c": {"bg": (255, 171, 145), "fg": (0, 0, 0)}}
        deep_orange_300 = {"mv": 9, "c": {"bg": (255, 138, 101), "fg": (0, 0, 0)}}
        deep_orange_400 = {"mv": 8, "c": {"bg": (255, 112, 67), "fg": (0, 0, 0)}}
        deep_orange_500 = {"mv": 6, "c": {"bg": (255, 87, 34), "fg": (255, 255, 255)}}
        deep_orange_600 = {"mv": 5, "c": {"bg": (244, 81, 30), "fg": (255, 255, 255)}}
        deep_orange_700 = {"mv": 4, "c": {"bg": (230, 74, 25), "fg": (255, 255, 255)}}
        deep_orange_800 = {"mv": 2, "c": {"bg": (216, 67, 21), "fg": (255, 255, 255)}}
        deep_orange_900 = {"mv": 1, "c": {"bg": (191, 54, 12), "fg": (255, 255, 255)}}
        deep_orange_100_accent = {"mv": 12, "c": {"bg": (255, 158, 128), "fg": (0, 0, 0)}}
        deep_orange_200_accent = {"mv": 10, "c": {"bg": (255, 110, 64), "fg": (0, 0, 0)}}
        deep_orange_400_accent = {"mv": 7, "c": {"bg": (255, 61, 0), "fg": (255, 255, 255)}}
        deep_orange_700_accent = {"mv": 3, "c": {"bg": (221, 44, 0), "fg": (255, 255, 255)}}
        orange = {"mv": 15, "c": {"bg": (255, 152, 0), "fg": (0, 0, 0)}}
        orange_50 = {"mv": 14, "c": {"bg": (255, 243, 224), "fg": (0, 0, 0)}}
        orange_100 = {"mv": 13, "c": {"bg": (255, 224, 178), "fg": (0, 0, 0)}}
        orange_200 = {"mv": 11, "c": {"bg": (255, 204, 128), "fg": (0, 0, 0)}}
        orange_300 = {"mv": 9, "c": {"bg": (255, 183, 77), "fg": (0, 0, 0)}}
        orange_400 = {"mv": 8, "c": {"bg": (255, 167, 38), "fg": (0, 0, 0)}}
        orange_500 = {"mv": 6, "c": {"bg": (255, 152, 0), "fg": (0, 0, 0)}}
        orange_600 = {"mv": 5, "c": {"bg": (251, 140, 0), "fg": (0, 0, 0)}}
        orange_700 = {"mv": 4, "c": {"bg": (245, 124, 0), "fg": (0, 0, 0)}}
        orange_800 = {"mv": 2, "c": {"bg": (239, 108, 0), "fg": (255, 255, 255)}}
        orange_900 = {"mv": 1, "c": {"bg": (230, 81, 0), "fg": (255, 255, 255)}}
        orange_100_accent = {"mv": 12, "c": {"bg": (255, 209, 128), "fg": (0, 0, 0)}}
        orange_200_accent = {"mv": 10, "c": {"bg": (255, 171, 64), "fg": (0, 0, 0)}}
        orange_400_accent = {"mv": 7, "c": {"bg": (255, 145, 0), "fg": (0, 0, 0)}}
        orange_700_accent = {"mv": 3, "c": {"bg": (255, 109, 0), "fg": (0, 0, 0)}}
        amber = {"mv": 15, "c": {"bg": (255, 193, 7), "fg": (0, 0, 0)}}
        amber_50 = {"mv": 14, "c": {"bg": (255, 248, 225), "fg": (0, 0, 0)}}
        amber_100 = {"mv": 13, "c": {"bg": (255, 236, 179), "fg": (0, 0, 0)}}
        amber_200 = {"mv": 11, "c": {"bg": (255, 224, 130), "fg": (0, 0, 0)}}
        amber_300 = {"mv": 9, "c": {"bg": (255, 213, 79), "fg": (0, 0, 0)}}
        amber_400 = {"mv": 8, "c": {"bg": (255, 202, 40), "fg": (0, 0, 0)}}
        amber_500 = {"mv": 6, "c": {"bg": (255, 193, 7), "fg": (0, 0, 0)}}
        amber_600 = {"mv": 5, "c": {"bg": (255, 179, 0), "fg": (0, 0, 0)}}
        amber_700 = {"mv": 4, "c": {"bg": (255, 160, 0), "fg": (0, 0, 0)}}
        amber_800 = {"mv": 2, "c": {"bg": (255, 143, 0), "fg": (0, 0, 0)}}
        amber_900 = {"mv": 1, "c": {"bg": (255, 111, 0), "fg": (0, 0, 0)}}
        amber_100_accent = {"mv": 12, "c": {"bg": (255, 229, 127), "fg": (0, 0, 0)}}
        amber_200_accent = {"mv": 10, "c": {"bg": (255, 215, 64), "fg": (0, 0, 0)}}
        amber_400_accent = {"mv": 7, "c": {"bg": (255, 196, 0), "fg": (0, 0, 0)}}
        amber_700_accent = {"mv": 3, "c": {"bg": (255, 171, 0), "fg": (0, 0, 0)}}
        yellow = {"mv": 15, "c": {"bg": (255, 235, 59), "fg": (0, 0, 0)}}
        yellow_50 = {"mv": 14, "c": {"bg": (255, 253, 231), "fg": (0, 0, 0)}}
        yellow_100 = {"mv": 13, "c": {"bg": (255, 249, 196), "fg": (0, 0, 0)}}
        yellow_200 = {"mv": 11, "c": {"bg": (255, 245, 157), "fg": (0, 0, 0)}}
        yellow_300 = {"mv": 9, "c": {"bg": (255, 241, 118), "fg": (0, 0, 0)}}
        yellow_400 = {"mv": 8, "c": {"bg": (255, 238, 88), "fg": (0, 0, 0)}}
        yellow_500 = {"mv": 6, "c": {"bg": (255, 235, 59), "fg": (0, 0, 0)}}
        yellow_600 = {"mv": 5, "c": {"bg": (253, 216, 53), "fg": (0, 0, 0)}}
        yellow_700 = {"mv": 4, "c": {"bg": (251, 192, 45), "fg": (0, 0, 0)}}
        yellow_800 = {"mv": 2, "c": {"bg": (249, 168, 37), "fg": (0, 0, 0)}}
        yellow_900 = {"mv": 1, "c": {"bg": (245, 127, 23), "fg": (0, 0, 0)}}
        yellow_100_accent = {"mv": 12, "c": {"bg": (255, 255, 141), "fg": (0, 0, 0)}}
        yellow_200_accent = {"mv": 10, "c": {"bg": (255, 255, 0), "fg": (0, 0, 0)}}
        yellow_400_accent = {"mv": 7, "c": {"bg": (255, 234, 0), "fg": (0, 0, 0)}}
        yellow_700_accent = {"mv": 3, "c": {"bg": (255, 214, 0), "fg": (0, 0, 0)}}
        lime = {"mv": 15, "c": {"bg": (205, 220, 57), "fg": (0, 0, 0)}}
        lime_50 = {"mv": 14, "c": {"bg": (249, 251, 231), "fg": (0, 0, 0)}}
        lime_100 = {"mv": 13, "c": {"bg": (240, 244, 195), "fg": (0, 0, 0)}}
        lime_200 = {"mv": 11, "c": {"bg": (230, 238, 156), "fg": (0, 0, 0)}}
        lime_300 = {"mv": 9, "c": {"bg": (220, 231, 117), "fg": (0, 0, 0)}}
        lime_400 = {"mv": 8, "c": {"bg": (212, 225, 87), "fg": (0, 0, 0)}}
        lime_500 = {"mv": 6, "c": {"bg": (205, 220, 57), "fg": (0, 0, 0)}}
        lime_600 = {"mv": 5, "c": {"bg": (192, 202, 51), "fg": (0, 0, 0)}}
        lime_700 = {"mv": 4, "c": {"bg": (175, 180, 43), "fg": (0, 0, 0)}}
        lime_800 = {"mv": 2, "c": {"bg": (158, 157, 36), "fg": (0, 0, 0)}}
        lime_900 = {"mv": 1, "c": {"bg": (130, 119, 23), "fg": (255, 255, 255)}}
        lime_100_accent = {"mv": 12, "c": {"bg": (244, 255, 129), "fg": (0, 0, 0)}}
        lime_200_accent = {"mv": 10, "c": {"bg": (238, 255, 65), "fg": (0, 0, 0)}}
        lime_400_accent = {"mv": 7, "c": {"bg": (198, 255, 0), "fg": (0, 0, 0)}}
        lime_700_accent = {"mv": 3, "c": {"bg": (174, 234, 0), "fg": (0, 0, 0)}}
        light_green = {"mv": 15, "c": {"bg": (139, 195, 74), "fg": (0, 0, 0)}}
        light_green_50 = {"mv": 14, "c": {"bg": (241, 248, 233), "fg": (0, 0, 0)}}
        light_green_100 = {"mv": 13, "c": {"bg": (220, 237, 200), "fg": (0, 0, 0)}}
        light_green_200 = {"mv": 11, "c": {"bg": (197, 225, 165), "fg": (0, 0, 0)}}
        light_green_300 = {"mv": 9, "c": {"bg": (174, 213, 129), "fg": (0, 0, 0)}}
        light_green_400 = {"mv": 8, "c": {"bg": (156, 204, 101), "fg": (0, 0, 0)}}
        light_green_500 = {"mv": 6, "c": {"bg": (139, 195, 74), "fg": (0, 0, 0)}}
        light_green_600 = {"mv": 5, "c": {"bg": (124, 179, 66), "fg": (0, 0, 0)}}
        light_green_700 = {"mv": 4, "c": {"bg": (104, 159, 56), "fg": (0, 0, 0)}}
        light_green_800 = {"mv": 2, "c": {"bg": (85, 139, 47), "fg": (255, 255, 255)}}
        light_green_900 = {"mv": 1, "c": {"bg": (51, 105, 30), "fg": (255, 255, 255)}}
        light_green_100_accent = {"mv": 12, "c": {"bg": (204, 255, 144), "fg": (0, 0, 0)}}
        light_green_200_accent = {"mv": 10, "c": {"bg": (178, 255, 89), "fg": (0, 0, 0)}}
        light_green_400_accent = {"mv": 7, "c": {"bg": (118, 255, 3), "fg": (0, 0, 0)}}
        light_green_700_accent = {"mv": 3, "c": {"bg": (100, 221, 23), "fg": (0, 0, 0)}}
        green = {"mv": 15, "c": {"bg": (76, 175, 80), "fg": (255, 255, 255)}}
        green_50 = {"mv": 14, "c": {"bg": (232, 245, 233), "fg": (0, 0, 0)}}
        green_100 = {"mv": 13, "c": {"bg": (200, 230, 201), "fg": (0, 0, 0)}}
        green_200 = {"mv": 11, "c": {"bg": (165, 214, 167), "fg": (0, 0, 0)}}
        green_300 = {"mv": 9, "c": {"bg": (129, 199, 132), "fg": (0, 0, 0)}}
        green_400 = {"mv": 8, "c": {"bg": (102, 187, 106), "fg": (0, 0, 0)}}
        green_500 = {"mv": 6, "c": {"bg": (76, 175, 80), "fg": (255, 255, 255)}}
        green_600 = {"mv": 5, "c": {"bg": (67, 160, 71), "fg": (255, 255, 255)}}
        green_700 = {"mv": 4, "c": {"bg": (56, 142, 60), "fg": (255, 255, 255)}}
        green_800 = {"mv": 2, "c": {"bg": (46, 125, 50), "fg": (255, 255, 255)}}
        green_900 = {"mv": 1, "c": {"bg": (27, 94, 32), "fg": (255, 255, 255)}}
        green_100_accent = {"mv": 12, "c": {"bg": (185, 246, 202), "fg": (0, 0, 0)}}
        green_200_accent = {"mv": 10, "c": {"bg": (105, 240, 174), "fg": (0, 0, 0)}}
        green_400_accent = {"mv": 7, "c": {"bg": (0, 230, 118), "fg": (0, 0, 0)}}
        green_700_accent = {"mv": 3, "c": {"bg": (0, 200, 83), "fg": (0, 0, 0)}}
        teal = {"mv": 15, "c": {"bg": (0, 150, 136), "fg": (255, 255, 255)}}
        teal_50 = {"mv": 14, "c": {"bg": (224, 242, 241), "fg": (0, 0, 0)}}
        teal_100 = {"mv": 13, "c": {"bg": (178, 223, 219), "fg": (0, 0, 0)}}
        teal_200 = {"mv": 11, "c": {"bg": (128, 203, 196), "fg": (0, 0, 0)}}
        teal_300 = {"mv": 9, "c": {"bg": (77, 182, 172), "fg": (0, 0, 0)}}
        teal_400 = {"mv": 8, "c": {"bg": (38, 166, 154), "fg": (0, 0, 0)}}
        teal_500 = {"mv": 6, "c": {"bg": (0, 150, 136), "fg": (255, 255, 255)}}
        teal_600 = {"mv": 5, "c": {"bg": (0, 137, 123), "fg": (255, 255, 255)}}
        teal_700 = {"mv": 4, "c": {"bg": (0, 121, 107), "fg": (255, 255, 255)}}
        teal_800 = {"mv": 2, "c": {"bg": (0, 105, 92), "fg": (255, 255, 255)}}
        teal_900 = {"mv": 1, "c": {"bg": (0, 77, 64), "fg": (255, 255, 255)}}
        teal_100_accent = {"mv": 12, "c": {"bg": (167, 255, 235), "fg": (0, 0, 0)}}
        teal_200_accent = {"mv": 10, "c": {"bg": (100, 255, 218), "fg": (0, 0, 0)}}
        teal_400_accent = {"mv": 7, "c": {"bg": (29, 233, 182), "fg": (0, 0, 0)}}
        teal_700_accent = {"mv": 3, "c": {"bg": (0, 191, 165), "fg": (0, 0, 0)}}
        cyan = {"mv": 15, "c": {"bg": (0, 188, 212), "fg": (255, 255, 255)}}
        cyan_50 = {"mv": 14, "c": {"bg": (224, 247, 250), "fg": (0, 0, 0)}}
        cyan_100 = {"mv": 13, "c": {"bg": (178, 235, 242), "fg": (0, 0, 0)}}
        cyan_200 = {"mv": 11, "c": {"bg": (128, 222, 234), "fg": (0, 0, 0)}}
        cyan_300 = {"mv": 9, "c": {"bg": (77, 208, 225), "fg": (0, 0, 0)}}
        cyan_400 = {"mv": 8, "c": {"bg": (38, 198, 218), "fg": (0, 0, 0)}}
        cyan_500 = {"mv": 6, "c": {"bg": (0, 188, 212), "fg": (255, 255, 255)}}
        cyan_600 = {"mv": 5, "c": {"bg": (0, 172, 193), "fg": (255, 255, 255)}}
        cyan_700 = {"mv": 4, "c": {"bg": (0, 151, 167), "fg": (255, 255, 255)}}
        cyan_800 = {"mv": 2, "c": {"bg": (0, 131, 143), "fg": (255, 255, 255)}}
        cyan_900 = {"mv": 1, "c": {"bg": (0, 96, 100), "fg": (255, 255, 255)}}
        cyan_100_accent = {"mv": 12, "c": {"bg": (132, 255, 255), "fg": (0, 0, 0)}}
        cyan_200_accent = {"mv": 10, "c": {"bg": (24, 255, 255), "fg": (0, 0, 0)}}
        cyan_400_accent = {"mv": 7, "c": {"bg": (0, 229, 255), "fg": (0, 0, 0)}}
        cyan_700_accent = {"mv": 3, "c": {"bg": (0, 184, 212), "fg": (0, 0, 0)}}
        light_blue = {"mv": 15, "c": {"bg": (3, 169, 244), "fg": (255, 255, 255)}}
        light_blue_50 = {"mv": 14, "c": {"bg": (225, 245, 254), "fg": (0, 0, 0)}}
        light_blue_100 = {"mv": 13, "c": {"bg": (179, 229, 252), "fg": (0, 0, 0)}}
        light_blue_200 = {"mv": 11, "c": {"bg": (129, 212, 250), "fg": (0, 0, 0)}}
        light_blue_300 = {"mv": 9, "c": {"bg": (79, 195, 247), "fg": (0, 0, 0)}}
        light_blue_400 = {"mv": 8, "c": {"bg": (41, 182, 246), "fg": (0, 0, 0)}}
        light_blue_500 = {"mv": 6, "c": {"bg": (3, 169, 244), "fg": (255, 255, 255)}}
        light_blue_600 = {"mv": 5, "c": {"bg": (3, 155, 229), "fg": (255, 255, 255)}}
        light_blue_700 = {"mv": 4, "c": {"bg": (2, 136, 209), "fg": (255, 255, 255)}}
        light_blue_800 = {"mv": 2, "c": {"bg": (2, 119, 189), "fg": (255, 255, 255)}}
        light_blue_900 = {"mv": 1, "c": {"bg": (1, 87, 155), "fg": (255, 255, 255)}}
        light_blue_100_accent = {"mv": 12, "c": {"bg": (128, 216, 255), "fg": (0, 0, 0)}}
        light_blue_200_accent = {"mv": 10, "c": {"bg": (64, 196, 255), "fg": (0, 0, 0)}}
        light_blue_400_accent = {"mv": 7, "c": {"bg": (0, 176, 255), "fg": (0, 0, 0)}}
        light_blue_700_accent = {"mv": 3, "c": {"bg": (0, 145, 234), "fg": (255, 255, 255)}}
        blue = {"mv": 15, "c": {"bg": (33, 150, 243), "fg": (255, 255, 255)}}
        blue_50 = {"mv": 14, "c": {"bg": (227, 242, 253), "fg": (0, 0, 0)}}
        blue_100 = {"mv": 13, "c": {"bg": (187, 222, 251), "fg": (0, 0, 0)}}
        blue_200 = {"mv": 11, "c": {"bg": (144, 202, 249), "fg": (0, 0, 0)}}
        blue_300 = {"mv": 9, "c": {"bg": (100, 181, 246), "fg": (0, 0, 0)}}
        blue_400 = {"mv": 8, "c": {"bg": (66, 165, 245), "fg": (0, 0, 0)}}
        blue_500 = {"mv": 6, "c": {"bg": (33, 150, 243), "fg": (255, 255, 255)}}
        blue_600 = {"mv": 5, "c": {"bg": (30, 136, 229), "fg": (255, 255, 255)}}
        blue_700 = {"mv": 4, "c": {"bg": (25, 118, 210), "fg": (255, 255, 255)}}
        blue_800 = {"mv": 2, "c": {"bg": (21, 101, 192), "fg": (255, 255, 255)}}
        blue_900 = {"mv": 1, "c": {"bg": (13, 71, 161), "fg": (255, 255, 255)}}
        blue_100_accent = {"mv": 12, "c": {"bg": (130, 177, 255), "fg": (0, 0, 0)}}
        blue_200_accent = {"mv": 10, "c": {"bg": (68, 138, 255), "fg": (255, 255, 255)}}
        blue_400_accent = {"mv": 7, "c": {"bg": (41, 121, 255), "fg": (255, 255, 255)}}
        blue_700_accent = {"mv": 3, "c": {"bg": (41, 98, 255), "fg": (255, 255, 255)}}
        indigo = {"mv": 15, "c": {"bg": (63, 81, 181), "fg": (255, 255, 255)}}
        indigo_50 = {"mv": 14, "c": {"bg": (232, 234, 246), "fg": (0, 0, 0)}}
        indigo_100 = {"mv": 13, "c": {"bg": (197, 202, 233), "fg": (0, 0, 0)}}
        indigo_200 = {"mv": 11, "c": {"bg": (159, 168, 218), "fg": (0, 0, 0)}}
        indigo_300 = {"mv": 9, "c": {"bg": (121, 134, 203), "fg": (255, 255, 255)}}
        indigo_400 = {"mv": 8, "c": {"bg": (92, 107, 192), "fg": (255, 255, 255)}}
        indigo_500 = {"mv": 6, "c": {"bg": (63, 81, 181), "fg": (255, 255, 255)}}
        indigo_600 = {"mv": 5, "c": {"bg": (57, 73, 171), "fg": (255, 255, 255)}}
        indigo_700 = {"mv": 4, "c": {"bg": (48, 63, 159), "fg": (255, 255, 255)}}
        indigo_800 = {"mv": 2, "c": {"bg": (40, 53, 147), "fg": (255, 255, 255)}}
        indigo_900 = {"mv": 1, "c": {"bg": (26, 35, 126), "fg": (255, 255, 255)}}
        indigo_100_accent = {"mv": 12, "c": {"bg": (140, 158, 255), "fg": (0, 0, 0)}}
        indigo_200_accent = {"mv": 10, "c": {"bg": (83, 109, 254), "fg": (255, 255, 255)}}
        indigo_400_accent = {"mv": 7, "c": {"bg": (61, 90, 254), "fg": (255, 255, 255)}}
        indigo_700_accent = {"mv": 3, "c": {"bg": (48, 79, 254), "fg": (255, 255, 255)}}
        deep_purple = {"mv": 15, "c": {"bg": (103, 58, 183), "fg": (255, 255, 255)}}
        deep_purple_50 = {"mv": 14, "c": {"bg": (237, 231, 246), "fg": (0, 0, 0)}}
        deep_purple_100 = {"mv": 13, "c": {"bg": (209, 196, 233), "fg": (0, 0, 0)}}
        deep_purple_200 = {"mv": 11, "c": {"bg": (179, 157, 219), "fg": (0, 0, 0)}}
        deep_purple_300 = {"mv": 9, "c": {"bg": (149, 117, 205), "fg": (255, 255, 255)}}
        deep_purple_400 = {"mv": 8, "c": {"bg": (126, 87, 194), "fg": (255, 255, 255)}}
        deep_purple_500 = {"mv": 6, "c": {"bg": (103, 58, 183), "fg": (255, 255, 255)}}
        deep_purple_600 = {"mv": 5, "c": {"bg": (94, 53, 177), "fg": (255, 255, 255)}}
        deep_purple_700 = {"mv": 4, "c": {"bg": (81, 45, 168), "fg": (255, 255, 255)}}
        deep_purple_800 = {"mv": 2, "c": {"bg": (69, 39, 160), "fg": (255, 255, 255)}}
        deep_purple_900 = {"mv": 1, "c": {"bg": (49, 27, 146), "fg": (255, 255, 255)}}
        deep_purple_100_accent = {"mv": 12, "c": {"bg": (179, 136, 255), "fg": (0, 0, 0)}}
        deep_purple_200_accent = {"mv": 10, "c": {"bg": (124, 77, 255), "fg": (255, 255, 255)}}
        deep_purple_400_accent = {"mv": 7, "c": {"bg": (101, 31, 255), "fg": (255, 255, 255)}}
        deep_purple_700_accent = {"mv": 3, "c": {"bg": (98, 0, 234), "fg": (255, 255, 255)}}
        purple = {"mv": 15, "c": {"bg": (156, 39, 176), "fg": (255, 255, 255)}}
        purple_50 = {"mv": 14, "c": {"bg": (243, 229, 245), "fg": (0, 0, 0)}}
        purple_100 = {"mv": 13, "c": {"bg": (225, 190, 231), "fg": (0, 0, 0)}}
        purple_200 = {"mv": 11, "c": {"bg": (206, 147, 216), "fg": (0, 0, 0)}}
        purple_300 = {"mv": 9, "c": {"bg": (186, 104, 200), "fg": (255, 255, 255)}}
        purple_400 = {"mv": 8, "c": {"bg": (171, 71, 188), "fg": (255, 255, 255)}}
        purple_500 = {"mv": 6, "c": {"bg": (156, 39, 176), "fg": (255, 255, 255)}}
        purple_600 = {"mv": 5, "c": {"bg": (142, 36, 170), "fg": (255, 255, 255)}}
        purple_700 = {"mv": 4, "c": {"bg": (123, 31, 162), "fg": (255, 255, 255)}}
        purple_800 = {"mv": 2, "c": {"bg": (106, 27, 154), "fg": (255, 255, 255)}}
        purple_900 = {"mv": 1, "c": {"bg": (74, 20, 140), "fg": (255, 255, 255)}}
        purple_100_accent = {"mv": 12, "c": {"bg": (234, 128, 252), "fg": (0, 0, 0)}}
        purple_200_accent = {"mv": 10, "c": {"bg": (224, 64, 251), "fg": (255, 255, 255)}}
        purple_400_accent = {"mv": 7, "c": {"bg": (213, 0, 249), "fg": (255, 255, 255)}}
        purple_700_accent = {"mv": 3, "c": {"bg": (170, 0, 255), "fg": (255, 255, 255)}}
        pink = {"mv": 15, "c": {"bg": (233, 30, 99), "fg": (255, 255, 255)}}
        pink_50 = {"mv": 14, "c": {"bg": (252, 228, 236), "fg": (0, 0, 0)}}
        pink_100 = {"mv": 13, "c": {"bg": (248, 187, 208), "fg": (0, 0, 0)}}
        pink_200 = {"mv": 11, "c": {"bg": (244, 143, 177), "fg": (0, 0, 0)}}
        pink_300 = {"mv": 9, "c": {"bg": (240, 98, 146), "fg": (0, 0, 0)}}
        pink_400 = {"mv": 8, "c": {"bg": (236, 64, 122), "fg": (0, 0, 0)}}
        pink_500 = {"mv": 6, "c": {"bg": (233, 30, 99), "fg": (255, 255, 255)}}
        pink_600 = {"mv": 5, "c": {"bg": (216, 27, 96), "fg": (255, 255, 255)}}
        pink_700 = {"mv": 4, "c": {"bg": (194, 24, 91), "fg": (255, 255, 255)}}
        pink_800 = {"mv": 2, "c": {"bg": (173, 20, 87), "fg": (255, 255, 255)}}
        pink_900 = {"mv": 1, "c": {"bg": (136, 14, 79), "fg": (255, 255, 255)}}
        pink_100_accent = {"mv": 12, "c": {"bg": (255, 128, 171), "fg": (0, 0, 0)}}
        pink_200_accent = {"mv": 10, "c": {"bg": (255, 64, 129), "fg": (255, 255, 255)}}
        pink_400_accent = {"mv": 7, "c": {"bg": (245, 0, 87), "fg": (255, 255, 255)}}
        pink_700_accent = {"mv": 3, "c": {"bg": (197, 17, 98), "fg": (255, 255, 255)}}
        brown = {"mv": 15, "c": {"bg": (121, 85, 72), "fg": (255, 255, 255)}}
        brown_50 = {"mv": 14, "c": {"bg": (239, 235, 233), "fg": (0, 0, 0)}}
        brown_100 = {"mv": 13, "c": {"bg": (215, 204, 200), "fg": (0, 0, 0)}}
        brown_200 = {"mv": 11, "c": {"bg": (188, 170, 164), "fg": (0, 0, 0)}}
        brown_300 = {"mv": 9, "c": {"bg": (161, 136, 127), "fg": (255, 255, 255)}}
        brown_400 = {"mv": 8, "c": {"bg": (141, 110, 99), "fg": (255, 255, 255)}}
        brown_500 = {"mv": 6, "c": {"bg": (121, 85, 72), "fg": (255, 255, 255)}}
        brown_600 = {"mv": 5, "c": {"bg": (109, 76, 65), "fg": (255, 255, 255)}}
        brown_700 = {"mv": 4, "c": {"bg": (93, 64, 55), "fg": (255, 255, 255)}}
        brown_800 = {"mv": 2, "c": {"bg": (78, 52, 46), "fg": (255, 255, 255)}}
        brown_900 = {"mv": 1, "c": {"bg": (62, 39, 35), "fg": (255, 255, 255)}}
        grey = {"mv": 15, "c": {"bg": (158, 158, 158), "fg": (0, 0, 0)}}
        grey_50 = {"mv": 14, "c": {"bg": (250, 250, 250), "fg": (0, 0, 0)}}
        grey_100 = {"mv": 13, "c": {"bg": (245, 245, 245), "fg": (0, 0, 0)}}
        grey_200 = {"mv": 11, "c": {"bg": (238, 238, 238), "fg": (0, 0, 0)}}
        grey_300 = {"mv": 9, "c": {"bg": (224, 224, 224), "fg": (0, 0, 0)}}
        grey_400 = {"mv": 8, "c": {"bg": (189, 189, 189), "fg": (0, 0, 0)}}
        grey_500 = {"mv": 6, "c": {"bg": (158, 158, 158), "fg": (0, 0, 0)}}
        grey_600 = {"mv": 5, "c": {"bg": (117, 117, 117), "fg": (255, 255, 255)}}
        grey_700 = {"mv": 4, "c": {"bg": (97, 97, 97), "fg": (255, 255, 255)}}
        grey_800 = {"mv": 2, "c": {"bg": (66, 66, 66), "fg": (255, 255, 255)}}
        grey_900 = {"mv": 1, "c": {"bg": (33, 33, 33), "fg": (255, 255, 255)}}
        blue_grey = {"mv": 15, "c": {"bg": (96, 125, 139), "fg": (255, 255, 255)}}
        blue_grey_50 = {"mv": 14, "c": {"bg": (236, 239, 241), "fg": (0, 0, 0)}}
        blue_grey_100 = {"mv": 13, "c": {"bg": (207, 216, 220), "fg": (0, 0, 0)}}
        blue_grey_200 = {"mv": 11, "c": {"bg": (176, 190, 197), "fg": (0, 0, 0)}}
        blue_grey_300 = {"mv": 9, "c": {"bg": (144, 164, 174), "fg": (0, 0, 0)}}
        blue_grey_400 = {"mv": 8, "c": {"bg": (120, 144, 156), "fg": (255, 255, 255)}}
        blue_grey_500 = {"mv": 6, "c": {"bg": (96, 125, 139), "fg": (255, 255, 255)}}
        blue_grey_600 = {"mv": 5, "c": {"bg": (84, 110, 122), "fg": (255, 255, 255)}}
        blue_grey_700 = {"mv": 4, "c": {"bg": (69, 90, 100), "fg": (255, 255, 255)}}
        blue_grey_800 = {"mv": 2, "c": {"bg": (55, 71, 79), "fg": (255, 255, 255)}}
        blue_grey_900 = {"mv": 1, "c": {"bg": (38, 50, 56), "fg": (255, 255, 255)}}
        black = {"mv": 15, "c": {"bg": (0, 0, 0), "fg": (255, 255, 255)}}
        white = {"mv": 15, "c": {"bg": (255, 255, 255), "fg": (0, 0, 0)}}


class CustomisedLogs:
    def __init__(self, verbosity: int = 100, maxLogCount: int = 100):
        """
        Initialise the CustomisedLogs and then use the public functions to display colored logs
        :param verbosity: Integer value to set minimum threshold of log verbosity
        :param maxLogCount: Maximum count of logs to store in memory, Values available as list in `CustomisedLogs.history`
        """
        from colr import color as __colorPack
        from time import ctime as __ctimePack
        self.Colors = Imports.Colors
        self.history = []
        self.__colorPack = __colorPack
        self.__ctimePack = __ctimePack
        self._verbosity = verbosity
        self._maxLogCount = maxLogCount

    def __log(self, string: str, back: tuple[int, int, int], fore: tuple[int, int, int]):
        """
        Private function to finally print the colored text onto terminal and remove older logs if exceeds max count.
        :param string: The string to print
        :param back: RGB tuple specifying the background color
        :param fore: RGB tuple specifying the foreground color
        :return:
        """
        self.history.append(string)
        if len(self.history) > self._maxLogCount:
            self.history.pop(0)
        print(self.__colorPack(string, back=back, fore=fore))

    def __formString(self, category: str, *args) -> str:
        """
        Decorate the log string and all other arguments passed into a single string
        :param category: A string representing the category of the log (user defined)
        :param args: Additional parameters needed to be logged
        :return:
        """
        return f"[{self.__ctimePack()}] [{category}] {' '.join([str(arg) for arg in args])} "

    def log(self, color: Imports.Colors, category: str, *args) -> str:
        """
        Accepts color and other parameters to compile into the final output with colours
        :param color: Must be a Member of CustomisedLogs.Colors
        :param category: String representing the category of the log (user defined)
        :param args: Additional parameters needed to be logged
        :return: 
        """
        try:
            if color.name not in self.Colors._member_names_: raise
        except:
            self.log(self.Colors.grey, "INVALID-COLOR", f"{color} must be a member of `LoggerPack.Colors`")
            color = self.Colors.black
        string = self.__formString(category, *args)
        if color.value["mv"] <= self._verbosity:
            self.__log(string, back=color.value["c"]["bg"], fore=color.value["c"]["fg"])
        return string
