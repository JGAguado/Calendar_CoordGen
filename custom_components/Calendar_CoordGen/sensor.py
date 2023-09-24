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
        vol.Required("ax"): cv.string,
        vol.Required("bx"): cv.string,
        vol.Required("ay"): cv.string,
        vol.Required("by"): cv.string,
        vol.Required(CONF_NAME): cv.string,
    }
)


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the fuel tracker sensor."""

    _LOGGER.info("init sensor")
    name = config.get(CONF_NAME)
    ax = config.get("ax")
    bx = config.get("bx")
    ay = config.get("ay")
    by = config.get("by")

    fn = MonthData(name, ax, bx, ay, by)

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
        return True

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return self.data.attr

        
    @property
    def icon(self):
        return "mdi:calendar-month"
    
    def update(self):
        self.data.get_month()


class MonthData:
    def __init__(self, name, ax, bx, ay, by):
        self.name = name
        self.attr = {}
        self.coeffs = [int(ax), int(bx), int(ay), int(by)]
        
        self.get_month()

    def get_month(self):
        calendar = {}
        month = datetime.date.today().month
        year = datetime.date.today().year
        next_month = month + 1
        next_year = year
        if next_month >12:
            next_month = 1
            next_year += 1
        [ax, bx, ay, by] = self.coeffs
        row = 0
        days_in_month = (datetime.date(next_year, next_month, 1) - datetime.date(year, month, 1)).days
        # print(days_in_month)
        for day in range(1, days_in_month + 1):
            date = datetime.date(year, month, day)
            day_of_week = date.weekday()
            calendar[day] = [day_of_week*ax + bx, row*ay + by]
            if day_of_week > 5:
                row += 1

        self.attr['days'] = calendar
        
