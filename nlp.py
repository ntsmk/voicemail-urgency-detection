from google.cloud import language_v1
import csv

# Tried most of API methods now but not helpful to detect urgency. Need to create a new model
class NLP:
    def test_sentiment(self, texts):
        """
        take voicemail info as input and analyze the urgency using analyzeSentiment method
        :param texts: dict contains voicemail text and id
        :return: results list
        """
        result_list = [["ID", "Urgency", "Sentiment score", "Text"]]
        result = ""
        client = language_v1.LanguageServiceClient()
        for id,text in texts.items():
            if len(text.split()) > 20:  # eliminate short message like null
                document  = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
                response = client.analyze_sentiment(request={"document": document})
                sentiment_score = response.document_sentiment.score
                rounded_score = round(sentiment_score, 2)
                if sentiment_score <= -0.5:
                    result = [id, "High", rounded_score, text]
                    result_list.append(result)
                else:
                    result = [id, "Low", rounded_score, text]
                    result_list.append(result)

        return result_list

    def test_annotate(self, texts):
        """
        take voicemail info as input and analyze the urgency using annotateText method
        :param texts: dict contains voicemail text and id
        :return: results list
        """
        result_list = [["ID", "Sentiment score", "Entities", "Syntax", "Text"]]
        result = ""
        client = language_v1.LanguageServiceClient()
        for id, text in texts.items():
            if len(text.split()) > 20: # eliminate short message like null
                document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
                features = {
                    "extract_syntax": True,
                    "extract_entities": True,
                    "extract_document_sentiment": True
                }
                response = client.annotate_text(request={"document": document, "features": features})
                sentiment_score = round(response.document_sentiment.score,2)
                entities = response.entities
                entity_list = []
                for entity in entities:
                    entity_list.append(f"{entity.name}({language_v1.Entity.Type(entity.type_).name})")
                syntaxes = response.tokens
                syntax_list = []
                for syntax in syntaxes:
                    syntax_list.append(f"{syntax.text.content}: {language_v1.PartOfSpeech.Tag(syntax.part_of_speech.tag).name}")
                result = [id, sentiment_score, entity_list, syntax_list, text]
                result_list.append(result)
        return result_list

    def test_classify(self, texts):
        """
        take voicemail info as input and analyze the urgency using classifyText method
        :param texts: dict contains voicemail text and id
        :return: results list
        """
        result_list = [["ID", "Category", "Text"]]
        result = ""
        client = language_v1.LanguageServiceClient()
        for id, text in texts.items():
            if len(text.split()) > 20:  # eliminate short message like null
                document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
                response = client.classify_text(request={"document": document})
                categories = response.categories
                category_list = []
                for category in categories:
                    category_list.append(category.name)
                result = [id, category_list, text]
                result_list.append(result)
        return result_list


    def create_plain_list(self, texts):
        """
        take voicemail info as input and return plain list
        :param texts: dict contains voicemail text and id
        :return: results list
        """
        result_list = [["id", "text", "label"]]
        result = ""
        for id, text in texts.items():
            if len(text.split()) > 20:  # eliminate short message like null
                clean_text = text.replace("\n", " ")
                result = [id, clean_text]
                result_list.append(result)
        return result_list

    def create_csv(self, result_list):
        """
        take result list as input and export it to csv file
        :param result_list: result list after analyzing
        :return: csv file
        """
        data = result_list

        with open('output2.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows(data)

        print("CSV file created successfully!")