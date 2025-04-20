import serial
import time
import os

def open_irtoy(port="COM3", baudrate=115200):
    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)
        ser.reset_input_buffer()
        print(f"✅ Connected to IR Toy on {port}")
        return ser
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def record_signal(ser, duration=5):
    ser.write(b'\x03')  # Start sampling mode
    print("📡 Recording IR signal for", duration, "seconds...")
    start = time.time()
    data = b''
    while time.time() - start < duration:
        if ser.in_waiting:
            data += ser.read(ser.in_waiting)
    ser.write(b'\x00')  # Exit sampling mode
    print("✅ Done recording.")
    return data

def save_signal(filename, data):
    os.makedirs("recorded", exist_ok=True)
    with open(os.path.join("recorded", filename), "wb") as f:
        f.write(data)
    print(f"💾 Saved to recorded/{filename}")

def send_raw_signal(ser, filename):
    file_path = os.path.join("recorded", filename)
    if not os.path.exists(file_path):
        print("❌ File not found.")
        return
    with open(file_path, "rb") as f:
        signal_data = f.read()
    ser.write(b'S')  # Enter transmit mode
    time.sleep(0.2)
    ser.write(signal_data)
    ser.write(b'\x00')  # End transmission
    print("📤 Signal sent!")
