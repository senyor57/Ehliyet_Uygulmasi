def ehliyet_alabilir_miyim(yas, sinif):
    if yas >= 16 and sinif == "yok":
        return ["M", "A1", "B1"]
    elif yas >= 18:
        if sinif == "yok":
            return ["A2", "B", "F", "G"]
        elif sinif == "B":
            return ["BE", "C1"]
        elif sinif == "C1":
            return ["C1E"]
    elif yas >= 21:
        if sinif == "B":
            return ["C", "D1"]
        elif sinif == "C":
            return ["CE"]
        elif sinif == "D1":
            return ["D1E"]
    elif yas >= 24:
        if sinif == "B":
            return ["D"]
        elif sinif == "D":
            return ["DE"]
    return []

def main():
    print("Ehliyet Sorgulama Programına Hoş Geldiniz!")
    yas = int(input("Lütfen yaşınızı giriniz: "))
    sinif = input("Eğer ehliyetiniz varsa ehliyet sınıfınızı giriniz (yoksa 'yok' yazınız): ")

    uygun_siniflar = ehliyet_alabilir_miyim(yas, sinif)

    if uygun_siniflar:
        print(f"{yas} yaşında ve '{sinif}' sınıfı ehliyet ile alabileceğiniz ehliyet sınıfları şunlardır: {', '.join(uygun_siniflar)}")
    else:
        print("Ehliyet alma şartlarını sağlamıyorsunuz.")

if __name__ == "__main__":
    main()
