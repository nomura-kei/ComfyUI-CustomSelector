from typing import Dict, Tuple


class ToString:

    @classmethod
    def INPUT_TYPES(s) -> Dict[str, object]:
        return {
            "required": {
                "number": (
                    "INT",
                    {
                        "default": 0,
                        "forceInput": True,
                    },
                ),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "to_string"
    OUTPUT_NODE = True
    CATEGORY = "utils/CustomSelector"

    def to_string(self, number: int) -> Tuple[int]:
        """Converts a number to a string

        Args:
            number (int): The number to convert

        Returns:
            str: The converted string
        """
        return (str(number),)
