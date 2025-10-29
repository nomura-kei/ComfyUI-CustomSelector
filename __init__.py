"""
・-―+ Text Selector +―-・
https://github.com/nomura-kei/ComfyUI-TextSelector/
"""

from .concatenate_ex import ConcatenateEx
from .lora_loader_from_string import LoraLoaderFromString
from .number_filter import NumberFilter
from .number_generator import NumberGenerator
from .text_selector import TextMapSelector, TextSelector
from .to_int import ToInt
from .to_string import ToString

from .checkpoint_loader_simple_from_string import CheckpointLoaderSimpleFromString

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "CheckpointLoaderSimpleFromString": CheckpointLoaderSimpleFromString,
    "ConcatenateEx": ConcatenateEx,
    "LoraLoaderFromString": LoraLoaderFromString,
    "TextSelector": TextSelector,
    "TextMapSelector": TextMapSelector,
    "NumberGenerator": NumberGenerator,
    "NumberFilter": NumberFilter,
    "ToInt": ToInt,
    "ToString": ToString,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "CheckpointLoaderSimpleFromString": "Checkpoint Loader Simple From String",
    "ConcatenateEx": "Concatenate Ex",
    "LoraLoaderFromString": "LoRA Loader From String",
    "TextSelector": "Text Selector",
    "TextMapSelector": "Text Map Selector",
    "NumberGenerator": "Number Generator",
    "NumberFilter": "Number Filter",
    "ToInt": "To Int",
    "ToString": "To String",
}


__all__ = (
    "ODE_CLASS_MAPPINGS",
    "NODE_CLASS_MAPPINGS",
)
