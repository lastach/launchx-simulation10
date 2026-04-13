"""
Exit Pathways & Legacy
Entrepreneurship Simulation

The capstone simulation. You have been building ThermaLoop for 3 years.
The company is real, growing, and generating revenue. Now the biggest
strategic questions arrive: What is your endgame? Sell? Go public?
Keep building? Shut down and start something new?

Players navigate 5 quarters of high-stakes decisions involving acquisition
offers, investor pressure, team dynamics, market shifts, and personal
tradeoffs. Every choice shapes four outcome dimensions:
Financial Return, Team Legacy, Market Impact, and Personal Fulfillment.
"""

import math
import random
from typing import Dict, List, Tuple, Any
from collections import defaultdict

import streamlit as st

# ---------------------------------------------------------------------------
# Page setup
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Exit Pathways & Legacy",
    page_icon="trophy",
    layout="wide",
)

hide_streamlit_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Custom CSS
# ---------------------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --brand-primary: #EA6534;
    --brand-light: #FEF0EB;
    --brand-dark: #446276;
    --brand-hover: #F87B4D;
    --gold-accent: #D97706;
    --gold-light: #FEF3C7;
    --green-accent: #10B981;
    --green-light: #D1FAE5;
    --red-accent: #EF4444;
    --red-light: #FEE2E2;
    --blue-accent: #3B82F6;
    --blue-light: #DBEAFE;
    --bg-cream: #FAFAF8;
    --text-dark: #1F2937;
    --text-muted: #6B7280;
}

.stApp {
    background-color: var(--bg-cream);
    font-family: 'Inter', sans-serif;
}

.game-header {
    background: linear-gradient(135deg, #446276 0%, #5A7D8F 40%, #EA6534 100%);
    color: white;
    padding: 2rem 2.5rem;
    border-radius: 16px;
    margin-bottom: 1.5rem;
}

.game-header h1 {
    margin: 0;
    font-size: 2rem;
    font-weight: 800;
    letter-spacing: -0.02em;
}

.game-header p {
    margin: 0.5rem 0 0 0;
    opacity: 0.92;
    font-size: 1.05rem;
}

.quarter-badge {
    display: inline-block;
    background: var(--brand-primary);
    color: white;
    padding: 0.35rem 1.1rem;
    border-radius: 20px;
    font-weight: 600;
    font-size: 0.9rem;
    margin-bottom: 0.8rem;
}

.metric-card {
    background: white;
    border: 1px solid #E5E7EB;
    border-radius: 12px;
    padding: 1.2rem;
    text-align: center;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06);
}

.metric-card .metric-value {
    font-size: 1.8rem;
    font-weight: 700;
    color: var(--text-dark);
}

.metric-card .metric-label {
    font-size: 0.78rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-top: 0.3rem;
}

.offer-card {
    background: white;
    border: 2px solid #E5E7EB;
    border-radius: 14px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    transition: border-color 0.2s, box-shadow 0.2s;
}

.offer-card:hover {
    border-color: var(--brand-primary);
    box-shadow: 0 4px 12px rgba(234, 101, 52, 0.12);
}

.offer-card h3 {
    margin: 0 0 0.5rem 0;
    color: var(--brand-dark);
    font-size: 1.15rem;
}

.offer-card .offer-tag {
    display: inline-block;
    padding: 0.2rem 0.7rem;
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: 600;
    margin-right: 0.4rem;
}

