# Node Sonos HTTP API Home Assistant ingetration

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![hacs][hacsbadge]][hacs]
![Project Maintenance][maintenance-shield]
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

[![Discord][discord-shield]][discord]
[![Community Forum][forum-shield]][forum]

_Integration to integrate with [node-sonos-http-api][https://github.com/jishi/node-sonos-http-api]._

It allows you to trigger presets defined in `node-sonos-http-api`from home assistant, as it creates a button entity for every preset defined in node-sonos-http-api.

**This integration will set up the following platforms.**

| Platform | Description                      |
| -------- | -------------------------------- |
| `button` | Allows you to activate a preset. |

## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
1. If you do not have a `custom_components` directory (folder) there, you need to create it.
1. In the `custom_components` directory (folder) create a new folder called `node_sonos_http_api`.
1. Download _all_ the files from the `custom_components/node_sonos_http_api/` directory (folder) in this repository.
1. Place the files you downloaded in the new directory (folder) you created.
1. Restart Home Assistant
1. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Integration blueprint"

## Configuration is done in the UI

<!---->

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

---

[integration_blueprint]: https://github.com/hco/ha-node-sonos-http-api/
[commits-shield]: https://img.shields.io/github/commit-activity/y/hco/ha-node-sonos-http-api.svg?style=for-the-badge
[commits]: https://github.com/hco/ha-node-sonos-http-api/commits/main
[hacs]: https://github.com/hacs/integration
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[license-shield]: https://img.shields.io/github/license/hco/ha-node-sonos-http-api.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-Hans--Christian%20Otto-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/hco/ha-node-sonos-http-api.svg?style=for-the-badge
[releases]: https://github.com/hco/ha-node-sonos-http-api/releases
