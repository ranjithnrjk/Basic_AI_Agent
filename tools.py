from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name='Search',
    func=search.run,
    description='useful for when you need to answer questions about current events with DuckDuckGo',
)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

def save_to_file(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    formatted_text = f"--- Reseach Output --- \nTimestamp: {timestamp}\n\n{data}\n\n--- End of Output ---"

    with open(filename, "a", encoding="utf-8") as file:
        file.write(formatted_text)

    return f"Data successfully saved to file: {filename}"

save_tool = Tool(
    name="Save_text_to_File",
    func= save_to_file,
    description="useful for saving data to a file",
)