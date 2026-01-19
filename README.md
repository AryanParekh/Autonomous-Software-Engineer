# 🤖 Autonomous Software Engineer

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![LangGraph](https://img.shields.io/badge/LangGraph-State_Machine-orange)
![Docker](https://img.shields.io/badge/Docker-Sandboxed_Execution-blue)
![License](https://img.shields.io/badge/License-MIT-green)

An autonomous coding agent that **writes, tests, runs, and debugs** its own code. 
Powered by **LangGraph** and **GPT-4o**, it mimics a real-world engineering team (Developer, QA, Executor) to solve complex algorithmic problems without human intervention.

## 🧠 The Architecture

This project simulates a closed-loop software development lifecycle using a State Graph:

```mermaid
graph TD
    Start([🚀 Start]) --> Dev[👨‍💻 Developer Agent]
    Dev --> QA[🕵️‍♂️ QA Agent]
    QA --> Exec[🐳 Docker Executor]
    
    Exec -- "❌ Test Failed" --> Dev
    Exec -- "✅ All Passed" --> Success([🏆 Mission Accomplished])

    subgraph "Self-Healing Loop"
    Dev
    QA
    Exec
    end
