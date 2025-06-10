"""
MCP Stock Tracking App - Gradio Frontend
"""

import gradio as gr

# Custom CSS for better styling
custom_css = """
.main-header {
    text-align: center;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 2rem;
    border-radius: 15px;
    margin-bottom: 1.5rem;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
}

.search-section {
    background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
    padding: 2rem;
    border-radius: 12px;
    margin: 1rem 0;
    border: 1px solid #e2e8f0;
}

.info-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1rem 0;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    border-left: 4px solid #667eea;
}

.roadmap-item {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 1rem;
    margin: 0.5rem 0;
    border-left: 3px solid #10b981;
}

.tech-stack {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin: 1rem 0;
}

.tech-item {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 1rem;
    text-align: center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}
"""

def search_stock(symbol):
    """Enhanced placeholder function with realistic mock data"""
    if not symbol.strip():
        return "⚠️ Please enter a stock symbol!"
    
    symbol = symbol.upper().strip()
    
    # Mock data for demonstration with realistic stock information
    mock_data = {
        "AAPL": {
            "name": "Apple Inc.",
            "price": 189.42,
            "change": +2.35,
            "change_percent": +1.26,
            "volume": "45.2M",
            "market_cap": "2.95T",
            "pe_ratio": 28.5,
            "recommendation": "BUY"
        },
        "GOOGL": {
            "name": "Alphabet Inc.",
            "price": 142.56,
            "change": -1.23,
            "change_percent": -0.85,
            "volume": "28.7M",
            "market_cap": "1.78T",
            "pe_ratio": 24.2,
            "recommendation": "HOLD"
        },
        "MSFT": {
            "name": "Microsoft Corporation",
            "price": 378.85,
            "change": +5.67,
            "change_percent": +1.52,
            "volume": "32.1M",
            "market_cap": "2.81T",
            "pe_ratio": 31.8,
            "recommendation": "BUY"
        },
        "TSLA": {
            "name": "Tesla Inc.",
            "price": 248.98,
            "change": -8.45,
            "change_percent": -3.28,
            "volume": "67.4M",
            "market_cap": "793B",
            "pe_ratio": 45.7,
            "recommendation": "HOLD"
        },
        "NVDA": {
            "name": "NVIDIA Corporation",
            "price": 891.23,
            "change": +15.78,
            "change_percent": +1.80,
            "volume": "41.8M",
            "market_cap": "2.20T",
            "pe_ratio": 65.4,
            "recommendation": "BUY"
        },
        "AMZN": {
            "name": "Amazon.com Inc.",
            "price": 156.78,
            "change": +3.12,
            "change_percent": +2.03,
            "volume": "38.9M",
            "market_cap": "1.64T",
            "pe_ratio": 42.1,
            "recommendation": "BUY"
        },
        "META": {
            "name": "Meta Platforms Inc.",
            "price": 298.45,
            "change": -2.89,
            "change_percent": -0.96,
            "volume": "22.6M",
            "market_cap": "756B",
            "pe_ratio": 23.8,
            "recommendation": "HOLD"
        }
    }
    
    if symbol in mock_data:
        data = mock_data[symbol]
        change_emoji = "📈" if data["change"] > 0 else "📉"
        change_color = "🟢" if data["change"] > 0 else "🔴"
        
        # Determine trend and volatility
        if abs(data["change_percent"]) > 3:
            volatility = "High"
            vol_emoji = "⚡"
        elif abs(data["change_percent"]) > 1:
            volatility = "Moderate"
            vol_emoji = "📊"
        else:
            volatility = "Low"
            vol_emoji = "😌"
        
        trend = "Bullish 🐂" if data["change"] > 0 else "Bearish 🐻"
        
        # Recommendation styling
        rec_map = {
            "BUY": "🟢 BUY",
            "HOLD": "🟡 HOLD", 
            "SELL": "🔴 SELL"
        }
        rec_display = rec_map.get(data["recommendation"], data["recommendation"])
        
        return f"""� **Stock Analysis for {symbol}**

## �📊 {data['name']}

### 💰 **Price Information**
- **Current Price**: ${data['price']:.2f}
- **Daily Change**: {change_color} {data['change']:+.2f} ({data['change_percent']:+.2f}%)
- **Volume**: {data['volume']}

### 📈 **Market Data**
- **Market Cap**: ${data['market_cap']}
- **P/E Ratio**: {data['pe_ratio']}
- **Trend**: {trend}
- **Volatility**: {vol_emoji} {volatility}

### 🎯 **Investment Analysis** (Demo)
- **Recommendation**: {rec_display}
- **Risk Level**: {"Low" if data["pe_ratio"] < 25 else "Moderate" if data["pe_ratio"] < 40 else "High"}
- **Growth Potential**: {"High" if data["change_percent"] > 1 else "Moderate"}

---

✨ **Note**: This is demo data for testing purposes. 
🚀 **Coming Soon**: Real-time data via MCP server connection!"""
    
    else:
        # Handle unknown symbols with helpful suggestions
        popular_symbols = ["AAPL", "GOOGL", "MSFT", "TSLA", "NVDA", "AMZN", "META"]
        suggestions = ", ".join(popular_symbols)
        
        return f"""🔍 **Searching for {symbol}**...

⚠️ **Demo Mode**: Currently showing sample data for popular stocks

📝 **Available Demo Symbols**: 
{suggestions}

🔄 **Symbol Entered**: `{symbol}`
📊 **Status**: Will be supported with real-time data in the next update!

### 🚀 **What's Coming**:
- Real-time data for **all** stock symbols
- MCP server integration with live market feeds
- Advanced technical analysis and indicators
- Portfolio tracking and alerts

**💡 Tip**: Try one of the available demo symbols above to see the full analysis interface!"""

