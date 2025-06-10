---
title: MCP Stock Tracking App
emoji: 📈
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 5.33.1
app_file: app.py
pinned: false
license: mit
---

# MCP Stock Tracking App 📈

A stock analysis application powered by Model Context Protocol (MCP) for real-time data and investment insights.

## 🏗️ Architecture

```
┌─────────────────────┐    HTTP/JSON    ┌──────────────────────┐
│   Gradio Frontend   │ ◄─────────────► │   Modal MCP Server   │
│  (Hugging Face)     │      REST API   │     (Backend)        │
└─────────────────────┘                 └──────────────────────┘
```

## � Getting Started

```bash
pip3 install -r requirements.txt
python3 app.py
```

## 📄 License

MIT License
