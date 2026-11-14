# TrendPilot - Local Agentic AI Content Assistant

## 1. Project Overview

TrendPilot is a local Agentic AI Content Assistant developed as part of the AIRI Team PITB AI Internship Task 2.

The application uses Ollama with the Gemma 3:4B language model to generate structured social media content based on the user's topic, selected platform, preferred tone, and output type.

TrendPilot demonstrates an agentic workflow that includes task planning, content generation, content review, memory management, and local file saving.

Unlike a basic chatbot, the application organizes these activities into a structured workflow and stores generated results locally for future reference.

## 2. Technologies Used

- **Programming Language:** Python
- **Local LLM Runtime:** Ollama
- **Language Model:** Gemma 3:4B
- **API Communication:** Requests
- **Memory Storage:** JSON
- **Output Format:** Markdown
- **PDF Generation:** ReportLab

## 3. Key Features

- **Trend Idea Generator:** Generates creative social media content ideas.
- **Caption Writer:** Creates captions according to the selected platform and tone.
- **Hashtag Generator:** Suggests relevant hashtags for generated content.
- **Reel Script Generator:** Generates short-form video scripts.
- **Content Reviewer:** Reviews generated content and provides improvement suggestions.
- **File Saver:** Saves generated results as Markdown files.
- **Memory Management:** Stores and retrieves previous outputs using JSON-based memory.

## 4. Supported Platforms

TrendPilot supports content generation for:

- Instagram
- LinkedIn
- YouTube
- X (Twitter)
- Facebook

## 5. Agent Workflow

The application follows a structured workflow:

1. The user enters a topic, platform, tone, and output type.
2. The agent processes the user's request.
3. A content generation plan is prepared.
4. The required content generation functionality is executed.
5. Content is generated using the local Gemma 3:4B model through Ollama.
6. The generated content is reviewed.
7. The result is saved locally using the File Saver functionality.
8. The application returns the generated content and saved file information.

## 6. Project Structure

```text
agentic_ai_task_2/
|-- app/
|   |-- main.py
|   |-- agent.py
|   |-- tools.py
|   |-- memory.py
|   `-- prompts.py
|-- outputs/
|   |-- generated_posts/
|   |-- generated_scripts/
|   `-- saved_results/
|-- tests/
|   `-- test_cases.md
|-- screenshots/
|   |-- ollama_running.png
|   |-- demo_output.png
|   `-- saved_file_output.png
|-- report/
|   |-- final_report.pdf
|   `-- generate_report.py
|-- README.md
|-- requirements.txt
`-- demo.py
```

## 7. Installation and Setup

### Prerequisites

Make sure the following are installed:

- Python
- Ollama
- Gemma 3:4B model

### Step 1: Install Ollama

Download and install Ollama from:

https://ollama.com/

### Step 2: Download the Model

Open a terminal and execute:

```bash
ollama pull gemma3:4b
```

### Step 3: Install Project Dependencies

Navigate to the project directory and run:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

Make sure Ollama is running and execute:

```bash
python demo.py
```

Follow the terminal instructions to enter the topic, select a platform, choose a tone, and select the required output type.

## 8. Testing

The project includes 10 documented test cases covering different topics, platforms, tones, and output types.

Test cases and their results are available in:

`tests/test_cases.md`

The documented test results indicate that all 10 test cases passed after the improvements.

## 9. Screenshots

The `screenshots/` directory contains project screenshots, including:

- Ollama model verification.
- CLI application execution.
- Generated content and saved file output.

These screenshots provide visual evidence of the application's execution and output.

## 10. Final Project Report

The final project report is available at:

`report/final_report.pdf`

The report documents:

- Project overview and objectives.
- Technologies and tools used.
- Agent workflow.
- Implementation details.
- Testing and test results.
- Error analysis.
- Screenshots and conclusion.

## 11. Limitations

- Content generation depends on the locally installed language model.
- The application does not verify generated ideas against live social media trends.
- Output quality may vary depending on the topic, prompt, and model response.
- Generated content may require human review before publishing.
- Model performance depends on the available system resources.

## 12. Future Improvements

Potential future enhancements include:

- Integrating live web search for current trends.
- Developing a Streamlit-based graphical user interface.
- Improving memory management using SQLite.
- Adding user feedback and content refinement.
- Exploring larger local language models.
- Improving automated content evaluation.

## 13. Privacy

TrendPilot uses a local language model through Ollama. Prompts are processed through the locally running model rather than requiring a hosted LLM API.

The application stores generated results and memory locally in project files.

## 14. Assignment Details

- **Program:** AIRI Team - PITB AI Internship
- **Task:** Agentic AI Assistant - Task 2
- **Project:** TrendPilot - Local Agentic AI Content Assistant

## 15. What I Learned

Through this project, I gained practical experience in:

- Running a local language model using Ollama and Gemma 3:4B.
- Connecting Python applications with the Ollama API using Requests.
- Understanding agent planning and tool execution.
- Organizing content generation, review, and file-saving functionality.
- Implementing JSON-based memory management.
- Testing AI applications and analyzing errors.
- Understanding the importance of human review and fact-checking.

## 16. LinkedIn Project Summary

**TrendPilot - Local Agentic AI Content Assistant**

TrendPilot is a local Agentic AI project developed using Python, Ollama, and Gemma 3:4B.

The application accepts a topic, platform, tone, and output type. It prepares a content generation plan, generates social media content, reviews the output, saves results as Markdown files, and maintains records using JSON-based memory.

The project demonstrates practical implementation of local LLM integration, agent workflows, content generation, memory management, testing, and error analysis.

**Demo Command:**

`python demo.py`

**GitHub Repository:**

TrendPilot-Local-Agentic-AI

## 17. LinkedIn Post

I am pleased to share my project, **TrendPilot - Local Agentic AI Content Assistant**, developed as part of the AIRI Team PITB AI Internship Task 2.

Built using Python, Ollama, and Gemma 3:4B, TrendPilot demonstrates a local Agentic AI workflow for generating and reviewing social media content.

Key implementation areas include:

- Local LLM integration with Ollama.
- Agent planning and workflow execution.
- Social media content generation.
- Content review and improvement suggestions.
- JSON-based memory management.
- Markdown file saving.
- Testing and error analysis across 10 test cases.

Working on this project helped me gain practical experience in developing and testing local Agentic AI applications.

#AgenticAI #ArtificialIntelligence #Python #Ollama #LLM #PITB
