
from ota import OTAUpdater
from wifi_config import SSID, PASSWORD

firmware_url = "https://raw.githubusercontent.com/bd4inside/OTA_BassNeopixels/"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")

ota_updater.download_and_install_update_if_available()

print("Works")
