from typing import Dict,Any
from utils import get_logger, extract_json_from_text

logger = get_logger(__name__)


class OutputParser:
    def parse_llm_output(self, llm_output:str) -> Dict[str, Any]:

        logger.info("Parsing LLM output.")

        parsed_output = extract_json_from_text(llm_output)

        if parsed_output:
            logger.info("Successfully parsed LLM output to JSON")
            return parsed_output
        else:
            logger.warning("No JSON found in LLM output")
            fallback_results = {
                "label": "Uncertain", 
                "reasoning": "Could not parse AI response",
                "intent": "Unknown",
                "risk_factors": ["Parsing Error"]
            }
            return fallback_results

