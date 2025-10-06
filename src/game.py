"""
Main game logic
"""

import json
import random
from src.scam_detector import ScamDetector
from src.ui import *
from config.settings import POINTS_CORRECT, POINTS_INCORRECT


class ScamDetectiveGame:
    """Main game controller"""
    
    def __init__(self):
        self.detector = ScamDetector()
        self.score = 0
        self.scenarios_completed = 0
        self.scenarios = self.load_scenarios()
    
    def load_scenarios(self):
        """Load scenarios from JSON file"""
        try:
            with open('data/scam_scenarios.json', 'r') as f:
                data = json.load(f)
                return data['scenarios']
        except FileNotFoundError:
            print(f"{Colors.RED}Error: scam_scenarios.json not found!{Colors.END}")
            return []
    
    def play(self):
        """Main game loop"""
        print_header()
        print(f"{Colors.WHITE}Welcome to Scam Detective Training!{Colors.END}")
        print(f"Learn to identify scams just like Silver Guard does.\n")
        input("Press Enter to start...")
        
        # Shuffle scenarios for variety
        random.shuffle(self.scenarios)
        
        for scenario in self.scenarios:
            self.play_scenario(scenario)
        
        print_final_score(self.score, self.scenarios_completed)
    
    def play_scenario(self, scenario):
        """Play a single scenario"""
        self.scenarios_completed += 1
        
        # Display scenario
        print_scenario(
            self.scenarios_completed,
            len(self.scenarios),
            scenario['type'],
            scenario.get('caller', scenario.get('sender', 'Unknown')),
            scenario['message']
        )
        
        # Optional: Show AI analysis
        if show_analysis_option():
            analysis = self.detector.analyze_message(scenario['message'])
            print_analysis(analysis)
        
        # Get player decision
        player_thinks_scam = get_player_input()
        
        # Check answer
        correct = player_thinks_scam == scenario['is_scam']
        points = POINTS_CORRECT if correct else POINTS_INCORRECT
        self.score += points
        
        # Show result
        print_result(correct, points, scenario['explanation'])
        print_score(self.score, self.scenarios_completed, len(self.scenarios))
