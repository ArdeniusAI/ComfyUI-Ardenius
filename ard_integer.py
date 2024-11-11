"""
@author: initials AMA
@title: Ardenius
@nickname: Ardenius
@description: ARD integer: outputs an integer number
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

class ARD_INTEGER:
    # def __init__(self):
    #     pass
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Ix": ("INT", {"default": 1, "tooltip": "input an integer or float"})
            }
        }

    RETURN_NAMES = ("integer",)
    RETURN_TYPES = ("INT",)
    FUNCTION = "ard_integer"

    CATEGORY = "Ardenius"
    DESCRIPTION = "ARD integer: outputs an integer number"

    def ard_integer(self, Ix):

        if not isinstance(Ix, int):
            output_integer = int(Ix)
        else:
            output_integer = Ix

        return (output_integer,)