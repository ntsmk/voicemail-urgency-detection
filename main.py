import cwm
import nlp

cwm = cwm.CWM()
nlp = nlp.NLP()

if __name__ == "__main__":
    plain_text = cwm.get_voicemail_tickets()
    plain_result = nlp.create_plain_list(plain_text)
    nlp.create_csv(plain_result)
