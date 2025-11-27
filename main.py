from termcolor import colored
from tools.weather_tool import get_weather
from tools.system_info import get_system_info
from tools.file_organizer import smart_organize
from tools.google_calendar_tool import add_event, show_events

# ====== Helper UI ======
def ai(text):
    print(colored(f"[R4 Agent] {text}", "cyan"))

def think(text):
    print(colored(f"[Thinking] {text}", "yellow"))

def user_input(prompt="You: "):
    return input(colored(prompt, "green"))


# ====== Greeting ======
def greet_user():
    ai("Halo Runni! 👋 Aku R4 Agent, asisten yang selalu siap bantu kamu 💙")
    ai("Kalau bingung mau mulai apa, ketik 'menu' ya ✨\n")

# ====== MENU ======
def show_menu():
    ai("Ini fitur yang bisa aku lakukan:")
    print(colored("1. Cek Cuaca 🌤️", "yellow"))
    print(colored("2. Buat Jadwal ke Google Calendar 📅", "yellow"))
    print(colored("3. Lihat Jadwal Mendatang 📆", "yellow"))
    print(colored("4. Cek System Info 💻", "yellow"))
    print(colored("5. File Organizer 📂", "yellow"))
    print(colored("6. Keluar ❌", "yellow"))

# --- CUACA ---
def handle_weather(user):
    think("Sedang mencari kota...")

    words = user.lower().split()
    city = None

    # Ambil kota setelah kata 'di' atau 'cuaca'
    for i, w in enumerate(words):
        if w in ["di", "ke", "cuaca", "kota"]:
            if i + 1 < len(words):
                city = words[i + 1]
                break

    if not city:
        ai("Kamu mau cek cuaca di kota mana?")
        city = user_input()

    think(f"Mengambil data cuaca untuk {city}...")
    ai(get_weather(city))

# --- GOOGLE CALENDAR: ADD EVENT ---
def handle_calendar_add():
    ai("Oke! Yuk buat jadwal baru di Google Calendar ✨")

    title = user_input("Judul: ")
    date = user_input("Tanggal (YYYY-MM-DD): ")

    think("Mengirim ke Google Calendar...")
    try:
        ai(add_event(title, date))
    except Exception as e:
        ai(f"Terjadi error: {e}")

# --- GOOGLE CALENDAR: SHOW EVENT ---
def handle_calendar_show():
    think("Mengambil jadwal upcoming...")
    try:
        ai(show_events())
    except Exception as e:
        ai(f"Error: {e}")

# --- SYSTEM INFO ---
def handle_system_info():
    think("Mengambil informasi sistem...")
    ai(get_system_info())

# --- FILE ORGANIZER ---
def handle_file_organizer():
    ai("Masukkan folder yang mau dirapikan:")
    ai("Contoh: C:/Users/NAMA/Downloads")

    path = user_input("Folder: ")

    ai(f"Kamu yakin mau rapikan folder ini?\n➡ {path}")
    confirm = user_input("Ketik 'ya' untuk melanjutkan: ").lower()

    if confirm != "ya":
        ai("Oke, batal yaa 😊")
        return

    think("Sedang merapikan file...")
    ai(smart_organize(path))

# ====== MAIN LOOP ======
def main():
    greet_user()

    while True:
        user = user_input()

        # Greeting Friendly
        if any(greet in user.lower() for greet in ["halo", "hai", "hello", "hi"]):
            ai("Haii Runni! Seneng banget kamu nyapa duluan 💙")
            ai("Kalau butuh apa-apa, ketik 'menu' ya ✨")
            continue

        #End Season Greetings
        if any(x in user.lower() for x in ["makasih", "makasi", "thanks", "thank you", "terima kasih"]):
            ai("Sama-samaaa Runniii 💙 Senang bisa bantu kamu!")
            ai("Kalau ada yang mau kamu tanyain lagi, tinggal bilang aja ya ✨")
            continue

        # Menu
        if user.lower() in ["menu", "fitur", "help"]:
            show_menu()
            continue

        # --- MENU ANGKA ---
        if user == "1": 
            handle_weather(user)
            continue

        if user == "2": 
            handle_calendar_add()
            continue

        if user == "3": 
            handle_calendar_show()
            continue

        if user == "4": 
            handle_system_info()
            continue

        if user == "5": 
            handle_file_organizer()
            continue

        if user == "6":
            ai("Dadah Runniii 💙 Semoga harimu menyenangkan! ✨")
            break

        # --- Natural command detection ---
        if "cuaca" in user.lower():
            handle_weather(user)
            continue

        if "jadwal" in user.lower():
            handle_calendar_add()
            continue

        if "rapi" in user.lower() or "organize" in user.lower():
            handle_file_organizer()
            continue

        if "system" in user.lower():
            handle_system_info()
            continue

        ai("Hmm aku belum paham maksudmu, coba ketik 'menu' ya ✨")

if __name__ == "__main__":
    main()
