import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883

TEMP_THRESHOLD = 32
HUM_THRESHOLD = 65

# ---------------- CALLBACKS ---------------- #

def on_connect(client, userdata, flags, rc, properties=None):
    print("Connected to MQTT Broker")
    # 🔴 IMPORTANT: use UNIQUE topics
    client.subscribe("harshad/sensor/temperature")
    client.subscribe("harshad/sensor/humidity")

def on_message(client, userdata, msg):
    # Safe decode (prevents UnicodeDecodeError)
    payload = msg.payload.decode("utf-8", errors="ignore").strip()

    if payload == "":
        return  # ignore empty/binary messages

    try:
        value = float(payload)
    except ValueError:
        print(f"Ignored non-numeric message: {payload}")
        return

    if msg.topic == "harshad/sensor/temperature":
        print(f"Temperature: {value} °C")
        if value > TEMP_THRESHOLD:
            print("⚠ ALERT: High Temperature")

    elif msg.topic == "harshad/sensor/humidity":
        print(f"Humidity: {value} %")
        if value > HUM_THRESHOLD:
            print("⚠ ALERT: High Humidity")

# ---------------- CLIENT SETUP ---------------- #

client = mqtt.Client(
    client_id="Harshad_Subscriber",
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2
)

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_forever()
