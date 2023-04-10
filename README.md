
#Swahili Sentiment Analyzer using Support Vector Machines (SVM)

This project implements a Swahili sentiment analyzer using Support Vector Machines (SVM) for binary classification. The model was trained on a Swahili dataset containing tweets labeled as positive or negative.

##Data Collection and Preprocessing

The dataset was collected from Twitter using the Tweepy API and was manually labeled as positive or negative. The data preprocessing included removing URLs, mentions, hashtags, and non-alphanumeric characters. The preprocessed tweets were tokenized, lemmatized, and stopwords were removed.

##Model Training

The preprocessed tweets were converted into a matrix of token counts using the CountVectorizer function from scikit-learn. The matrix was then normalized using the TfidfTransformer function. The resulting matrix was used to train an SVM model for binary classification.

The SVM model achieved an accuracy of 85% on the test set.

##User Interface

The Swahili Sentiment Analyzer was deployed using Gradio, an open-source web interface for machine learning models. The interface allows users to input a text in Swahili and get the predicted sentiment of the text.

##Instructions to Run the Code

Clone the repository using the command:
git clone https://github.com/yourusername/Swahili-Sentiment-Analyzer.git

Install the required packages using the command:
pip install -r requirements.txt

Run the notebook Swahili Sentiment Analyzer.ipynb and follow the instructions to train the SVM model and launch the Gradio interface.

##Conclusion
This project implements a Swahili sentiment analyzer using Support Vector Machines (SVM) for binary classification. The model achieved an accuracy of 85% on the test set. The Swahili Sentiment Analyzer was deployed using Gradio, an open-source web interface for machine learning models.
