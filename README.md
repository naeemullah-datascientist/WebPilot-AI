# 🌐 WebPilot AI: Autonomous Web Navigator

**WebPilot AI** is an intelligent, autonomous browser agent designed to navigate the web, perform complex searches, and extract data just like a human—but at machine speed. Instead of relying on brittle, hard-coded scripts, it leverages **Large Language Models (LLMs)** and **Playwright** to understand web content semantically and make real-time decisions.

---

##  Why WebPilot AI?
Traditional automation tools (like Selenium) break the moment a website updates its UI or changes a button's ID. **WebPilot AI is different.** 
- **Design Agnostic:** It analyzes the "meaning" of a page. Even if the search bar moves or changes its CSS class, the agent "reasons" its way to find the right element.
- **Goal-Oriented:** You give it a mission, and it figures out the steps to get there autonomously.

##  Key Features
- **Autonomous Reasoning Loop:** Uses a "Thought-Action-Observation" cycle to complete multi-step tasks.
- **Dynamic Element Interaction:** Automatically handles browser navigation, text input, and clicking through dynamic content.
- **High-Performance Inference:** Powered by **Llama 3.3-70B (via Groq)** for sub-second reasoning and decision-making.
- **Self-Correction:** Built to handle dynamic UI changes and recover from selector timeouts.
- **Async Architecture:** Developed using Python's `asyncio` and Playwright for high-speed, non-blocking execution.

##  Tech Stack
- **Engine:** Python & Playwright (Asynchronous API)
- **Brain (LLM):** Llama 3.3-70B via Groq (OpenAI Proxy logic)
- **Framework:** LangChain (Core Messaging & Orchestration)
- **Environment:** Managed via `python-dotenv` for secure API handling

##  How it Works (The Workflow)
1. **Perception:** The agent launches a Chromium instance and extracts the simplified inner text of the page.
2. **Analysis:** It sends the task and current page state to the LLM.
3. **Decision:** The AI evaluates the page and responds with a specific action (e.g., `SEARCH`, `CLICK`, or `ANSWER`).
4. **Execution:** The custom engine translates the AI's decision into a Playwright command.
5. **Observation:** The agent observes the result of its action on the new page and repeats the cycle until the mission is accomplished.

##  Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/naeemullah-datascientist/WebPilot-AI.git
   cd WebPilot-AI

Install Dependencies:

code
Bash
download
content_copy
expand_less
pip install -r requirements.txt
playwright install chromium

Configure Environment Variables:
Create a .env file in the root directory and add your Groq API Key:

code
Text
download
content_copy
expand_less
GROQ_API_KEY=your_gsk_key_here

Run the Agent:

code
Bash
download
content_copy
expand_less
python main.py
📊 Sample Mission

User Prompt: "Find out who coined the term Artificial Intelligence and in what year."

The AI Workflow:

Navigates to Google.com.

Identifies the search bar and types "Who coined the term Artificial Intelligence".

Analyzes the search results and clicks on the most relevant link.

Reads the page content, extracts the fact, and terminates.

Final Result: "John McCarthy, in 1955."

 Developed by

Naeem Ullah
Final Year Data Science Student @ PUCIT
LinkedIn 
