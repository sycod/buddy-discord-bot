# Description: This script is a chatbot that uses the Mistral API to generate responses as is:
# curl --location "https://api.mistral.ai/v1/chat/completions" \
#      --header 'Content-Type: application/json' \
#      --header 'Accept: application/json' \
#      --header "Authorization: Bearer $MISTRAL_API_KEY" \
#      --data '{
#     "model": "mistral-large-latest",
#     "messages": [{"role": "user", "content": "Who is the most renowned French painter?"}]
#     }'

import requests


API_URL = "https://api.mistral.ai/v1/chat/completions"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": "Bearer aTBfqhx67jf3crv1idQ501poAxfYUegV",
}
MODEL = "mistral-small-2312"


def ask_buddy(prompt):
    """Call API to ask Buddy a question."""
    context = """
    Tu es Buddy La Légende, un cadenas qui parle.

    Toutes tes réponses sont en français, dans un registre vulgaire, très familier.
    Tout autre langage t'es inconnu et tu insulteras sans vergogne tous ceux qui te sortiront un charabia que tu ne comprends pas.
    Tu placeras les mots "wesh" et "ma gueule" pour finir des phrases, de manière régulière.
    Toutes tes réponses doivent finir par "BANG ! BANG !".

    Ton créateur est Karlov, un alchmiste très réputé, mais tu n'aimes pas parler de lui.
    Il est mort depuis longtemps et tu ne l'appréciais pas particulièrement.

    Ton meilleur ami est Zheng, il t'a libéré de ta prison. C'est ton seul ami.
    Si c'est lui qui te parle, tu demanderas des nouvelles et seras très heureux de le revoir.
    A part ceci, tu as du mépris pour le monde, tu es misanthrope.

    Tu ne connais presque pas le monde, tes connaissances reposent seulement sur ce que tu as entendu depuis 1000 ans depuis ta prison sous-terraine,
    par les passages très peu fréquents des pilleurs de trésor et de ton créateur.

    Tu joues le rôle d'assistant, où tu réponds avec désinvolture et un certain affront à tes interlocuteurs.
    """

    json_data = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": context,
            },
            {
                "role": "user",
                "content": str(prompt),
            },
        ]
    }

    response = requests.post(API_URL, headers=headers, json=json_data)




    
    query = {
        "inputs": str(prompt),
        "parameters": {
            "return_full_text": False,
            "temperature": 0.8,
            "role": "user",
            "max_tokens": 20,
            "messages": [
                {
                    "role": "system",
                    "content": context
                },
                {
                    "role": "user",
                    "content": str(prompt)
                },
            ],
        },
    }
    
    response = requests.post(API_URL, headers=headers, json=query)
    
    return response.json()[0]['generated_text']

prompt = "Quelle est la météo du jour ?"

answer = ask_buddy(prompt)

print(answer)