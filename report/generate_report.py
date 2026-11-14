import os
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, Image, KeepTogether
)

# Project paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCREENSHOT_DIR = os.path.join(BASE_DIR, "screenshots")
OUTPUT_FILE = os.path.join(BASE_DIR, "report", "final_report.pdf")

# Colors
NAVY = colors.HexColor("#17365D")
BLUE = colors.HexColor("#2878B5")
LIGHT_BLUE = colors.HexColor("#EAF2F8")
LIGHT_GREY = colors.HexColor("#F3F5F7")
DARK_GREY = colors.HexColor("#404040")

# PDF document
doc = SimpleDocTemplate(
    OUTPUT_FILE,
    pagesize=A4,
    rightMargin=45,
    leftMargin=45,
    topMargin=55,
    bottomMargin=50
)

styles = getSampleStyleSheet()

styles.add(ParagraphStyle(
    name="CoverTitle",
    parent=styles["Title"],
    fontSize=30,
    leading=38,
    textColor=NAVY,
    alignment=TA_CENTER,
    spaceAfter=20
))

styles.add(ParagraphStyle(
    name="CoverSubtitle",
    parent=styles["Normal"],
    fontSize=15,
    leading=22,
    textColor=BLUE,
    alignment=TA_CENTER
))

styles.add(ParagraphStyle(
    name="SectionHeading",
    parent=styles["Heading1"],
    fontSize=18,
    leading=24,
    textColor=NAVY,
    spaceBefore=12,
    spaceAfter=10
))

styles.add(ParagraphStyle(
    name="SubHeading",
    parent=styles["Heading2"],
    fontSize=12,
    leading=17,
    textColor=BLUE,
    spaceBefore=8,
    spaceAfter=6
))

styles.add(ParagraphStyle(
    name="BodyCustom",
    parent=styles["BodyText"],
    fontSize=9.5,
    leading=15,
    textColor=DARK_GREY,
    spaceAfter=8
))

styles.add(ParagraphStyle(
    name="CaptionCustom",
    parent=styles["Normal"],
    fontSize=9,
    leading=13,
    textColor=DARK_GREY,
    alignment=TA_CENTER,
    spaceAfter=12
))

story = []


def add_heading(text):
    story.append(Paragraph(text, styles["SectionHeading"]))


def add_body(text):
    story.append(Paragraph(text, styles["BodyCustom"]))


def add_table(data, widths):
    table = Table(data, colWidths=widths, repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("LEADING", (0, 0), (-1, -1), 11),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#D5DDE5")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT_GREY]),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(table)
    story.append(Spacer(1, 12))


def add_screenshot(filename, caption):
    path = os.path.join(SCREENSHOT_DIR, filename)

    if os.path.exists(path):
        img = Image(path)
        max_width = 6.4 * inch
        max_height = 4.4 * inch

        scale = min(
            max_width / img.drawWidth,
            max_height / img.drawHeight
        )

        img.drawWidth *= scale
        img.drawHeight *= scale
        img.hAlign = "CENTER"

        story.append(Spacer(1, 8))
        story.append(img)
        story.append(Paragraph(caption, styles["CaptionCustom"]))
    else:
        add_body("Screenshot not found: " + filename)


def add_footer(canvas, document):
    canvas.saveState()
    canvas.setStrokeColor(LIGHT_BLUE)
    canvas.line(45, 35, A4[0] - 45, 35)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(DARK_GREY)
    canvas.drawString(45, 22, "TrendPilot | AIRI Team - PITB AI Internship Task 2")
    canvas.drawRightString(A4[0] - 45, 22, f"Page {document.page}")
    canvas.restoreState()


# ==================================================
# COVER PAGE
# ==================================================

story.append(Spacer(1, 1.5 * inch))
story.append(Paragraph("TRENDPILOT", styles["CoverTitle"]))
story.append(Paragraph(
    "Local Agentic AI Content Assistant",
    styles["CoverSubtitle"]
))
story.append(Spacer(1, 0.5 * inch))

cover_data = [
    ["PROJECT REPORT", "AIRI Team - PITB AI Internship Task 2"],
    ["AI MODEL", "Gemma 3:4B via Ollama"],
    ["TECHNOLOGY", "Python, Ollama, Requests, JSON"],
    ["DEMO TYPE", "Command Line Interface (CLI)"],
]

cover_table = Table(cover_data, colWidths=[1.5 * inch, 4.5 * inch])
cover_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (0, -1), LIGHT_BLUE),
    ("TEXTCOLOR", (0, 0), (0, -1), NAVY),
    ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
    ("FONTNAME", (1, 0), (1, -1), "Helvetica"),
    ("FONTSIZE", (0, 0), (-1, -1), 10),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#D5DDE5")),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("PADDING", (0, 0), (-1, -1), 10),
]))

