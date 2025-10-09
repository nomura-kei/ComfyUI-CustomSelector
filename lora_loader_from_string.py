from nodes import LoraLoader


class LoraLoaderFromString(LoraLoader):
    """LoRA の名称を STRING として受け取れるようにした LoRA Loader"""

    def __init__(self):

        self.loaded_lora = None

    @classmethod
    def INPUT_TYPES(cls):
        # INPUT_TYPES の `lora_name` を STRING に変更
        input_types = super().INPUT_TYPES()
        input_types["required"]["lora_name"] = ("STRING", {"tooltip": "The name of the LoRA."})
        return input_types

    RETURN_TYPES = ("MODEL", "CLIP")
    OUTPUT_TOOLTIPS = ("The modified diffusion model.", "The modified CLIP model.")
    FUNCTION = "load_lora"

    CATEGORY = "utils/CustomSelector"
    DESCRIPTION = (
        "LoRAs are used to modify diffusion and CLIP models,"
        "altering the way in which latents are denoised such as applying styles."
        "Multiple LoRA nodes can be linked together."
    )
