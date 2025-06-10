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
    border: 1p                    #                                                   # Left Column - Main Results
                    with gr.Column(scale=2):
                        stock_info = gr.Markdown(
                            label="📊 Stock Information",
                            value="Enter a stock symbol and click Search to see detailed information...",
                            elem_classes=["main-content-card"],
                            show_label=False
                        )
                        
                        analysis_info = gr.Markdown(
                            label="📈 Investment Analysis",
                            value="Analysis results will appear here...",
                            elem_classes=["main-content-card"],
                            show_label=False
                        )tock_info = gr.Markdown(
                            label="📊 Stock Information",
                            value="Enter a stock symbol and click Search to see detailed information...",
                            elem_classes=["main-content-card"],
                            show_label=False
                        )
                        
                        analysis_info = gr.Markdown(
                            label="📈 Investment Analysis",
                            value="Analysis results will appear here...",
                            elem_classes=["main-content-card"],
                            show_label=False
                        )lumn - Main Results
                    with gr.Column(scale=2):
                        stock_info = gr.Markdown(
                            label="📊 Stock Information",
                            value="Enter a stock symbol and click Search to see detailed information...",
                            elem_classes=["main-content-card"],
                            show_label=False
                        )
                        
                        analysis_info = gr.Markdown(
                            label="📈 Investment Analysis",
                            value="Analysis results will appear here...",
                            elem_classes=["main-content-card"],
                            show_label=False
                        ) Main Results
                    with gr.Column(scale=2):
                        stock_info = gr.Markdown(
                            label="📊 Stock Information",
                            value="Enter a stock symbol and click Search to see detailed information...",
                            elem_classes=["main-content-card"],
                            show_label=False
                        )
                        
                        analysis_info = gr.Markdown(
                            label="📈 Investment Analysis",
                            value="Analysis results will appear here...",
                            elem_classes=["main-content-card"],
                            show_label=False
                        )f0;
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

.compact-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 1rem;
    margin: 0.5rem 0;
    box-shadow: 0 2px 12px rgba(0,0,0,0.05);
    border-left: 3px solid #667eea;
}

.main-content-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 1.5rem;
    margin: 0.5rem 0;
    box-shadow: 0 2px 12px rgba(0,0,0,0.05);
    overflow: hidden;
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

