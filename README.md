### Equity Research Tool
The Equity Research Tool is designed to assist users in conducting thorough research and analysis on equity-related topics by answering questions based on web links provided by the user. It focuses on delivering detailed insights, data interpretation, and market trends related to the equity provided through external web links. By utilizing this tool, users can:
  * Analyze stock performance, financial reports, or market news.
  * Gain insights on specific companies, sectors, or industries.
  * Answer equity-related queries such as valuation metrics, price trends, and investment opportunities.

Tools used during the project are- Python, Langchain, StramLit APP, OPENAI API
* Python Environment Setup:
The first step was to create a Python virtual environment for the project. A requirements.txt file was generated, listing all the necessary Python libraries required for the project.

* Webpage Development using Streamlit:
A simple and interactive webpage was created using Streamlit, a Python framework for building data-driven web applications. The webpage allows users to input web URLs related to equity research. These URLs are fed into the backend for further processing.

* URL Processing and Data Extraction:
In the backend, the input URLs provided by the user are processed using the UnstructuredURLLoader function. Once the text is extracted, it is split into manageable tokens to ensure efficient processing.

* Embedding Creation with OpenAI and FAISS:
The tokenized text is then embedded using OpenAI’s embeddings model. This step converts the raw text into vector representations. The resulting vector embeddings are stored in a vector database using FAISS (Facebook AI Similarity Search).

* Storing Embeddings in a Pickle File:
To optimize performance, the embeddings are saved to a pickle file. Pickle is a Python module used for serializing and de-serializing Python objects. The pickle file serves as a cached database of the processed embeddings.

* Querying and Answering Questions:
When a user asks a question through the webpage, the system loads the pickle file containing the embeddings. The query is then matched against these embeddings to find the most relevant sections of the text. Using ChatGPT, the retrieved content is processed to generate a coherent and detailed response.
Finally, the result is displayed on the webpage, providing the user with an accurate and well-formed answer.
