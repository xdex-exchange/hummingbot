from decimal import Decimal

from pydantic import ConfigDict, Field, SecretStr

from hummingbot.client.config.config_data_types import BaseConnectorConfigMap
from hummingbot.core.data_type.trade_fee import TradeFeeSchema

CENTRALIZED = True

EXAMPLE_PAIR = "BTC-USD"

DEFAULT_FEES = TradeFeeSchema(
    maker_percent_fee_decimal=Decimal("0.0001"),
    taker_percent_fee_decimal=Decimal("0.0005"),
)


def clamp(value, minvalue, maxvalue):
    return max(minvalue, min(value, maxvalue))


class DydxV4PerpetualTestnetConfigMap(BaseConnectorConfigMap):
    connector: str = "dydx_v4_perpetual_testnet"
    dydx_v4_perpetual_testnet_secret_phrase: SecretStr = Field(
        default=...,
        json_schema_extra={
            "prompt": "Enter your dydx v4 secret_phrase(24 words)",
            "is_secure": True,
            "is_connect_key": True,
            "prompt_on_new": True,
        },
    )
    dydx_v4_perpetual_testnet_chain_address: SecretStr = Field(
        default=...,
        json_schema_extra={
            "prompt": "Enter your dydx v4 chain address ( starts with 'dydx' )",
            "is_secure": True,
            "is_connect_key": True,
            "prompt_on_new": True,
        },
    )
    model_config = ConfigDict(title="dydx_v4_perpetual_testnet")


KEYS = DydxV4PerpetualTestnetConfigMap.model_construct()
