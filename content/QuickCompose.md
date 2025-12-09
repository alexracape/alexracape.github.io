# QuickCompose


## Problem

While interning at New York Life, I worked with a team of interns to help life insurance with their email marketing campaigns. Currently, agents spend a significant amount of time drafting emails, and smaller firms often don't have the resources to pursue marketing whatsoever.


## Solution

Our solution was to build an MCP (Model Context Protocol) server that would allow LLMs to access and use tools to draft personalized and compliant email campaigns. MCP essentially provides an LLM with a list of tools that it can use to accomplish a task. In our use case, we built tools for pulling Salesforce CRM data, fetching New York Life branded assets, checking compliance, and finally sending the email via AWS SES.

Our implementation was informed by the feedback we got from agents, managers, and members of our marketing and compliance teams. Agents were extremely excited to see features like  mailing list curation with natural language and fastracked compliance checking. The compliance team was just excited to have a tool that could take some work off of their plate.


## Impact

This project was an important proof of concept, and it sparked a lot of interest from senior management in pursuing this technology further. In our conversations with agents, they said that they could spend up to an hour drafting an email whereas our tool would take only a few minutes. In addition, our tool would speed up the compliance process which typically takes several days. 

