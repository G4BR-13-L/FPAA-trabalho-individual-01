fn karatsuba(x: usize, y: usize) -> usize{
    if x < 10 || y < 10 {
        return x * y;
    }

    let n:usize = max_numero_digitos(x,y);
    let m = n / 2;

    let (alta1, baixa1) = dividir(x, m);
    let (alta2, baixa2) = dividir(y, m);

    let z0 = karatsuba(baixa1, baixa2);
    let z1 = karatsuba(baixa1 + alta1, baixa2 + alta2);
    let z2 = karatsuba(alta1, alta2);

    let resultado = (z2 * 10_usize.pow(2 * m as u32)) + ((z1 - z2 - z0) * 10_usize.pow(m as u32)) + z0;
    return resultado;
}

fn dividir(num:usize, m:usize) -> (usize, usize){
    let divisor = 10_usize.pow(m as u32);

    let alta = num / divisor;
    let baixa = num % divisor;
    return (alta, baixa);
}

// Retorna o maior numero de digitos entre 2 numeros
fn max_numero_digitos(x:usize, y:usize) -> usize{
    let x_digitos = contar_digitos(x);
    let y_digitos = contar_digitos(y);

    if x_digitos > y_digitos {
        return x_digitos;
    }

    y_digitos

}

//conta a quantidade de digitos de um numero
fn contar_digitos(num:usize) -> usize{
    let mut contagem = 0;
    let mut n = num.clone();

    if n == 0 {
        return 1
    }

    while n != 0 {
        n /= 10;
        contagem += 1;
    }

    contagem
}

fn main() {
    println!("{}", karatsuba(2,2));
    println!("{}", karatsuba(3,3));
    println!("{}", karatsuba(4,4));
    println!("{}", karatsuba(10,10));
    println!("{}", karatsuba(3,5));
    println!("{}", karatsuba(1000,1000));
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn testar_karatsuba_com_numeros_pequenos() {
        assert_eq!(karatsuba(0, 0), 0);
        assert_eq!(karatsuba(0, 5), 0);
        assert_eq!(karatsuba(5, 0), 0);
        assert_eq!(karatsuba(1, 1), 1);
        assert_eq!(karatsuba(2, 3), 6);
        assert_eq!(karatsuba(4, 5), 20);
        assert_eq!(karatsuba(9, 9), 81);
        assert_eq!(karatsuba(10, 10), 100);
        assert_eq!(karatsuba(12, 13), 156);
        assert_eq!(karatsuba(15, 15), 225);
    }

    #[test]
    fn testar_karatsuba_com_numeros_medios() {
        assert_eq!(karatsuba(123, 456), 56088);
        assert_eq!(karatsuba(999, 999), 998001);
        assert_eq!(karatsuba(1000, 1000), 1_000_000);
        assert_eq!(karatsuba(1234, 5678), 7_006_652);
        assert_eq!(karatsuba(9876, 5432), 53_646_432);
        assert_eq!(karatsuba(1111, 1111), 1_234_321);
        assert_eq!(karatsuba(2222, 3333), 7_405_926);
        assert_eq!(karatsuba(4444, 5555), 24_686_420);
        assert_eq!(karatsuba(12345, 6789), 83_810_205);
        assert_eq!(karatsuba(54321, 12345), 670_592_745);
    }

    #[test]
    fn testar_karatsuba_com_numeros_grandes() {
        assert_eq!(karatsuba(123456, 654321), 80_779_853_376);
        assert_eq!(karatsuba(999999, 999999), 999_998_000_001);
        assert_eq!(karatsuba(1000000, 1000000), 1_000_000_000_000);
        assert_eq!(karatsuba(1234567, 7654321), 9_449_772_114_007);
        assert_eq!(karatsuba(9876543, 1234567), 12_193_254_061_881);
        assert_eq!(karatsuba(1111111, 1111111), 1_234_567_654_321);
        assert_eq!(karatsuba(2222222, 3333333), 7_407_405_925_926);
        assert_eq!(karatsuba(4444444, 5555555), 24_691_353_086_420);
        assert_eq!(karatsuba(12345678, 87654321), 1_082_152_022_374_638);
        assert_eq!(karatsuba(98765432, 12345678), 1_219_326_221_002_896);
    }

    #[test]
    fn testar_karatsuba_com_numeros_de_tamanhos_diferentes() {
        assert_eq!(karatsuba(123, 4567), 561_741);
        assert_eq!(karatsuba(1234, 567), 699_678);
        assert_eq!(karatsuba(12345, 67), 827_115);
        assert_eq!(karatsuba(123456, 7), 864_192);
        assert_eq!(karatsuba(1, 999999), 999_999);
        assert_eq!(karatsuba(999999, 1), 999_999);
        assert_eq!(karatsuba(1000000, 1), 1_000_000);
        assert_eq!(karatsuba(1, 1000000), 1_000_000);
        assert_eq!(karatsuba(123456789, 987654321), 121_932_631_112_635_269);
        assert_eq!(karatsuba(987654321, 123456789), 121_932_631_112_635_269);
    }

    #[test]
    fn testar_karatsuba_com_numeros_grandes_e_zeros_no_meio() {
        assert_eq!(karatsuba(102030, 405060), 41_328_271_800);
        assert_eq!(karatsuba(1002003, 4005006), 4_013_028_027_018);
        assert_eq!(karatsuba(12300456, 78900567), 970_512_952_758_552);
        assert_eq!(karatsuba(100000001, 200000002), 20_000_000_400_000_002);
        assert_eq!(karatsuba(999000999, 888000888), 887_113_774_224_887_112);
    }
}

