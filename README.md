# ComfyUI TY_Captioner 节点

一个用于生成图像描述的ComfyUI自定义节点。

## 功能特点

- 简洁现代的UI设计，白色和蓝绿色为主色调
- 左侧标签页：参考图像输入
- 右侧标签页：描述输入/输出
- 支持自定义描述提示词
- 可选的自动描述生成功能
- 中文界面支持

## 安装方法

1. 将 `ComfyUI_TY_Captioner` 文件夹复制到 ComfyUI 的 `custom_nodes` 目录
2. 重启 ComfyUI

## 使用方法

1. 在节点列表中查找"南光AIGC"类别
2. 添加"TY_Captioner"节点
3. 连接图像输入到"参考图像"端口
4. 设置描述提示词（可选）
5. 运行工作流获取图像描述
6. 描述输出可连接到其他节点的文本输入

## 输入参数

- **image**: 输入图像（必填）
- **caption_prompt**: 描述生成提示词（默认提供中文提示）
- **enable_captioning**: 启用描述生成功能
- **description_input**: 手动输入描述（可选）

## 输出

- **description**: 生成的图像描述文本

## 注意事项

- 当前版本使用示例描述生成逻辑
- 如需实际图像描述功能，需集成BLIP、CLIP等模型
- 界面已优化为中文显示

### 南光AIGC

南光AIGC-AIGC全能方案设计解决专家 VX:nankodesign2001

南光AIGC绘画 仙宫云新人注册网址---https://www.xiangongyun.com/register/MJAT43 新人注册仙宫云送5元代金券， 填写邀请码（输入我们的邀请码：MJAT43 ）还额外送3元代金券 完成后可以得到仙宫云8元账户余额，可以免费带你玩转5小时发高配4090 D显卡AIGC绘画。


PS软件（AI）插件
https://istarry.com.cn/?sfrom=jbEHmC
提供多种强大的AI功能，轻松提升设计效率，邀您免费体验

通过这个链接注册送1000RH币：https://pre.runninghub.cn/?inviteCode=t7ztfeiw 注册领1000RH币可以免费生成好多图片视频哦！

### 三大自媒体平台

小红书
https://www.xiaohongshu.com/user/profile/5fe63b41000000000100811d?m_source=itab

抖音
https://www.douyin.com/user/self?showTab=post

bilibili（B站）
https://space.bilibili.com/404783526


### 如果您受益于本项目，不妨请作者喝杯咖啡，您的支持是我最大的动力

<div style="display: flex; justify-content: left; gap: 20px;">
    <img src="https://github.com/balu112121/ComfyUI_NanKo_AI_Recognize/blob/main/Alipay.jpg" width="300" alt="支付宝收款码">
    <img src="https://github.com/balu112121/ComfyUI_NanKo_AI_Recognize/blob/main/WeChat.jpg" width="300" alt="微信收款码">
</div>

# 商务合作
如果您有定制工作流/节点的需求，或者想要学习插件制作的相关课程，请联系我
wechat:nankodesign2001
