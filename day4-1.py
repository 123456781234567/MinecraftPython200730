# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 09:24:01 2020

@author: user
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
number = 1
x,y,z = mc.player.getPos()
for i in range(200):
    for j in range(number):
        mc.spawnEntity(x,y,z,385)
    number = number * 2
    mc.postToChat(str(number)+" silver fish(s) are generated")