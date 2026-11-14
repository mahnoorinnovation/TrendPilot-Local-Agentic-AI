# TrendPilot AI Agent - Test Cases

## Project: TrendPilot
## Model: Gemma 3:4B via Ollama

| Test ID | Topic | Platform | Tone | Output Type | Expected Result |
|---|---|---|---|---|---|
| TC-01 | Artificial Intelligence in Education | LinkedIn | Professional | Post | Complete LinkedIn post without Reel Script |
| TC-02 | Cybersecurity Awareness for Students | Instagram | Friendly | Post | Friendly caption, relevant hashtags, and suggestions |
| TC-03 | Healthy Study Habits | Facebook | Casual | Post | Clear and engaging Facebook content |
| TC-04 | Python Programming for Beginners | YouTube | Professional | Reel | Short video script with hook, explanation, visuals, and closing |
| TC-05 | Benefits of Machine Learning | Instagram | Casual | Reel | Instagram Reel script with relevant hashtags |
| TC-06 | Importance of Time Management | LinkedIn | Professional | Complete Plan | Complete content plan with caption and Reel Script |
| TC-07 | Environmental Protection | Facebook | Friendly | Complete Plan | Complete structured content plan |
| TC-08 | Data Science Career Opportunities | X | Professional | Post | Concise post appropriate for X |
| TC-09 | Robotics in Modern Education | YouTube | Friendly | Complete Plan | Content plan with suitable title and thumbnail text |
| TC-10 | Digital Privacy Awareness | Instagram | Professional | Post | Complete post with relevant privacy-related hashtags |

## Expected Checks

For each test:
- The agent should accept the provided inputs.
- The agent should create an execution plan.
- The content generator tool should be called.
- The reviewer tool should review the generated content.
- The file saver should save the generated result.
- The memory system should store the result.
- The generated content should follow the selected platform, tone, and output type.
- The response should not be incomplete or truncated.

## Test Results

Actual results will be recorded after running each test.

| Test ID | Actual Result | Status | Error / Observation |
|---|---|---|---|
| TC-01 | Complete content generated, reviewed, and saved | PASS | Output: trendpilot_20261114_172157.md |
| TC-02 | Complete content generated, reviewed, and saved | PASS | Output: trendpilot_20261114_172712.md |
| TC-03 | Facebook post generated, reviewed, and saved | PASS | Output: trendpilot_20261114_175027.md |
| TC-04 | YouTube Reel script generated, reviewed, and saved | PASS | Output: trendpilot_20261114_175749.md |
| TC-05 | Instagram Reel generated, reviewed, and saved | PASS | Output: trendpilot_20261114_184333.md |
| TC-06 | Complete LinkedIn plan with caption and Reel script generated, reviewed, and saved | PASS | Output: trendpilot_20261114_190119.md |
| TC-07 | Facebook Complete Plan generated, reviewed, and saved | PASS | Output: trendpilot_20261114_190949.md |
| TC-08 | X post generated after prompt improvement | PASS (Retest) | Output: trendpilot_20261114_192529.md; initial failure documented |
| TC-09 | YouTube Complete Plan generated, reviewed, and saved | PASS | Output: trendpilot_20261114_193622.md |
| TC-10 | Instagram privacy awareness post generated, reviewed, and saved | PASS | Output: trendpilot_20261114_194232.md |

## Error Analysis

Error analysis will be completed after executing the test cases.

| Error ID | Error / Observation | Possible Cause | Corrective Action |
|---|---|---|---|
| E-01 | Initial content generation was truncated | Low generation token limit | Increased num_predict from 180 to 900 |
| E-02 | Initial review output was truncated | Review response was too lengthy | Added concise review instructions with a 150-word limit |
| E-03 | Post output initially included a Reel Script | Prompt did not distinguish output types | Updated prompt to generate sections according to output type |
| E-04 | Initial TC-08 output generated LinkedIn-style content instead of X content | Platform-specific prompt instructions were insufficient | Added explicit X platform rules and retested successfully |
| E-05 | Some generated content included unverified or unsupported suggestions, such as statistics or audience assumptions | Model-generated content may include unsupported details | Avoid publishing unverified claims; verify facts and audience assumptions before use |
| E-06 | TC-10 caption was generic and included unnecessary thumbnail suggestions for a Post | Output sections were not fully optimized for each content format | Improve format-specific instructions and review generated content before publishing |

## Conclusion

TrendPilot successfully executed all 10 test cases across different topics, platforms, tones, and output types. All test cases passed after resolving the identified issues, including the successful retest of TC-08. The agent demonstrated content generation, review, file saving, and memory functionality. Some content quality limitations remain and should be considered before publishing generated content.
















