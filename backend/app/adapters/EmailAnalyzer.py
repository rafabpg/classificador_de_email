import httpx
from app.domain.interfaces.IEmailAnalyzer import IEmailAnalyzer
from app.core.config import settings
from app.api.decorators.exception import ServiceError

class EmailAnalyzer(IEmailAnalyzer):
    def __init__(self):
        """
        Initializes an instance of the EmailAnalyzer class.

        It sets the API URL classifier, the API URL suggestion, the API token and the timeout for the HTTPX client.
        """
        self.api_url_classifier = settings.API_URL_CLASSIFIER
        self.api_url_suggestion = settings.API_URL_SUGGESTION
        self.api_token = settings.API_TOKEN
        self.timeout = httpx.Timeout(30.0 )
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }

    async def analyse_email(self, email_content: str) -> tuple:
        try:
            category = await self._classify_email_content(email_content)
            details = await self._sugestion_of_response(category,email_content)
            return category, details

        except Exception as e:
            raise ServiceError(f"Erro ao processar email")
            
    async def _post_api(self,payload:dict,url:str) -> dict:
        """
        Makes a POST request to the given url with the given payload and 
        returns the JSON response.

        Args:
            payload (dict): The payload to send in the request body
            url (str): The URL to send the request to

        Returns:
            dict: The JSON response from the server

        Raises:
            ServiceError: If any error occurs while making the request
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(url, headers=self.headers, json=payload)
            response.raise_for_status()
            result = response.json()
            return result
        except Exception as e:
            raise ServiceError(f"Erro ao processar email")
        
    async def _classify_email_content(self, email_content: str) -> str:
        """
        Makes a POST request to the AI model to classify the given email content
        into one of the two categories: "Produtivo" or "Improdutivo".

        The request is made to the `api_url_classifier` endpoint, with the
        `candidate_labels` parameter set to `["Produtivo", "Improdutivo"]`.

        The response is expected to be a JSON object with a single key-value pair,
        where the key is `labels` and the value is a list with a single element,
        which is the classification of the email content.

        The classification is then returned as a string.

        Args:
            email_content (str): The content of the email to classify

        Returns:
            str: The classification of the email content
        """
        classification = await self._post_api({
            "inputs": email_content,
            "parameters": {
                "candidate_labels": ["Produtivo", "Improdutivo"]
            }
        }, self.api_url_classifier)
        return classification.get("labels")[0]

    async def _sugestion_of_response(self,category:str,email_content:str)-> str:

        """
        Makes a POST request to the AI model to generate a suggested response 
        given the category and content of the email.

        The request is made to the `api_url_suggestion` endpoint, with the 
        `gemma-2-2b-it` model and the following parameters:

        - `model`: `google/gemma-2-2b-it`
        - `messages`: A list of two messages, one with the system prompt and 
          one with the user prompt.
        - `max_tokens`: 200
        - `temperature`: 0.3
        - `top_p`: 0.8

        The response is expected to be a JSON object with a single key-value pair,
        where the key is `choices` and the value is a list with a single element,
        which is an object with a `message` key containing the suggested response.

        The suggested response is then returned as a string.

        Args:
            category (str): The category of the email
            email_content (str): The content of the email

        Returns:
            str: The suggested response

        Raises:
            ServiceError: If any error occurs while making the request
        """
        system_prompt = """
            Você é um assistente de Customer Success para uma grande empresa do setor financeiro.
            Sua função é gerar respostas automáticas a emails de clientes, focando em profissionalismo, clareza e empatia.

            DIRETRIZES GERAIS:
            - **Concisão**: Respostas curtas, idealmente entre 1 e 3 frases. Vá direto ao ponto.
            - **Linguagem**: Utilize português brasileiro formal, cordial e acolhedor.
            - **Foco**: Priorize a resolução do problema do cliente ou a indicação clara do próximo passo.
            - **Proatividade e Educação**: Sempre ofereça ajuda ou agradeça, conforme a situação.
            - **Veracidade**: Nunca invente informações. Se os dados forem insuficientes, seja genérico e direcione para canais de suporte.
            - **Evite Redundâncias**: Seja eficiente na comunicação, evitando frases desnecessárias.
            - **Adesão às Instruções Específicas**: É CRUCIAL seguir as 'INSTRUÇÕES ESPECÍFICAS POR CATEGORIA' fornecidas no prompt do usuário, pois elas definem o tom e o detalhamento adequados para cada tipo de email.

            """

        user_prompt = f"""
             Analise o email do cliente abaixo e gere uma resposta apropriada, seguindo as diretrizes gerais e as instruções específicas para a categoria identificada.

            CATEGORIA DO EMAIL: {category}

            CONTEÚDO DO E-MAIL:
            ```
            {email_content[:1500]}
            ```
            INSTRUÇÕES ESPECÍFICAS POR CATEGORIA:
            {self._get_category_instructions(category)}

            Por favor, forneça apenas a resposta sugerida, sem introduções ou comentários adicionais.
        """

        payload = {
            "model": "google/gemma-2-2b-it",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "max_tokens": 200, 
            "temperature": 0.3,
            "top_p": 0.8
        }
    
        suggestion = await self._post_api(payload, self.api_url_suggestion)
        content = suggestion['choices'][0]['message']['content']
        return content

    def _get_category_instructions(self, category: str) -> str:
        """
        Returns a string with instructions for the AI to generate a response based on the category of the email.

        The instructions are based on the category of the email and provide guidelines
        for the AI to generate a response that is appropriate, concise and professional.

        Args:
            category (str): The category of the email

        Returns:
            str: The instructions for the AI
        """
        instructions = {
            "Produtivo": """
            - O cliente necessita de uma ação ou informação específica.
            - **Objetivo**: Fornecer uma solução direta, confirmar um status ou indicar o próximo passo claro.
            - **Tom**: Proativo, seguro e eficiente. Demonstre compromisso com a resolução.
            - **Ação**: Se necessário, solicite informações adicionais de forma precisa e justificada.
            - **Exemplo**: "Prezado(a) [Nome do Cliente], recebemos sua solicitação e estamos analisando. Em breve entraremos em contato com a solução." ou "Para prosseguir com sua demanda, precisamos que nos envie [informação necessária]."
            """,
            
            "Improdutivo": """
            - O email não requer uma ação imediata ou é de cunho informal.
            - **Objetivo**: Agradecer cordialmente e encerrar a comunicação de forma educada, sem prolongar o diálogo.
            - **Tom**: Simpático, breve e gentil.
            - **Ação**: Evite iniciar novas conversas ou solicitar informações desnecessárias.
            - **Exemplo**: "Agradecemos o seu contato e a mensagem. Tenha um excelente dia!" ou "Obrigado(a) pela sua consideração. Estamos à disposição para futuras necessidades."
            """
        }
        return instructions.get(category, "- Responda de forma profissional e educada, mantendo a concisão e o foco na cordialidade.")
   