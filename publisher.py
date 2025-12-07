import time
import json
import paho.mqtt.client as mqtt

# User details
student_name = "Sandhiya M"
unique_id = "42130410"

# MQTT broker details
mqtt_broker = "localhost"   # or your broker IP
mqtt_port = 1883
mqtt_user = "sandhiya"
mqtt_password = "Sandhiya@28"

# Base topics
base_topic = "home/sandhiya-2025/sensor"
discovery_prefix = "homeassistant"
base_id = "sandhiya_2025"

# Create MQTT client
client = mqtt.Client()
client.username_pw_set(mqtt_user, mqtt_password)

try:
    client.connect(mqtt_broker, mqtt_port, 60)
    print(f"Connected to MQTT broker at {mqtt_broker}:{mqtt_port}")
except Exception as e:
    print("Failed to connect to broker:", e)
    exit()

client.loop_start()

# Define sensors
sensors = {
    "temperature": {"unit": "°C", "device_class": "temperature"},
    "humidity": {"unit": "%", "device_class": "humidity"},
    "light": {"unit": "lx", "device_class": "illuminance"}
}

# Publish discovery config for each sensor
for sensor_type, props in sensors.items():
    config_topic = f"{discovery_prefix}/sensor/{base_id}_{sensor_type}/config"
    config_payload = {
        "name": f"Sandhiya {sensor_type.capitalize()}",
        "state_topic": f"{base_topic}/{sensor_type}",
        "unit_of_measurement": props["unit"],
        "device_class": props["device_class"],
        "unique_id": f"{base_id}_{sensor_type}"
    }
    client.publish(config_topic, json.dumps(config_payload), retain=True)

# Publish sensor values in a loop
while True:
    temperature = 25
    humidity = 60
    light = 24

    client.publish(f"{base_topic}/temperature", temperature)
    client.publish(f"{base_topic}/humidity", humidity)
    client.publish(f"{base_topic}/light", light)

    print("Published:")
    print(f"Temperature = {temperature}")
    print(f"Humidity = {humidity}")
    print(f"Light = {light}")
    print("----------------------------")

    time.sleep(5)