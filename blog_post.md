---
title: "I Built an AI Agent to Kill Bad Product Ideas"
date: 2026-01-18
description: "How I built a Streamlit app that uses the 9 Levers Framework to ruthlessly evaluate product ideas and email you a detailed report."
tags: [AI, Streamlit, Python, Product Management]
---

We've all been there: you have a "billion-dollar idea" at 2 AM. You buy the domain, set up the repo, and maybe even start coding. But should you?

To save myself (and you) from the sunk cost fallacy, I built the **Product Decision Agent**. It’s an AI-powered tool that acts as your ruthless co-founder, forcing you to answer the hard questions before you commit.

## How It Works

The app implements the **9 Levers Framework**, a mental model for vetting startups. Instead of a simple chat that drifts off-topic, I built a structured workflow:

1.  **The Inputs**: You fill out a form covering critical levers like *Market Window*, *Strategic Moat*, and *Distribution Edge*. You can even upload your pitch deck (PDF).
2.  **The Analysis**: GPT-4o acts as the critic, analyzing your inputs against the framework to find holes in your logic.
3.  **The Delivery**: Instead of just displaying text on a screen, the agent generates a professional HTML report and emails it directly to your inbox.

## The Tech Stack

I kept the architecture clean and deployable:

*   **Frontend**: [Streamlit](https://streamlit.io/) for rapid UI development.
*   **Backend**: Python with `openai` for reasoning and `resend` for transactional emails.
*   **Deployment**: Hosted on Streamlit Cloud (or locally with Docker).
*   **Security**: Environment variables for all API keys, ensuring no secrets are ever committed to GitHub.

## Why Email?

Chat bots are ephemeral. Product strategies are durable. I wanted the output to be something you could save, forward to a co-founder, or look back on in 6 months. By moving the "result" to email, the app becomes a tool for generating *artifacts*, not just conversation.

## Try It Out

I’ve open-sourced the code on [GitHub](https://github.com/cpkcode/gonogo). You can clone it, customize the system prompt, and spin up your own decision engine.

Or, try the live demo right here:

<iframe
  src="https://gonogo-agent.streamlit.app/?embed=true"
  height="850"
  style="width:100%;border:none;"
></iframe>
