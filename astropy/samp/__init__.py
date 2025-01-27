# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
This subpackage provides classes to communicate with other applications via the
`Simple Application Messaging Protocol (SAMP)
<http://www.ivoa.net/documents/SAMP/>`_.

Before integration into Astropy it was known as
`SAMPy <https://pypi.org/project/sampy/>`_, and was developed by Luigi Paioro
(INAF - Istituto Nazionale di Astrofisica).
"""

from astropy import config as _config

from .client import *  # noqa: F401, F403
from .constants import *  # noqa: F401, F403
from .errors import *  # noqa: F401, F403
from .hub import *  # noqa: F401, F403
from .hub_proxy import *  # noqa: F401, F403
from .integrated_client import *  # noqa: F401, F403
from .utils import *  # noqa: F401, F403


class Conf(_config.ConfigNamespace):
    """
    Configuration parameters for `astropy.samp`.
    """

    use_internet = _config.ConfigItem(
        True,
        "Whether to allow `astropy.samp` to use "
        "the internet, if available.",
        aliases=['astropy.samp.utils.use_internet'])

    n_retries = _config.ConfigItem(10,
        "How many times to retry communications when they fail")


conf = Conf()
