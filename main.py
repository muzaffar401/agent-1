from agents import Agent,AsyncOpenAI,OpenAIChatCompletionsModel,RunConfig,Runner
import os
from dotenv import load_dotenv
import chainlit as cl

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

agent = Agent(
    name="Ai Assistant",
    instructions="You are a helpful assistant to answer any question"
)

@cl.on_chat_start
async def handle_chat_message():
    cl.user_session.set("history",[])
    await cl.Message(content="Hello, How may i help you").send()


@cl.on_message
async def handle_message(message:cl.Message):
    history = cl.user_session.get("history")
    history.append({"role":"user","content":message.content})
    result = await Runner.run(
        starting_agent=agent,
        input=history,
        run_config=config
    )
    history.append({"role":"assistant","content":result.final_output})
    cl.user_session.set("history",history)

    await cl.Message(content=result.final_output).send()
