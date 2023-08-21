## 安装和使用

### 安装修改版的WeChatTweak
我的[WeChatTweak](https://github.com/sunnyyoung/WeChatTweak-macOS) [修改版](https://github.com/JettChenT/WeChatTweak-macOS)通过`/wechat/chatlog`提供了一个用于查找聊天历史的API端口。

1. 下载修改后的[wechattweak-cli](https://github.com/JettChenT/WeChatTweak-CLI/releases/latest/download/wechattweak-cli)
2. 运行 `chmod +x wechattweak-cli`
3. 运行 `sudo ./wechattweak-cli install`

### 运行导出器
1. 运行 `pip install -r requirements.txt`
2. 创建一个文件夹 `./foo` (可选)
3. 运行 `python main.py ./foo`

运行完成后，你和微信内所有联系人的聊天历史记录都会被应导出到文件夹 `foo`。

## 要求
目前仅支持macOS（>=10.12）。
