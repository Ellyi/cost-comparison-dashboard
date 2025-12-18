"""
Cost calculator for different AI API providers
Pricing as of December 2024
"""

class CostCalculator:
    """Calculate costs for Claude, GPT, and Gemini APIs"""
    
    # Pricing per 1M tokens (input)
    PRICING = {
        'claude_sonnet': {
            'name': 'Claude Sonnet 4',
            'input': 3.00,   # $3 per 1M input tokens
            'output': 15.00  # $15 per 1M output tokens
        },
        'claude_opus': {
            'name': 'Claude Opus 4',
            'input': 15.00,
            'output': 75.00
        },
        'gpt4': {
            'name': 'GPT-4o',
            'input': 2.50,
            'output': 10.00
        },
        'gpt4_mini': {
            'name': 'GPT-4o Mini',
            'input': 0.15,
            'output': 0.60
        },
        'gemini_pro': {
            'name': 'Gemini 1.5 Pro',
            'input': 1.25,
            'output': 5.00
        }
    }
    
    def calculate_cost(self, model_key, input_tokens, output_tokens):
        """
        Calculate cost for a specific model
        
        Args:
            model_key: Key from PRICING dict
            input_tokens: Number of input tokens
            output_tokens: Number of output tokens
            
        Returns:
            dict with cost breakdown
        """
        pricing = self.PRICING[model_key]
        
        # Calculate costs (convert tokens to millions)
        input_cost = (input_tokens / 1_000_000) * pricing['input']
        output_cost = (output_tokens / 1_000_000) * pricing['output']
        total_cost = input_cost + output_cost
        
        return {
            'name': pricing['name'],
            'input_cost': round(input_cost, 4),
            'output_cost': round(output_cost, 4),
            'total_cost': round(total_cost, 4),
            'cost_per_message': round(total_cost / (input_tokens / 500), 6)  # Assuming 500 tokens per message
        }
    
    def calculate_all(self, messages, tokens_per_message):
        """
        Calculate costs for all models
        
        Args:
            messages: Number of messages
            tokens_per_message: Average tokens per message
            
        Returns:
            dict with all model costs and comparison
        """
        # Assume 50/50 split between input and output
        total_input_tokens = messages * tokens_per_message * 0.5
        total_output_tokens = messages * tokens_per_message * 0.5
        
        results = {}
        costs = []
        
        for model_key in self.PRICING.keys():
            cost_data = self.calculate_cost(model_key, total_input_tokens, total_output_tokens)
            results[model_key] = cost_data
            costs.append((model_key, cost_data['total_cost']))
        
        # Find cheapest
        costs.sort(key=lambda x: x[1])
        cheapest = costs[0][0]
        
        # Calculate savings
        most_expensive = costs[-1][1]
        potential_savings = most_expensive - costs[0][1]
        
        return {
            'results': results,
            'summary': {
                'cheapest_model': self.PRICING[cheapest]['name'],
                'cheapest_cost': round(costs[0][1], 4),
                'most_expensive_cost': round(most_expensive, 4),
                'potential_savings': round(potential_savings, 4),
                'total_messages': messages,
                'total_tokens': messages * tokens_per_message
            }
        }