def search_stock_enhanced(symbol):
    """Enhanced search function that returns organized data for multiple UI components"""
    if not symbol.strip():
        empty_status = """
        <div class="info-card">
            <h4>⚠️ Input Required</h4>
            <p style="text-align: center; color: #ef4444;">
                Please enter a stock symbol
            </p>
        </div>
        """
        return (
            "⚠️ Please enter a stock symbol!",
            "",
            empty_status,
            empty_status
        )
    
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
        
        # Stock Information (Main Display)
        stock_info = f"""# 📊 {data['name']} ({symbol})

## 💰 Current Price: ${data['price']:.2f}
### {change_color} Daily Change: {data['change']:+.2f} ({data['change_percent']:+.2f}%)

#### 📈 Market Data
- **Volume**: {data['volume']}
- **Market Cap**: ${data['market_cap']}
- **P/E Ratio**: {data['pe_ratio']}
- **Trend**: {trend}
"""

        # Investment Analysis (Separate Display)  
        analysis_info = f"""## 🎯 Investment Analysis

### {rec_display}

#### 📊 Key Metrics
- **Risk Level**: {"Low" if data["pe_ratio"] < 25 else "Moderate" if data["pe_ratio"] < 40 else "High"}
- **Volatility**: {vol_emoji} {volatility}
- **Growth Potential**: {"High" if data["change_percent"] > 1 else "Moderate"}

*Note: This is demo data for testing purposes.*
"""

        # Quick Stats (Compact HTML Card)
        quick_stats = f"""
        <div class="compact-card">
            <h4 style="margin: 0 0 0.75rem 0; font-size: 1rem;">⚡ Quick Stats</h4>
            <div style="text-align: center;">
                <div style="font-size: 1.4em; font-weight: bold; margin: 0.5rem 0; color: {'#10b981' if data['change'] > 0 else '#ef4444'};">
                    ${data['price']:.2f}
                </div>
                <div style="margin: 0 0 0.75rem 0; color: {'#10b981' if data['change'] > 0 else '#ef4444'}; font-size: 0.9rem;">
                    {data['change']:+.2f} ({data['change_percent']:+.2f}%)
                </div>
                <div style="display: flex; justify-content: space-between; margin: 0.5rem 0; font-size: 0.85rem; color: #64748b;">
                    <span><strong>Vol:</strong> {data['volume']}</span>
                    <span><strong>P/E:</strong> {data['pe_ratio']}</span>
                </div>
                <div style="font-size: 0.85rem; color: #64748b;">
                    <strong>Cap:</strong> ${data['market_cap']}
                </div>
            </div>
        </div>
        """
        
        # Search Status (Compact HTML Card)
        search_status = f"""
        <div class="compact-card">
            <h4 style="margin: 0 0 0.75rem 0; font-size: 1rem;">✅ Found</h4>
            <div style="text-align: center;">
                <div style="margin: 0.5rem 0; color: #10b981; font-weight: bold;">
                    {symbol}
                </div>
                <div style="margin: 0 0 0.75rem 0; font-size: 0.85rem; color: #64748b;">
                    Demo data loaded
                </div>
                <div style="font-size: 1.2em; margin: 0.5rem 0;">
                    {rec_map.get(data["recommendation"], data["recommendation"])}
                </div>
                <div style="font-size: 0.8rem; color: #64748b;">
                    Real-time coming soon
                </div>
            </div>
        </div>
        """
        
        return stock_info, analysis_info, quick_stats, search_status
    
    else:
        # Handle unknown symbols
        popular_symbols = ["AAPL", "GOOGL", "MSFT", "TSLA", "NVDA", "AMZN", "META"]
        
        stock_info = f"""# 🔍 Searching for {symbol}

## ⚠️ Demo Mode Active

Currently showing sample data for popular stocks only.

### 📝 Available Demo Symbols:
{', '.join(popular_symbols)}

### 🔄 Symbol Entered: `{symbol}`
This symbol will be supported with real-time data in the next update!
"""

        analysis_info = """## 🚀 What's Coming

### Real-time Features:
- Live data for **all** stock symbols
- MCP server integration with market feeds  
- Advanced technical analysis
- Portfolio tracking and alerts

**💡 Tip**: Try one of the available demo symbols to see the full interface!
"""

        quick_stats = f"""
        <div class="compact-card">
            <h4 style="margin: 0 0 0.75rem 0; font-size: 1rem;">📋 Symbol Status</h4>
            <div style="text-align: center;">
                <div style="font-size: 1.1em; font-weight: bold; margin: 0.5rem 0; color: #f59e0b;">
                    {symbol}
                </div>
                <div style="margin: 0 0 0.75rem 0; color: #64748b; font-size: 0.85rem;">
                    Not in demo data
                </div>
                <div style="font-size: 0.8rem; color: #64748b; line-height: 1.3;">
                    Try: AAPL, GOOGL, MSFT, TSLA, NVDA, AMZN, META
                </div>
            </div>
        </div>
        """
        
        search_status = """
        <div class="compact-card">
            <h4 style="margin: 0 0 0.75rem 0; font-size: 1rem;">🔄 Status</h4>
            <div style="text-align: center;">
                <div style="margin: 0.5rem 0; color: #f59e0b; font-weight: bold;">
                    Not Found
                </div>
                <div style="margin: 0 0 0.75rem 0; font-size: 0.85rem; color: #64748b;">
                    Demo mode only
                </div>
                <div style="font-size: 0.8rem; color: #64748b;">
                    Limited symbols available
                </div>
            </div>
        </div>
        """
        
        return stock_info, analysis_info, quick_stats, search_status

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
                
                # Enhanced Output Layout with multiple components
                with gr.Row():
                    # Left Column - Main Results
                    with gr.Column(scale=2):
                        stock_info = gr.Markdown(
                            label="📊 Stock Information",
                            value="Enter a stock symbol and click Search to see detailed information...",
                            elem_classes=["main-content-card"],
                            show_label=False
                        )
                        
                        analysis_info = gr.Markdown(
                            label="� Investment Analysis",
                            value="Analysis results will appear here...",
                            elem_classes=["main-content-card"],
                            show_label=False
                        )
                    
                    # Right Column - Compact Quick Stats & Status
                    with gr.Column(scale=1):
                        quick_stats = gr.HTML(
                            value="""
                            <div class="compact-card">
                                <h4 style="margin: 0 0 0.75rem 0; font-size: 1rem;">📋 Quick Stats</h4>
                                <div style="text-align: center; color: #64748b; font-size: 0.9rem;">
                                    Search for a stock to see quick statistics
                                </div>
                            </div>
                            """,
                            show_label=False
                        )
                        
                        search_status = gr.HTML(
                            value="""
                            <div class="compact-card">
                                <h4 style="margin: 0 0 0.75rem 0; font-size: 1rem;">🔍 Status</h4>
                                <div style="text-align: center; color: #64748b; font-size: 0.9rem;">
                                    Ready to search
                                </div>
                            </div>
                            """,
                            show_label=False
                        )
                
                # Connect button click to enhanced handler functions
                search_btn.click(
                    fn=search_stock_enhanced,
                    inputs=symbol_input,
                    outputs=[stock_info, analysis_info, quick_stats, search_status]
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
