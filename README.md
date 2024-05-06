# Government-Document-Chatbot(C4GT)
A bot capable of answering user questions based on RAG framework using government data extracted from PDFs.


Welcome to the Government Document Chatbot repository! This project aims to build a chatbot that can extract information from government documents in English and Hindi, allowing users to query and retrieve relevant data. The chatbot is designed to support multi-language queries and integrates natural language understanding (NLU) techniques to understand user requests.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
The Government Document Chatbot provides a streamlined approach to access government data from sources like [upvidhai.gov.in](https://upvidhai.gov.in/Act.aspx) and [shasanadesh.up.gov.in](https://shasanadesh.up.gov.in/). The chatbot can extract text from PDF files, including those with text layers and those requiring Optical Character Recognition (OCR), and supports natural language queries to retrieve relevant information.

## Features
- **Data Collection and Integration**: Collects and integrates government data from specified sources.
- **Language Processing Capability**: Extracts English and Hindi text from PDFs, supporting OCR for scanned documents.
- **Natural Language Understanding (NLU)**: Parses user queries and retrieves relevant content.
- **Content Structuring and Storage**: Structures extracted text for efficient storage and retrieval.
- **Multi-Language Support**: Supports multiple languages for user queries and content retrieval.
- **LLM Integration and Training**: Integrates a Large Language Model (LLM) for generating cohesive answers.

## Technology Stack
- **Python**: The primary programming language for this project.
- **Requests**: For HTTP requests and web scraping.
- **BeautifulSoup**: For HTML parsing and extracting links.
- **PyPDF2**: For extracting text from PDFs.
- **pytesseract**: For Optical Character Recognition (OCR).
- **SQLite**: For database storage and content management.
- **Google Translate API**: For translation and multi-language support.
- **Transformers**: For integrating a Large Language Model (LLM).

## Setup and Installation
To set up the project on your local machine, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/itsharisudhan/Government-Document-Chatbot.git
   cd Government-Document-Chatbot
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   .\venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Tesseract OCR**
   - [Download and install Tesseract](https://github.com/tesseract-ocr/tesseract) if not already installed.
   - Ensure it's in your system's PATH or specify the Tesseract executable path in your code.

## Usage
After setting up the project, you can run the chatbot and interact with it to retrieve information from government documents:

1. **Start the Chatbot**
   ```bash
   python chatbot.py
   ```

2. **Query the Chatbot**
   - You can ask questions related to government documents, such as "What is the content of this act?" or "Give me information about this document."
   - The chatbot will respond with relevant information based on its knowledge base and processing capabilities.

## Contributing
We welcome contributions to improve the Government Document Chatbot. If you'd like to contribute, please follow these steps:

1. Fork the repository and create a new branch for your changes.
2. Make your changes and test them thoroughly.
3. Submit a pull request with a clear description of your changes.

For more detailed guidelines, see our [Contributing Guidelines](CONTRIBUTING.md).

## License
This project is licensed under the [MIT License](LICENSE). See the LICENSE file for details.

---

Thank you for using the Government Document Chatbot! If you have any questions or need assistance, please open an issue in this repository.
```

This README file includes a project overview, features, technology stack, setup and installation instructions, usage guidelines, contribution process, and licensing information. It is designed to be informative and user-friendly to help people understand and use the chatbot effectively.
