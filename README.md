# IR Toolkit - Command-Line IR Controller

**IR Toolkit** is a powerful and extensible Python-based command-line tool that allows you to control IR-enabled devices like TVs, ACs, audio systems, lights, and more using a USB Infrared Toy. The project supports signal recording, decoding, and replaying, and uses a large LIRC-based `.conf` remote database.

---

## 📦 Features

- ✅ Record raw IR signals from physical remotes
- ✅ Send IR signals directly to devices using USB IR Toy
- ✅ Use LIRC-compatible `.conf` files to simulate any known remote
- ✅ Filter remotes by device type and brand
- ✅ Simulate button presses from real remote layouts
- ✅ Fully command-line based (no GUI bloat)
- ✅ Designed for extensibility and clean terminal automation

---

## 🧰 Requirements

- Python 3.7+
- USB Infrared Toy (v1 or v2)
- LIRC remote config database (`.conf` files)
- `pyserial` for communication with USB IR Toy

### 🔧 Installation

```bash
git clone https://github.com/AhsanUllahv/IR-Toolkit.git
cd IR-Toolkit
pip install pyserial
```

---

## 🖥️ Project Structure

```
IR-Toolkit/
├── ir_controller.py         # Main command-line interface
├── irtoy_serial.py          # Handles communication with USB IR Toy
├── recorded/                # Stores raw recorded IR signals
└── remotes/                 # LIRC-compatible database of remotes
```

---

## 🚀 How to Use

### 1. Connect your USB Infrared Toy

Make sure it's plugged in and visible under Device Manager. On Windows, it usually shows up as `COM3`, `COM4`, etc.

---

### 2. Start the CLI

```bash
python ir_controller.py
```

You’ll see a menu like:

```
==== USB IR Toy CLI ====
1. Record new IR signal
2. Send saved IR signal
3. Use Database to control device
4. Exit
```

---

### 3. Use LIRC Database to Control a Device

- Choose device type (e.g., TV, AC)
- Select a brand (e.g., LG, Samsung)
- Pick one of the matched `.conf` files
- View and select the button (e.g., `KEY_POWER`, `KEY_VOLUMEUP`)
- Transmit the IR signal

---

### 4. Record Raw IR Signals from Real Remotes

- Choose "Record new IR signal"
- Press the button on your remote
- The signal is saved in `recorded/`

---

## 📂 Supported Devices

- TVs (LG, Samsung, Sony, etc.)
- Air Conditioners
- Lighting systems
- Audio systems & soundbars
- DVD/Blu-ray players
- Game consoles
- Projectors
- Set-Top Boxes
- Printers/Scanners
- Smart home devices

> Over 300 brands supported across 10 device categories.

---

## 🛡️ Ethical Use Message

> ⚠️ **This software is intended for ethical, educational, and personal use only.**

Please do **not** use IR Toolkit to interfere with public devices, copy private remote signals without consent, or perform actions that could be considered intrusive or illegal. Misuse of this tool may violate device laws in your region.

**By using this software, you agree to use it responsibly.** 🙏

---

## 📄 License

This project is licensed under the **MIT License** – giving users maximum freedom to use, modify, and share.

See the [LICENSE](./LICENSE) file for details.

---

## 👨‍💻 Author

**Ahsan Ullah**  
Made with ❤️ and Python  
GitHub: [@AhsanUllahv](https://github.com/AhsanUllahv)

---

## 🙌 Contributions

Have ideas or want to help expand the device database?

Pull requests are welcome!  
Just fork the repo, create a new branch, and submit your change.

---

## 🌐 Resources

- [USB Infrared Toy by Dangerous Prototypes](http://dangerousprototypes.com/docs/USB_Infrared_Toy)
- [LIRC Remote Configuration Files](http://lirc.sourceforge.net/remotes/)
- [pyserial documentation](https://pyserial.readthedocs.io)