from flask import Flask, request, jsonify
from flasgger import Swagger
from src.llm_client import LLMClient
from src.file_manager import FileManager
from src.compliance_checker import ComplianceChecker

# Initialize Flask app
app = Flask(__name__)
swagger = Swagger(app)

# Configuration variables
LLM_MODEL = 'lmstudio-ai/gemma-2b-it-GGUF'
BASE_URL = "https://localhost:1234/v1"
API_KEY = "lm-studio"

# Initialize LLM client and File Manager
llm_client = LLMClient(base_url=BASE_URL, api_key=API_KEY, model=LLM_MODEL)
file_manager = FileManager()
compliance_checker = ComplianceChecker(llm_client, file_manager)

@app.route('/check_compliance', methods=['POST'])
def check_webpage_compliance():
    """
    Check webpage compliance against a policy
    ---
    tags:
      - Compliance
    parameters:
      - name: body
        in: body
        required: true
        description: JSON body containing URLs for the policy and the webpage to check
        schema:
          type: object
          properties:
            policy_url:
              type: string
              example: "https://stripe.com/docs/treasury/marketing-treasury"
            webpage_url:
              type: string
              example: "https://mercury.com/"
    responses:
      200:
        description: Compliance check results
        schema:
          type: object
          properties:
            policy_url:
              type: string
              description: URL of the compliance policy
            webpage_url:
              type: string
              description: URL of the webpage checked for compliance
            findings:
              type: string
              description: Non-compliant sections found in the webpage
    """
    data = request.json
    policy_url = data['policy_url']
    webpage_url = data['webpage_url']

    # Check webpage compliance
    result_data = compliance_checker.check_webpage_compliance(policy_url, webpage_url)

    return jsonify(result_data)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
