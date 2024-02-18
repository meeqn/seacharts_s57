from __future__ import annotations

from abc import ABC
from dataclasses import dataclass, field

from shapely import geometry as geo

from seacharts.layers.layer import Layer, ZeroDepth, SingleDepth, MultiDepth


@dataclass
class Regions(Layer, ABC):
    geometry: geo.MultiPolygon = field(default_factory=geo.MultiPolygon)


@dataclass
class ZeroDepthRegions(Regions, ZeroDepth, ABC):
    pass


@dataclass
class SingleDepthRegions(Regions, SingleDepth, ABC):
    @property
    def name(self) -> str:
        return self.__class__.__name__ + f"{self.depth}m"


@dataclass
class MultiDepthRegions(Regions, MultiDepth, ABC):
    pass


@dataclass
class Seabed(SingleDepthRegions):
    z_order = -300


@dataclass
class Land(ZeroDepthRegions):
    z_order = -100


@dataclass
class Shore(ZeroDepthRegions):
    z_order = -200
