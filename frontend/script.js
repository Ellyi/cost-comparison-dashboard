const API_URL = 'https://cost-comparison-dashboard-production.up.railway.app/api';

async function calculateCosts() {
    const messages = parseInt(document.getElementById('messages').value);
    const tokens = parseInt(document.getElementById('tokens').value);
    
    if (messages <= 0 || tokens <= 0) {
        alert('Please enter valid positive numbers');
        return;
    }
    
    document.getElementById('loading').style.display = 'block';
    document.getElementById('results').style.display = 'none';
    
    try {
        const response = await fetch(`${API_URL}/calculate`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                messages: messages,
                tokens_per_message: tokens
            })
        });
        
        if (!response.ok) throw new Error('API request failed');
        
        const data = await response.json();
        displayResults(data);
        
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to calculate costs. Make sure backend is running.');
    } finally {
        document.getElementById('loading').style.display = 'none';
    }
}
function displayResults(data) {
    const { results, summary } = data;
    
    const summaryHTML = `
        <div class="summary-item">
            <span class="summary-label">Cheapest Model:</span>
            <span class="summary-value">${summary.cheapest_model}</span>
        </div>
        <div class="summary-item">
            <span class="summary-label">Cheapest Cost:</span>
            <span class="summary-value">$${summary.cheapest_cost.toFixed(2)}</span>
        </div>
        <div class="summary-item">
            <span class="summary-label">Most Expensive:</span>
            <span class="summary-value">$${summary.most_expensive_cost.toFixed(2)}</span>
        </div>
        <div class="summary-item">
            <span class="summary-label">Potential Savings:</span>
            <span class="summary-value" style="color: #10b981;">$${summary.potential_savings.toFixed(2)}</span>
        </div>
        <div class="summary-item">
            <span class="summary-label">Total Messages:</span>
            <span class="summary-value">${summary.total_messages.toLocaleString()}</span>
        </div>
        <div class="summary-item">
            <span class="summary-label">Total Tokens:</span>
            <span class="summary-value">${summary.total_tokens.toLocaleString()}</span>
        </div>
    `;
    document.getElementById('summary').innerHTML = summaryHTML;

    const cheapestModel = summary.cheapest_model;
    
    Object.keys(results).forEach(modelKey => {
        const model = results[modelKey];
        const isCheapest = model.name === cheapestModel;
        
        const cardHTML = `
            ${isCheapest ? '<div class="cheapest-badge">🏆 Best Value</div>' : ''}
            <div class="model-name">${model.name}</div>
            <div class="model-cost">$${model.total_cost.toFixed(2)}</div>
            <div class="cost-breakdown">
                <div>Input: $${model.input_cost.toFixed(4)}</div>
                <div>Output: $${model.output_cost.toFixed(4)}</div>
                <div style="margin-top: 10px; font-weight: 600;">
                    ${(model.cost_per_message * 1000).toFixed(3)}¢ per message
                </div>
            </div>
        `;
        
        document.getElementById(modelKey).innerHTML = cardHTML;
    });
    
    document.getElementById('results').style.display = 'block';
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('messages').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') calculateCosts();
    });
    
    document.getElementById('tokens').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') calculateCosts();
    });
});