# 💬 AI Assistant using OpenAI Agent SDK, OpenRouter & Chainlit

This project is a smart AI assistant built using the **OpenAI Agents SDK**, **OpenRouter**, and **Chainlit**. It uses the **DeepSeek model** via OpenRouter to understand and respond to user questions like a helpful chatbot.

---

## 🚀 Features

- ✅ Interactive AI assistant
- ✅ Memory of previous messages in the session
- ✅ Powered by **Agentic AI** (via OpenAI Agents SDK)
- ✅ Hosted in a beautiful **Chainlit UI**
- ✅ Uses **DeepSeek Chat Model (v3)** for natural conversations
- ✅ Uses **OpenRouter** as the model provider instead of OpenAI

---

## 🧠 Technologies Used

| Tech | Purpose |
|------|---------|
| 🧠 OpenAI Agent SDK | To manage the agent's reasoning and behavior |
| 🌐 OpenRouter | To use models like DeepSeek as OpenAI-compatible APIs |
| 💬 DeepSeek Chat v3 | Language model that answers user queries |
| 🧵 Chainlit | UI framework to chat with the agent |
| 🔐 dotenv | Load `.env` file to manage API keys securely |

---

## 🔧 Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
````

2. **Create a `.env` file** and add your OpenRouter API key:

```
OPEN_ROUTER_API_KEY=your_openrouter_key_here
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

> Example requirements.txt:

```txt
openai-agents
chainlit
python-dotenv
```

4. **Run your Chainlit app**

```bash
chainlit run main.py
```

---

## 🧩 How It Works (Step by Step)

1. **Agent Setup**

   * You create an agent using `OpenAI Agent SDK`.
   * This agent uses the **DeepSeek model** through **OpenRouter**.
   * Instructions tell the agent to behave like a helpful assistant.

2. **Chainlit Integration**

   * When the chat starts, it says hello.
   * On each user message:

     * The message is added to `history`.
     * The whole history is passed to the `Runner`.
     * The Runner sends the conversation to the agent.
     * The final reply is sent back to Chainlit's frontend.

3. **Memory (Session-based)**

   * You use `cl.user_session` to remember the conversation during a session.

---

## 🧠 What is OpenAI Agent SDK?

OpenAI’s **Agent SDK** allows you to:

* Define agents that can reason, plan, and act.
* Use different models (like OpenAI, DeepSeek) as the agent's brain.
* Chain steps together (tool use, memory, functions).

In your project, you're using just one agent (`Assistant`) for general conversation.

---

## 🌍 Why OpenRouter?

Instead of only using OpenAI models, you’re using [OpenRouter](https://openrouter.ai), which gives access to many models like:

* Claude
* Gemini
* Mistral
* DeepSeek ✅ (what you're using here)

---

## 📸 Screenshot (optional)

> Add a screenshot of your Chainlit chat UI here.

---

## 📚 Future Ideas

* Add tools (e.g., calculator, weather, email)
* Use file upload or document reading
* Save full chat history to a database

---

## 📄 License

This project is open-source and free to use under the MIT License.

