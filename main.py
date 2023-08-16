import json

import typer
from pathlib import Path
import requests
from tqdm import tqdm

app = typer.Typer()

# Credits: YoungLord https://github.com/Young-Lord/QQ-History-Backup/blob/b7d7f136020d0699c8dd802b3dff65247aeb6698/QQ_History.py#L99
def getSafePath(ans: str) -> str:
    ban_words = "\\  /  :  *  ?  \"  '  <  >  |  $  \r  \n".replace(
        ' ', '')
    ban_strips = "#/~"
    while True:
        ans_bak = ans
        for i in ban_words:
            ans = ans.replace(i, "")
        for i in ban_strips:
            ans = ans.strip(i)
        if ans == ans_bak:  # 多次匹配
            break
    return ans

def export_chathistory(user_id: str):
    res = requests.get("http://localhost:48065/wechat/chatlog", params={
        "userId": user_id,
        "count": 100000
    }).json()
    return res['chatLogs']

@app.command()
def export_all(dest: Path):
    if not dest.is_dir():
        typer.echo("Destination path is not a directory!", err=True)
        return
    all_users = requests.get("http://localhost:48065/wechat/search").json()

    for user in tqdm(all_users['items']):
        usr_chatlog = export_chathistory(user['arg'])
        out_path = dest/getSafePath((user['title'] or "")+"-"+user['arg']+'.json')
        with open(out_path, 'w') as f:
            json.dump(usr_chatlog, f)

if __name__ == "__main__":
    app()