"""Integrity and elementary sanity checks, NOT verification of the analytic proof."""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json, math, sys

def require(ok, message):
    if not ok:
        raise ValueError(message)

def verify(root):
    manifest = json.loads((root/'MANIFEST.json').read_text())
    for row in manifest['files']:
        p = root/row['path']
        require(p.is_file(), 'Missing payload: '+row['path'])
        require(hashlib.sha256(p.read_bytes()).hexdigest() == row['sha256'], 'Digest mismatch: '+row['path'])
        require(p.stat().st_size == row['size_bytes'], 'Size mismatch: '+row['path'])
    return len(manifest['files'])

def checks():
    # General symmetric quadratic-form expansion in two formal density variables.
    for a in range(-4,5):
        for b in range(-4,5):
            lhs = F(b*b-a*a,2)
            rhs = a*(b-a)+F((b-a)**2,2)
            require(lhs == rhs, 'Quadratic-form expansion')
    # L2-normalized dilation: gradient exponent -2; quartic Coulomb exponent -1.
    require(2*(-F(3,2))+3 == 0, 'L2 normalization exponent')
    require(2*(-F(3,2)-1)+3 == -2, 'Kinetic scaling')
    require(4*(-F(3,2))+6-1 == -1, 'Quartic Coulomb scaling')
    require(2*(-F(3,2))+6-1 == 2, 'Quadratic Coulomb scaling')
    require(-2+1 == -1, 'Effective quartic parameter qR')
    require(math.isclose(4*math.pi/(2*math.pi)*0.5,1), 'Eigenstate norm')
    require(math.isclose(-4*math.pi*(math.pi/2),-2*math.pi**2), 'Dilation derivative')
    require(math.pi**2/3-1 > 0, 'Degree-two multiplier sign')
    # A deliberate wrong expansion must be rejected by the same predicate.
    rejected=False
    try:
        require(F(9-1,2) == 1*(3-1)-F((3-1)**2,2), 'Deliberate wrong sign')
    except ValueError:
        rejected=True
    require(rejected, 'Negative control failed')
    return '81 quadratic identities, 8 scaling/normalization/mode checks, wrong-sign rejection'

if __name__ == '__main__':
    root=Path(__file__).resolve().parents[1]
    print(json.dumps({'payload_files':verify(root), 'sanity':checks(), 'optimized':not __debug__, 'boundary':'Finite sanity and integrity only; no analytic-proof verification.'}))
