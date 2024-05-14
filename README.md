
# Clarity-from-Chaos

### Abstract
Issue threads are essential in software development, encompassing problem descriptions, developer discussions, and proposed solutions. Summarizing these threads effectively is crucial because it enables developers to quickly capture essential insights, facilitating improved and faster decision-making. To understand the significance of these threads, we conducted a survey involving both industry professionals and researchers. We found that navigating through extensive issue threads presents considerable difficulty for both sectors. To address this need, we explore the use of Large Language Models (LLMs) such as GPT-3.5, GPT-4, Llama-2, and CodeLlama for summarizing these threads. In our prompt engineering method, guided by 26 principles, we focus on crafting prompts that yield summaries beneficial for developers. Using suitable prompts, our evaluation framework employs a hybrid approach, integrating both state-of-the-art automated metrics and human judgment, ensuring summaries are contextually accurate and reliable. Additionally, we propose a self-evaluation approach for LLMs, providing preliminary results that contribute to our automated evaluation framework. Our analysis shows GPT-4 as the standout model, producing summaries with greater accuracy and conciseness, which highlights its effectiveness in meeting the summarization needs of these threads. Furthermore, our generated prompts have significantly contributed to enhancing the quality of summaries. We aim to direct future research, emphasizing the potential of LLMs to transform how developers engage with issue threads. 


### Dataset
The PI-Link dataset used for the issue threads can be found in from here https://www.kaggle.com/datasets/zakareaalshara/android-closed-issues-20110101-20210101-clean. The generated summaries from each model are available in the 'Dataset' folder.


This GitHub repository includes all the necessary code for the evaluation metrics within the 'Evaluation Metrics' folder, accompanied by a README file with instructions on how to run them. 

