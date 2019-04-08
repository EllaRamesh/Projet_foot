#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 18:11:12 2019

@author: 3670714
"""


from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam
from soccersimulator import VolleySimulation, volley_show_simu
from soccersimulator import settings

class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        return SoccerAction(Vector2D.create_random(),Vector2D.create_random())
    
    
class Attaque(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Attaque")
       

    def compute_strategy(self, state, id_team, id_player):
#        listeop = [state.player_state(id_team, id_player).position for (id_team , id_player) in self.state.players if id_team != self.id_team]
#        op_le_plus_proche = min([(state.player_state(id_team,id_player).position.distance(player), player) for player in listeop])[1]
        id_team_adv = 2
        if (id_team == 1):
            id_team_adv = 2
        else:
            id_team_adv = 1
        if (id_team_adv != id_team):
            pos_adv_x = state.player_state(id_team_adv , id_player).position.x
            pos_adv_y = state.player_state(id_team_adv , id_player).position.y
            pos_adv = state.player_state(id_team_adv ,id_player).position
        
        v1 = pos_adv - state.ball.position+ 5 * state.ball.vitesse
        v2 = v1.normalize()*10
        
        cours_vers_ballon = SoccerAction((state.ball.position+ 5 * state.ball.vitesse)- state.player_state(id_team,id_player).position)
        
        if(id_team == 2):
            if (pos_adv_x > settings.GAME_WIDTH/2. and pos_adv_y > settings.GAME_HEIGHT/2. ):
                return SoccerAction(state.ball.position+ 5 * state.ball.vitesse -  Vector2D(settings.GAME_WIDTH - 50, 30), v2) + cours_vers_ballon
            else : 
                return SoccerAction(state.ball.position+ 5 * state.ball.vitesse -  Vector2D(settings.GAME_WIDTH - 50, 75), v2) + cours_vers_ballon
        else:
            if (pos_adv_x > settings.GAME_WIDTH/2. and pos_adv_y > settings.GAME_HEIGHT/2. ):
                return SoccerAction(state.ball.position+ 5 * state.ball.vitesse -  Vector2D(settings.GAME_WIDTH/4., 30), v2) + cours_vers_ballon
            else : 
                return SoccerAction(state.ball.position+ 5 * state.ball.vitesse -  Vector2D(settings.GAME_WIDTH/4. , 45), v2) + cours_vers_ballon
# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Player 1", Attaque())  # Random strategy
team2.add("Player 2", Attaque())   # Random strategy

# Create a match
simu = VolleySimulation(team1, team2)

# Simulate and display the match
volley_show_simu(simu)