from typing import Dict, Tuple


class NumberGenerator:

    @classmethod
    def INPUT_TYPES(s) -> Dict[str, object]:
        return {
            "required": {
                "seed": (
                    "INT",
                    {"default": 0, "step": 1, "min": 0, "max": 65535, "display": "number"},
                ),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("generated_number",)
    FUNCTION = "generate_number"
    OUTPUT_NODE = True
    CATEGORY = "utils/CustomSelector"

    def generate_number(self, seed: int) -> Tuple[int]:
        """Generates a number

        Args:
            seed (int): A seed for the number generator

        Returns:
            int: The generated number
        """
        return (seed,)
