import json

import typer
from pathlib import Path
import requests
from tqdm import tqdm

app = typer.Typer()

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
        with open(dest/((user['title'] or "")+user['arg']+'.json'), 'w') as f:
            json.dump(usr_chatlog, f)

if __name__ == "__main__":
    app()