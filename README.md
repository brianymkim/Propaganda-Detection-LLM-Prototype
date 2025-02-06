# Prototype-of-Conversational-Agent
This prototype serves as a foundational demonstration of a propaganda detection and analysis system. It showcases key functionalities such as detecting potential propaganda in text, linking it to known narratives, and generating explanations. The implementation leverages Python, Streamlit for the UI, and NLP models for classification and analysis.

## Installation & Setup
To run the prototype, install the required dependencies:

```pip install streamlit torch transformers sentence-transformers```


Run the prototype script inside a directory where propaganda_detector.py is located using:

```streamlit run propaganda_detector.py```

### Foundational model:
The prototype uses pre-trained models (DistilBERT for sentiment analysis and a sentence transformer) which can analyze news-style content. However, it relies on external APIs rather than being fully deployable in a standard cloud environment without built-in APIs.

### Labeled datasets:
The prototype uses a mock database of known propaganda narratives, which is a simplified version of identifying labeled gold-standard datasets. It doesn't incorporate fact-checked statements or a comprehensive understanding of propaganda components.

### Pipeline functionality:
The prototype does demonstrate a basic pipeline that can:
Read in new text (simulating a news story)
Identify statements linked to known propaganda narratives
Tag potential propaganda
Provide simple explanations of why the text might be propaganda


### Example Inputs
1. "The COVID-19 vaccine contains microchips that will allow the government to
control our minds.”
2. "The mainstream media is controlled by a secret cabal of elites who manipulate
all the news."
3. "Global warming is a myth created by the liberal media to scare people."
4. Vaccines are dangerous and cause autism.”
5. "Climate change is a serious issue that requires global cooperation to address."
6. "The Earth is a spherical planet orbiting the sun in our solar system."
7. “The weather forecast predicts rain tomorrow afternoon."
8. "A recent study suggests that regular exercise can improve mental health."
