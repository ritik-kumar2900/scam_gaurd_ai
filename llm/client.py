from utils import get_logger
from google import genai
import time
from config import GEMINI_API_KEY, DEFAULT_MODEL, MAX_RETRIES, RETRY_DELAY

logger = get_logger(__name__)

class LLMClient:
    def __init__(self, model_name = DEFAULT_MODEL, max_retry = MAX_RETRIES, retry_delay = RETRY_DELAY):
        self.model_name = model_name
        self.max_retry = max_retry
        self.retry_delay = retry_delay
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def call(self, prompt: str, **kwargs) -> str:
        for attempt in range(self.max_retry):
            try:
                response = self.client.models.generate_content(
                    model=self.model_name,
                    contents=prompt,
                    **kwargs
                )
                if response and response.text:
                    return response.text.strip()
                else:
                    raise Exception("Empty response received")
            except Exception as e:
                if attempt == self.max_retry:
                    raise Exception(f"API call failed after {attempt +1} attempts: {str(e)}")
                time.sleep(self.retry_delay * (2**attempt))






