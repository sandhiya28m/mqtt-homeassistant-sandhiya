# mqtt-homeassistant-sandhiya
Home Assistant – MQTT Integration with Python Publisher

This project demonstrates how to integrate a Python MQTT publisher with Home Assistant running in VirtualBox using a Mosquitto MQTT Broker. Sensor data such as temperature, humidity, and light is published from Python and auto-discovered inside Home Assistant.

Project Overview

This project includes:

Home Assistant OS running in VirtualBox

Mosquitto MQTT Broker with secure authentication

Python publisher script using the paho.mqtt.client library

MQTT Discovery for auto-creating entities in Home Assistant

Real-time sensor updates visible in Home Assistant Dashboard

Architecture

Python Publisher → MQTT Broker (Mosquitto) → Home Assistant → Dashboard

1. Home Assistant OS Setup (VirtualBox)

Installed Home Assistant OS inside VirtualBox.

Configured networking (Bridged / NAT) to enable communication.

Verified connectivity between Python publisher, Home Assistant, and MQTT broker.

2. Mosquitto MQTT Broker Configuration

Installed Mosquitto locally.

Created a secure username and password (not included here).

Verified that the broker accepts connections from:

Python publisher script

Home Assistant MQTT integration

3. Python Publisher (publisher.py)

Developed using the paho.mqtt.client library.

Publishes JSON sensor data every 5 seconds:

Temperature

Humidity

Light

MQTT Topics:

home/sandhiya-2025/sensor/temperature
home/sandhiya-2025/sensor/humidity
home/sandhiya-2025/sensor/light

Discovery topics:

homeassistant/sensor/<unique_id>/config

4. Home Assistant MQTT Discovery

Enabled MQTT integration in Home Assistant.

Published retained discovery configuration messages with:

Name

Device class

Unit of measurement

Unique ID

Home Assistant automatically created sensor entities without YAML configuration.

5. Data Verification

Using mosquitto_sub:

Confirmed that Python is publishing correct values.

Using Home Assistant MQTT Listener:

Verified incoming JSON payloads.

Confirmed that values update in real-time.

6. Auto-Discovered Entities

Home Assistant automatically created:

sensor.sandhiya_temperature

sensor.sandhiya_humidity

sensor.sandhiya_light
