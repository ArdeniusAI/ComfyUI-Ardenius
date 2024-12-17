"""
@author: initials AMA
@title: Ardenius
@nickname: Ardenius
@description: ARD seed: default seed plus outputs an integer number increment
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

class ARD_SEED:
    # def __init__(self):
    #     pass
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "max_count": ("INT", {"default": 1}),
                "seed": ("INT", {"default": 1, "min": 1, "max": 0xffffffffffffffff, "step": 1})
            }
        }

    RETURN_NAMES = ("seed", "seed_float")
    RETURN_TYPES = ("INT", "FLOAT",)
    FUNCTION = "ard_seed"

    CATEGORY = "Ardenius"
    DESCRIPTION = "ARD seed: default seed plus outputs an integer number increment"

    def ard_seed(self, max_count, seed):
        if seed > max_count:
            seed = 1
        seed_float = float(seed)
        return (seed, seed_float)