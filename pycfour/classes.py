
from dataclasses import dataclass, field


@dataclass
class Calculation:
    calc_id: int = 0
    filepath: str = ""
    comment: str = ""
    e_scf: float = 0.
    e_ccsd: float = 0.
    e_ccsd_t: float = 0.
    e_ccsdt: float = 0.
    e_t: float = 0.
    e_zpe: float = 0.
    e_dboc: float = 0.
    e_rel: float = 0.
    frequencies: List[float] = field(default_factory=list)
    


@dataclass

    