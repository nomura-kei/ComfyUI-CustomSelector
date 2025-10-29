from typing import Dict, Tuple


class ConcatenateEx:

    @classmethod
    def INPUT_TYPES(s) -> Dict[str, object]:
        return {
            "required": {
                "delimiter": ("STRING", { "default": ",", }),
                "string_1": ("STRING", { "default": "", "forceInput": True, },),
                "string_2": ("STRING", { "default": "", "forceInput": True, },),
                "string_3": ("STRING", { "default": "", "forceInput": True, },),
                "string_4": ("STRING", { "default": "", "forceInput": True, },),
                "string_5": ("STRING", { "default": "", "forceInput": True, },),
                "string_6": ("STRING", { "default": "", "forceInput": True, },),
                "string_7": ("STRING", { "default": "", "forceInput": True, },),
                "string_8": ("STRING", { "default": "", "forceInput": True, },),
                "string_9": ("STRING", { "default": "", "forceInput": True, },),
                "string_10": ("STRING", { "default": "", "forceInput": True, },),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "concatenate"
    OUTPUT_NODE = True
    CATEGORY = "utils/CustomSelector"

    def concatenate(self,
                    delimiter: str,
                    string_1: str,
                    string_2: str,
                    string_3: str,
                    string_4: str,  
                    string_5: str,
                    string_6: str,
                    string_7: str,
                    string_8: str,
                    string_9: str,
                    string_10: str
                    ) -> Tuple[str]:
        result = delimiter.join([
            string_1,
            string_2,
            string_3,
            string_4,
            string_5,
            string_6,
            string_7,
            string_8,
            string_9,
            string_10,
            ])
        return (result,)
