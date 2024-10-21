from openai import OpenAI

class LLMClient:
    def __init__(self, base_url, api_key, model):
        self.client = OpenAI(base_url=base_url, api_key=api_key)
        self.model = model

    def check_compliance(self, policy, content):
        prompt_messages = [
            {"role": "system", "content": "Check the following content for compliance against this policy:"},
            {"role": "user", "content": f"Policy:\n{policy}"},
            {"role": "user", "content": f"Content:\n{content}"},
            {"role": "user", "content": "Does the content comply with the policy? Also mention which area in policy it complies with."}
        ]
        response = self.client.chat.completions.create(
            model=self.model,
            messages=prompt_messages,
            temperature=0.7
        )
        return response.choices[0].message.content
