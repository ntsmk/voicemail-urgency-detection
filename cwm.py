from pyconnectwise import ConnectWiseManageAPIClient
import os
from dotenv import load_dotenv

PAGE_SIZE = 1000

class CWM:
    def __init__(self):
        load_dotenv()
        company_id = os.getenv("company_id")
        manage_url = os.getenv("manage_url")
        client_id = os.getenv("client_id")
        public_key = os.getenv("public_key")
        private_key = os.getenv("private_key")
        self.manage_api_client = ConnectWiseManageAPIClient(company_id, manage_url, client_id, public_key, private_key)

    def get_voicemail_tickets(self):
        """
        get voicemail text and ticket id
        :return: dict contains get voicemail text and ticket id
        """
        result_dic = {}
        voicemail_tickets = self.manage_api_client.service.tickets.get(params={
            'conditions': 'summary contains "Voicemail for" ',
            'orderBy': 'id desc',
            'pageSize': PAGE_SIZE,
        })

        for ticket in voicemail_tickets:
            notes = self.manage_api_client.service.tickets.id(ticket.id).notes.get()
            ticket_id = notes[0].ticket_id
            initial_note = notes[0].text.split("--- Google transcription result ---", 1)[-1].strip()
            if initial_note not in ["(Google was unable to recognize any speech in audio data.)", "null", "null\nnull"]:
                result_dic.update({ticket_id:initial_note.lower()})
        return result_dic
