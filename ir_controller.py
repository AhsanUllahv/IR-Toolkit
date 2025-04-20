import os
from irtoy_serial import open_irtoy, record_signal, save_signal, send_raw_signal

# Full device categories and brands
DEVICE_CATEGORIES = {
    "TV": [
        "LG", "Samsung", "Sony", "Panasonic", "Philips", "Toshiba", "Sharp", "Vizio", "Hisense", "TCL", "Sanyo", "JVC",
        "Hitachi", "RCA", "Insignia", "Westinghouse", "Pioneer", "Grundig", "Loewe", "Metz", "Blaupunkt", "Skyworth",
        "Changhong", "Haier", "Konka", "Vestel", "Bush", "Finlux", "Alba", "Polaroid", "Element", "Seiki", "Magnavox",
        "Emerson", "AOC", "Beko", "Coby", "Curtis", "Dynex", "Ecco", "Etron", "Funai", "GoldStar", "Hannspree", "iLo",
        "Luxor", "Medion", "Micromax", "NEC", "Orion", "Proscan", "Sansui", "Sceptre", "Supersonic", "Thomson",
        "ViewSonic", "Zenith"
    ],
    "Air Conditioner": [
        "Carrier", "Trane", "Lennox", "American Standard", "Goodman", "Amana", "HEIL", "Rheem", "York", "Ruud", "Daikin",
        "Gree", "Haier", "LG", "Mitsubishi", "Panasonic", "Samsung", "Hitachi", "Whirlpool", "Voltas", "Blue Star",
        "Fujitsu", "Midea", "Black+Decker", "GE", "Whynter", "Shinco", "Pro Breeze", "Rovsun", "Frigidaire",
        "Friedrich", "Arctic King", "TCL", "Aux", "Chigo", "Electrolux", "Kelvinator", "O General", "Sanyo", "Sharp",
        "Toshiba", "Westinghouse"
    ],
    "Lighting": [
        "Philips Hue", "Mi", "TP-Link", "Wipro", "Syska", "LIFX", "Yeelight", "Acuity Brands", "Artemide", "Aputure",
        "Artcraft", "Anglepoise", "Bevolo", "BernzOmatic", "GE Lighting", "Cree", "Osram", "Sylvania", "Feit Electric",
        "Leviton", "Lutron", "Hubbell", "Cooper Lighting", "Lithonia Lighting", "MaxLite", "Satco", "Progress Lighting",
        "RAB Lighting", "Nora Lighting", "Halo", "Kichler", "Westinghouse Lighting", "Juno Lighting", "TCP", "Zumtobel",
        "Fagerhult", "iGuzzini", "WE-EF", "Thorn Lighting", "Havells", "Bajaj", "Surya", "Orient Electric"
    ],
    "Audio System": [
        "Bose", "JBL", "Sony", "Yamaha", "LG", "Samsung", "Polk Audio", "Denon", "Onkyo", "Pioneer", "Harman Kardon",
        "Vizio", "Sonos", "Klipsch", "Marshall", "Bang & Olufsen", "Bowers & Wilkins", "Cambridge Audio", "KEF",
        "Definitive Technology", "Edifier", "Creative", "Altec Lansing", "Behringer", "Cerwin-Vega", "DALI", "Focal",
        "Infinity", "Jamo", "Mackie", "Monitor Audio", "NAD", "Q Acoustics", "Wharfedale", "Acoustic Energy", "Canton",
        "Elac", "GoldenEar", "Paradigm", "PSB", "SVS", "Tannoy"
    ],
    "DVD/Blu-ray Player": [
        "Sony", "LG", "Samsung", "Panasonic", "Philips", "Toshiba", "Pioneer", "Sharp", "Magnavox", "JVC", "Denon",
        "OPPO Digital", "Cambridge Audio", "Yamaha", "Marantz", "Onkyo", "Teac", "NAD", "Integra", "Harman Kardon",
        "Sanyo", "Funai", "Coby", "Curtis", "Daewoo", "Ematic", "GPX", "Haier", "Hitachi", "Insignia", "RCA",
        "Sylvania", "Zenith"
    ],
    "Game Console": [
        "Sony PlayStation", "Microsoft Xbox", "Nintendo", "Sega", "Atari", "Intellivision", "ColecoVision", "Neo Geo",
        "Panasonic 3DO", "Philips CD-i", "TurboGrafx-16", "Vectrex", "Magnavox Odyssey", "Fairchild Channel F",
        "Bally Astrocade", "Commodore 64 GS", "Amiga CD32", "Apple Pippin", "Bandai Playdia", "Casio Loopy",
        "Mattel HyperScan", "Nokia N-Gage", "Ouya", "Steam Machine", "Atari Jaguar", "GamePark GP32", "Gizmondo",
        "Tapwave Zodiac"
    ],
    "Set-Top Box": [
        "Tata Sky", "Dish TV", "Airtel Digital TV", "Comcast Xfinity", "DirecTV", "Sky", "Roku", "Apple TV",
        "Amazon Fire TV", "Google Chromecast", "HUMAX", "Technicolor", "Arris", "Huawei", "ZTE", "Sagemcom",
        "Kaon Media", "Pace", "Motorola", "Cisco", "Echostar", "Foxtel", "Fetch TV", "Freeview", "Freesat", "Netgem",
        "Vestel", "Strong", "Amiko", "Dreambox", "Vu+", "Openbox", "MAG", "Infomir", "Formuler", "Zgemma", "Octagon",
        "Edision", "Enigma2"
    ],
    "Projector": [
        "Epson", "BenQ", "Sony", "LG", "Panasonic", "Optoma", "ViewSonic", "NEC", "Acer", "Dell", "Hitachi",
        "InFocus", "JVC", "Barco", "Christie", "Vivitek", "Canon", "Sharp", "Samsung", "Hisense", "Toshiba", "Ricoh",
        "Philips", "Xiaomi", "JMGO", "XGIMI", "Anker Nebula", "AAXA", "Vankyo", "Yaber", "Eiki", "Dukane",
        "Digital Projection", "Casio", "Runco", "Sim2", "Wolf Cinema"
    ],
    "Printer/Scanner": [
        "HP", "Canon", "Epson", "Brother", "Lexmark", "Xerox", "Kyocera", "Ricoh", "Samsung", "Dell", "OKI", "Panasonic",
        "Sharp", "Toshiba", "Fujitsu", "Zebra", "Dymo", "Konica Minolta", "NEC", "Olivetti", "Seiko", "TallyGenicom",
        "Gestetner", "Nashuatec", "Lanier", "Savin", "Pitney Bowes", "Sindoh", "Triumph-Adler", "Utax", "Sanyo"
    ],
    "Computer Peripheral": [
        "Logitech", "Razer", "Corsair", "SteelSeries", "Microsoft", "HP", "Dell", "Asus", "Acer", "Lenovo",
        "Cooler Master", "Mad Catz", "HyperX", "Turtle Beach", "Roccat", "Redragon", "Anker", "Sades", "A4Tech",
        "Trust", "Genius", "Kensington", "3Dconnexion", "CH Products", "Saitek", "Thrustmaster", "Hori", "Elecom",
        "Glorious", "Keychron", "Das Keyboard", "Filco", "Ducky", "Varmilo", "Leopold", "Topre", "Realforce"
    ]
}


