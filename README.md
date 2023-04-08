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
Output generated dictionary :

```
{1: [250, 150], 2: [260, 150], 3: [200, 165], 4: [210, 165], 5: [220, 165], 6: [230, 165], 7: [240, 165], 8: [250, 165], 9: [260, 165], 10: [200, 180], 11: [210, 180], 12: [220, 180], 13: [230, 180], 14: [240, 180], 15: [250, 180], 16: [260, 180], 17: [200, 195], 18: [210, 195], 19: [220, 195], 20: [230, 195], 21: [240, 195], 22: [250, 195], 23: [260, 195], 24: [200, 210], 25: [210, 210], 26: [220, 210], 27: [230, 210], 28: [240, 210], 29: [250, 210], 30: [260, 210]}

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

