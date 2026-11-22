from flask import Flask, request
import requests
import os

app = Flask(__name__)
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1574007671655235604/DDp97PUIJc5vxPKW347LQCHiiQPHrMuhegWeA7LtymOFnCIBRubPJXn4r-X5FdRg61PM"

# DATABASE CIOO - CUMA SECRET / ETERNAL / DIVINE DIO!
# Format: "Nama Pet": (Emoji, Area, Recommend Speed, Value, Berat Dasar)
DATABASE = {
    # --- DIVINE CIOO ---
    "Spirit World Guardian": ("👑", "Fusion / Spirit World", "50B", "$26B/s", "?? Kg"),
    "Xenorath": ("🐉", "Alien Biome", "250B", "$25B/s", "8.500 Kg"),
    "Prismare": ("💎", "Alien Biome", "250B", "$20B/s", "8.500 Kg"),
    "Sapphire Leviathan": ("💙", "Crystal Egg / Shop", "50B", "$15B/s", "?? Kg"),
    "Voidseer Pumpkin": ("🎃", "Halloween Dimension", "50B", "$12.5B/s", "60.000 Kg"),
    "Obsidian Rex": ("🦖", "Alien Biome", "250B", "$12.5B/s", "8.500 Kg"),
    "Royal Skywhale": ("🐋", "Enchanted Forest", "50B", "$8B/s", "?? Kg"),
    "Nightflame": ("🔥", "Titan Temple", "2.5B+", "$3B/s", "?? Kg"),
    "Kitsune": ("🦊", "Cherry Blossom", "2.5B", "$3.2B/s", "?? Kg"),
    "Unicorn": ("🦄", "Cosmic", "700M", "$1B/s", "?? Kg"),
    # --- ETERNAL CIOO ---
    "Celestial Sunlion": ("🦁", "Enchanted Forest", "50B", "$2B/s", "?? Kg"),
    "Viridian Prowler": ("🐺", "Alien Biome", "250B", "$3B/s", "8.500 Kg"),
    "Gorilla King": ("🦍", "Titan Temple", "2.5B+", "$880M/s", "?? Kg"),
    "Oni Tiger": ("🐯", "Cherry Blossom", "2.5B", "$600M/s", "?? Kg"),
    "Eternal Lunar Dragon": ("🐲", "Cosmic", "700M", "$250M/s", "?? Kg"),
    "Mosasaurus": ("🦕", "Prehistoric", "18M", "$180M/s", "?? Kg"),
    # --- SECRET CIOO ---
    "Starry Fox": ("🦊", "Enchanted Forest", "50B", "$750M/s", "?? Kg"),
    "Aurora Stag": ("🦌", "Alien Biome", "250B", "$1.2B/s", "8.500 Kg"),
    "Stag": ("🦌", "Cherry Blossom", "2.5B", "$145M/s", "?? Kg"),
    "Werewolf": ("🐺", "Halloween Dimension", "50B", "$1.3B/s", "?? Kg"),
}

BOLEH = ["Secret", "Eternal", "Divine"]

@app.route('/egg-spawn', methods=['POST'])
def egg_spawn():
    data = request.json
    pet_name = data.get("egg")
    rarity = data.get("rarity")
    # Ini Dio Cioo, yang dikirim dari game Dio, berat asli Dio!
    weight_asli = data.get("weight", "?? Kg")
    area_asli = data.get("area", "Unknown")

    if rarity not in BOLEH:
        return "Skip"

    # Cari Dio di database Cioo, kalo dak ketemu Dio, pake data dari game Dio!
    info = DATABASE.get(pet_name, ("🥚", area_asli, "Cek di game", "Cek di game", weight_asli))
    emoji, area_db, speed, value, weight_db = info

    # Kalo game ngirim weight asli Dio, pake yang asli Dio!
    final_weight = weight_asli if weight_asli != "?? Kg" else weight_db
    final_area = area_asli if area_asli != "Unknown" else area_db

    # INI DIO FORMAT KAU CIOO, PERSIS DIO!
        pesan = f"""@everyone ⚡🔥 🔥⚡ @everyone
**{rarity.upper()} SPAWN!**

🦁 **Pet:** {emoji} {pet_name}
📍 **Area:** {final_area}
🏃 **Recommend Speed:** {speed}

**Value:** {value}
**Weight:** {final_weight}

🎮 **JOIN GAME:**
https://www.roblox.com/games/107778070777162/Steal-an-Egg

_*📢 buruan join game & steal sebelum keduluan orang lain ‼️*_
_*👀 Pantengin terus discord ini agar tidak ketinggalan info spawn berikutnya ‼️*_

*⛔ Dilarang keras mengcopy apapun yang ada disini tanpa izin*"""

    requests.post(DISCORD_WEBHOOK, json={"content": pesan})
    return "OK"
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
