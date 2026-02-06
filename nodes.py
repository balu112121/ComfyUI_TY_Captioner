import torch
import numpy as np
from PIL import Image
import folder_paths
import comfy.sd
import comfy.utils
from comfy.cli_args import args
import nodes
import hashlib
import json
import os

class TY_Captioner:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "caption_prompt": ("STRING", {
                    "multiline": True,
                    "default": "请提供此图像的详细说明。如果您熟悉图像中的任何角色、如名人、电影角色或动画人物，请直接使用他们的名字。描述应尽可能详细，但不应超过200字。"
                }),
                "enable_captioning": ("BOOLEAN", {"default": True}),
            },
            "optional": {
                "description_input": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("description",)
    FUNCTION = "generate_caption"
    CATEGORY = "南光AIGC"
    OUTPUT_NODE = True

    def __init__(self):
        pass

    def generate_caption(self, image, caption_prompt, enable_captioning, description_input=""):
        # 如果有用户输入的描述，优先使用
        if description_input and description_input.strip():
            description = description_input.strip()
        elif enable_captioning:
            # 这里可以集成实际的图像描述模型
            # 目前返回一个示例描述
            description = self.generate_dummy_caption(image, caption_prompt)
        else:
            description = "图像描述功能已禁用"
        
        return (description,)

    def generate_dummy_caption(self, image, prompt):
        # 这是一个示例函数，实际应用中应该集成BLIP、CLIP等图像描述模型
        # 这里返回一个模拟的描述
        
        # 将tensor转换为PIL图像用于分析
        if len(image.shape) == 4:
            image = image[0]
        
        image_np = image.cpu().numpy()
        image_np = (image_np * 255).astype(np.uint8)
        
        if len(image_np.shape) == 3 and image_np.shape[2] == 4:
            pil_image = Image.fromarray(image_np, mode='RGBA')
        elif len(image_np.shape) == 3 and image_np.shape[2] == 3:
            pil_image = Image.fromarray(image_np, mode='RGB')
        else:
            pil_image = Image.fromarray(image_np)
        
        # 获取图像基本信息
        width, height = pil_image.size
        image_hash = hashlib.md5(pil_image.tobytes()).hexdigest()[:8]
        
        # 生成示例描述
        description = f"这是一张{width}x{height}像素的图像，包含丰富的视觉内容。图像构图平衡，色彩鲜明，具有很好的视觉吸引力。"
        description += " 场景中的元素排列有序，光影效果自然，展示了高质量的视觉表现。"
        description += " 图像细节清晰，纹理丰富，能够传达出特定的氛围和情感。"
        
        # 如果prompt中有特定要求，可以进一步处理
        if "角色" in prompt or "人物" in prompt:
            description += " 图像中的人物特征鲜明，姿态自然，表情生动。"
        
        if "详细" in prompt:
            description += " 从构图上分析，主体突出，背景协调，空间感良好。色彩搭配和谐，明暗对比适中。"
        
        return description[:200]  # 限制在200字以内

# 节点注册
NODE_CLASS_MAPPINGS = {
    "TY_Captioner": TY_Captioner
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TY_Captioner": "TY_Captioner"
}