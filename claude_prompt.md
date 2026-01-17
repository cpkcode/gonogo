# Prompt for Claude

Please create a single-file React Artifact that implements the **Product Decision Agent** application.

## Goal
Build a fully interactive "Product Decision Agent" that guides users through the **9 Levers Framework** to evaluate a product idea. The application should be ruthlessly logic-driven, helping users combat cognitive biases.

## Technical Requirements
- **Tech Stack**: React, Tailwind CSS, Lucide React (for icons).
- **Format**: Single file (Artifact standard).
- **Design**: clean, professional, "ruthless but fair" aesthetic. Dark mode preferred or high-contrast light mode.

## Functional Requirements
The application should have the following flow:
1.  **Welcome Screen**: Brief intro to the "Product Decision Agent" persona.
2.  **Assessment Wizard**: A step-by-step interface for the 9 Levers.
    *   **The 9 Levers**:
        1.  Market Window (Weight: 3x)
        2.  Strategic Moat (Weight: 3x)
        3.  Distribution Edge (Weight: 3x)
        4.  Conviction Level (Weight: 2x)
        5.  Option Value (Weight: 2x)
        6.  External Validation (Weight: 2x)
        7.  Regulatory Ease (Weight: 2x)
        8.  Pipeline Alternatives (Weight: 2x)
        9.  Sunk Cost Bias (Weight: -1x) [PENALTY]
    *   **Per Step UI**:
        *   Title & Category.
        *   **Rubric Display**: Show the specific criteria for scores 9-10, 6-8, 3-5, 1-2 (Use the content provided below).

        *   **Evidence Input**: A text area for the user to answer the specific questions for this lever.
        *   **AI Evaluation**: The app should use the provided API Key to send the evidence + rubric to an LLM (Claude/OpenAI) and get a JSON response containing:
            *   Score (1-10)
            *   Reasoning/Critique
            *   Confidence
        *   **Display**: Show the AI's calculated score and reasoning. Allow the user to override if necessary, but default to AI judgment.
3.  **Settings/Configuration**:
    *   **API Key Input**: A secure field to input an OpenAI or Anthropic API Key (required for the AI evaluation to work).
4.  **Results Dashboard**:
    *   **Total Score Calculation**: Sum of (Score * Weight). Max 170.
    *   **Decision Thresholds**:
        *   **> 70**: STRONG GO
        *   **40 - 69**: CAUTIOUS PROCEED
        *   **< 40**: STRONG NO-GO
    *   **Visuals**: A bar chart or visual breakdown of the score contributors.
    *   **Recommendation Text**: Based on the score.

## Logic & Context
Use the following documentation to populate the **Rubrics**, **Descriptions**, and **Logic** for each lever exactly.

---
Logic and Rubric Details:

[PASTE CONTENT OF product_decision_agent_prompt.md HERE]
---
