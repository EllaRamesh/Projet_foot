#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 17:04:04 2019

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
    
    
class Echauffement(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Echauffement")
       

    def compute_strategy(self, state, id_team, id_player):
#        s = tools.MyState(state,id_team,id_player)
#        t = action.Shoot(s)
#        return t.tire_vers_but
#        self.state = state
#        self.id_team = idteam
#        self.id_player = idplayer
#        self.key = (idteam,idplayer)
        
        if(id_team == 2):
            return SoccerAction(state.ball.position+ 5 * state.ball.vitesse - state.player_state(id_team,id_player).position, Vector2D(0,settings.GAME_HEIGHT/2) - state.ball.position+ 5 * state.ball.vitesse)
        else:
            return SoccerAction(state.ball.position+ 5 * state.ball.vitesse - state.player_state(id_team,id_player).position, Vector2D(settings.GAME_WIDTH, settings.GAME_HEIGHT/2) - state.ball.position+ 5 * state.ball.vitesse)
# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Player 1", Echauffement())  # Random strategy
team2.add("Player 2", Echauffement())   # Random strategy

# Create a match
simu = VolleySimulation(team1, team2)

# Simulate and display the match
volley_show_simu(simu)