## Installation and Usage

### Installing Modified WeChatTweak
My modified version of WeChatTweak provides an API endpoint for Chat history lookup via `/wechat/chatlog`

1. Download the modified [wechattweak-cli](https://github.com/JettChenT/WeChatTweak-CLI/releases/latest/download/wechattweak-cli)
2. Run `chmod +x wechattweak-cli`
3. Run `sudo ./wechattweak-cli install`

### Running the exporter
1. Run `pip install -r requirements.txt`
2. Create an arbitrary folder `./foo`
3. Run `python main.py ./foo`

After the run finishes, the chat history you have in your computer with each of your contacts
should be exported to folder `foo`.

## Requirements
Currently, only macOS(>=10.12) is supported.

