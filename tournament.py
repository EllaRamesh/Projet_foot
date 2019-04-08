#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 16:29:58 2019

@author: 3672216
"""

from mbappepresident import Fonceur2Strategy, DefenseStrategy,FonceurStrategy
from soccersimulator import Simulation, show_simu
from mbappepresident import get_team

team1 = get_team(1)
team2 = get_team(1)

# Add players
#team1.add("Random", RandomStrategy()) 
#team2.add("manel", DefenseStrategy())  # Random strategy
#team1.add("zizou", FonceurStrategy())   # Static strategy

simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)