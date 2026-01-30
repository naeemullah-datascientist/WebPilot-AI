import os
import asyncio
from dotenv import load_dotenv
from playwright.async_api import async_playwright
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

load_dotenv()

async def run_custom_agent(task):
    print(f"--- 🚀 WebPilot Custom Agent (Groq): {task} ---")
    
    # 1. Setup Groq Brain (Fast & Reliable)
    api_key = os.getenv("GROQ_API_KEY")
    llm = ChatGroq(
        model="llama-3.3-70b-versatile", 
        groq_api_key=api_key,
        temperature=0
    )

    async with async_playwright() as p:
        # 2. Launch Browser
        browser = await p.chromium.launch(headless=False) # Headless=False taake aap dekh sakein
        page = await browser.new_page()
        
        print("🌐 Browser Opened. Navigating to Google...")
        await page.goto("https://www.google.com")
        await asyncio.sleep(2) # Wait for page load

        # 3. Autonomous Loop
        for step in range(1, 6):
            print(f"\n📍 Step {step}: Analyzing page...")
            
            # Extract clean text from the page
            simplified_text = await page.evaluate("() => document.body.innerText.substring(0, 4000)")

            prompt = f"""
            You are an autonomous web agent.
            TASK: {task}
            CURRENT PAGE CONTENT (First 4000 chars):
            {simplified_text}

            What is your next move? 
            If you see the answer on the page, respond with ANSWER: [the answer].
            If you need to search, respond with SEARCH: [search term].
            If you need to click a link, respond with CLICK: [link text].
            
            Respond ONLY with the instruction.
            """

            response = await llm.ainvoke([HumanMessage(content=prompt)])
            ai_decision = response.content
            print(f"🤖 AI Decision: {ai_decision}")

            if "ANSWER:" in ai_decision:
                print(f"\n✅ Mission Accomplished!")
                print(f"RESULT: {ai_decision}")
                break
            
            # --- EXECUTION LOGIC ---
            if "SEARCH:" in ai_decision:
                search_term = ai_decision.split("SEARCH:")[1].strip()
                # Use a reliable selector for Google Search Bar
                await page.fill('textarea[name="q"]', search_term)
                await page.press('textarea[name="q"]', "Enter")
                print(f"🔍 Searching for: {search_term}")
                await asyncio.sleep(4) # Wait for results
            
            elif "CLICK:" in ai_decision:
                link_text = ai_decision.split("CLICK:")[1].strip()
                # Attempt to click the first search result (h3 tag)
                await page.click("h3")
                print(f"🖱 Clicking first result...")
                await asyncio.sleep(4)
            
            else:
                # If AI gives general text, try to just find the answer
                print("🤔 AI is thinking... trying to find final answer.")

        print("\n--- 🏁 Task Finished ---")
        await asyncio.sleep(5)
        await browser.close()

if __name__ == "__main__":
    mission = "Who coined the term Artificial Intelligence and in what year?"
    asyncio.run(run_custom_agent(mission))