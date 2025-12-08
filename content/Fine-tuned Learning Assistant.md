# Fine-tuned Learning Assistant

> This project is currently a work in progress. 

I was inspired by the years that I speant as a Learning Assistant at Bowdoin to create an assistant that could help students like a good TA would. When you go to office hours, you wouldn't expect to have the TA immediately give you a solution that you can copy and paste. Instead, you expect the TA to support you in your learning process instead of supplanting it. 

In this project, I have been using Constitutional AI to fine-tune an LLM. I built the Constitutional AI procedure and was able to generate a dataset with 10,000 examples.

Currently, I am exploring different fine-tuning algorithms like DPO and GRPO to see which one works best for this task. The initial training runs show the model becoming overly cautious and evasive, so I am working on tuning the hyperparameters used during training. 


[Dataset →](https://huggingface.co/datasets/aracape/cai-education-single-turn)

[Most recent model →](https://huggingface.co/aracape/teaching-assistant-8B-dpo)

[Source →](https://github.com/alexracape/consititutional-ai)
