import pytest

from utils.distance import barcode_distance

testdata = [
    ('AAAA', 'AAAA', 0),
    ('AAAA', 'AAAT', 1),
    ('AAAA','AAAAT',0),
    ('AAAAT','AAAA',1),
    ('ATCGT', 'TATCG', 5),
    ('TATCG', 'ATCGT', 5),
    ('ATCGT', 'TATCGG', 5),
    ('TATCGG', 'ATCGT', 6),
    ('ATCGT-AAAAA', 'TATCGG-AAAAA', 5),
    ('TATCGG-AAAAA', 'ATCGT-AAAAA', 6),
    ('AAAAA-ATCGT', 'AAAAA-TATCGG', 5),
    ('AAAAA-TATCGG', 'AAAAA-ATCGT', 6),
    ('AAAA', 'AAAA-TTTT', 0),
    ('AAAA-TTTT', 'AAAA', 4),
    ('AAAA-TTTT', 'AAAA-TTTT', 0),
    ('AAA-TTT', 'AAAA-TTTT', 0),
    ('AAAA-TTTT', 'AAA-TTT', 2),
    ('AA-TTTT', 'AAAA-TTTT', 0),
    ('AAAA-TTTT', 'AA-TTTT', 2),
    ('A-TTTT', 'AAAA-TTTT', 0),
    ('AAAA-TTTT', 'A-TTTT', 3),
    ('TTTT', 'AAAA-TTTT', 4),
    ('AAAA-TTTT', 'TTTT', 8),
    ('AAAT-TTTA', 'AAAA-TTTT', 2),
    ('AAAA-TTTT', 'AAAT-TTTA', 2)
]


@pytest.mark.parametrize("target,other,expected", testdata)
def test_barcode_distance(target, other, expected):
    assert barcode_distance(target, other) == expected
