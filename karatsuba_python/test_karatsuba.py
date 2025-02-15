from main import karatsuba

def test_numeros_pequenos():
    assert karatsuba(0, 0) == 0
    assert karatsuba(0, 5) == 0
    assert karatsuba(5, 0) == 0
    assert karatsuba(1, 1) == 1
    assert karatsuba(2, 3) == 6
    assert karatsuba(4, 5) == 20
    assert karatsuba(9, 9) == 81
    assert karatsuba(10, 10) == 100
    assert karatsuba(12, 13) == 156
    assert karatsuba(15, 15) == 225

def test_numeros_medios():
    assert karatsuba(123, 456) == 56088
    assert karatsuba(999, 999) == 998001
    assert karatsuba(1000, 1000) == 1_000_000
    assert karatsuba(1234, 5678) == 7_006_652
    assert karatsuba(9876, 5432) == 53_646_432
    assert karatsuba(1111, 1111) == 1_234_321
    assert karatsuba(2222, 3333) == 7_405_926
    assert karatsuba(4444, 5555) == 24_686_420
    assert karatsuba(12345, 6789) == 83_810_205
    assert karatsuba(54321, 12345) == 670_592_745

def test_numeros_grandes():
    assert karatsuba(123456, 654321) == 80_779_853_376
    assert karatsuba(999999, 999999) == 999_998_000_001
    assert karatsuba(1000000, 1000000) == 1_000_000_000_000
    assert karatsuba(1234567, 7654321) == 9_449_772_114_007
    assert karatsuba(9876543, 1234567) == 12_193_254_061_881
    assert karatsuba(1111111, 1111111) == 1_234_567_654_321
    assert karatsuba(2222222, 3333333) == 7_407_405_925_926
    assert karatsuba(4444444, 5555555) == 24_691_353_086_420
    assert karatsuba(12345678, 87654321) == 1_082_152_022_374_638
    assert karatsuba(98765432, 12345678) == 1_219_326_221_002_896

def test_karatsuba_com_numeros_de_tamanhos_diferentes():
    assert karatsuba(123, 4567) == 561_741
    assert karatsuba(1234, 567) == 699_678
    assert karatsuba(12345, 67) == 827_115
    assert karatsuba(123456, 7) == 864_192
    assert karatsuba(1, 999999) == 999_999
    assert karatsuba(999999, 1) == 999_999
    assert karatsuba(1000000, 1) == 1_000_000
    assert karatsuba(1, 1000000) == 1_000_000
    assert karatsuba(123456789, 987654321) == 121_932_631_112_635_269
    assert karatsuba(987654321, 123456789) == 121_932_631_112_635_269

def test_karatsuba_com_numeros_grandes_e_zeros_no_meio():
    assert karatsuba(102030, 405060) == 41_328_271_800
    assert karatsuba(1002003, 4005006) == 4_013_028_027_018
    assert karatsuba(12300456, 78900567) == 970_512_952_758_552
    assert karatsuba(100000001, 200000002) == 20_000_000_400_000_002
    assert karatsuba(999000999, 888000888) == 887_113_774_224_887_112
