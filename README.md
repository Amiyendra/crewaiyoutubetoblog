# YouTube-Powered Blog Researcher and Writer Agents

This project uses **CrewAI** agents to create a powerful system for researching and writing blogs based on content from YouTube videos. With distinct roles and capabilities, the agents extract relevant information from videos and craft compelling narratives for technology enthusiasts.

---

## Features

### 1. Blog Researcher Agent
- **Role**: Extracts relevant content from YouTube videos.
- **Specialization**: Focused on topics related to AI, Data Science, Machine Learning, and Generative AI.
- **Capabilities**:
  - Leverages the `yt_tool` for interacting with YouTube content.
  - Maintains memory and context for efficient research.
  - Uses advanced LLM capabilities for understanding video content.

### 2. Blog Writer Agent
- **Role**: Creates engaging and simplified blogs based on YouTube video content.
- **Specialization**: Narrates tech stories in an accessible manner, making complex topics understandable.
- **Capabilities**:
  - Utilizes insights from the Researcher Agent to craft blogs.
  - Focused on delivering concise, captivating, and informative content.
  - Uses LLM-powered language generation with a creative flair.

---

## Requirements

### Python Libraries
- **CrewAI**: To create and manage intelligent agents.
- **dotenv**: For securely managing API keys and environment variables.

### API Keys
1. **OpenAI API Key**: Required for language model-based tasks.
2. **YouTube API (via yt_tool)**: Required for interacting with YouTube content.

---

## Setup and Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-folder>
