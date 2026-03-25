# Auto-generated
from enum import Enum

class Intent(str, Enum):
    REFUND = "refund"
    COMPLAINT = "complaint"
    INQUIRY = "inquiry"

class AgentRoute(str, Enum):
    SUPPORT = "support"
    RETENTION = "retention"
    FRAUD = "fraud"

class FraudDecision(str, Enum):
    APPROVE = "approve"
    BLOCK = "block"
    REVIEW = "review"

class OfferType(str, Enum):
    DISCOUNT = "discount"
    REPLACEMENT = "replacement"
    NONE = "none"