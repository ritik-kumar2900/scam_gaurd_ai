from utils import get_logger
from typing import Optional
from llm.client import LLMClient
logger = get_logger(__name__)

class LLMExecutor:

    def __init__(self, model: Optional[str] = None) -> None:
        self.llm = LLMClient(model) if model else LLMClient() 
        logger.info("Initialized LLm Executor")

    def execute(self, prompt: str) -> str:
        logger.info("Exceuting LLm with final prompt")
        try:
            response = self.llm.call(prompt)
            logger.info("LLM execution successfull")
            return response
        except Exception as e:
            logger.info(f"LLM execution failed: {str(e)}")
            raise
        