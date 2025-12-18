"""
Flask backend for Cost Comparison Dashboard
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from .calculator import CostCalculator

app = Flask(__name__)
CORS(app)  # Allow frontend to connect

calculator = CostCalculator()

@app.route('/api/calculate', methods=['POST'])
def calculate_costs():
    """
    Calculate AI API costs based on user input
    
    Expected JSON:
    {
        "messages": 1000,
        "tokens_per_message": 500
    }
    """
    try:
        data = request.get_json()
        
        messages = data.get('messages', 0)
        tokens_per_message = data.get('tokens_per_message', 0)
        
        if messages <= 0 or tokens_per_message <= 0:
            return jsonify({'error': 'Invalid input values'}), 400
        
        results = calculator.calculate_all(messages, tokens_per_message)
        
        return jsonify(results), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)