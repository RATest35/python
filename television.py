class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

    def power(self):
        """
        Switches the status between status: On or Off
        :return:
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self):
        """
        Switches the mute status from On or Off
        :return:
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.MIN_VOLUME
                self.MIN_VOLUME = 0
            else:
                self.__muted = True
                self.MIN_VOLUME = self.__volume
                self.__volume = 0

    def channel_up(self):
        """
        Increases channel and if channel is max sets channel to minimum
        :return:
        """
        if self.__status:
            if self.__channel < self.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self):
        """
        Decreases channel and if channel is min sets channel to max
        :return:
        """
        if self.__status:
            if self.__channel > self.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self):
        """
        Unmutes TV then increases volume unless volume is max then nothing happens
        :return:
        """
        if self.__status:
            if self.__muted:
                self.mute()
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """
        Unmutes TV then increases volume unless volume is max then nothing happens
        :return:
        """
        if self.__status:
            if self.__muted:
                self.mute()
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        return f'Power - [{self.__status}], Channel - [{self.__channel}], Volume - [{self.__volume}]'
