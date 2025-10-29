from typing import Dict, Tuple


class TextSelector:
    """TextSelector From Line Number"""

    @classmethod
    def INPUT_TYPES(s) -> Dict[str, object]:
        return {
            "required": {
                "text_list": (
                    "STRING",
                    {
                        "multiline": True,
                    },
                ),
                "seed": (
                    "INT",
                    {
                        "default": 0,
                        "step": 1,
                        "display": "line_number",
                    },
                ),
            },
        }

    RETURN_TYPES = (
        "STRING",
        "INT",
    )
    RETURN_NAMES = (
        "selected_text",
        "selected_line_number",
    )
    FUNCTION = "select_text"
    OUTPUT_NODE = True
    CATEGORY = "utils/CustomSelector"

    def select_text(self, text_list: str, seed: int) -> Tuple[str, int]:
        """Selects a text from a list of texts

        Args:
            text_list(str): A list of texts
            seed(int): A seed for the random number generator

        Returns:
            str: The selected text
            int: The line number of the selected text
        """
        lines = text_list.splitlines()
        num_lines = len(lines)
        if num_lines == 0:
            return ("", 0)

        selected_line_number = seed % num_lines
        selected_text = lines[selected_line_number]
        return (selected_text, selected_line_number)


class TextMapSelector:
    """Text Selector Node"""

    @classmethod
    def INPUT_TYPES(s) -> Dict[str, object]:
        return {
            "required": {
                "text_map": (
                    "STRING",
                    {
                        "multiline": True,
                        "placeholder": "key1: value1\nkey2: value2\n...",
                    },
                ),
                "key": (
                    "STRING",
                    {
                        "default": "",
                        "multiline": False,
                        "placeholder": "key1",
                    },
                ),
            },
        }

    RETURN_TYPES = (
        "STRING",
        "STRING",
        "INT",
    )
    RETURN_NAMES = (
        "selected_key",
        "selected_value",
        "selected_line_number",
    )
    FUNCTION = "select_text"
    OUTPUT_NODE = True
    CATEGORY = "utils/CustomSelector"

    def select_text(self, text_map: str, key: str) -> Tuple[str, str, int]:
        lines = text_map.splitlines()
        map_dict = {}
        for idx, line in enumerate(lines):
            split_line = line.split(":", maxsplit=1)
            tmp_key = split_line[0].strip()
            tmp_value = split_line[1].strip() if len(split_line) > 1 else ""
            map_dict[tmp_key] = {
                "key": tmp_key,
                "value": tmp_value,
                "line_number": idx,
            }

        selected_map = map_dict.get(key, {"key": "", "value": "", "line_number": 0})
        selected_key = selected_map["key"]
        selected_value = selected_map["value"]
        selected_line_number = selected_map["line_number"]
        return (selected_key, selected_value, selected_line_number)
