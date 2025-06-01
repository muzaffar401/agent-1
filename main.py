from agents import Agent,AsyncOpenAI,OpenAIChatCompletionsModel,set_tracing_disabled,Runner
import os 
from dotenv import load_dotenv
import chainlit as cl

load_dotenv()


openrouter_api_key = os.getenv("OPEN_ROUTER_API_KEY")
openrouter_base_url = "https://openrouter.ai/api/v1"
deepseek_model = "deepseek/deepseek-chat-v3-0324:free"

provider = AsyncOpenAI(
    api_key=openrouter_api_key,
    base_url=openrouter_base_url
)


set_tracing_disabled(disabled=True)


agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant to answer any question",
    model=OpenAIChatCompletionsModel(model=deepseek_model,openai_client=provider)
)

@cl.on_chat_start
async def handle_chat():
    cl.user_session.set("history",[])
    await cl.Message(content="Hello,How may i help you😊").send()

@cl.on_message
async def handle_message(message:cl.Message):
    history = cl.user_session.get("history")
    history.append({"role":"user","content":message.content})
    result = await Runner.run(
    starting_agent=agent,
    input=history
    )
    history.append({"role":"assistant","content":result.final_output})
    cl.user_session.set("history",history)
    await cl.Message(content=result.final_output).send()


    



