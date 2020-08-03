# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 17:34:39 2020

@author: User
"""

from mcpi.minecraft import Minecraft
import timemc = Minecraft.create()
time.sleep(5)
x,y,z =mc.player.getTilePos()
mc.setBlock(x,y,z,206)
mc.setBlock(x,y+1,z,206)
mc.setBlock(x,y+2,z,206)
mc.setBlock(x,y+3,z,206)
mc.setBlock(x,y+4,z,206)
mc.setBlock(x,y+5,z,206)
mc.setBlock(x,y+6,z,206)
mc.setBlock(x,y+7,z,206)
mc.setBlock(x,y+8,z,206)
mc.setBlock(x,y+9,z,206)


from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x, y, z = mc.player.getTilePos()
mc.setBlock(x, y-1, z+1 ,206)
mc.setBlock(x, y-1, z-1 ,206)
mc.setBlock(x+1, y-1, z ,206)
mc.setBlock(x-1, y-1, z ,206)
mc.setBlock(x-1, y-1, z+1 ,206)
mc.setBlock(x+1, y-1, z+1 ,206)
mc.setBlock(x+1, y-1, z-1 ,206)
mc.setBlock(x-1, y-1, z-1,206)

mc.postToChat("I'm watching you")

while True:
    x, y, z = mc.player.getTilePos()
    mc.postToChat("You are located on X:" + str(x) 
                  + ", Y:" +str(y) + ", Z:" + str(z))


