# TrendPilot – Local Agentic AI Assistant

## 1. Project Overview

TrendPilot is a local Agentic AI assistant developed as part of the AIRI Team PITB AI Internship Task 2.

It uses Ollama with the Gemma 3:4B language model to generate structured social media content based on a user's topic, selected platform, tone, and output type.

Unlike a basic chatbot, TrendPilot follows an agentic workflow by planning tasks, using multiple tools, reviewing generated content, managing memory, and saving final results locally.

## 2. Technologies Used

- Python
- Ollama
- Gemma 3:4B
- Requests
- JSON
- Markdown
- ReportLab (for PDF report generation)

## 3. Key Features

- **Trend Idea Generator:** Generates creative content ideas.
- **Caption Writer:** Creates platform-specific captions.
- **Hashtag Generator:** Suggests relevant hashtags.
- **Reel Script Generator:** Creates short-form video scripts.
- **Content Reviewer:** Reviews generated content and suggests improvements.
- **File Saver:** Saves generated results as Markdown files.
- **Memory Management:** Stores and retrieves previous outputs.

## 4. Supported Platforms

- Instagram
- LinkedIn
- YouTube
- X (Twitter)
- Facebook

## 5. Agent Workflow

1. User enters a topic, platform, tone, and output type.
2. The agent understands the user's request.
3. The agent creates a content generation plan.
4. It selects and calls the required tools.
5. The content is generated using the local LLM.
6. The Content Reviewer checks the generated output.
7. The File Saver stores the final result.
8. The agent returns the generated content and saved file path.

## 6. Project Structure

```text
agentic_ai_task_2/
│
├── app/
│   ├── main.py
│   ├── agent.py
│   ├── tools.py
│   ├── memory.py
│   └── prompts.py
│
├── outputs/
│   └── saved_results/
│
├── tests/
│   └── test_cases.md
│
├── screenshots/
│   ├── ollama_running.png
│   ├── demo_output.png
│   └── saved_file_output.png
│
├── report/
│   ├── final_report.pdf
│   └── generate_report.py
│
├── README.md
├── requirements.txt
└── demo.py
```

## 7. Installation and Setup

### Prerequisites

- Python installed
- Ollama installed
- Gemma 3:4B model

### Step 1: Download the Model

```bash
ollama pull gemma3:4b
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Application

Make sure Ollama is running, then execute:

```bash
python demo.py
```

Follow the terminal instructions to enter the topic, select the platform, choose a tone, and select the output type.

## 8. Testing

The project was tested using 10 different test cases covering multiple topics, platforms, tones, and output types.

The test cases and their results are documented in:

`tests/test_cases.md`

All 10 test cases passed after the improvements.

## 9. Screenshots

The `screenshots/` directory contains:

- Ollama model verification
- CLI demo execution
- Generated and saved content output

## 10. Final Report

The final project report is available at:

`report/final_report.pdf`

It documents the project overview, workflow, tools, testing, error analysis, screenshots, and conclusion.

## 11. Limitations

- Content generation depends on the locally installed language model.
- Generated ideas are not verified against live social media trends.
- Output quality may vary depending on the topic and prompt.
- Human review is recommended before publishing generated content.

## 12. Future Improvements

- Integrate live web search for current trends.
- Add a Streamlit-based user interface.
- Improve memory using SQLite.
- Add user feedback and content refinement.
- Explore larger local language models.

## 13. Privacy

TrendPilot uses a local language model through Ollama. Prompts are processed by the local model rather than requiring a hosted LLM API.

## 14. Internship Information

**Program:** AIRI Team – PITB AI Internship  
**Task:** Agentic AI Assistant – Task 2  
**Project:** TrendPilot – Local Agentic AI Assistant
