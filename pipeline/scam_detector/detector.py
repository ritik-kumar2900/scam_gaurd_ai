from typing import List, Dict, Any
from .executor import LLMExecutor
from .parser import OutputParser
from .builder import build_prompt
from utils import get_logger

logger = get_logger(__name__)


class ScamDetector: 
    """
    Main class for detection logic
    """
    def __init__(self, strategy: str ="react") -> None:
        self.parser = OutputParser()
        self.executor = LLMExecutor()
        self.strategy = strategy
        logger.info(f"Initialized Scam Detector with strategy -> {self.strategy}")

    def detect(self, message: str) -> Dict[str,Any]:
        """
        Runs the main scam detection pipeline
        """
        logger.info(f"Started detection for message -> {message}")
        try:
            prompt = build_prompt(message, self.strategy)
            raw_response = self.executor.execute(prompt)
            parsed_result = self.parser.parse_llm_output(raw_response)
            logger.info("Detection successful!!")
            return parsed_result
        except Exception as e:
            logger.error(f"Detection pipeline failed: {e}")


        
