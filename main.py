#!/usr/bin/env python3
"""
Silver Guard Demo Game
Entry point for the Scam Detective training game
"""

from src.game import ScamDetectiveGame


def main():
    """Run the game"""
    try:
        game = ScamDetectiveGame()
        game.play()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()
