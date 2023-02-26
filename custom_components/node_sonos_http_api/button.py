import logging

import aiohttp

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.components.button import ButtonEntity

_LOGGER = logging.getLogger(__name__)


class NodeSonosHttpApiClient:
    def __init__(self, host):
        self.host = host.rstrip("/")

    async def async_get_presets(self):
        """Get a list of presets."""
        return await self.async_get_data("preset")

    async def async_get_data(self, suffix=""):
        """Make a GET request to the URL + suffix and return the response as a dictionary."""
        url = f"{self.host}/{suffix.lstrip('/')}"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status != 200:
                        _LOGGER.error(
                            "Failed to get data from Node-Sonos API: %s",
                            response.reason,
                        )
                        return {}
                    data = await response.json()
                    return data
        except aiohttp.ClientError as error:
            _LOGGER.error("Error getting data from Node-Sonos API: %s", error)
            return {}

    async def async_activate_preset(self, preset):
        """Activate the preset."""
        return await self.async_get_data(f"preset/{preset}")

    async def async_validate_connection(self):
        """Make a request against the host URL + '/zones' to validate the connection."""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.host}/zones") as response:
                    if response.status != 200:
                        _LOGGER.error(
                            "Failed to validate connection to Node-Sonos API: %s",
                            response.reason,
                        )
                        return False
                    data = await response.json()
                    if not isinstance(data, list):
                        _LOGGER.error(
                            "Failed to validate connection to Node-Sonos API: Invalid JSON response"
                        )
                        return False
                    return True
        except aiohttp.ClientError as error:
            _LOGGER.error("Error validating connection to Node-Sonos API: %s", error)
            return False


class NodeSonosPresetButton(ButtonEntity):
    _attr_has_entity_name = True
    _attr_name = None

    def __init__(self, api_client: NodeSonosHttpApiClient, preset: str):
        self.preset = preset
        self.api_client = api_client
        # replace camelCase with spaces and capitalize
        name = self.preset[0].upper()
        for char in self.preset[1:]:
            if char.isupper():
                name += " "
            name += char

        # replace underscores with spaces
        name = name.replace("_", " ")
        self._attr_name = name

    async def async_press(self) -> None:
        await self.api_client.async_activate_preset(self.preset)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> bool:
    """Set up the Node-Sonos integration."""
    host = config_entry.data["host"]
    api_client = NodeSonosHttpApiClient(host)
    if await api_client.async_validate_connection():
        _LOGGER.debug("Connection to Node-Sonos API successful")
        presets = await api_client.async_get_presets()
        _LOGGER.debug("Got presets from Node-Sonos API: %s", presets)
        async_add_entities(
            NodeSonosPresetButton(api_client, preset) for preset in presets
        )

        return True
    else:
        _LOGGER.error("Failed to validate connection to Node-Sonos API")
        return False
