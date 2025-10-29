from nodes import CheckpointLoaderSimple

class CheckpointLoaderSimpleFromString(CheckpointLoaderSimple):
    @classmethod
    def INPUT_TYPES(cls):
        input_types = super().INPUT_TYPES()
        input_types["required"]["ckpt_name"] = (
            "STRING", {"tooltip": "The name of the checkpoint (model) to load."})
        return input_types

    RETURN_TYPES = ("MODEL", "CLIP", "VAE")
    OUTPUT_TOOLTIPS = ("The model used for denoising latents.",
                       "The CLIP model used for encoding text prompts.",
                       "The VAE model used for encoding and decoding images to and from latent space.")
    FUNCTION = "load_checkpoint"

    CATEGORY = "utils/CustomSelector"
    DESCRIPTION = "Loads a diffusion model checkpoint, diffusion models are used to denoise latents."
