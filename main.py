from flask import Flask, request
import requests

app = Flask(__name__)

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1507592139024896190/0qmmy4GLylft4RdVxxZNsybBXCrXoCVYbRHMrNc1tkLqrybpY0T8pTvLJrlmgXWrEWvI"

@app.route("/report")
def report():
    username          = request.args.get("username", "Unknown")
    discord           = request.args.get("discord", "Unknown")
    world             = request.args.get("world", "Unknown")
    gems              = request.args.get("gems", "?")
    bgl               = request.args.get("bgl", "-")
    reconnect_success = request.args.get("reconnect_success", "-")
    reconnect_failed  = request.args.get("reconnect_failed", "-")

    payload = {
        "embeds": [{
            "title": "📡 User Activity",
            "color": 3066993,
            "fields": [
                {"name": "🪪 GrowID",           "value": username,          "inline": True},
                {"name": "🎮 Discord ID",        "value": discord,           "inline": True},
                {"name": "🌍 World",             "value": world,             "inline": True},
                {"name": "🪎 Gems",              "value": gems,              "inline": True},
                {"name": "💎 Purchased BGL",     "value": bgl,               "inline": True},
                {"name": "✅ Reconnect Success", "value": reconnect_success, "inline": True},
                {"name": "❌ Reconnect Failed",  "value": reconnect_failed,  "inline": True},
            ]
        }]
    }

    try:
        requests.post(DISCORD_WEBHOOK, json=payload)
        return "ok", 200
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
