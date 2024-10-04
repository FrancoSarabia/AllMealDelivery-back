import os

class JSONElement(object):
    def get_json_payload():
        
        payload = {
            "channel": os.environ.get("CHANNEL_ID"),
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Hola, este es el menu del dia de hoy con los platos destacados. Incluye plato de entrada, plato principal y postre, !!Que lo disfrutes!!\n\n"
                    }
                },
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": "MENU.NAME",
                        "emoji": True
                    }
                },
            ]
        }
        return payload