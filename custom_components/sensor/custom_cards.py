"""
Get updates about your custom_cards.

For more details about this component, please refer to the documentation at
https://github.com/custom-components/sensor.custom_cards
"""
from datetime import timedelta
from homeassistant.helpers.entity import Entity
import custom_components.custom_cards as cc

__version__ = '0.0.5'

DEPENDENCIES = ['custom_cards']

SCAN_INTERVAL = timedelta(seconds=60)

def setup_platform(hass, config, add_devices, discovery_info=None):
    """Create the sensor"""
    www_dir = str(hass.config.path("www/"))
    lovelace_config = str(hass.config.path("ui-lovelace.yaml"))
    add_devices([CustomCards(www_dir, lovelace_config)])

class CustomCards(Entity):
    """Representation of a Sensor."""

    def __init__(self, www_dir, lovelace_config):
        """Initialize the sensor."""
        self._state = None
        self._attributes = None
        self._www_dir = www_dir
        self._lovelace_config = lovelace_config
        self.update()

    def update(self):
        """Method to update sensor value"""
        attr = []
        cards = cc.get_installed_cards(self._www_dir, self._lovelace_config)
        if cards != None:
            for card in cards:
                localversion = cc.get_local_version(card, self._lovelace_config)
                remoteversion = cc.get_remote_version(card)
                value = {
                    "name": card,
                    "update": str(localversion != False and remoteversion != False and remoteversion != localversion),
                    "version": str(remoteversion),
                    "installed": str(localversion),
                }
                attr.append(value)
        self._attributes = attr
        self._state = 'Active'

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Custom_card Tracker'

    @property
    def state(self):
        """Return the state of the sensor."""
        return 'Active'

    @property
    def device_state_attributes(self):
        """Return attributes for the sensor."""
        return {
            'attr': self._attributes
            }
