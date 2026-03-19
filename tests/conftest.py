import sys
from unittest.mock import MagicMock

gsplat_mock = MagicMock()
sys.modules["gsplat"] = gsplat_mock
sys.modules["gsplat.rendering"] = gsplat_mock.rendering
