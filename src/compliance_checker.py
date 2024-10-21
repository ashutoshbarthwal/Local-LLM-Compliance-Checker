import requests
from bs4 import BeautifulSoup

class ComplianceChecker:
    def __init__(self, llm_client, file_manager):
        self.llm_client = llm_client
        self.file_manager = file_manager

    def get_webpage_content(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        return text.strip()

    def check_webpage_compliance(self, policy_url, webpage_url):
        # Fetch content from policy and webpage
        policy_content = self.get_webpage_content(policy_url)
        webpage_content = self.get_webpage_content(webpage_url)

        # Save policy and website content to files
        policy_filename = f"{policy_url.split('/')[-1]}.txt"
        webpage_filename = f"{webpage_url.split('/')[-2]}.txt"
        self.file_manager.save_to_file(self.file_manager.policy_dir, policy_filename, policy_content)
        self.file_manager.save_to_file(self.file_manager.website_dir, webpage_filename, webpage_content)

        # Perform compliance check using LLM
        findings = self.llm_client.check_compliance(policy_content, webpage_content)

        # Save the findings (results) to a JSON file
        result_filename = f"{webpage_url.split('/')[-2]}.json"
        result_data = {
            'policy_url': policy_url,
            'webpage_url': webpage_url,
            'findings': findings
        }
        self.file_manager.save_result(result_filename, result_data)

        return result_data
