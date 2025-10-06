"""
User interface functions for the terminal game
"""

import time
from config.settings import Colors


def print_header():
    """Display game header"""
    print("\n" + "=" * 70)
    print(f"{Colors.CYAN}{Colors.BOLD}🛡️  SILVER GUARD - SCAM DETECTIVE TRAINING{Colors.END}")
    print("=" * 70 + "\n")


def print_scenario(scenario_num, total, scenario_type, sender, message):
    """Display a scenario to the player"""
    print(f"\n{Colors.YELLOW}📱 Scenario {scenario_num}/{total}{Colors.END}")
    print(f"{Colors.BOLD}Type:{Colors.END} {scenario_type.upper()}")
    
    if scenario_type == "phone":
        print(f"{Colors.BOLD}Caller:{Colors.END} {sender}")
    else:
        print(f"{Colors.BOLD}From:{Colors.END} {sender}")
    
    print(f"\n{Colors.WHITE}{message}{Colors.END}\n")
    print("-" * 70)


def print_analysis(analysis):
    """Display AI analysis of the message"""
    print(f"\n{Colors.CYAN}🤖 Silver Guard Analysis:{Colors.END}")
    print(f"  Risk Level: {get_risk_color(analysis['risk_level'])}{analysis['risk_level']}{Colors.END}")
    print(f"  Suspicious Keywords Found: {analysis['keyword_count']}")
    
    if analysis['found_keywords']:
        keywords_str = ", ".join(analysis['found_keywords'])
        print(f"  Examples: {Colors.YELLOW}{keywords_str}{Colors.END}")
    
    if analysis['has_suspicious_request']:
        print(f"  {Colors.RED}⚠️  Contains suspicious requests{Colors.END}")
    
    print(f"  Urgency Level: {int(analysis['urgency_score'] * 100)}%")


def get_risk_color(risk_level):
    """Return appropriate color for risk level"""
    if risk_level == "HIGH":
        return Colors.RED + Colors.BOLD
    elif risk_level == "MEDIUM":
        return Colors.YELLOW
    else:
        return Colors.GREEN


def print_result(correct, points, explanation):
    """Display whether the player was correct"""
    print("\n" + "=" * 70)
    if correct:
        print(f"{Colors.GREEN}{Colors.BOLD}✅ CORRECT! +{points} points{Colors.END}")
    else:
        print(f"{Colors.RED}{Colors.BOLD}❌ INCORRECT! {points} points{Colors.END}")
    
    print(f"\n{explanation}")
    print("=" * 70)
    time.sleep(2)


def print_score(score, scenarios_completed, total_scenarios):
    """Display current score"""
    print(f"\n{Colors.BOLD}Score: {score} | Progress: {scenarios_completed}/{total_scenarios}{Colors.END}")


def print_final_score(score, total):
    """Display final game results"""
    print("\n" + "=" * 70)
    print(f"{Colors.CYAN}{Colors.BOLD}🎮 GAME OVER!{Colors.END}")
    print("=" * 70)
    print(f"\nFinal Score: {Colors.BOLD}{score}{Colors.END} points")
    print(f"Scenarios Completed: {total}")
    
    percentage = (score / (total * 10)) * 100 if total > 0 else 0
    
    if percentage >= 80:
        print(f"\n{Colors.GREEN}🏆 Excellent! You're a Scam Detection Expert!{Colors.END}")
    elif percentage >= 60:
        print(f"\n{Colors.YELLOW}👍 Good job! You're getting the hang of it!{Colors.END}")
    else:
        print(f"\n{Colors.RED}📚 Keep practicing! Scammers are tricky!{Colors.END}")
    
    print("\nRemember: Silver Guard will help protect against these scams in real-time!")
    print("=" * 70 + "\n")


def get_player_input():
    """Get player's scam/legit decision"""
    while True:
        print(f"\n{Colors.BOLD}Is this a SCAM or LEGITIMATE?{Colors.END}")
        choice = input("Enter 'S' for Scam or 'L' for Legitimate: ").strip().upper()
        
        if choice in ['S', 'L']:
            return choice == 'S'
        else:
            print(f"{Colors.RED}Invalid input. Please enter 'S' or 'L'.{Colors.END}")


def show_analysis_option():
    """Ask if player wants to see AI analysis"""
    choice = input(f"\n{Colors.CYAN}See AI analysis? (y/n): {Colors.END}").strip().lower()
    return choice == 'y'