.tag-financial { background: var(--green-light); color: #065F46; }
.tag-team { background: var(--blue-light); color: #1E40AF; }
.tag-impact { background: var(--gold-light); color: #92400E; }
.tag-personal { background: var(--brand-light); color: var(--brand-dark); }

.event-card {
    background: linear-gradient(135deg, #FEF3C7 0%, #FDE68A 100%);
    border: 2px solid #F59E0B;
    border-radius: 12px;
    padding: 1.2rem;
    margin: 1rem 0;
}

.event-card.negative {
    background: linear-gradient(135deg, #FEE2E2 0%, #FECACA 100%);
    border-color: #EF4444;
}

.event-card.positive {
    background: linear-gradient(135deg, #D1FAE5 0%, #A7F3D0 100%);
    border-color: #10B981;
}

.insight-box {
    background: var(--brand-light);
    border-left: 4px solid var(--brand-primary);
    border-radius: 0 12px 12px 0;
    padding: 1rem 1.2rem;
    margin: 1rem 0;
    font-size: 0.95rem;
    color: #374151;
}

.score-ring {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 80px;
    height: 80px;
    border-radius: 50%;
    font-size: 1.6rem;
    font-weight: 700;
    color: white;
}

.founder-type-card {
    background: linear-gradient(135deg, #446276 0%, #EA6534 100%);
    color: white;
    padding: 2rem;
    border-radius: 16px;
    text-align: center;
    margin: 1rem 0;
}

.founder-type-card h2 {
    margin: 0;
    font-size: 1.6rem;
    font-weight: 800;
}

.founder-type-card p {
    margin: 0.5rem 0 0 0;
    opacity: 0.92;
    font-size: 1rem;
}

.progress-bar-container {
    background: #E5E7EB;
    border-radius: 8px;
    height: 10px;
    overflow: hidden;
    margin: 0.5rem 0;
}

.progress-bar-fill {
    height: 100%;
    border-radius: 8px;
    transition: width 0.4s ease;
}

.journal-entry {
    background: white;
    border-left: 3px solid var(--brand-primary);
    padding: 0.8rem 1rem;
    margin: 0.5rem 0;
    border-radius: 0 8px 8px 0;
    font-size: 0.9rem;
}

.stButton > button {
    border-radius: 8px;
    font-weight: 600;
    padding: 0.5rem 1.5rem;
    background-color: #EA6534 !important;
    color: white !important;
    border: none !important;
}

.stButton > button:hover {
    background-color: #F87B4D !important;
    color: white !important;
}

.stButton > button:active, .stButton > button:focus {
    background-color: #D4572C !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Game Data: ThermaLoop at Year 3
# ---------------------------------------------------------------------------

COMPANY_BASELINE = {
    "name": "ThermaLoop",
    "product": "Smart ventilation retrofit kits for homes",
    "age_years": 3,
    "arr": 2_400_000,       # $2.4M ARR
    "mrr": 200_000,
    "customers": 4_200,
    "employees": 18,
    "cash_on_hand": 800_000,
    "burn_rate": 160_000,   # monthly
    "gross_margin": 0.62,
    "growth_rate_monthly": 0.06,  # 6% MoM
    "churn_monthly": 0.035,
    "nps": 52,
    "runway_months": 5,
    "total_raised": 3_500_000,
    "investor_ownership": 0.35,
    "founder_ownership": 0.45,
    "employee_pool": 0.15,
    "advisor_ownership": 0.05,
}

# ---------------------------------------------------------------------------
# Quarter scenarios: each quarter has context, an event, and choices
# ---------------------------------------------------------------------------

QUARTERS = [
    # Q1: The First Offer
    {
        "id": "q1",
        "title": "Quarter 1: The Knock on the Door",
        "context": (
            "ThermaLoop is growing steadily. Your smart vent kits are in 4,200 homes, "
            "customers love the product (NPS 52), and monthly revenue just hit $200K. "
            "But runway is tight at 5 months, and your lead investor is pushing you to "
            "think about your next move.\n\n"
            "Then an email lands from Carrier Global, one of the largest HVAC companies "
            "in the world. They want to meet."
        ),
        "event": {
            "type": "positive",
            "title": "Acquisition Interest",
            "text": (
                "Carrier Global's VP of Strategy has reached out. They are building a "
                "smart home division and see ThermaLoop as a potential bolt-on acquisition. "
                "They have not named a price yet, but your banker estimates a range of "
                "$8M to $12M based on comparable deals."
            ),
        },
        "choices": [
            {
                "id": "q1_explore",
                "label": "Take the meeting and explore",
                "description": (
                    "You will hear Carrier out, share high-level metrics, and learn "
                    "what an acquisition could look like. No commitment yet."
                ),
                "effects": {
                    "financial": 5, "team": 0, "impact": 0, "personal": 3,
                },
                "narrative": (
                    "You fly to Charlotte for the meeting. Carrier's team is impressive "
                    "but corporate. They talk about 'integration roadmaps' and "
                    "'synergy realization timelines.' You leave with a mix of excitement "
                    "and unease. Your banker says this is textbook: keep them warm, "
                    "create urgency, and explore other options simultaneously."
                ),
                "flag": "explored_carrier",
                "metric_changes": {"arr": 0, "cash_on_hand": -5000, "nps": 0},
            },
            {
                "id": "q1_decline",
                "label": "Politely decline for now",
                "description": (
                    "You tell Carrier you are focused on growth and not exploring exits. "
                    "This keeps your team focused but closes a window."
                ),
                "effects": {
                    "financial": -3, "team": 5, "impact": 2, "personal": 2,
                },
                "narrative": (
                    "Your team rallies when they hear you are staying the course. "
                    "Morale spikes. But your lead investor pulls you aside at your "
                    "next board meeting: 'That was a real option you just let expire. "
                    "In this market, acquirers don't come back twice.' You feel "
                    "the weight of that comment for weeks."
                ),
                "flag": "declined_carrier",
                "metric_changes": {"arr": 50_000, "cash_on_hand": 0, "nps": 3},
            },
            {
                "id": "q1_fundraise",
                "label": "Use the interest as leverage to fundraise",
                "description": (
                    "You tell your investors about Carrier's interest and use it to "
                    "kick off a Series A process. Risky if it leaks, but could solve "
                    "your runway problem."
                ),
                "effects": {
                    "financial": 8, "team": -2, "impact": 3, "personal": -1,
                },
                "narrative": (
                    "The fundraising process is grueling. 47 investor meetings in "
                    "6 weeks while trying to keep the business running. Two of your "
                    "engineers start updating their LinkedIn profiles. But the Carrier "
                    "interest creates real FOMO. You land a $4M Series A at a $20M "
                    "pre-money valuation. Runway extended to 18 months. Your ownership "
                    "dilutes from 45% to 34%, but the company now has fuel."
                ),
                "flag": "raised_series_a",
                "metric_changes": {"arr": 0, "cash_on_hand": 4_000_000, "nps": -2},
            },
        ],
    },
    # Q2: The Growth vs. Profit Crossroads
    {
        "id": "q2",
        "title": "Quarter 2: Growth vs. Sustainability",
        "context": (
            "Three months have passed. ThermaLoop is now at $2.8M ARR. A new dynamic "
            "has emerged: your largest customer segment (homeowners) is showing signs of "
            "saturation in your core markets, but a new B2B opportunity has appeared. "
            "Property management companies want a bulk version of your product.\n\n"
            "Meanwhile, your team is burning out. Your VP of Engineering just asked for "
            "a 'real conversation' about the pace."
        ),
        "event": {
            "type": "neutral",
            "title": "Strategic Crossroads",
            "text": (
                "You have three paths forward. Each one changes what ThermaLoop becomes "
                "and shapes who would want to acquire or invest in you down the road."
            ),
        },
        "choices": [
            {
                "id": "q2_b2b_pivot",
                "label": "Pivot to B2B property management",
                "description": (
                    "Shift focus to bulk deals with property managers. Higher revenue "
                    "per deal, but longer sales cycles and a complete go-to-market overhaul."
                ),
                "effects": {
                    "financial": 7, "team": -3, "impact": 4, "personal": -2,
                },
                "narrative": (
                    "The pivot is painful. Half your marketing content becomes irrelevant "
                    "overnight. Your consumer brand loyalists feel abandoned. But the "
                    "first property management deal closes at $180K/year, more than your "
                    "top 50 consumer customers combined. Your VP of Engineering is "
                    "frustrated by the pivot whiplash. Two junior devs resign."
                ),
                "flag": "pivoted_b2b",
                "metric_changes": {"arr": 400_000, "cash_on_hand": -100_000, "nps": -8},
            },
            {
                "id": "q2_double_consumer",
                "label": "Double down on consumer with new markets",
                "description": (
                    "Expand geographically into 5 new metro areas. Keep the product "
                    "and brand you have built, just reach more people."
                ),
                "effects": {
                    "financial": 3, "team": 2, "impact": 6, "personal": 3,
                },
                "narrative": (
                    "The geographic expansion feels natural. Your playbook works. "
                    "Customer acquisition costs are slightly higher in new markets, "
                    "but the unit economics hold. Your team appreciates the steady "
                    "direction. NPS stays strong. An industry publication names "
                    "ThermaLoop one of the 'Top 10 Climate Tech Startups to Watch.'"
                ),
                "flag": "expanded_consumer",
                "metric_changes": {"arr": 200_000, "cash_on_hand": -200_000, "nps": 5},
            },
            {
                "id": "q2_profitability",
                "label": "Cut burn and push toward profitability",
                "description": (
                    "Slow hiring, reduce marketing spend, and focus on unit economics. "
                    "Growth slows, but you extend runway dramatically and reduce "
                    "dependence on investors."
                ),
                "effects": {
                    "financial": 2, "team": -1, "impact": -2, "personal": 6,
                },
                "narrative": (
                    "You make the hard calls. Marketing budget cut by 40%. One contractor "
                    "let go. Growth slows to 3% monthly, but your burn drops to $95K. "
                    "For the first time, you can see a path to breakeven without raising "
                    "another dollar. Your board is mixed: some investors love the "
                    "discipline, others worry you are 'thinking too small.'"
                ),
                "flag": "chose_profitability",
                "metric_changes": {"arr": 80_000, "cash_on_hand": 200_000, "nps": 0},
            },
        ],
    },
    # Q3: The Big Offer or the Vision
    {
        "id": "q3",
        "title": "Quarter 3: The Real Offer",
        "context": (
            "ThermaLoop is now at roughly $3.2M ARR. The market is heating up. "
            "Two competitors have raised large rounds. A smart home conglomerate "
            "just went public. And then your phone rings."
        ),
        "event": {
            "type": "positive",
            "title": "Formal Acquisition Offer",
            "text": (
                "Honeywell has made a formal offer: $18M cash plus $4M in earnouts "
                "tied to 18 months of retention. Your investors would 2x their money. "
                "You would personally net roughly $6.5M after taxes and preferences. "
                "Your employees with stock options would see meaningful payouts.\n\n"
                "But there is a catch: Honeywell wants to fold ThermaLoop into their "
                "existing product line. The brand would disappear within a year."
            ),
        },
        "choices": [
            {
                "id": "q3_accept",
                "label": "Accept the Honeywell offer",
                "description": (
                    "Take the guaranteed outcome. $18M + earnout. Your team gets paid. "
                    "You get financial security. ThermaLoop lives on inside Honeywell, "
                    "but not as its own brand."
                ),
                "effects": {
                    "financial": 10, "team": 5, "impact": -4, "personal": 2,
                },
                "narrative": (
                    "The deal closes in 8 weeks. Signing day is surreal: you built "
                    "this from a dorm room idea, and now you are wiring $6.5M to your "
                    "bank account. Your early employees get checks that change their "
                    "lives. But walking into the Honeywell office on day one of the "
                    "earnout, wearing a corporate badge with your name on it, feels "
                    "strange. ThermaLoop's website redirects to honeywell.com/thermaloop "
                    "within 3 months. By month 6, even that page is gone."
                ),
                "flag": "accepted_acquisition",
                "metric_changes": {"arr": 0, "cash_on_hand": 18_000_000, "nps": 0},
            },
            {
                "id": "q3_negotiate",
                "label": "Counter at $28M with brand preservation",
                "description": (
                    "Push back hard. Ask for a higher price and a clause that keeps "
                    "ThermaLoop as an independent brand for 3 years. Bold, but risks "
                    "Honeywell walking away."
                ),
                "effects": {
                    "financial": 4, "team": 2, "impact": 5, "personal": 4,
                },
                "narrative": (
                    "Honeywell's team goes quiet for two agonizing weeks. Then they "
                    "come back: $22M with a 2-year brand independence clause. Not "
                    "everything you wanted, but meaningful. The negotiation taught you "
                    "something: the brand you built has real value, and you are a better "
                    "negotiator than you thought. You tell them you need a week to decide."
                ),
                "flag": "negotiated_higher",
                "metric_changes": {"arr": 0, "cash_on_hand": -20_000, "nps": 0},
            },
            {
                "id": "q3_reject",
                "label": "Reject and bet on yourself",
                "description": (
                    "Walk away from the offer entirely. You believe ThermaLoop can be "
                    "worth $100M+ in 3 years. But the road there is uncertain, and "
                    "your investors may not agree."
                ),
                "effects": {
                    "financial": -5, "team": 3, "impact": 8, "personal": 7,
                },
                "narrative": (
                    "Your lead investor asks for an emergency board call. 'You just "
                    "turned down a 5x return for our fund,' they say, barely hiding "
                    "frustration. But your co-founder and VP of Engineering are fired up. "
                    "'This is why we joined,' your VP says. The next quarter will be "
                    "the hardest yet: you need to prove the rejection was the right call."
                ),
                "flag": "rejected_offer",
                "metric_changes": {"arr": 100_000, "cash_on_hand": -80_000, "nps": 4},
            },
        ],
    },
    # Q4: The Crisis
    {
        "id": "q4",
        "title": "Quarter 4: The Storm",
        "context": (
            "The macro environment shifts dramatically. Interest rates spike. "
            "The housing market slows. Two of your competitors announce layoffs. "
            "Your largest B2B customer delays their renewal. And personally, "
            "something unexpected happens."
        ),
        "event": {
            "type": "negative",
            "title": "Convergent Crises",
            "text": (
                "Three things hit at once:\n\n"
                "1. Your co-founder tells you they are experiencing burnout and "
                "needs to step back to a part-time role.\n\n"
                "2. A supply chain disruption doubles the cost of your vent hardware "
                "for the next two quarters.\n\n"
                "3. Your Series A lead investor's fund is struggling and they hint "
                "they cannot participate in future rounds."
            ),
        },
        "choices": [
            {
                "id": "q4_hunker",
                "label": "Hunker down and survive",
                "description": (
                    "Cut 30% of the team, freeze hiring, renegotiate vendor contracts. "
                    "Painful, but extends runway through the storm."
                ),
                "effects": {
                    "financial": 5, "team": -8, "impact": -3, "personal": -4,
                },
                "narrative": (
                    "The layoffs are the hardest thing you have ever done. Six people "
                    "who trusted you, gone. You personally call each one. The "
                    "survivors are shaken but grateful. Burn drops by 40%. You "
                    "negotiate a 90-day payment extension with your hardware supplier. "
                    "The company will survive, but the culture is forever changed."
                ),
                "flag": "survived_crisis",
                "metric_changes": {"arr": -100_000, "cash_on_hand": 150_000, "nps": -6},
            },
            {
                "id": "q4_acquire_competitor",
                "label": "Acquire a struggling competitor",
                "description": (
                    "One of your competitors is about to shut down. Their tech is "
                    "complementary and they have 800 customers. You could acquire them "
                    "for pennies, but integration will be brutal."
                ),
                "effects": {
                    "financial": 6, "team": -4, "impact": 7, "personal": -3,
                },
                "narrative": (
                    "You acquire VentWise for $400K in stock and assumption of "
                    "$200K in liabilities. Their 800 customers bring your total past "
                    "5,000. Their senior engineer is brilliant and stays. But merging "
                    "two codebases, two cultures, and two customer support queues while "
                    "your co-founder is part-time nearly breaks you. You sleep 4 hours "
                    "a night for two months. The combined company is stronger, but "
                    "you are running on fumes."
                ),
                "flag": "acquired_competitor",
                "metric_changes": {"arr": 300_000, "cash_on_hand": -200_000, "nps": -3},
            },
            {
                "id": "q4_strategic_partner",
                "label": "Seek a strategic partnership",
                "description": (
                    "Instead of fighting alone, bring in a strategic partner. "
                    "A utility company has expressed interest in bundling ThermaLoop "
                    "with their energy efficiency programs."
                ),
                "effects": {
                    "financial": 3, "team": 2, "impact": 5, "personal": 1,
                },
                "narrative": (
                    "Duke Energy signs a 2-year distribution deal. They will bundle "
                    "ThermaLoop kits with their home energy audit program across "
                    "the Carolinas. You give up margin (they take 25% of kit sales) "
                    "but gain access to 500K homes with zero customer acquisition cost. "
                    "Your co-founder can step back knowing the company has a stable "
                    "channel. The partnership is not glamorous, but it might be "
                    "the smartest move you have made."
                ),
                "flag": "formed_partnership",
                "metric_changes": {"arr": 200_000, "cash_on_hand": 100_000, "nps": 2},
            },
        ],
    },
    # Q5: The Endgame Decision
    {
        "id": "q5",
        "title": "Quarter 5: The Endgame",
        "context": (
            "One year has passed since Carrier first knocked on your door. "
            "ThermaLoop is different now, shaped by every choice you made. "
            "It is time for the final decision: what does the next chapter look like?"
        ),
        "event": {
            "type": "neutral",
            "title": "Your Legacy, Your Choice",
            "text": (
                "You sit in a quiet room with your journal, a spreadsheet, and the "
                "weight of everything that got you here. Four paths forward have "
                "crystallized, each reflecting a different philosophy about what "
                "building a company really means."
            ),
        },
        "choices": [
            {
                "id": "q5_sell",
                "label": "Sell the company",
                "description": (
                    "Accept the best acquisition offer on the table. Take the financial "
                    "outcome, reward your team, and move on to the next chapter of your life."
                ),
                "effects": {
                    "financial": 9, "team": 4, "impact": -2, "personal": 3,
                },
                "narrative": (
                    "The deal closes. The number in your bank account is real. "
                    "Your early employees cry at the closing dinner, some from joy, "
                    "some from something more complicated. You did what most founders "
                    "never do: you created something valuable enough that someone "
                    "else wanted to buy it. What you do next is wide open."
                ),
                "flag": "exit_acquisition",
                "metric_changes": {},
            },
            {
                "id": "q5_scale",
                "label": "Raise a big round and go for scale",
                "description": (
                    "Raise a Series B, hire aggressively, and try to become the "
                    "category leader. The IPO dream. High risk, high potential reward."
                ),
                "effects": {
                    "financial": 3, "team": 2, "impact": 9, "personal": -3,
                },
                "narrative": (
                    "You raise $15M at a $60M valuation. Your ownership dilutes to "
                    "18%, but 18% of something big could be life-changing. The next "
                    "two years will be a sprint: 50 employees, three new markets, "
                    "a hardware V3. The IPO path is long and uncertain, but you are "
                    "playing for the biggest possible outcome. Your life is the company "
                    "now, fully and completely."
                ),
                "flag": "exit_scale",
                "metric_changes": {},
            },
            {
                "id": "q5_lifestyle",
                "label": "Build a profitable lifestyle business",
                "description": (
                    "Stop chasing growth at all costs. Make ThermaLoop profitable, "
                    "keep the team small, and build a business that funds the life you "
                    "want to live."
                ),
                "effects": {
                    "financial": 4, "team": 6, "impact": 3, "personal": 9,
                },
                "narrative": (
                    "You buy out your investors at a fair price using company profits "
                    "over 18 months. ThermaLoop becomes fully yours. Revenue grows "
                    "slowly but steadily. You hire a COO and step back to 3 days a "
                    "week. You start mentoring other founders. The business will never "
                    "be a unicorn, but it pays you $400K a year, employs 15 people "
                    "who love their jobs, and gives you time for everything else."
                ),
                "flag": "exit_lifestyle",
                "metric_changes": {},
            },
            {
                "id": "q5_shutdown",
                "label": "Wind down and start something new",
                "description": (
                    "The honest truth: your heart is not in it anymore. Close "
                    "ThermaLoop responsibly, learn from everything, and channel that "
                    "experience into your next venture."
                ),
                "effects": {
                    "financial": -5, "team": -3, "impact": 2, "personal": 6,
                },
                "narrative": (
                    "You spend 3 months winding down responsibly: finding jobs for "
                    "every team member, transitioning customers to a competitor, and "
                    "returning unused capital to investors. It feels like failure, "
                    "but experienced founders tell you otherwise. You learned more "
                    "in 3 years than most people learn in a decade. Six months later, "
                    "you start something new with sharper instincts and zero regrets."
                ),
                "flag": "exit_shutdown",
                "metric_changes": {},
            },
        ],
    },
]

# ---------------------------------------------------------------------------
# Founder exit archetypes
# ---------------------------------------------------------------------------
EXIT_ARCHETYPES = {
    "The Dealmaker": {
        "description": (
            "You have a sharp eye for timing and value. You instinctively understand "
            "when to hold and when to fold, and you treat every interaction as a "
            "potential opportunity. Founders like you build companies that are "
            "attractive to acquirers because you think about optionality from day one."
        ),
        "strengths": "Negotiation, pattern recognition, financial acumen",
        "watchout": (
            "Be careful not to optimize so heavily for the exit that you forget to "
            "build something you are proud of. The best deals come from companies "
            "that were not built to be sold."
        ),
        "real_world": "Brian Chesky explored multiple acquisition offers before taking Airbnb public. Reid Hoffman sold LinkedIn to Microsoft for $26B at exactly the right moment.",
    },
    "The Empire Builder": {
        "description": (
            "You do not think in terms of exits. You think in terms of legacy. "
            "Given the choice between a safe outcome and a shot at category dominance, "
            "you choose dominance every time. This takes extraordinary conviction "
            "and tolerance for risk."
        ),
        "strengths": "Vision, resilience, long-term thinking",
        "watchout": (
            "Empire building can become an identity trap. Make sure your ambition "
            "is serving the mission, not the other way around. The graveyard of "
            "startups is full of founders who could not take 'yes' for an answer."
        ),
        "real_world": "Elon Musk repeatedly rejected acquisition offers for Tesla. Sara Blakely held Spanx for 20+ years before selling a majority stake at a $1.2B valuation.",
    },
    "The Craftsperson": {
        "description": (
            "For you, the business is the point. You care more about building "
            "something that works beautifully, day after day, than hitting a "
            "headline number. Profitability and autonomy matter more to you than "
            "scale and speed."
        ),
        "strengths": "Sustainability, team culture, product quality",
        "watchout": (
            "The lifestyle path can sometimes be a way of avoiding hard decisions "
            "about growth. Make sure you are choosing this path because it fits "
            "your values, not because it feels safe."
        ),
        "real_world": "Jason Fried built Basecamp (now 37signals) into a profitable, calm company without ever raising a traditional round. Mailchimp operated profitably for 20 years before selling to Intuit for $12B.",
    },
    "The Serial Founder": {
        "description": (
            "You are wired to start things. The early days, the uncertainty, the "
            "invention: that is where you come alive. You would rather close one "
            "chapter cleanly and start a new one than spend years optimizing "
            "something that no longer excites you."
        ),
        "strengths": "Self-awareness, adaptability, creative energy",
        "watchout": (
            "Starting is addictive. Make sure you are not running from the hard "
            "parts of building. The founders who change the world usually do it by "
            "staying, not by starting over."
        ),
        "real_world": "Jack Dorsey co-founded Twitter, then went on to build Square (now Block). Ev Williams started Blogger, sold to Google, then founded Twitter, then started Medium.",
    },
    "The Balanced Navigator": {
        "description": (
            "You resist easy categorization. You weigh financial outcomes, team "
            "welfare, market impact, and personal fulfillment with equal attention. "
            "This balance is rare and powerful. It means you can adapt to whatever "
            "the situation demands."
        ),
        "strengths": "Judgment, empathy, strategic flexibility",
        "watchout": (
            "Balance can sometimes look like indecision. At certain inflection "
            "points, founders need to commit fully to one direction. Make sure your "
            "balance is a strength, not a way of avoiding commitment."
        ),
        "real_world": "Whitney Wolfe Herd balanced personal mission, team building, and financial outcomes to take Bumble public. Stewart Butterfield pivoted from a game to Slack, balancing vision with practical opportunity.",
    },
}


# ---------------------------------------------------------------------------
# Session state
# ---------------------------------------------------------------------------
def init_state():
    defaults = {
        "stage": "intro",
        "quarter": 0,
        "choices_made": [],
        "flags": [],
        "scores": {"financial": 0, "team": 0, "impact": 0, "personal": 0},
        "journal": [],
        "company": dict(COMPANY_BASELINE),
        "email_captured": False,
        "user_email": "",
        # Goal-based scoring: founder declares their primary goal upfront
        # so we can evaluate alignment between intent and actual choices.
        "founder_goal": None,  # one of: financial, team, impact, personal, balanced
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------
def add_score(effects: Dict[str, int]):
    for dim, val in effects.items():
        if dim in st.session_state.scores:
            st.session_state.scores[dim] += val


def apply_metric_changes(changes: Dict[str, Any]):
    for k, v in changes.items():
        if k in st.session_state.company:
            st.session_state.company[k] += v


def get_letter_grade(score: int, max_score: int) -> str:
    pct = score / max_score if max_score > 0 else 0
    # Grading is curved because no single path can maximize all dimensions.
    # Achieving ~60% of the theoretical max reflects strong, thoughtful play.
    if pct >= 0.65:
        return "A"
    elif pct >= 0.50:
        return "B"
    elif pct >= 0.35:
        return "C"
    elif pct >= 0.20:
        return "D"
    else:
        return "F"


def determine_archetype() -> str:
    s = st.session_state.scores
    max_dim = max(s, key=s.get)
    max_val = s[max_dim]

    # Check for balanced
    values = list(s.values())
    avg = sum(values) / len(values)
    spread = max(values) - min(values)
    if spread <= 8:
        return "The Balanced Navigator"

    # Check flags for specific archetypes
    flags = st.session_state.flags

    if "exit_shutdown" in flags:
        return "The Serial Founder"
    if "exit_lifestyle" in flags:
        return "The Craftsperson"
    if "exit_scale" in flags:
        return "The Empire Builder"
    if "exit_acquisition" in flags or "accepted_acquisition" in flags:
        return "The Dealmaker"

    # Fallback based on scores
    if max_dim == "financial":
        return "The Dealmaker"
    elif max_dim == "impact":
        return "The Empire Builder"
    elif max_dim == "personal":
        return "The Craftsperson"
    elif max_dim == "team":
        return "The Balanced Navigator"
    return "The Balanced Navigator"


def render_progress_bar(value: int, max_val: int, color: str = "#EA6534"):
    pct = min(100, max(0, int((value / max_val) * 100))) if max_val > 0 else 0
    st.markdown(f"""
    <div class="progress-bar-container">
        <div class="progress-bar-fill" style="width: {pct}%; background: {color};"></div>
    </div>
    """, unsafe_allow_html=True)


def render_metric_card(label: str, value: str, sublabel: str = ""):
    extra = f'<div style="font-size:0.72rem;color:#9CA3AF;margin-top:2px;">{sublabel}</div>' if sublabel else ""
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{value}</div>
        <div class="metric-label">{label}</div>
        {extra}
    </div>
    """, unsafe_allow_html=True)


def render_company_dashboard():
    c = st.session_state.company
    cols = st.columns(4)
    with cols[0]:
        render_metric_card("ARR", f"${c['arr']:,.0f}", "Annual recurring revenue")
    with cols[1]:
        cash_display = c['cash_on_hand']
        render_metric_card("Cash", f"${cash_display:,.0f}", "On hand")
    with cols[2]:
        render_metric_card("Customers", f"{c['customers']:,}", "Active accounts")
    with cols[3]:
        render_metric_card("NPS", str(c['nps']), "Net Promoter Score")


# ---------------------------------------------------------------------------
# Stage: Intro
# ---------------------------------------------------------------------------
def render_intro():
    st.markdown("""
    <div class="game-header">
        <h1>Exit Pathways & Legacy</h1>
        <p>The capstone simulation: Where does your founder journey lead?</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("### The Story So Far")
        st.markdown(
            "You have spent three years building **ThermaLoop**, a smart ventilation "
            "retrofit kit that helps homeowners eliminate hot and cold spots while "
            "cutting energy bills. What started as a dorm room prototype is now a "
            "real company with real revenue, real employees, and real decisions ahead."
        )

        st.markdown("")
        st.markdown(
            "Over the next **5 quarters**, you will face the biggest strategic "
            "questions any founder encounters: When to sell. When to scale. When "
            "to pivot. When to walk away. There are no right answers, only tradeoffs "
            "that reveal what kind of founder you are."
        )

        st.markdown("")
        st.markdown("#### How This Works")
        st.markdown(
            "Each quarter brings new information, a key event, and a decision. "
            "Your choices shape four dimensions of your outcome:"
        )
        st.markdown(
            "**Financial Return** : What you and your stakeholders walk away with  \n"
            "**Team Legacy** : How your decisions affect the people who built this with you  \n"
            "**Market Impact** : The lasting mark ThermaLoop leaves on the world  \n"
            "**Personal Fulfillment** : Whether this journey gave you what you actually wanted"
        )

    with col2:
        st.markdown("### ThermaLoop Today")
        st.markdown("")
        c = COMPANY_BASELINE
        render_metric_card("ARR", f"${c['arr']:,.0f}")
        st.markdown("")
        render_metric_card("Customers", f"{c['customers']:,}")
        st.markdown("")
        render_metric_card("Team", f"{c['employees']} people")
        st.markdown("")
        render_metric_card("Runway", f"{c['runway_months']} months")
        st.markdown("")
        render_metric_card("Your Ownership", f"{int(c['founder_ownership']*100)}%")

    st.markdown("")
    st.markdown("---")
    st.markdown("")

    if st.button("Begin Your Endgame", type="primary", use_container_width=True):
        st.session_state.stage = "set_goal"
        st.session_state.quarter = 0
        st.rerun()


# ---------------------------------------------------------------------------
# Stage: Set Goal (declared before play; used for alignment scoring)
# ---------------------------------------------------------------------------
GOAL_OPTIONS = [
    {
        "key": "financial",
        "label": "Maximize Financial Return",
        "icon": "💰",
        "desc": "You want to walk away with the biggest possible payout for yourself, your team, and your investors. The win is liquidity and personal wealth.",
    },
    {
        "key": "team",
        "label": "Build Lasting Team Legacy",
        "icon": "🤝",
        "desc": "You want every person who built this with you to thrive — financially, professionally, and personally. The win is a team that calls this the best chapter of their careers.",
    },
    {
        "key": "impact",
        "label": "Maximize Market Impact",
        "icon": "🌍",
        "desc": "You want ThermaLoop to leave a permanent mark on the industry — better products, better standards, real climate impact at scale. The win is changing how things are done.",
    },
    {
        "key": "personal",
        "label": "Personal Fulfillment",
        "icon": "🧭",
        "desc": "You want this journey to give you what you actually wanted — autonomy, learning, time with family, the freedom to keep building. The win is finishing this without losing yourself.",
    },
    {
        "key": "balanced",
        "label": "Balanced Across All Four",
        "icon": "⚖️",
        "desc": "You want a respectable outcome across all four dimensions — no single thing dominates. The win is no major regrets in any direction.",
    },
]


def render_set_goal():
    st.markdown("""
    <div class="game-header">
        <h1>What's Your Goal?</h1>
        <p>Before you start: what does success actually look like for you?</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("")
    st.markdown(
        "Most founders never name their goal explicitly, then spend years frustrated "
        "that the outcome doesn't match what they secretly wanted. Pick one now. "
        "We'll measure how well your actual decisions align with this stated goal."
    )
    st.markdown("")

    # Render each goal as a card with a select button
    for goal in GOAL_OPTIONS:
        with st.container():
            st.markdown(f"""
            <div class="metric-card" style="text-align:left;padding:1.2rem;margin-bottom:0.6rem;">
                <div style="display:flex;align-items:center;gap:0.6rem;margin-bottom:0.4rem;">
                    <span style="font-size:1.6rem;">{goal['icon']}</span>
                    <span style="font-size:1.05rem;font-weight:700;color:#1F2937;">{goal['label']}</span>
                </div>
                <div style="color:#4B5563;font-size:0.92rem;">{goal['desc']}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"Choose: {goal['label']}", key=f"goal_{goal['key']}", use_container_width=True):
                st.session_state.founder_goal = goal["key"]
                st.session_state.stage = "play"
                st.rerun()


# ---------------------------------------------------------------------------
# Stage: Play (quarter loop)
# ---------------------------------------------------------------------------
def render_play():
    q_idx = st.session_state.quarter
    if q_idx >= len(QUARTERS):
        st.session_state.stage = "results"
        st.rerun()
        return

    q = QUARTERS[q_idx]

    # Header
    st.markdown(f"""
    <div class="game-header">
        <h1>Exit Pathways & Legacy</h1>
        <p>Quarter {q_idx + 1} of 5</p>
    </div>
    """, unsafe_allow_html=True)

    # Progress dots
    dots = ""
    for i in range(5):
        if i < q_idx:
            dots += '<span style="display:inline-block;width:12px;height:12px;border-radius:50%;background:#EA6534;margin:0 4px;"></span>'
        elif i == q_idx:
            dots += '<span style="display:inline-block;width:12px;height:12px;border-radius:50%;background:#D97706;margin:0 4px;border:2px solid #92400E;"></span>'
        else:
            dots += '<span style="display:inline-block;width:12px;height:12px;border-radius:50%;background:#E5E7EB;margin:0 4px;"></span>'
    st.markdown(f'<div style="text-align:center;margin-bottom:1.5rem;">{dots}</div>', unsafe_allow_html=True)

    # Company dashboard
    render_company_dashboard()
    st.markdown("")

    # Quarter title and context
    st.markdown(f"### {q['title']}")
    st.markdown(q["context"])

    # Event card
    event = q["event"]
    event_class = "event-card"
    if event["type"] == "positive":
        event_class += " positive"
    elif event["type"] == "negative":
        event_class += " negative"

    st.markdown(f"""
    <div class="{event_class}">
        <strong>{event['title']}</strong><br><br>
        {event['text']}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("")
    st.markdown("### What do you do?")
    st.markdown("")

    # Choice cards
    choice_key = f"choice_q{q_idx}"
    choice_labels = [c["label"] for c in q["choices"]]
    selected = st.radio(
        "Select your path:",
        choice_labels,
        key=choice_key,
        label_visibility="collapsed",
    )

    # Show description for selected choice
    for c in q["choices"]:
        if c["label"] == selected:
            st.markdown(f"""
            <div class="insight-box">
                {c['description']}
            </div>
            """, unsafe_allow_html=True)
            break

    st.markdown("")

    if st.button("Commit to This Decision", type="primary", use_container_width=True):
        # Find selected choice
        for c in q["choices"]:
            if c["label"] == selected:
                # Apply effects
                add_score(c["effects"])
                apply_metric_changes(c.get("metric_changes", {}))
                st.session_state.flags.append(c["flag"])
                st.session_state.choices_made.append({
                    "quarter": q_idx + 1,
                    "choice_id": c["id"],
                    "label": c["label"],
                    "narrative": c["narrative"],
                })
                st.session_state.journal.append(
                    f"Q{q_idx + 1}: {c['label']}"
                )

                # Move to narrative
                st.session_state.stage = "narrative"
                st.rerun()
                break


# ---------------------------------------------------------------------------
# Stage: Narrative (post-decision)
# ---------------------------------------------------------------------------
def render_narrative():
    q_idx = st.session_state.quarter
    last_choice = st.session_state.choices_made[-1]

    st.markdown(f"""
    <div class="game-header">
        <h1>Exit Pathways & Legacy</h1>
        <p>Quarter {q_idx + 1} of 5: Outcome</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"### {QUARTERS[q_idx]['title']}")
    st.markdown(f'**Your Decision:** {last_choice["label"]}')
    st.markdown("")

    st.markdown(f"""
    <div class="insight-box">
        {last_choice['narrative']}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("")

    # Show score changes
    choice_obj = None
    for c in QUARTERS[q_idx]["choices"]:
        if c["id"] == last_choice["choice_id"]:
            choice_obj = c
            break

    if choice_obj:
        st.markdown("#### Impact of Your Decision")
        cols = st.columns(4)
        dims = [
            ("Financial Return", "financial", "#10B981"),
            ("Team Legacy", "team", "#3B82F6"),
            ("Market Impact", "impact", "#D97706"),
            ("Personal Fulfillment", "personal", "#EA6534"),
        ]
        for col, (label, key, color) in zip(cols, dims):
            with col:
                val = choice_obj["effects"].get(key, 0)
                sign = "+" if val >= 0 else ""
                emoji = "up" if val > 0 else ("down" if val < 0 else "neutral")
                arrow = {"up": "^", "down": "v", "neutral": "~"}[emoji]
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-value" style="color:{color};">{sign}{val}</div>
                    <div class="metric-label">{label}</div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("")

    # Updated company dashboard
    st.markdown("#### ThermaLoop After This Quarter")
    render_company_dashboard()

    st.markdown("")

    btn_label = "Next Quarter" if q_idx < 4 else "See Your Results"
    if st.button(btn_label, type="primary", use_container_width=True):
        st.session_state.quarter += 1
        if st.session_state.quarter >= len(QUARTERS):
            st.session_state.stage = "results"
        else:
            st.session_state.stage = "play"
        st.rerun()


# ---------------------------------------------------------------------------
# Stage: Email Gate
# ---------------------------------------------------------------------------
def render_email_gate():
    st.markdown("""
    <div class="game-header">
        <h1>Your Founder Journey is Complete</h1>
        <p>Enter your email to unlock your full Exit Profile and personalized coaching</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("")
    st.markdown(
        "You just navigated five quarters of high-stakes decisions. Your choices "
        "reveal a distinct founder profile with unique strengths, blind spots, "
        "and real-world parallels. Enter your email below to see your full results."
    )

    st.markdown("")

    email = st.text_input("Email address", key="email_input", placeholder="you@example.com")

    st.markdown("")

    if st.button("Unlock My Results", type="primary", use_container_width=True):
        if email and "@" in email and "." in email:
            st.session_state.user_email = email
            st.session_state.email_captured = True
            st.session_state.stage = "results"
            st.rerun()
        else:
            st.error("Please enter a valid email address.")


# ---------------------------------------------------------------------------
# Stage: Results
# ---------------------------------------------------------------------------
def compute_goal_alignment(scores: Dict[str, int], max_possible: Dict[str, int], goal: str) -> Tuple[int, str, str]:
    """Return (alignment_pct, headline, explanation) comparing actual play to declared goal.

    For single-dimension goals: alignment = how much of that dimension's max the player
    achieved, with a small penalty when other dimensions dominate.
    For 'balanced': alignment rewards a tight spread across all four dimensions.
    """
    dim_labels = {
        "financial": "Financial Return",
        "team": "Team Legacy",
        "impact": "Market Impact",
        "personal": "Personal Fulfillment",
    }
    pcts = {k: (scores[k] / max_possible[k]) if max_possible.get(k) else 0 for k in scores}

    if goal == "balanced":
        # Lower spread = stronger alignment with a balanced goal
        spread = max(pcts.values()) - min(pcts.values())
        avg = sum(pcts.values()) / len(pcts)
        # Reward both balance (low spread) and absolute strength (high avg)
        align = max(0, min(100, int((avg * 70) + ((1 - spread) * 30))))
        if align >= 75:
            head = "Strong alignment"
            exp = "You wanted balance and you delivered it. Your scores are tight across all four dimensions and the average is solid."
        elif align >= 50:
            head = "Decent alignment"
            exp = f"You aimed for balance but the spread between your strongest and weakest dimension is wider than the goal implied ({int(spread*100)} pts)."
        else:
            head = "Weak alignment"
            exp = "You said balanced, but you played one dimension much harder than others. That's a useful self-insight."
        return align, head, exp

    # Single-dimension goals
    target_pct = pcts.get(goal, 0)
    other_max = max([pcts[k] for k in pcts if k != goal] or [0])
    # Alignment = how much of the goal dimension was achieved minus a penalty if another dim dominated
    penalty = max(0, other_max - target_pct) * 0.4
    align = max(0, min(100, int((target_pct - penalty) * 100)))
    label = dim_labels.get(goal, goal)
    strongest = max(pcts, key=pcts.get)
    if align >= 75:
        head = "Strong alignment"
        exp = f"You declared {label} as your goal and your decisions clearly optimized for it. {int(target_pct*100)}% of the maximum possible in that dimension."
    elif align >= 50:
        head = "Decent alignment"
        exp = f"You said {label} but your strongest actual dimension was {dim_labels.get(strongest, strongest)}. Closer than most, but the path diverged in a few key quarters."
    else:
        head = "Misalignment"
        exp = f"You said {label}, but your decisions actually optimized for {dim_labels.get(strongest, strongest)}. This is one of the most common founder gaps — declared goal vs. actual behavior."
    return align, head, exp


def render_results():
    archetype = determine_archetype()
    arch_data = EXIT_ARCHETYPES[archetype]
    scores = st.session_state.scores
    founder_goal = st.session_state.get("founder_goal") or "balanced"

    # Calculate max possible scores
    max_possible = {"financial": 0, "team": 0, "impact": 0, "personal": 0}
    for q in QUARTERS:
        for dim in max_possible:
            best = max(c["effects"].get(dim, 0) for c in q["choices"])
            max_possible[dim] += best

    total_score = sum(scores.values())
    total_max = sum(max_possible.values())

    # Goal alignment block — show this BEFORE the archetype so users see intent vs reality first
    goal_label_map = {g["key"]: g["label"] for g in GOAL_OPTIONS}
    align_pct, align_head, align_exp = compute_goal_alignment(scores, max_possible, founder_goal)
    align_color = "#10B981" if align_pct >= 75 else "#D97706" if align_pct >= 50 else "#EF4444"
    st.markdown(f"""
    <div style="background:#F9FAFB;border-left:5px solid {align_color};border-radius:10px;padding:1.2rem 1.4rem;margin-bottom:1.2rem;">
        <div style="font-size:0.78rem;text-transform:uppercase;letter-spacing:0.08em;color:#6B7280;margin-bottom:0.3rem;">Goal Alignment</div>
        <div style="display:flex;align-items:baseline;gap:0.8rem;">
            <span style="font-size:2rem;font-weight:800;color:{align_color};">{align_pct}%</span>
            <span style="font-size:1rem;font-weight:600;color:#1F2937;">{align_head}</span>
        </div>
        <div style="margin-top:0.6rem;color:#4B5563;font-size:0.92rem;">
            <strong>Your declared goal:</strong> {goal_label_map.get(founder_goal, founder_goal)}<br>
            {align_exp}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="founder-type-card">
        <p style="font-size:0.9rem;text-transform:uppercase;letter-spacing:0.1em;opacity:0.8;">Your Founder Exit Archetype</p>
        <h2>{archetype}</h2>
        <p>{arch_data['description'][:120]}...</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("")
    st.markdown("---")
    st.markdown("")

    # Score breakdown
    st.markdown("### Your Outcome Profile")

    dims = [
        ("Financial Return", "financial", "#10B981"),
        ("Team Legacy", "team", "#3B82F6"),
        ("Market Impact", "impact", "#D97706"),
        ("Personal Fulfillment", "personal", "#EA6534"),
    ]

    cols = st.columns(4)
    for col, (label, key, color) in zip(cols, dims):
        with col:
            val = scores[key]
            mx = max_possible[key]
            grade = get_letter_grade(val, mx)
            pct = int((val / mx) * 100) if mx > 0 else 0
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value" style="color:{color};">{grade}</div>
                <div class="metric-label">{label}</div>
                <div style="font-size:0.75rem;color:#9CA3AF;margin-top:4px;">{val} / {mx} pts ({pct}%)</div>
            </div>
            """, unsafe_allow_html=True)
            render_progress_bar(val, mx, color)

    st.markdown("")

    # Overall score
    overall_grade = get_letter_grade(total_score, total_max)
    overall_pct = int((total_score / total_max) * 100) if total_max > 0 else 0
    st.markdown(f"""
    <div style="text-align:center;margin:1.5rem 0;">
        <span style="font-size:0.8rem;text-transform:uppercase;letter-spacing:0.08em;color:#6B7280;">Overall Score</span><br>
        <span style="font-size:3rem;font-weight:800;color:#1F2937;">{overall_grade}</span>
        <span style="font-size:1.1rem;color:#6B7280;margin-left:0.5rem;">{total_score} / {total_max} ({overall_pct}%)</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Archetype deep dive
    st.markdown(f"### {archetype}")
    st.markdown(arch_data["description"])

    st.markdown("")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="insight-box">
            <strong>Your Strengths:</strong> {arch_data['strengths']}
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="insight-box" style="border-left-color:#D97706;">
            <strong>Watch Out For:</strong> {arch_data['watchout']}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("")
    st.markdown("#### Real World Parallels")
    st.markdown(arch_data["real_world"])

    st.markdown("")
    st.markdown("---")
    st.markdown("")

    # Journey recap
    st.markdown("### Your Decision Journal")

    for entry in st.session_state.choices_made:
        st.markdown(f"""
        <div class="journal-entry">
            <strong>Quarter {entry['quarter']}:</strong> {entry['label']}<br>
            <span style="color:#6B7280;font-size:0.85rem;">{entry['narrative'][:200]}...</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("")
    st.markdown("---")
    st.markdown("")

    # Personalized coaching
    st.markdown("### Personalized Coaching")
    coaching = generate_coaching(archetype, scores, max_possible)
    st.markdown(coaching)

    st.markdown("")
    st.markdown("---")
    st.markdown("")

    # CTA
    st.markdown("""
    <div style="text-align:center;padding:2rem;background:linear-gradient(135deg, #FEF0EB 0%, #FEF3C7 100%);border-radius:16px;">
        <h3 style="margin:0 0 0.5rem 0;color:#446276;">Ready to Build for Real?</h3>
        <p style="color:#6B7280;margin:0 0 1rem 0;">
            This simulation helps young entrepreneurs go from idea to launch with mentors,
            curriculum, and a community of builders.
        </p>
        <a href="#" target="_blank"
           style="display:inline-block;background:#EA6534;color:white;padding:0.7rem 2rem;border-radius:8px;text-decoration:none;font-weight:600;">
            Explore More Simulations
        </a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("")

    # Footer
    st.markdown("""
    <div style="text-align:center;padding:2rem 0 1rem 0;color:#9CA3AF;font-size:0.8rem;">
         | Exit Pathways & Legacy
    </div>
    """, unsafe_allow_html=True)

    # Restart button
    st.markdown("")
    if st.button("Play Again", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()


def generate_coaching(archetype: str, scores: Dict, max_possible: Dict) -> str:
    """Generate personalized coaching based on choices and scores."""
    flags = st.session_state.flags
    coaching_parts = []

    # Analyze score balance
    values = list(scores.values())
    strongest = max(scores, key=scores.get)
    weakest = min(scores, key=scores.get)

    dim_labels = {
        "financial": "Financial Return",
        "team": "Team Legacy",
        "impact": "Market Impact",
        "personal": "Personal Fulfillment",
    }

    coaching_parts.append(
        f"Your strongest dimension was **{dim_labels[strongest]}** and your "
        f"most underweighted dimension was **{dim_labels[weakest]}**. This is "
        f"a telling pattern."
    )

    # Specific coaching based on flags
    if "raised_series_a" in flags:
        coaching_parts.append(
            "You chose to fundraise early, which is a high-leverage move but comes "
            "with dilution and pressure. In the real world, using acquisition interest "
            "to create urgency in a fundraise is a well-known tactic, but it only "
            "works if the interest is genuine and the timing is right."
        )

    if "pivoted_b2b" in flags:
        coaching_parts.append(
            "Your B2B pivot showed courage but also highlighted a common founder trap: "
            "chasing revenue at the expense of team stability. The best pivots happen "
            "when the team understands and believes in the 'why' behind the shift."
        )

    if "chose_profitability" in flags:
        coaching_parts.append(
            "Choosing profitability over growth is one of the most contrarian moves "
            "a VC-backed founder can make. It requires conviction and often creates "
            "tension with investors who are optimizing for fund returns, not your "
            "personal outcomes."
        )

    if "accepted_acquisition" in flags:
        coaching_parts.append(
            "Taking an early acquisition offer can feel like 'leaving money on the "
            "table,' but data shows that most startups that reject acquisition offers "
            "end up worth less, not more. You made a statistically sound choice."
        )

    if "rejected_offer" in flags:
        coaching_parts.append(
            "Rejecting an acquisition offer takes real conviction. Only about 1 in 10 "
            "founders who reject offers end up building something worth more than what "
            "they turned down. But when it works, it works spectacularly."
        )

    if "acquired_competitor" in flags:
        coaching_parts.append(
            "Acquiring a competitor during a downturn is a move from the playbook of "
            "the best operators. It shows you can think opportunistically under pressure. "
            "The key learning: integration is always harder than the deal itself."
        )

    if "survived_crisis" in flags:
        coaching_parts.append(
            "Layoffs are the decision every founder dreads. You chose survival over "
            "sentiment. The real test of leadership is not whether you make the cut, "
            "but how you treat the people affected. That is what your team will remember."
        )

    # Archetype-specific closer
    if archetype == "The Dealmaker":
        coaching_parts.append(
            "As a Dealmaker archetype, your superpower is seeing the board from above "
            "while everyone else is focused on individual pieces. Your next growth edge: "
            "practice falling in love with a problem, not just the opportunity."
        )
    elif archetype == "The Empire Builder":
        coaching_parts.append(
            "As an Empire Builder, you have the drive to create something transformative. "
            "Your next growth edge: learn to distinguish between conviction and stubbornness. "
            "The best empire builders know when to adapt their vision to reality."
        )
    elif archetype == "The Craftsperson":
        coaching_parts.append(
            "As a Craftsperson, you understand that a great company is not just about "
            "scale, it is about quality and sustainability. Your next growth edge: get "
            "comfortable with strategic risk. Sometimes the craft requires bold moves."
        )
    elif archetype == "The Serial Founder":
        coaching_parts.append(
            "As a Serial Founder, you bring the rare ability to see each venture as a "
            "learning laboratory. Your next growth edge: practice staying. The compound "
            "effect of deep expertise in one domain can be more powerful than breadth."
        )
    else:
        coaching_parts.append(
            "As a Balanced Navigator, you have a rare gift: the ability to weigh "
            "competing priorities without losing sight of any of them. Your next "
            "growth edge: practice decisive action. Balance is a strength, but "
            "speed of commitment matters too."
        )

    return "\n\n".join(coaching_parts)


# ---------------------------------------------------------------------------
# Main render loop
# ---------------------------------------------------------------------------
stage = st.session_state.stage

if stage == "intro":
    render_intro()
elif stage == "set_goal":
    render_set_goal()
elif stage == "play":
    # Defensive: if a returning user lands on play without a goal, send to set_goal first
    if not st.session_state.get("founder_goal"):
        st.session_state.stage = "set_goal"
        st.rerun()
    render_play()
elif stage == "narrative":
    render_narrative()
elif stage == "email_gate":
    # Email gate removed; route directly to results
    st.session_state.stage = "results"
    st.rerun()
elif stage == "results":
    render_results()
