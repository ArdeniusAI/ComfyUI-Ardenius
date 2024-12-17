"""
@author: initials AMAA
@title: Ardenius
@nickname: Ardenius
@description: ARD control box is designed to gather workflow variables into 1 node.
"""
#  licensed under General Public License v3.0 all rights reserved © 2024
#  Owner initials: AMAA
#  nickname: Ardenius
#  email: ardenius7@gmail.com
#  website: https://ko-fi.com/ardenius
#  ➡️ follow me at https://ko-fi.com/ardenius in the top right corner (follow)
#  📸 Change the mood ! by Visiting my AI Image Gallery
#  🏆 Support me by getting Premium Members only Perks (Premium SD Models, ComfyUI custom nodes, and more to come)
#  below code is based upon ComfyUI code licensed under General Public License v3.0 https://www.gnu.org/licenses/gpl-3.0.txt by
#  contributers found here https://github.com/comfyanonymous/ComfyUI
#  thus all code here is released to the user as per the GPL V3.0 terms.


import os.path
import folder_paths
import numpy as np
import torch
import comfy.model_management
import comfy.samplers

MAX_RESOLUTION = 8192

class ARD_CONTROL_BOX:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        self.type = "output"
        self.prefix_append = ""
        self.compress_level = 0
        self.device = comfy.model_management.intermediate_device()

    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                    {
                    "cfg": ("FLOAT", {"default": 8, "min": 0.1, "max": 15, "step": 0.1}),
                    "steps": ("INT", {"default": 20, "min": 1, "max": 100, "step": 1}),
                    "denoise": ("FLOAT", {"default": 1.0, "min": 0.01, "max": 1.0, "step": 0.01}),
                    "scaler": ("FLOAT", {"default": 1.0, "min": 0.01, "max": 4.0, "step": 0.0001}),
                    "seed": ("INT", {"default": 1234567891, "min": 1, "max": 0xffffffffffffffff, "step": 1}),
                    "positive_prompt": ("CONDITIONING", {"default": ""}),
                    "negative_prompt": ("CONDITIONING", {"default": ""}),
                    "model": ("MODEL",),
                    "vae": ("VAE",),
                    "width": ("INT", {"default": 1024, "min": 64, "max": MAX_RESOLUTION, "step": 8}),
                    "height": ("INT", {"default": 1024, "min": 64, "max": MAX_RESOLUTION, "step": 8}),
                    "latent_width": ("INT", {"default": 1024, "min": 64, "max": MAX_RESOLUTION, "step": 8}),
                    "latent_height": ("INT", {"default": 1024, "min": 64, "max": MAX_RESOLUTION, "step": 8}),
                    "latent_batch_size": ("INT", {"default": 1, "min": 1, "max": 4096}),
                    "divx": ("INT", {"default": 8, "min": 8, "max": 4096, "step": 8}),
                    },
                }

    RETURN_NAMES = ("model", "positive", "negative", "latent_out", "seed", "cfg", "steps", "denoise", "scaler", "vae", "width", "height", "latent_width", "latent_height", "divx",)
    RETURN_TYPES = ("MODEL", "CONDITIONING", "CONDITIONING", "LATENT", "INT", "FLOAT", "INT", "FLOAT", "FLOAT", "VAE", "INT", "INT", "INT", "INT", "INT",)

    FUNCTION = "ard_control_box"

    OUTPUT_NODE = True

    CATEGORY = "Ardenius"
    DESCRIPTION = "ARD control box is designed to gather workflow variables into 1 node"

    def ard_control_box(self, cfg, steps, denoise, scaler, seed, positive_prompt, negative_prompt, model, vae, width, height, latent_width, latent_height, latent_batch_size, divx):

        remainder = width % divx
        width = width + remainder

        remainder = height % divx
        height = height + remainder

        remainder = latent_width % divx
        latent_width = latent_width + remainder

        remainder = latent_height % divx
        latent_height = latent_height + remainder

        latent_out = self.generate_latent(latent_width, latent_height, latent_batch_size, divx=8)

        return model, positive_prompt, negative_prompt, latent_out, seed, cfg, steps, denoise, scaler, vae, width, height, latent_width, latent_height, divx

    def generate_latent(self, width, height, latent_batch_size=1, divx=8):
        latent = torch.zeros([latent_batch_size, 4, height // divx, width // divx], device=self.device)
        return {"samples": latent}

