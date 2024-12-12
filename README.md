# MistralChatBotUpdated

![Work in Progress](https://img.shields.io/badge/status-in%20progress-orange)

**MistralChatBotUpdated** is a ChatBot that utilizes Streamlit as the graphical user interface (GUI) and integrates with the [Mistral API](https://docs.mistral.ai/api/) as its large language model (LLM). While there are several examples available, many rely on outdated versions of the Mistralai library (e.g., version 0.4.2). This project updates the libraries and provides an up-to-date implementation.

### Related Examples

- [Build an AI Chatbot with MistralAI + Streamlit](https://medium.com/bitgrit-data-science-publication/build-an-ai-chatbot-with-mistralai-streamlit-4f58d7fe4a22)
- [How to Build AI ChatBots with Mistral and Llama2](https://www.anaconda.com/blog/how-to-build-ai-chatbots-with-mistral-and-llama2)



## What Is Mistral AI?

[Mistral AI](https://mistral.ai/fr/) is a French company focused on developing open-source models for developers and small businesses. You can think of Mistral AI as an open-source alternative to [OpenAI](https://openai.com/).



## Usage
![streamlit-minstral_chatbot-2024-12-12-17-12-35](https://github.com/user-attachments/assets/15d87b4b-0cf9-476f-a53f-ca7c9197d3aa)



### Requirements

To use the application, follow these steps:

1. Obtain your Mistral API key by visiting [Mistral API Documentation](https://docs.mistral.ai/api/).
2. Save the API key in your `.env` file.
3. Fork this repository.
4. Navigate to the `src` folder.
5. Install dependencies by running:
   ```bash
   pip install -r packages.txt
   ```

Once all dependencies are installed, you can start the Streamlit server by running:
```bash
streamlit run mistral_chatbot.py
```



## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss your proposed modifications.

Make sure to update any tests as needed to reflect your changes.



## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

