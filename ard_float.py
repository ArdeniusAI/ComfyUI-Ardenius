"""
@author: initials AMAA
@title: Ardenius
@nickname: Ardenius
@description: ARD float: outputs a float number
"""
#  licensed under General Public License v3.0 all rights reserved © 2024
#  ( author initials AMAA Nickname Ardenius contact information ardenius7@gmail.com attribution link https://ko-fi.com/ardenius )
#  ➡️ follow me at https://ko-fi.com/ardenius in the top right corner (follow)
#  📸 Change the mood ! by Visiting my AI Image Gallery
#  🏆 Support me by getting Premium Members only Perks (Premium SD Models, ComfyUI custom nodes, and more to come)
#  below code is based upon ComfyUI code licensed under General Public License v3.0 https://www.gnu.org/licenses/gpl-3.0.txt by
#  contributers found here https://github.com/comfyanonymous/ComfyUI
#  thus all code here is released to the user as per the GPL V3.0 terms.

class ARD_FLOAT:
    # def __init__(self):
    #     pass
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Fx": ("FLOAT", {"default": 1, "tooltip": "input a float"}),
            },
        }

    RETURN_NAMES = ("float",)
    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "ard_float"

    CATEGORY = "Ardenius"
    DESCRIPTION = "ARD float: outputs a float number"

    def ard_integer(self, Fx):

        if not isinstance(Fx, float):
            output_float = float(Fx)
        else:
            output_float = Fx

        return (output_float,)