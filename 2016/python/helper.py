# -*- coding: utf-8 -*-

"""Helper functions"""
import os

__author__ = "Filip Koprivec"


def get_file(day, mode="r"):
    return open("../" + "input" + os.sep + str(day) + ".in", mode=mode)
