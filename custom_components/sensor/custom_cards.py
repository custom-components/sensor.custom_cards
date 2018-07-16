"""
Get updates about your custom_cards.

For more details about this component, please refer to the documentation at
https://github.com/custom-components/sensor.custom_cards
"""
import logging
import time
from datetime import timedelta
from homeassistant.helpers.entity import Entity
from custom_components.custom_cards import DATA_CC, SIGNAL_SENSOR_UPDATE
from homeassistant.helpers.dispatcher import async_dispatcher_connect
import custom_components.custom_cards as cc

__version__ = '0.0.6'

DEPENDENCIES = ['custom_cards']

SCAN_INTERVAL = timedelta(seconds=60)
_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_devices, discovery_info=None):
    """Create the sensor"""
    _LOGGER.info('Sensor %s version %s is starting', __version__, __name__.split('.')[1])
    add_devices([CustomCards(hass)])

class CustomCards(Entity):
    """Representation of a Sensor."""

    def __init__(self, hass):
        """Initialize the sensor."""
        self.hass = hass
        self._state = time.time()
        self._attributes = self.hass.data[DATA_CC]

    async def async_added_to_hass(self):
        """Register callbacks."""
        async_dispatcher_connect(
            self.hass, SIGNAL_SENSOR_UPDATE, self._update_callback)

    def _update_callback(self):
        """Method to update sensor value"""
        self._attributes = self.hass.data[DATA_CC]
        self._state = time.time()
        _LOGGER.debug('Sensor update for signal %s', self._attributes)
        self.async_schedule_update_ha_state(True)

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Custom Card Tracker'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def device_state_attributes(self):
        """Return attributes for the sensor."""
        return self._attributes