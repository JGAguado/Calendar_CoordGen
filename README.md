[![hacs][hacs-shield]][hacs]
[![GitHub Release][releases-shield]][releases]
[![License][license-shield]](LICENSE)

[![Project Maintenance][maintenance-shield]][maintenance]
[![BuyMeCoffee][buymecoffee-shield]][buymecoffee]

# Fuel Tracker

This integration generates an entity whose attributes are the days of the current month with coordinates (x, y) as properties for each day. 

This can be used later on to pass an ESPHome device with an e-Ink display, the array of monthly days with the coordinates in order to plot them correctly.


# Configuration

The integration requires to get the coefficient a0, b0 for the x axis and the a1, b1 for the y axis.

Parameter | Value(example)
-- | --
a0 | `10`
b0 | `200`
a1 | `15`
b1 | `150`


## Example
On the configuration.yml :

```yaml
sensor:
  - platform: calendar_cg
    name: Current_month
    a0: 10
    b0: 200
    a1: 15
    b1: 150
```





[hacs-shield]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[hacs]: https://github.com/custom-components/hacs

[releases-shield]: https://img.shields.io/github/release/JGAguado/Calendar_CoordGen.svg?style=for-the-badge
[releases]: https://github.com/JGAguado/Calendar_CoordGen/releases

[license-shield]: https://img.shields.io/github/license/JGAguado/Calendar_CoordGen.svg?style=for-the-badge

[maintenance-shield]: https://img.shields.io/badge/maintainer-J.%20G.%20Aguado-blue.svg?style=for-the-badge
[maintenance]: https://github.com/JGAguado

[buymecoffee-shield]: https://img.shields.io/badge/buy%20me%20a%20coffee-support-yellow.svg?style=for-the-badge
[buymecoffee]: https://www.buymeacoffee.com/J.G.Aguado

