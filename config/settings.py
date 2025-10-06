"""
Configuration settings for Silver Guard
"""

# Game settings
POINTS_CORRECT = 10
POINTS_INCORRECT = -5
SCENARIOS_TO_WIN = 5

# Scam detection thresholds
URGENCY_THRESHOLD = 0.7
SUSPICIOUS_KEYWORDS_MIN = 2

# Colors for terminal output (ANSI codes)
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

# Scam indicator keywords
SCAM_KEYWORDS = [
    'urgent', 'immediately', 'verify', 'suspended', 'account',
    'social security', 'IRS', 'lawsuit', 'arrest', 'warrant',
    'prize', 'winner', 'congratulations', 'claim', 'limited time',
    'wire transfer', 'gift card', 'bitcoin', 'confirm', 'password',
    'click here', 'act now', 'expires', 'final notice'
]
