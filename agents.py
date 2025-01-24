from crewai import Agent
from tools import yt_tool

from dotenv import load_dotenv
load_dotenv()
import os
os.environ["OPEN_API_KEY"]=os.getenv("OPENAPI_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4-0125-preview"


##Create a senior blog content researcher


blog_researcher=Agent(
    role='Blog Researcher from Youtube Videos',
    goal='get the relevant video content for the topic{topic} form Yt channel',
    verboe=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI Data Science, Machine learning and GEN AI and providing suggestion"
    ),
llm=llm,	
    tools=[yt_tool],
    allow_delegation=True
)



## creating a senior blog writer agent with yt tool
blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT channel',
    verboe=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topis, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
llm=llm,
    tools=[yt_tool],
    allow_delegation=False,
    
)
