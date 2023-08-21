import json
import typer
from pathlib import Path
import requests
from tqdm import tqdm
import xml.etree.ElementTree as ET

app = typer.Typer()

def get_safe_path(s: str) -> str:
    """
    Remove invalid characters to sanitize a path.
    :param s: str to sanitize
    :returns: sanitized str
    """
    ban_chars = "\\  /  :  *  ?  \"  '  <  >  |  $  \r  \n".replace(
        ' ', '')
    for i in ban_chars:
        s = s.replace(i, "")
    return s


def process_history(history: str):
    if history.startswith("<?xml") or history.startswith("<msg>"):
        try:
            root = ET.fromstring(history)
            title = root.find('.//title').text if root.find('.//title') is not None else None
            quoted = root.find('.//refermsg/content').text if root.find('.//refermsg/content') is not None else None
            if title and quoted:
                return {
                    "title": title,
                    "quoted": process_history(quoted)
                }
            if title:
                return title
        except Exception:
            return history
    return history

def export_chathistory(user_id: str):
    res = requests.get("http://localhost:48065/wechat/chatlog", params={
        "userId": user_id,
        "count": 100000
    }).json()
    for i in range(len(res['chatLogs'])):
        res['chatLogs'][i]['content'] = process_history(res['chatLogs'][i]['content'])
    return res['chatLogs']

@app.command()
def export_all(dest: Path):
    if not dest.is_dir():
        typer.echo("Destination path is not a directory!", err=True)
        return
    all_users = requests.get("http://localhost:48065/wechat/allcontacts").json()

    for user in tqdm(all_users):
        usr_chatlog = export_chathistory(user['arg'])
        out_path = dest/get_safe_path((user['title'] or "")+"-"+user['arg']+'.json')
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(usr_chatlog, f)

if __name__ == "__main__":
    app()