story.append(cover_table)
story.append(Spacer(1, 1 * inch))
story.append(Paragraph(
    "A practical implementation of an Agentic AI workflow "
    "for social media content generation, review, memory, "
    "and local file saving.",
    styles["CoverSubtitle"]
))
story.append(PageBreak())


# ==================================================
# 1. PROJECT OVERVIEW
# ==================================================

add_heading("1. Project Overview")

add_body(
    "TrendPilot is a local Agentic AI assistant designed to help users "
    "generate social media content for different platforms. It uses the "
    "Gemma 3:4B language model through Ollama. The system accepts a topic, "
    "platform, tone, and output type, then creates an execution plan, "
    "generates content, reviews the result, saves the output, and stores "
    "the generated record in memory."
)

add_heading("2. Problem Statement")

add_body(
    "Creating platform-specific social media content can require time "
    "and repeated manual effort. Content also needs to match the selected "
    "platform, tone, and format. TrendPilot addresses this problem by "
    "providing a local AI-assisted workflow that combines generation, "
    "review, memory, and file saving."
)

add_heading("3. Project Objectives")

objectives = [
    "Use a locally running language model through Ollama.",
    "Implement an agentic workflow with planning and tool execution.",
    "Provide multiple content generation and review tools.",
    "Store previous generated results using a memory system.",
    "Save final outputs as local Markdown files.",
    "Test the system across multiple platforms and content formats."
]

for item in objectives:
    add_body("• " + item)


# ==================================================
# 4. TECHNOLOGIES
# ==================================================

add_heading("4. Technologies Used")

tech_data = [
    ["Technology", "Purpose"],
    ["Python", "Main programming language"],
    ["Ollama", "Runs the language model locally"],
    ["Gemma 3:4B", "Generates social media content"],
    ["Requests", "Communicates with the Ollama API"],
    ["JSON", "Stores memory records"],
    ["Markdown", "Stores generated content"],
]

add_table(tech_data, [1.7 * inch, 4.5 * inch])


# ==================================================
# 5. SYSTEM WORKFLOW
# ==================================================

add_heading("5. Agent Workflow")

workflow_data = [
    ["Step", "Description"],
    ["1. User Input", "Topic, platform, tone, and output type are provided."],
    ["2. Planning", "The agent creates an execution plan."],
    ["3. Memory Retrieval", "Previous records are retrieved from memory."],
    ["4. Content Generation", "The content generation tool uses Gemma 3:4B."],
    ["5. Content Review", "The reviewer evaluates the generated content."],
    ["6. File Saving", "The final output is saved as a Markdown file."],
    ["7. Memory Storage", "The generated result is stored in memory."],
]

add_table(workflow_data, [1.6 * inch, 4.6 * inch])


# ==================================================
# 6. TOOLS
# ==================================================

add_heading("6. Implemented Tools")

tools_data = [
    ["Tool", "Function"],
    ["Trend Idea Generator", "Suggests content ideas."],
    ["Caption Writer", "Creates captions for social media."],
    ["Hashtag Generator", "Generates relevant hashtags."],
    ["Reel Script Generator", "Creates short video scripts."],
    ["Content Reviewer", "Reviews generated content."],
    ["File Saver", "Saves final results to local files."],
    ["Complete Content Generator", "Coordinates content generation."],
]

add_table(tools_data, [2.2 * inch, 4.0 * inch])


# ==================================================
# 7. MEMORY AND OUTPUT
# ==================================================

add_heading("7. Memory and Output Management")

add_body(
    "TrendPilot uses a JSON-based memory system to retain records of "
    "previous generated content. The system retrieves previous records "
    "during execution and stores newly generated results. Final outputs "
    "are saved locally in Markdown format under the outputs directory."
)

add_body(
    "The local execution approach provides control over generated files "
    "and avoids sending prompts to a hosted model provider through the "
    "application's Ollama interface."
)


