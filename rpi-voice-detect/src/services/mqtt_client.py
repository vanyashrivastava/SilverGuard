from paho.mqtt import client as mqtt

class MQTTClient:
    def __init__(self, broker, port, topic):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.client = mqtt.Client()

    def connect(self):
        """Connect to the MQTT broker."""
        try:
            self.client.connect(self.broker, self.port, 60)
            print(f"Connected to MQTT broker at {self.broker}:{self.port}")
        except Exception as e:
            print(f"Failed to connect to MQTT broker: {e}")

    def publish(self, message):
        """Publish a message to the specified topic."""
        try:
            self.client.publish(self.topic, message)
            print(f"Message published to {self.topic}: {message}")
        except Exception as e:
            print(f"Failed to publish message: {e}")

    def subscribe(self, on_message):
        """Subscribe to the specified topic."""
        self.client.subscribe(self.topic)
        self.client.on_message = on_message
        print(f"Subscribed to topic: {self.topic}")

    def loop_forever(self):
        """Start the MQTT client loop."""
        self.client.loop_forever()