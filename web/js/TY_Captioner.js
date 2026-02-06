import { app } from "../../scripts/app.js";

app.registerExtension({
    name: "ComfyUI_TY_Captioner",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === "TY_Captioner") {
            const onNodeCreated = nodeType.prototype.onNodeCreated;
            nodeType.prototype.onNodeCreated = function () {
                const r = onNodeCreated?.apply(this, arguments);
                
                // 添加自定义样式
                this.addWidgetStyle();
                
                return r;
            };
            
            // 自定义节点渲染
            nodeType.prototype.onDrawForeground = function (ctx) {
                if (this.flags.collapsed) return;
                
                // 绘制标签页背景
                const headerHeight = 30;
                ctx.fillStyle = "#f5f5f5";
                ctx.fillRect(0, 0, this.size[0], headerHeight);
                
                // 绘制标签页
                ctx.fillStyle = "#00b4a0";  // 蓝绿色
                ctx.fillRect(0, 0, this.size[0]/2, headerHeight);
                
                // 绘制标签页文字
                ctx.fillStyle = "#ffffff";
                ctx.font = "bold 12px Arial";
                ctx.textAlign = "center";
                ctx.textBaseline = "middle";
                
                ctx.fillText("参考图像", this.size[0]/4, headerHeight/2);
                ctx.fillText("描述", this.size[0]*3/4, headerHeight/2);
                
                // 绘制分隔线
                ctx.strokeStyle = "#cccccc";
                ctx.beginPath();
                ctx.moveTo(this.size[0]/2, 0);
                ctx.lineTo(this.size[0]/2, headerHeight);
                ctx.stroke();
            };
            
            nodeType.prototype.addWidgetStyle = function () {
                // 为文本输入框添加样式
                const widgets = this.widgets || [];
                for (const widget of widgets) {
                    if (widget.name === "caption_prompt" || widget.name === "description_input") {
                        widget.inputEl.style.background = "#f8f9fa";
                        widget.inputEl.style.border = "1px solid #e0e0e0";
                        widget.inputEl.style.borderRadius = "4px";
                        widget.inputEl.style.padding = "8px";
                        widget.inputEl.style.minHeight = "80px";
                        widget.inputEl.style.color = "#333";
                    }
                }
            };
        }
    },
});