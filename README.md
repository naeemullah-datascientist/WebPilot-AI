# 🌐 WebPilot AI: Autonomous Web Navigator

**WebPilot AI** is an intelligent, autonomous browser agent that performs web tasks just like a human. Instead of following rigid, hard-coded scripts, it uses **Large Language Models (LLMs)** and **Playwright** to understand page content and make real-time decisions to achieve a goal.

## Why it stands out
Traditional web scrapers break if a website changes its design. **WebPilot AI** is design-agnostic. It analyzes the "Semantic Meaning" of a page. If a button moves or a search bar changes its ID, the agent "reasons" its way through to find the correct element.

## Key Features
- **Autonomous Reasoning:** Uses an iterative loop (Step-by-Step) to decide whether to Search, Click, or provide an Answer.
- **Dynamic Action Handling:** Manages browser navigation, text input, and element interaction automatically via Playwright.
- **Optimized for Speed:** Powered by **Llama 3.3 (Groq)** for lightning-fast decision-making.
- **Custom Execution Loop:** Built with a custom async engine to avoid the limitations of third-party frameworks.

## Tech Stack
- **Engine:** Python & Playwright (Asynchronous API)
- **Intelligence:** Llama 3.3-70B via Groq
- **Orchestration:** LangChain (Core Logic)
- **Environment:** Managed via `.env` for secure API handling

## How it Works (The Workflow)
1. **Perception:** The agent opens the browser and extracts the "InnerText" of the page.
2. **Analysis:** It sends the task and page content to the LLM.
3. **Decision:** The AI responds with an action (e.g., `SEARCH: OpenAI Sora`).
4. **Execution:** Playwright executes the action on the live browser.
5. **Observation:** The agent looks at the new page and repeats until the task is complete.

##  Installation & Setup
1. **Clone the Repo:**
   ```bash
   git clone https://github.com/naeemullah-datascientist/WebPilot-AI.git
   cd WebPilot-AI
