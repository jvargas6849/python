class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Initialize the television with its default settings
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Turn on/off the television
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        Mutes or unmutes the television
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self) -> None:
        """
        Increases the television channel up
        Loops back to min once reaches max channel
        """
        if self.__status:
            self.__channel = self.__channel + 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decreases the television channel down
        Loops back to max once reaches min channel
        """
        if self.__status:
            self.__channel = self.__channel - 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL


    def volume_up(self) -> None:
        """
        Increases the television volume up
        Volume remains at max volume once reaches max volume
        """
        if self.__status:
            self.__muted = False
            self.__volume = self.__volume + 1
            if self.__volume > Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME

    def volume_down(self) -> None:
        """
        Decrease the television volume down
        Volume remains at min volume once reaches min volume
        """
        if self.__status:
            self.__muted = False
            self.__volume = self.__volume - 1
            if self.__volume < Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME

    def __str__(self) -> str:
        """
        Shows the television status, channel and volume
        :return: The string representation of the television
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = 0'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'