#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 17:10:49 2019

@author: 3672216
"""

from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu

from soccersimulator import settings
import math


class MyState(object):
    def __init__(self,state,idteam,idplayer):
        self.state = state
        self.id_team=idteam
        self.id_player= idplayer
        self.key = (idteam,idplayer)
    
    @property
    def ball_vitesse(self):
        return self.state.ball.vitesse
    
   
    
    
    @property
    def liste_equipier(self):
        return [self.state.player_state(id_team, id_player).position for (id_team, id_player) in self.state.players if id_team == self.id_team]
    
  
    @property
    #retourne la liste des opposants
    def listeop(self):
        return [self.state.player_state(id_team, id_player).position for (id_team , id_player) in self.state.players if id_team != self.id_team]
    
    @property
    #retourne l'opposant le plus proche
    def oppleplusproche(self):
        opponent = self.listeop
        return min([(self.my_position.distance(player), player) for player in opponent])[1]
    @property
    def equipier_le_plus_proche(self):
        equipier=self.liste_equipier
        return min([(self.my_position.distance(player), player) for player in equipier])[1]
    
    @property
    def coequipier(self):   
        for (id_team, id_player) in self.state.players :
            if (id_team == self.id_team) and (id_player != self.id_player): 
                return self.state.player_state(id_team, id_player).position
            
#====================================================================================================================================
#        Position
    @property
    def my_position(self):
      return self.state.player_state(self.id_team,self.id_player).position
    
    @property
    def id_team_adv(self):
        id_team = 2
        if (self.id_team == 1):
            return id_team
        else:
            id_team = 1
            return id_team
        
    @property    
    def position_adv(self):
        m = self.id_team_adv
        if (m != self.id_team):
            return self.state.player_state(m, self.id_player).position
    
    @property    
    def position_adv_x(self):
        m = self.id_team_adv
        if (m != self.id_team):
            return self.state.player_state(m, self.id_player).position.x
        
    @property    
    def position_adv_y(self):
        m = self.id_team_adv
        if (m != self.id_team):
            return self.state.player_state(m, self.id_player).position.y
        
    @property
    def my_positionx(self):
      return self.state.player_state(self.id_team,self.id_player).position.x
  
    @property
    def my_positiony(self):
      return self.state.player_state(self.id_team,self.id_player).position.y

    @property
    def ball_position(self):
        return self.state.ball.position
    @property
    def ball_positionx(self):
        return self.state.ball.position.x
    @property
    def ball_positiony(self):
        return self.state.ball.position.y
    
    @property
    def ball_position_futur(self):
         return self.ball_position+ 5 * self.ball_vitesse
     
    @property
    def adv_position_futur(self):
         return self.position_adv + 5 * settings.maxPlayerSpeed

    @property
    def distance_balle (self): 
        return self.ball_position.distance(self.player)
    
    @property
    def distance_balle_adv_proche(self):
        return self.ball_position.distance(self.opposant_le_plus_proche)
    
    @property    
    def adv_plus_proche_ball(self):
        opp = self.liste_opposant
        return min([(self.ball_position.distance(player),player)for player in opp])
        
    @property
    def goal(self):
        if(self.id_team == 2):
            return Vector2D(0,settings.GAME_HEIGHT/2)
        else :
            return Vector2D(settings.GAME_WIDTH, settings.GAME_HEIGHT/2)
   
    @property
    def corner(self):
       return  Vector2D((2-self.id_team)*settings.GAME_WIDTH,settings.GAME_HEIGHT)
   
    @property
    def corner_haut(self):
       return  Vector2D(0,settings.GAME_HEIGHT)
   
    @property
    def corner_bas(self):
       return  Vector2D(0,0)
   
   
    @property 
    def coequipier(self):   
        for (id_team, id_player) in self.state.players :
            if (id_team == self.id_team) and (id_player != self.id_player) : 
                return self.state.player_state(id_team, id_player).position
    @property
    def entreballetbut(self):
        vecteurballbut=Vector2D(((2-self.id_team)*settings.GAME_WIDTH)-self.ball_positionx,settings.GAME_HEIGHT/2.-self.ball_positiony)
        vecteurballjoueur=Vector2D(self.my_positionx-self.ball_positionx,self.my_positiony-self.ball_positiony)
        return SoccerAction(vecteurballbut - vecteurballjoueur)
    
            

    @property
    def att(self):
        if self.id_team == 1 :
            (posattx,nextpos) = (self.my_positionx < settings.GAME_WIDTH*(1/2), settings.GAME_WIDTH*(3/5))
        else : 
            (posattx,nextpos) = (self.my_positionx > settings.GAME_WIDTH*(1/2), settings.GAME_WIDTH*(2/5))
        return (posattx,nextpos)
    
    @property
    def defe(self):
        if self.id_team == 1 :
            (posdef,condition) = (1/4, self.ball_position_futur.x > settings.GAME_WIDTH*(1/3))
        else : 
            (posdef, condition) = (3/4, self.ball_position_futur.x < settings.GAME_WIDTH*(2/3))
        return (posdef,condition)
    
    @property
    def posaillier1(self):   
        for (id_team, id_player) in self.state.players :
            if (id_team == self.id_team) and (id_player != self.id_player) and (id_player == 1):
                return self.state.player_state(id_team, id_player).position
            
    @property
    def posaillier2(self):   
        for (id_team, id_player) in self.state.players :
            if (id_team == self.id_team) and (id_player != self.id_player) and (id_player == 2):
                return self.state.player_state(id_team, id_player).position
    
    @property
    def posattaquant(self):   
        for (id_team, id_player) in self.state.players :
            if (id_team == self.id_team) and (id_player != self.id_player) and (id_player == 0): 
                return self.state.player_state(id_team, id_player).position 
    @property
    def stratatt(self):
        if self.att[0] :
            #if self.my_positiony < settings.GAME_HEIGHT/2 :
                if self.my_position.distance(self.ball_position)<settings.PLAYER_RADIUS + settings.BALL_RADIUS :
                    return SoccerAction(shoot=Vector2D(self.att[1], 0)-self.my_position)
                else :
                    return SoccerAction(acceleration=self.ball_position_futur-self.my_position) 
            #else : 
               # if self.my_position.distance(self.ball_position)<settings.PLAYER_RADIUS + settings.BALL_RADIUS :
                   # return SoccerAction(shoot=Vector2D(self.att[1], settings.GAME_HEIGHT)-self.my_position)
               # else :
                   # return SoccerAction(acceleration=self.ball_position_futur-self.my_position)
        else : 
            if self.my_position.distance(self.ball_position)<settings.PLAYER_RADIUS + settings.BALL_RADIUS :
                return SoccerAction(shoot=self.goal-self.my_position)
            else :
                return SoccerAction(acceleration=self.ball_position_futur-self.my_position)