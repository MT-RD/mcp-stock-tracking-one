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
    """Simple placeholder function for stock search"""
    if not symbol.strip():
        return "⚠️ Please enter a stock symbol!"
    
    return f"🔍 Searching for {symbol.upper()}...\n\n✨ Coming soon! MCP server connection will be added in the next update.\n\n📊 Features being developed:\n• Real-time stock prices\n• Investment analysis\n• Smart recommendations\n• Portfolio tracking"

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
                
                # Output area for search results
                result_output = gr.Textbox(
                    label="📋 Search Results", 
                    lines=6,
                    interactive=False,
                    placeholder="Enter a stock symbol and click Search to see results..."
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
