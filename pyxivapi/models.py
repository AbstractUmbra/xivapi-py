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


from typing import ClassVar, List

from .exceptions import XIVAPIInvalidFilter


class Filter:
    """
    Model class for DQL filters
    """

    comparisons: ClassVar[List[str]] = ["gt", "gte", "lt", "lte"]

    def __init__(self, field: str, comparison: str, value: int) -> None:
        comparison = comparison.lower()

        if comparison not in self.comparisons:
            raise XIVAPIInvalidFilter(f'"{comparison}" is not a valid DQL filter comparison.')

        self.field = field
        self.comparison = comparison
        self.value = value


class Sort:
    """
    Model class for sort field
    """

    def __init__(self, field: str, ascending: bool) -> None:
        self.field = field
        self.ascending = ascending
