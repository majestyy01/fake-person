from faker import Faker
from colorama import init, Fore
import time
#WoxicDEV
#İnstagram : @woxicev

init(autoreset=True)

fake = Faker()

def print_red(text):
    print(Fore.RED + text + Fore.RESET)

def print_pink(text):
    print(Fore.MAGENTA + text + Fore.RESET)

def print_blue(text):
    print(Fore.CYAN + text + Fore.RESET)

def main_menu():
    while True:
        print_red("    __      __            .__       ________  _______________   ____")
        print_red("   /  \    /  \_______  __|__| ____ \______ \ \_   _____/\   \ /   /")
        print_red("   \   \/\/   /  _ \  \/  /  |/ ___\ |    |  \ |    __)_  \   Y   / ")
        print_red("    \        (  <_> >    <|  \  \___ |    `   \|        \  \     /")
        print_red("     \__/\  / \____/__/\_ \__|\___  >_______  /_______  /   \___/")
        print_red("          \/             \/       \/        \/        \/ ")
        print_red("")
        print_red("                                                      @wocixdev")
        print_pink("1. Rastgele Bilgi Üret")
        print_pink("2. Hakkımda Bilgisi")
        print_pink("0. Çıkış")

        choice = input("Seçiminizi yapın: ")

        if choice == "1":
            generate_info()
        elif choice == "2":
            about_me()
        elif choice == "0":
            print_red("Programdan çıkılıyor. İyi günler!")
            break
        else:
            print_red("Geçersiz seçim! Lütfen tekrar deneyin.")

