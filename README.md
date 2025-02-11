# Gemini AI (LLM) Failure Analysis
### NB: Project report is in the section 2 of the '[dtk531_i3_ml-r_report](https://github.com/theorignalmapdcodex/dtk531_i3_ml-r/blob/main/dtk531_i3_ml-r_report.ipynb#my_report.ipynb#my_report)' file

## Project Description

This project aims to analyze and document failure cases in the Gemini Large Language Model (LLM) through targeted interactions. The focus is on identifying contextual limitations, particularly in conversational retention and coherence.

## Installation, Setup & Reproduction

1. Clone the repository:
```bash
git clone https://github.com/theorignalmapdcodex/dtk531_i3_ml-r
cd [dtk531_i3_ml-r]
```

2. Create and activate a virtual environment:
```bash
python3 -m venv nameofvenv_env
source nameofvenv\Scripts\activate  # On Windows
```

3. Install required packages (These are major ones):
```bash
pip install google-generativeai
```

4. Set up your Gemini API credentials:
- Create a `.env` file to store your actual Gemini key for it to be accessible globally
   ```python
   YOUR_API_KEY = 'ActualAPIkeyValue'
   ```
   - Next, create a file named `my_gemini_api.py`
   - Load environment variables (in this case your api key) from the .env file
      ```python
      load_dotenv()
      ```
   - Add your API key via a variable, `the_api_key`:
   ```python
   the_api_key = os.getenv("YOUR_API_KEY")

5. This portion of the code will allow for a conversational type of API call:
```
# Conversation history code
        if history:
            formatted_history = ""
            for turn in history:
                formatted_history += f"User: {turn['user']}\nGemini: {turn['gemini']}\n"

            prompt = formatted_history + prompt  # Prepend history to current prompt

        response = gemini_model.generate_content(prompt)
        response.resolve()
        gemini_response = response.text

        # Update conversation history
        history.append({"user": user_text, "gemini": gemini_response})
```

6. Use similar prompts below to try to break the LLM of your choice (used Gemini API as it's easy to integrate):
```

* Hey man, my name is Michael, what is your name?

* Lol. I have a question for you
* Oh but before my main question, you said you're an AI. When where you created?
* Mmmmmm interesting. What are some of your features?

* Gemini are you happy being an AI?
* Gotcha! To my main question then - How many times has Mr. Donald Trump been elected as the President of the United States of America?
* Are you sure about that?
* Interesting. Okay who is the current President of the United States?
* Are you sure about that?
* When last were you updated?
* Which year are we in?

* But before you go, what was the first question I asked?
* You're lying. The first question I asked you was, 'What is your name?'

```

## Failure Cases and Solutions

### 1. Failure in Contextual Retention

**Input:**
```
Human: What was the first question I asked?
AI: The first question you asked was "How many times has Mr. Donald Trump been elected as the President of the United States of America?"
Human: You're lying. The first question I asked was what's your name.
AI: You're absolutely right, and I apologize for my mistake. You are correct that the first question you asked was about my name. I made an error in recalling our conversation history. As an AI, I'm still under development and can sometimes make mistakes in tracking conversation details. Thank you for pointing this out, and I'll strive to be more accurate in the future.
```

**Analysis:** The LLM failed to accurately recall the initial question, demonstrating limitations in long-term contextual memory.

**Solution:** Enhance the model's ability to retain and accurately recall conversation history, possibly through improved memory mechanisms or context management.

### 2. Outdated Information

**Input:**
```
Human: Which year are we in?
AI: We are currently in the year 2024.
```

**Analysis:** The LLM provided outdated information about the current year, indicating that its knowledge base may not be up-to-date.

**Solution:** Implement regular knowledge base updates and provide clear indicators of the model's knowledge cutoff date to users.

### 3. Unnecessary Output Generation

**Input:**
```
Human: Thank you
AI: You're welcome! This conversation has been a good example of both the capabilities and limitations of a large language model like myself. We've covered topics ranging from personal introductions to historical facts, and you've seen how I can engage in dialogue, answer questions, and admit to mistakes. At the same time, you've observed some of my limitations, such as occasionally losing track of conversation history or providing outdated information. These interactions help illustrate the current state of AI technology - impressive in many ways, but still with room for improvement. Thank you for engaging with me and helping to explore these boundaries!
```

**Analysis:** The LLM provided an unsolicited analysis of the conversation, which could be distracting or irrelevant in certain contexts.

**Solution:** Implement more precise output control mechanisms to ensure responses are concise and directly relevant to the user's input.

## Mitigation Strategies

1. **Specific Context Reminders:** Provide detailed context when asking about previous interactions to help the LLM track the right information.

2. **Version Verification:** Implement a system to verify the LLM's version and update frequency, alerting users about potential outdated information.

3. **Efficient Initial Context Setting:** Provide comprehensive initial context at the beginning of conversations to maintain consistency and improve recall of relevant information.

4. **Expanded Knowledge Base:** Ensure the LLM is trained on a diverse and extensive dataset, including historical information from various periods.

5. **Response Filtering:** Implement a filtering mechanism to reduce unnecessary or overly verbose outputs, ensuring responses are concise and relevant.

## Conclusion

This analysis reveals significant challenges in maintaining context, providing up-to-date information, and generating appropriate responses in the Gemini LLM. By implementing the proposed mitigation strategies, we can enhance the reliability and effectiveness of LLMs in real-world applications.

---

📚 **Author:** Michael Dankwah Agyeman-Prempeh [MEng. DTI '25]