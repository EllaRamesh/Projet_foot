#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:16:29 2019

@author: 3672216
"""

from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from .tools import *

from soccersimulator import settings
import math


class Move(object):
    def __init__(self,MyState):
        self.MyState = MyState
        
    @property
    def cour_vers_ballon(self):
        return SoccerAction(self.MyState.ball_position - self.MyState.my_position)
    
    def deplaceVers(self, pointx, pointy):
        dep = Vector2D(pointx, pointy)
        return SoccerAction(dep - self.MyState.my_position)
    
   
    
    
    
class Shoot(object):
    def __init__(self,MyState):
        self.MyState = MyState
        
       
    @property
    def tire_vers_but(self):
        return SoccerAction(self.MyState.ball_position_futur - self.MyState.my_position, self.MyState.goal - self.MyState.ball_position_futur)
    
    def tire_vers(self,position,puissance):
        v1=position - self.MyState.ball_position_futur
        v2=v1.normalize()*puissance
        return SoccerAction(self.MyState.ball_position_futur - self.MyState.my_position, v2)
   
    
    def petit_tire(self,pos):
        
        v1= pos-self.MyState.my_position
        return v1.normalize()*1.2     
        

    
        
        
#    def passe_att_att(self, puissance, position):
#        
#        