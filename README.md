## Overview

#TODO /join TelegemChannelLink (can telegram api do that?)

Following data flow might be efficient:
- llm/t5 model that categorizes user telegram message into available pipeline, sends out request to that pipeline, returns result - similar to https://huggingface.co/papers/2307.16789 or similar papers, or much easier, with hardcode and very fire data pipelines for now 

- data pipeline 1: DSPy local / remote LLMs APIs response on prompt  
  
- data pipeline 2: DSPy local / remote LLMs APIs response on prompt with RAG 
  
- data pipeline 3: SD image generation 
! difference between /name_of_pipeline approach is that funnel llm(or t5) model can masseuse user prompt / control generation / repeat on failure
! "how's my usage of computer/tech is different from usage of X user cohort" where X user cohort is cohort of users whom you want tool to be used
  
- data pipeline 4: fetch urls mentioned or prompted by user, transcribe them (apple podcast audio/youtube-dl link video), if it's webpage PDFy it, OCR if it's Image, PDF without OCR level, caption PDF figures and Images, create index of transcriptions, figures and captions 
then respond on prompt in environment of that RAG index
  
4.1: if user requests, output link to / .zip / github repo with all intermediary conversion steps and indexes
  
- data pipeline/feature 5: user gives github link and asks to perform actions over repository 
 
Either surrealdb, or qdrant, marqo //
surrealdb is sqlite-posgesql embedded/clould db with bunch of features
qdrant is simple vector storage
marqo is knowledge base

## Additional comments:

There is very little utility that individual developer or non corporate backed group of individuals that can be provided with just OpenAI GPT4 (or  lesser model) can provide without adding functionality that OpenAI won't provide: 
1. Per prompt deep dive: crawling, fetching, indexing of the prompt related links, then grounded response - Open AI UI can provide only limited deepness level, proposed system can index vast knowledge that is private files of user/message/attachments history/specific to prompt 
2. Specific referenced knowledge lookup: "find on this Youtube channel", "find in this podcast" - OpenAI won't do that because silly lawyers  
3. User Filesystem / Cloud Storage Management and File Editing 
4. Virtual Machines, Shells, Credentials, Cloud Management, UI Control - tons of development on this area 
5. Comprehensive code / any file generation / delivery / execution / continuous fine tuning 

These things are mostly glue code - code for which APIs are known; classes of models that will be available ("text to text", "image and text to image", "text to video" etc) are known too; likely leaders in software for inference are already out there (local ai, olllama etc), so all that could be already development in expectation of arrival of better models/ hope to continuously improve current models under usage feedback collection
...
"I would ask such bot":
turn https://m.youtube.com/watch?v=giN2pbwpISs&t=612s (or any other podcast with books summaries, for example https://podcasts.apple.com/us/podcast/literature-and-history/id1083737218 ) into pdf presentation of mentioned quotes in original and translation + video of all quotes in context of page with voice over of podcast

old comment:
so, total future vision of project:
 - fastAPI Python DSPy optimized (re learning, pipeline in separate docker file, runs daily on history collected by dev instance) local llm/trained by human in conversation feedback / remote OpenAI call llm trainer server with conversation history recall, shell tool, scripting language repl tool
 - rust cli repl / stdin/out chatlog cat app that has chatbot written in gluon language with hot reloading that uses fastAPI Python DSPy for inference and code base knowledge grounded text generation
 - (much later) UnrealEngine, Swift, Bevy, WebGPU, Any, VisionSwift Game Engine integration / llm tool usage training "imagine game level"
 - (later) LaTeX, video formats generation with domain/filtered (imagined) dataset specific Loras / other tunings  (imagine paper, imagine movie, imagine legal paper in given jurisdiction)

how would you go about building that, trying to make sure that most of the code that can be written by llm (and assuming that all will given amount of tries/collecting feedback and retraining between attempts) will be written by llm if possible
(it's purpose of proposed system - to write itself with help of human feedback leveraging llm under training, and integrate maximum amount of apis possible eventually (and as result to be the best framework for responding on any prompt of any user, eventually))


## Useful ML/AI links:
PyTorch revolutionised neural networks, DSPy is here to do the same for LLMs 
https://www.linkedin.com/pulse/pytorch-revolutionised-neural-networks-dspy-here-do-same-mohamed-jama-ds93f?utm_source=share&utm_medium=member_android&utm_campaign=share_via

Podcast to rewatch: https://youtu.be/_ye26_8XPcs?si=L1hyFAENvrJwMZtc,
https://youtu.be/NoaDWKHdkHg?si=D9ApoucexVick9x6 (about DSPY, RAG, LLM)
https://www.youtube.com/watch?app=desktop&v=T-D1OfcDW1M (RAG)
__________________________________________________________________________________________

## TELEGRAM LIMITS DOC:
https://limits.tginfo.me/en