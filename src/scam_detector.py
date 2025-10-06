"""
Scam detection logic - analyzes messages for scam indicators
"""

from config.settings import SCAM_KEYWORDS, URGENCY_THRESHOLD


class ScamDetector:
    """Analyzes messages and identifies potential scams"""
    
    def __init__(self):
        self.scam_keywords = SCAM_KEYWORDS
    
    def analyze_message(self, message):
        """
        Analyze a message for scam indicators
        Returns: dict with analysis results
        """
        message_lower = message.lower()
        
        # Check for scam keywords
        found_keywords = [kw for kw in self.scam_keywords if kw in message_lower]
        keyword_count = len(found_keywords)
        
        # Check for urgency indicators
        urgency_words = ['urgent', 'immediately', 'now', 'expires', 'final', 'last chance']
        urgency_score = sum(1 for word in urgency_words if word in message_lower) / len(urgency_words)
        
        # Check for suspicious requests
        suspicious_requests = [
            'social security number', 'password', 'pin', 'account number',
            'wire transfer', 'gift card', 'bitcoin', 'click here', 'verify'
        ]
        has_suspicious_request = any(req in message_lower for req in suspicious_requests)
        
        return {
            'keyword_count': keyword_count,
            'found_keywords': found_keywords[:3],  # Show up to 3
            'urgency_score': urgency_score,
            'has_suspicious_request': has_suspicious_request,
            'risk_level': self._calculate_risk_level(keyword_count, urgency_score, has_suspicious_request)
        }
    
    def _calculate_risk_level(self, keyword_count, urgency_score, has_suspicious_request):
        """Calculate overall risk level: LOW, MEDIUM, HIGH"""
        if keyword_count >= 3 or (urgency_score > URGENCY_THRESHOLD and has_suspicious_request):
            return "HIGH"
        elif keyword_count >= 2 or urgency_score > 0.5:
            return "MEDIUM"
        else:
            return "LOW"