def list_devices():
    print("\nAvailable device types:")
    for i, device in enumerate(DEVICE_CATEGORIES.keys(), 1):
        print(f"{i}. {device}")
    choice = int(input("Select a device type: "))
    return list(DEVICE_CATEGORIES.keys())[choice - 1]


def list_brands(device_type):
    brands = DEVICE_CATEGORIES[device_type]
    print(f"\nAvailable brands for {device_type}:")
    for i, brand in enumerate(brands, 1):
        print(f"{i}. {brand}")
    choice = int(input("Select a brand: "))
    return brands[choice - 1]


def find_config_files(device_type, brand):
    remotes_path = os.path.join(os.path.dirname(__file__), "remotes")
    brand_folder = brand.lower()
    matches = []
    for root, dirs, files in os.walk(remotes_path):
        if os.path.basename(root).lower() == brand_folder:
            for f in files:
                if f.endswith(".conf"):
                    matches.append(os.path.join(root, f))
    return matches




def show_main_menu():
    print("\n==== USB IR Toy CLI ====")
    print("1. Record new IR signal")
    print("2. Send saved IR signal")
    print("3. Use Database to control device")
    print("4. Exit")
    return input("Choose an option: ")


def send_keys_from_conf(ser, config_file):
    keys = []
    in_codes_section = False

    with open(config_file, "r") as f:
        for line in f:
            line = line.strip()
            if line.lower().startswith("begin codes"):
                in_codes_section = True
                continue
            if line.lower().startswith("end codes"):
                break
            if in_codes_section and line:
                parts = line.split()
                if len(parts) >= 2:
                    key_name = parts[0]
                    label = ""
                    if '#' in line:
                        label = line.split('#', 1)[1].strip()
                    display_name = f"{key_name} ({label})" if label else key_name
                    keys.append((key_name, display_name))

    if not keys:
        print("❌ No keys found in config.")
        return

    print("\nAvailable keys:")
    for i, (_, display) in enumerate(keys, 1):
        print(f"{i}. {display}")

    idx = int(input("Select a key to send: ")) - 1
    key_selected = keys[idx][0]
    print(f"📤 Sending key: {key_selected}")
    print(f"✅ (Simulated) Sent key: {key_selected}")



def run():
    port = input("🔌 Enter COM port for IR Toy (e.g., COM3): ")
    ser = open_irtoy(port)
    if not ser:
        return

    recorded_path = os.path.join(os.path.dirname(__file__), "recorded")
    os.makedirs(recorded_path, exist_ok=True)

    while True:
        choice = show_main_menu()

        if choice == "1":
            name = input("Enter name for this signal (e.g. power_on.raw): ")
            duration = int(input("Recording duration in seconds: "))
            data = record_signal(ser, duration)
            save_signal(os.path.join(recorded_path, name), data)

        elif choice == "2":
            files = os.listdir(recorded_path)
            if not files:
                print("No recorded signals available.")
                continue
            for i, f in enumerate(files, 1):
                print(f"{i}. {f}")
            idx = int(input("Select file to send: ")) - 1
            send_raw_signal(ser, os.path.join(recorded_path, files[idx]))

        elif choice == "3":
            device_type = list_devices()
            brand = list_brands(device_type)
            matched_files = find_config_files(device_type, brand)

            if not matched_files:
                print(f"❌ No remote configs found for {brand}")
                continue

            print(f"\n✅ Found {len(matched_files)} config(s) for {brand}:")
            for i, f in enumerate(matched_files, 1):
                print(f"{i}. {os.path.basename(f)}")
            idx = int(input("Select a config to use: ")) - 1
            selected_file = matched_files[idx]

            print(f"\n📂 Selected config: {selected_file}")
            send_keys_from_conf(ser, selected_file)

        elif choice == "4":
            print("👋 Goodbye!")
            break

        else:
            print("❗ Invalid choice.")


if __name__ == "__main__":
    run()
