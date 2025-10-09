from typing import Dict, Tuple


class ToInt:

    @classmethod
    def INPUT_TYPES(s) -> Dict[str, object]:
        return {
            "required": {
                "string": (
                    "STRING",
                    {
                        "default": "",
                        "forceInput": True,
                    },
                ),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("number",)
    FUNCTION = "to_int"
    OUTPUT_NODE = True
    CATEGORY = "utils/CustomSelector"

    def to_int(self, string: str) -> Tuple[str]:
        """Converts a string to a number

        Args:
            string (str): The string to convert

        Returns:
            int: The converted number

        """
        return (int(string),)
