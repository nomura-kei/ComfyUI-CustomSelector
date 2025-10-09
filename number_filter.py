from typing import Dict, Tuple


class NumberFilter:

    @classmethod
    def INPUT_TYPES(s) -> Dict[str, object]:
        return {
            "required": {
                "number": (
                    "INT",
                    {"default": 0, "step": 1, "display": "number", "forceInput": True},
                ),
                "min": ("INT", {"default": 0, "step": 1, "min": 0, "max": 65535, "display": "min"}),
                "max": ("INT", {"default": 0, "step": 1, "min": 0, "max": 65535, "display": "min"}),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("filtered_number",)
    FUNCTION = "filter_number"
    OUTPUT_NODE = True
    CATEGORY = "utils/CustomSelector"

    def filter_number(self, number: int, min: int, max: int) -> Tuple[int]:
        """
        Filters a number to be within a given range

        Args:
            number (int): The number to be filtered
            min (int): The minimum value of the range
            max (int): The maximum value of the range

        Returns:
            Tuple[int]: The filtered number
        """
        filtered_number = (number - min) % (max - min + 1) + min
        return (filtered_number,)