def generate_info():
    print_blue("***** İsim ve Adres Bilgileri *****")
    print_red("Ad Soyad:")
    print(str(fake.name()))
    time.sleep(0.1)

    print_red("Ad:")
    print(str(fake.first_name()))
    time.sleep(0.1)

    print_red("Soyad:")
    print(str(fake.last_name()))
    time.sleep(0.1)

    print_red("Unvan:")
    print(str(fake.prefix()))
    time.sleep(0.1)

    print_red("Sonek:")
    print(str(fake.suffix()))
    time.sleep(0.1)

    print_red("Adres:")
    print(str(fake.address()))
    time.sleep(0.1)

    print_red("Şehir:")
    print(str(fake.city()))
    time.sleep(0.1)

    print_red("Eyalet:")
    print(str(fake.state()))
    time.sleep(0.1)

    print_red("Ülke:")
    print(str(fake.country()))
    time.sleep(0.1)

    print_red("Posta Kodu:")
    print(str(fake.zipcode()))
    time.sleep(0.1)

    print_blue("***** İletişim Bilgileri *****")
    print_red("E-posta:")
    print(str(fake.email()))
    time.sleep(0.1)

    print_red("Telefon Numarası:")
    print(str(fake.phone_number()))
    time.sleep(0.1)

    print_red("Şirket E-posta:")
    print(str(fake.company_email()))
    time.sleep(0.1)

    print_blue("***** Tarih ve Saat *****")
    print_red("Doğum Tarihi:")
    print(str(fake.date_of_birth()))
    time.sleep(0.1)

    print_red("Bu Yılın Tarihi:")
    print(str(fake.date_this_decade()))
    time.sleep(0.1)

    print_red("Bu Yüzyılın Tarihi:")
    print(str(fake.date_this_century()))
    time.sleep(0.1)

    print_red("Bu Ayın Saati:")
    print(str(fake.date_time_this_month()))
    time.sleep(0.1)

    print_red("Bu Yılın Saati:")
    print(str(fake.date_time_this_decade()))
    time.sleep(0.1)

    print_blue("***** Meslek ve Şirket Bilgileri *****")
    print_red("Meslek:")
    print(str(fake.job()))
    time.sleep(0.1)

    print_red("Şirket:")
    print(str(fake.company()))
    time.sleep(0.1)

    print_red("Yakalama Cümlesi:")
    print(str(fake.catch_phrase()))
    time.sleep(0.1)

    print_red("BS:")
    print(str(fake.bs()))
    time.sleep(0.1)

    print_blue("***** Finansal Bilgiler *****")
    print_red("Kredi Kartı Numarası:")
    print(str(fake.credit_card_number()))
    time.sleep(0.1)

    print_red("Kredi Kartı Sağlayıcısı:")
    print(str(fake.credit_card_provider()))
    time.sleep(0.1)

    print_red("Kredi Kartı Son Kullanma Tarihi:")
    print(str(fake.credit_card_expire()))
    time.sleep(0.1)

    print_blue("***** Rasgele Sayılar ve Yazılar *****")
    print_red("Rasgele Sayı:")
    print(str(fake.random_number()))
    time.sleep(0.1)

    print_red("Rasgele Eleman:")
    print(str(fake.random_element()))
    time.sleep(0.1)

    print_red("Rasgele Elemanlar:")
    print(str(fake.random_elements()))
    time.sleep(0.1)

    print_red("Rasgele Tamsayı:")
    print(str(fake.random_int()))
    time.sleep(0.1)

    print_red("Rasgele Örnek:")
    print(str(fake.random_sample()))
    time.sleep(0.1)

    print_blue("***** Metin Oluşturma *****")
    print_red("Kelime:")
    print(str(fake.word()))
    time.sleep(0.1)

    print_red("Cümle:")
    print(str(fake.sentence()))
    time.sleep(0.1)

    print_red("Cümleler:")
    print(str(fake.sentences()))
    time.sleep(0.1)

    print_red("Paragraf:")
    print(str(fake.paragraph()))
    time.sleep(0.1)

    print_red("Paragraflar:")
    print(str(fake.paragraphs()))
    time.sleep(0.1)

    print_blue("***** Internet ve Web *****")
    print_red("URL:")
    print(str(fake.url()))
    time.sleep(0.1)

    print_red("URI:")
    print(str(fake.uri()))
    time.sleep(0.1)

    print_red("Domain Adı:")
    print(str(fake.domain_name()))
    time.sleep(0.1)

    print_red("Resim URL'si:")
    print(str(fake.image_url()))
    time.sleep(0.1)

    print_red("IPv4 Adresi:")
    print(str(fake.ipv4()))
    time.sleep(0.1)

    print_blue("***** Renk ve Para Birimi *****")
    print_red("Renk Adı:")
    print(str(fake.color_name()))
    time.sleep(0.1)

    print_red("Para Birimi Kodu:")
    print(str(fake.currency_code()))
    time.sleep(0.1)

    print_blue("***** UUID ve Boolean *****")
    print_red("UUID:")
    print(str(fake.uuid4()))
    time.sleep(0.1)

    print_red("Boolean Değeri:")
    print(str(fake.boolean()))
    time.sleep(0.1)

    print_blue("***** Dil *****")
    print_red("Dil Kodu:")
    print(str(fake.language_code()))
    time.sleep(0.1)

    print_red("Kelime (Özel Kelime Listesi ile):")
    print(str(fake.word(ext_word_list=None)))
    time.sleep(0.1)

    print_red("Cümle (Özel Kelime Listesi ile):")
    print(str(fake.sentence(ext_word_list=None)))
    time.sleep(0.1)

    print_blue("***** Sosyal Medya ve Internet *****")
    print_red("Kullanıcı Adı:")
    print(str(fake.user_name()))
    time.sleep(0.1)

    print_red("Şifre:")
    print(str(fake.password()))
    time.sleep(0.1)

    print_red("Kullanıcı Aracı:")
    print(str(fake.user_agent()))
    time.sleep(0.1)

    print_red("2.Kullanıcı Adı:")
    print(str(fake.user_name()))
    time.sleep(0.1)

    print_red("2.Şifre:")
    print(str(fake.password()))
    time.sleep(0.1)

    print_red("2.Kullanıcı Aracı:")
    print(str(fake.user_agent()))
    time.sleep(0.1)

    print_red("3.Kullanıcı Adı:")
    print(str(fake.user_name()))
    time.sleep(0.1)

    print_red("3.Şifre:")
    print(str(fake.password()))
    time.sleep(0.1)

    print_red("3.Kullanıcı Aracı:")
    print(str(fake.user_agent()))
    time.sleep(0.1)

    print_red("4.Kullanıcı Adı:")
    print(str(fake.user_name()))
    time.sleep(0.1)

    print_red("4.Şifre:")
    print(str(fake.password()))
    time.sleep(0.1)

    print_red("4.Kullanıcı Aracı:")
    print(str(fake.user_agent()))
    time.sleep(0.1)

    print_red("5.Kullanıcı Adı:")
    print(str(fake.user_name()))
    time.sleep(0.1)

    print_red("5.Şifre:")
    print(str(fake.password()))
    time.sleep(0.1)

    print_red("5.Kullanıcı Aracı:")
    print(str(fake.user_agent()))
    time.sleep(0.1)

    print_blue("***** Diğer *****")
    print_red("Dosya Adı:")
    print(str(fake.file_name()))
    time.sleep(0.1)

    print_red("Dosya Uzantısı:")
    print(str(fake.file_extension()))
    time.sleep(0.1)

    print_blue("***** Ulusal Kimlik Bilgileri *****")
    print_red("SSN:")
    print(str(fake.ssn()))
    time.sleep(0.1)

    print_blue("***** Biyografi ve Rastgele Bilgiler *****")
    print_red("Profil:")
    print(str(fake.profile()))
    time.sleep(0.1)

    print_red("Basit Profil:")
    print(str(fake.simple_profile()))
    time.sleep(0.1)

    input("Enter tuşuna basarak ana menüye dönün...")

def about_me():
    while True:
        print_red("Hakkımda:")
        print(str(fake.paragraph()))
        print("Evet Üstte Gördüğünüz Metinde Fake bir Metindi :D,Sürekli Değişiyor")
        print("Bu tool python ile faker kütüphanesi kullanılarak yazılmıştır.Bilgiler tamamen fake olup gerçeklikle alakası bulunmamaktadır.")
        print("İletişim:")
        print("İnstagram : woxicdev")
        print("Discord : WoxicDEV")
        time.sleep(0.1)

        input("Enter tuşuna basarak ana menüye dönün...")
        break

if __name__ == "__main__":
    main_menu()
