#!/usr/bin/env python

import discord
from toscanbot import ToscanBot
import yaml

with open('config/settings.yml', 'r') as stream:
    BotSettings = yaml.safe_load(stream)


bot = ToscanBot()

