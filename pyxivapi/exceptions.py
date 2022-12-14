"""
MIT License

Copyright (c) 2019 Lethys

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

__all__ = (
    "XIVAPIForbidden",
    "XIVAPIBadRequest",
    "XIVAPINotFound",
    "XIVAPIServiceUnavailable",
    "XIVAPIInvalidLanguage",
    "XIVAPIInvalidIndex",
    "XIVAPIInvalidColumns",
    "XIVAPIInvalidFilter",
    "XIVAPIInvalidWorlds",
    "XIVAPIInvalidDatacenter",
    "XIVAPIError",
    "XIVAPIInvalidAlgo",
)


class XIVAPIForbidden(Exception):
    """
    XIVAPI Forbidden Request error
    """

    pass


class XIVAPIBadRequest(Exception):
    """
    XIVAPI Bad Request error
    """

    pass


class XIVAPINotFound(Exception):
    """
    XIVAPI not found error
    """

    pass


class XIVAPIServiceUnavailable(Exception):
    """
    XIVAPI service unavailable error
    """

    pass


class XIVAPIInvalidLanguage(Exception):
    """
    XIVAPI invalid language error
    """

    pass


class XIVAPIInvalidIndex(Exception):
    """
    XIVAPI invalid index error
    """

    pass


class XIVAPIInvalidColumns(Exception):
    """
    XIVAPI invalid columns error
    """

    pass


class XIVAPIInvalidFilter(Exception):
    """
    XIVAPI invalid filter error
    """

    pass


class XIVAPIInvalidWorlds(Exception):
    """
    XIVAPI invalid world(s) error
    """

    pass


class XIVAPIInvalidDatacenter(Exception):
    """
    XIVAPI invalid datacenter error
    """

    pass


class XIVAPIError(Exception):
    """
    XIVAPI error
    """

    pass


class XIVAPIInvalidAlgo(Exception):
    """
    Invalid String Algo
    """

    pass
