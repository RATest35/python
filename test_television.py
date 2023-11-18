import unittest
from television import *


class TestCase(unittest.TestCase):

    def test___init__(self):
        test = Television()
        self.assertEqual(str(test), f'Power - [False], Channel - [0], Volume - [0]')

    def test_power(self):
        test = Television()
        test.power()
        self.assertEqual(str(test), f'Power - [True], Channel - [0], Volume - [0]')
        test.power()
        self.assertEqual(str(test), f'Power - [False], Channel - [0], Volume - [0]')

    def test_mute(self):
        test = Television()
        test.power()
        test.volume_up()
        test.mute()
        self.assertEqual(str(test), f'Power - [True], Channel - [0], Volume - [0]')
        test.mute()
        self.assertEqual(str(test), f'Power - [True], Channel - [0], Volume - [1]')
        test.power()
        test.mute()
        self.assertEqual(str(test), f'Power - [False], Channel - [0], Volume - [1]')
        test.mute()
        self.assertEqual(str(test), f'Power - [False], Channel - [0], Volume - [1]')

    def test_channel_up(self):
        test = Television()
        test.channel_up()
        self.assertEqual(str(test), f'Power - [False], Channel - [0], Volume - [0]')
        test.power()
        test.channel_up()
        self.assertEqual(str(test), f'Power - [True], Channel - [1], Volume - [0]')
        test.channel_up()
        test.channel_up()
        test.channel_up()
        self.assertEqual(str(test), f'Power - [True], Channel - [0], Volume - [0]')

    def test_channel_down(self):
        test = Television()
        test.channel_down()
        self.assertEqual(str(test), f'Power - [False], Channel - [0], Volume - [0]')
        test.power()
        test.channel_down()
        self.assertEqual(str(test), f'Power - [True], Channel - [3], Volume - [0]')

    def test_volume_up(self):
        test = Television()
        test.volume_up()
        self.assertEqual(str(test), f'Power - [False], Channel - [0], Volume - [0]')
        test.power()
        test.volume_up()
        self.assertEqual(str(test), f'Power - [True], Channel - [0], Volume - [1]')
        test.mute()
        test.volume_up()
        self.assertEqual(str(test), f'Power - [True], Channel - [0], Volume - [2]')
        test.volume_up()
        self.assertEqual(str(test), f'Power - [True], Channel - [0], Volume - [2]')

    def test_volume_down(self):
        test = Television()
        test.volume_down()
        self.assertEqual(str(test), f'Power - [False], Channel - [0], Volume - [0]')
        test.power()
        test.volume_up()
        test.volume_up()
        test.volume_down()
        self.assertEqual(str(test), f'Power - [True], Channel - [0], Volume - [1]')
        test.mute()
        test.volume_down()
        self.assertEqual(str(test), f'Power - [True], Channel - [0], Volume - [0]')
        test.volume_down()
        self.assertEqual(str(test), f'Power - [True], Channel - [0], Volume - [0]')