def create_interface():
    """Create a styled Gradio interface with tabs"""
    with gr.Blocks(
        title="MCP Stock Tracker",
        css=custom_css,
        theme=gr.themes.Soft(
            primary_hue=gr.themes.colors.blue,
            secondary_hue=gr.themes.colors.purple,
            font=[gr.themes.GoogleFont("Inter"), "system-ui", "sans-serif"]
        )
    ) as app:
        
        # Header with gradient styling
        gr.HTML("""
        <div class="main-header">
            <h1>📈 MCP Stock Tracking App</h1>
            <p style="font-size: 1.2em; margin: 0.5rem 0;">Intelligent stock analysis powered by Model Context Protocol</p>
            <p style="opacity: 0.9; margin: 0;">Real-time insights • Smart recommendations • Portfolio tracking</p>
        </div>
        """)
        
        with gr.Tabs():
            # Stock Search Tab with enhanced styling
            with gr.Tab("🔍 Stock Search"):
                gr.HTML('<div class="search-section">')
                gr.Markdown("### 🎯 Search and analyze any stock symbol")
                
                with gr.Row():
                    symbol_input = gr.Textbox(
                        label="📊 Stock Symbol", 
                        placeholder="Enter a stock symbol (e.g., AAPL, GOOGL, MSFT)",
                        scale=3
                    )
                    search_btn = gr.Button("🔍 Search", variant="primary", scale=1, size="lg")
                
                gr.HTML('</div>')
                
                # Output area for search results - using Markdown for proper formatting
                result_output = gr.Markdown(
                    label="📋 Search Results",
                    value="Enter a stock symbol and click Search to see results...",
                    height=400
                )
                
                # Connect button click to handler function
                search_btn.click(
                    fn=search_stock,
                    inputs=symbol_input,
                    outputs=result_output
                )
            
            # About Tab with enhanced cards
            with gr.Tab("ℹ️ About"):
                gr.HTML("""
                <div class="info-card">
                    <h3>🚀 About MCP Stock Tracker</h3>
                    <p>This application demonstrates the power of <strong>Model Context Protocol (MCP)</strong> for building 
                    intelligent, connected financial applications.</p>
                </div>
                """)
                
                gr.Markdown("""
                #### 🏗️ System Architecture
                ```
                ┌─────────────────────┐    HTTP/JSON    ┌──────────────────────┐
                │   Gradio Frontend   │ ◄─────────────► │   Modal MCP Server   │
                │  (Hugging Face)     │      REST API   │     (Backend)        │
                └─────────────────────┘                 └──────────────────────┘
                ```
                """)
                
                gr.HTML("""
                <div class="tech-stack">
                    <div class="tech-item">
                        <h4>🎨 Frontend</h4>
                        <p><strong>Gradio + Python</strong><br>Interactive web interface</p>
                    </div>
                    <div class="tech-item">
                        <h4>⚡ Backend</h4>
                        <p><strong>Modal + FastAPI</strong><br>Scalable cloud compute</p>
                    </div>
                    <div class="tech-item">
                        <h4>📊 Data</h4>
                        <p><strong>yfinance + APIs</strong><br>Real-time market data</p>
                    </div>
                    <div class="tech-item">
                        <h4>🤖 Protocol</h4>
                        <p><strong>Model Context Protocol</strong><br>AI-powered insights</p>
                    </div>
                </div>
                """)
                
                gr.HTML("""
                <div class="info-card">
                    <h4>✨ Key Features (Coming Soon)</h4>
                    <ul style="margin: 1rem 0;">
                        <li>📊 <strong>Real-time stock prices</strong> and market data</li>
                        <li>🔍 <strong>Smart ticker symbol search</strong> with fuzzy matching</li>
                        <li>📈 <strong>Comprehensive investment analysis</strong> with AI insights</li>
                        <li>💼 <strong>Portfolio tracking</strong> and performance monitoring</li>
                    </ul>
                </div>
                """)
            
            # Coming Soon Tab with styled roadmap
            with gr.Tab("🚀 Coming Soon"):
                gr.HTML("""
                <div class="info-card">
                    <h3>🎯 Development Roadmap</h3>
                    <p>Exciting features and improvements planned for upcoming releases!</p>
                </div>
                """)
                
                gr.HTML("""
                <div class="roadmap-item">
                    <h4>📅 Phase 1: Core Features (Next Update)</h4>
                    <ul>
                        <li>✅ Basic UI and navigation</li>
                        <li>🔄 MCP server connection</li>
                        <li>🔄 Real-time stock price lookup</li>
                        <li>🔄 Input validation and error handling</li>
                    </ul>
                </div>
                
                <div class="roadmap-item">
                    <h4>📅 Phase 2: Analysis Features</h4>
                    <ul>
                        <li>📊 Technical indicators and charts</li>
                        <li>📈 Performance analysis and trends</li>
                        <li>🎯 Investment scoring algorithms</li>
                        <li>📋 Detailed company information</li>
                    </ul>
                </div>
                
                <div class="roadmap-item">
                    <h4>📅 Phase 3: Advanced Features</h4>
                    <ul>
                        <li>💼 Portfolio management system</li>
                        <li>🔔 Price alerts and notifications</li>
                        <li>🤖 AI-powered market insights</li>
                        <li>📱 Mobile-responsive design</li>
                    </ul>
                </div>
                """)
                
                gr.HTML("""
                <div class="info-card" style="text-align: center;">
                    <h4>🌟 Stay tuned for regular updates!</h4>
                    <p>Follow our progress and be the first to try new features.</p>
                </div>
                """)
        
        # Footer
        gr.HTML("""
        <div style="text-align: center; padding: 2rem; margin-top: 2rem; background: #f8fafc; border-radius: 10px;">
            <p style="margin: 0; color: #64748b;">
                🚀 Built with <strong>Gradio</strong> • <strong>Modal</strong> • <strong>Model Context Protocol</strong>
            </p>
        </div>
        """)
    
    return app

if __name__ == "__main__":
    app = create_interface()
    app.launch()
