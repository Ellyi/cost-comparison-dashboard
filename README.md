# AI Cost Comparison Dashboard

Compare costs across Claude, GPT, and Gemini APIs to find the most cost-effective option for your use case.

## Features

- Real-time cost calculations for Claude Sonnet/Opus, GPT-4o/Mini, and Gemini Pro
- Interactive comparison showing cheapest option
- Cost breakdown (input/output tokens)
- Potential savings calculator
- Clean, professional UI

## Screenshots

![Dashboard Interface](screenshot.png)

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **APIs:** Anthropic, OpenAI, Google Gemini pricing data

## Setup

### Prerequisites

- Python 3.8+

### Installation

1. Clone repository:
```bash
git clone https://github.com/Ellyi/cost-comparison-dashboard.git
cd cost-comparison-dashboard
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run backend:
```bash
python -m backend.app
```

4. Open `frontend/index.html` in browser

## Usage

1. Enter number of messages you plan to send
2. Enter average tokens per message
3. Click "Calculate Costs"
4. See which AI model is cheapest for your use case

## Pricing (Dec 2024)

- **Claude Sonnet 4:** $3 input / $15 output per 1M tokens
- **Claude Opus 4:** $15 input / $75 output per 1M tokens  
- **GPT-4o:** $2.50 input / $10 output per 1M tokens
- **GPT-4o Mini:** $0.15 input / $0.60 output per 1M tokens
- **Gemini 1.5 Pro:** $1.25 input / $5 output per 1M tokens

## Author

Built by Elijah Onyancha - AI Integration Specialist

📫 [GitHub](https://github.com/Ellyi)