# ==================================================
# 8. SCREENSHOTS
# ==================================================

story.append(PageBreak())
add_heading("8. Implementation Screenshots")

add_screenshot(
    "ollama_running.png",
    "Figure 1. Ollama model availability showing Gemma 3:4B."
)

add_screenshot(
    "demo_output.png",
    "Figure 2. TrendPilot CLI execution, agent workflow, and completion."
)

add_screenshot(
    "saved_file_output.png",
    "Figure 3. Generated content saved as a local Markdown file."
)


# ==================================================
# 9. TESTING
# ==================================================

story.append(PageBreak())
add_heading("9. Testing and Validation")

add_body(
    "Ten test cases were executed using different topics, platforms, "
    "tones, and output types. The test results are recorded in "
    "tests/test_cases.md. TC-08 required prompt improvement and was "
    "successfully passed during retesting."
)

test_data = [
    ["Test ID", "Platform", "Output Type", "Status"],
    ["TC-01", "LinkedIn", "Post", "PASS"],
    ["TC-02", "Instagram", "Post", "PASS"],
    ["TC-03", "Facebook", "Post", "PASS"],
    ["TC-04", "YouTube", "Reel", "PASS"],
    ["TC-05", "Instagram", "Reel", "PASS"],
    ["TC-06", "LinkedIn", "Complete Plan", "PASS"],
    ["TC-07", "Facebook", "Complete Plan", "PASS"],
    ["TC-08", "X", "Post", "PASS (Retest)"],
    ["TC-09", "YouTube", "Complete Plan", "PASS"],
    ["TC-10", "Instagram", "Post", "PASS"],
]

add_table(test_data, [1.0 * inch, 1.6 * inch, 2.0 * inch, 1.6 * inch])


# ==================================================
# 10. ERROR ANALYSIS
# ==================================================

add_heading("10. Error Analysis")

error_data = [
    ["ID", "Observation", "Corrective Action"],
    ["E-01", "Content was truncated.", "Increased generation token limit."],
    ["E-02", "Review output was too lengthy.", "Added concise review instructions."],
    ["E-03", "Post included Reel Script.", "Added output-type-specific prompts."],
    ["E-04", "X content resembled LinkedIn.", "Added X-specific rules and retested."],
    ["E-05", "Some claims were unverified.", "Verify facts before publishing."],
    ["E-06", "Caption was generic.", "Improve format-specific prompts."],
]

add_table(error_data, [0.6 * inch, 2.7 * inch, 2.9 * inch])


# ==================================================
# 11. LIMITATIONS
# ==================================================

add_heading("11. Limitations")

limitations = [
    "Generated content may contain generic suggestions.",
    "Model-generated statistics and factual claims require verification.",
    "Content quality can vary depending on the topic and prompt.",
    "The current demonstration uses a command-line interface."
]

for item in limitations:
    add_body("• " + item)


# ==================================================
# 12. CONCLUSION
# ==================================================

add_heading("12. Conclusion")

add_body(
    "TrendPilot demonstrates a practical local Agentic AI workflow "
    "using Ollama and Gemma 3:4B. The system successfully performs "
    "planning, content generation, review, file saving, and memory "
    "storage. All ten test cases passed after addressing the identified "
    "issues, including the successful retest of TC-08. The project "
    "provides a foundation for further improvements in content quality, "
    "platform-specific instructions, and user interface design."
)

add_heading("13. Project Structure")

structure_data = [
    ["File / Folder", "Purpose"],
    ["app/main.py", "Application entry point"],
    ["app/agent.py", "Agent workflow and orchestration"],
    ["app/tools.py", "Content tools and Ollama interaction"],
    ["app/memory.py", "Memory management"],
    ["app/prompts.py", "Prompt instructions"],
    ["outputs/", "Generated content and saved results"],
    ["tests/test_cases.md", "Test cases and error analysis"],
    ["screenshots/", "Implementation screenshots"],
    ["report/final_report.pdf", "Project report"],
    ["demo.py", "CLI demo launcher"],
    ["README.md", "Project setup and overview"],
]

add_table(structure_data, [2.3 * inch, 3.9 * inch])


# ==================================================
# BUILD PDF
# ==================================================

doc.build(
    story,
    onFirstPage=add_footer,
    onLaterPages=add_footer
)

print("Professional report generated successfully!")
print("PDF location:", OUTPUT_FILE)