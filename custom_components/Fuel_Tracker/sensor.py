"""
Calendar Coordinates Generator for Home Assistant
------------------------------------------------------------
%   Description: Script for generating coordinates (X,Y) based on the monthly days of a calendar
%   Author: J.G.Aguado
%   Date of creation: 08/04/2023
------------------------------------------------------------
"""

import logging

import datetime
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import CONF_API_KEY, CONF_NAME
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity import Entity
import voluptuous as vol

_LOGGER = logging.getLogger(__name__)

DOMAIN = "sensor"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required("a0"): cv.string,
        vol.Required("b0"): cv.string,
        vol.Required("a1"): cv.string,
        vol.Required("b1"): cv.string,
        vol.Required(CONF_NAME): cv.string,
    }
)


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the fuel tracker sensor."""

    _LOGGER.info("init sensor")
    name = config.get(CONF_NAME)
    a0 = config.get("a0")
    b0 = config.get("b0")
    a1 = config.get("a1")
    b1 = config.get("b1")

    fn = MonthData(name, a0, b0, a1, b1)

    if not fn:
        _LOGGER.error("Unable to create the Calendar sensor")
        return

    add_entities([MonthSensor(hass, fn)], True)


class MonthSensor(Entity):
    def __init__(self, hass, fn):
        self._hass = hass
        self.data = fn

    @property
    def name(self):
        """Return the name of the sensor."""
        return "{}".format(self.data.name)

    @property
    def state(self):
        """Return the state of the device."""
        return self.data.attr

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return self.data.attr

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return "N/A"
        
    @property
    def icon(self):
        return "mdi-calendar-month"
    
    def update(self):
        self.data.get_month()


class MonthData:
    def __init__(self, name, a0, b0, a1, b1):
        self.name = name
        self.attr = {}
        self.x = [a0, b0]
        self.y = [a1, b1]
        
        self.get_month()

    def get_month(self):
        calendar = {}
        if month is None:
            month = datetime.date.today().month
        year = datetime.date.today().year
        row = 0
        for day in range(1, 32):
            try:
                date = datetime.date(year, month, day)
                day_of_week = date.weekday()
                calendar[day] = [day_of_week*self.x[0] + self.x[1], row*self.y[0] + self.y[1]]
                if day_of_week > 5:
                    row += 1
            except ValueError:
                break

        self.attr = calendar
        
