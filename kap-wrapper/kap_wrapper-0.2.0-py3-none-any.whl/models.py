from enum import Enum


class Base:
    def __repr__(self):
        return str(self.__dict__)


class Kap(Base):
    def __init__(self, data):
        self.founder = data["founder"]
        self.start_date = data["start_date"]
        self.duration = data["duration"]
        self.fund_url = data["fund_url"]
        self.strategy = data["strategy"]
        self.risk_rate = data["risk_rate"]
        self.daily_cost = data["daily_cost"]
        self.annual_cost = data["annual_cost"]

class FundGroup(str, Enum):
    BORSA_YATIRIM_FONLARI = "BYF"
    YATIRIM_FONLARI = "YF"
    EMEKLILIK_YATIRIM_FONLARI = "EYF"
    OKS_EMEKLILIK_YATIRIM_FONLARI = "OKS"
    YABANCI_YATIRIM_FONLARI = "YYF"
    VARLIK_FINANSMAN_FONLARI = "VFF"
    KONUT_FINANSMAN_FONLARI = "KFF"
    GAYRIMENKUL_YATIRIM_FONLARI = "GMF"


class Subject(str, Enum):
    SORUMLULUK_BEYANI = "4028328d537aad0a015383da38914598"
    ALTI_AYLIK_RAPOR = "8aca490d51458dcf015147f9e6c203f2"
    ARACI_KURUMA_ODENEN_KOMISYON_VE_VARLIK_ALIM_SATIM_BILGILERI = "8aca490d502dd03b01502dd9c9c60040"
    BIR_SONRAKI_YILA_ILISKIN_GERCEKLESEBILECEK_TAHMINI_TAKIP_FARKI = "4028328d537aad0a015383d773c44584"
    BORSA_DISI_REPO_TERS_REPO_SOZLESMESI = "8aca490d502dd03b01502ddc1678004d"
    BORSA_DISI_SOZLESMELERE_ILISKIN_ILKELER = "8aca490d502dd03b01502decce7600f6"
    BYF_IC_TUZUK_ = "8aca490d51067d0c0151068012540011"
    FINANSAL_RAPOR = "8aca490d502dd03b01502deede79010a"
    FINANSAL_TABLO_BILDIRIMI = "8aca490d502dd03b01502df05c54011a"
    FON_GIDER_BILGILERI = "8aca490d502dd03b01502dde122c0058"
    FON_KURUCUSUNA_YONETICISINE_PORTFOY_SAKLAYICISINA_YETKILENDIRILMIS_KATILIMCIYA_ILISKIN_ACIKLAMA = "8aca490d51058254015105abe3790143"
    FON_SUREKLI_BILGILENDIRME_FORMU = "4028328d53a8d2060153bce347f94a5d"
    FON_TASFIYE_DUYURUSU = "8aca490d502dd03b01502de59b460090"
    FON_TOPLAM_GIDER_KESINTISI_ORANI_BILGILERI_ = "8aca490d51458dcf015147f8cd8903e7"
    FON_TOPLAM_GIDER_ORANI_VE_FON_TOPLAM_GIDERININ_DAGILIMI = "4028328d537aad0a015383d09b184552"
    FON_UNVAN_DEGISIKLIGI = "8aca490d51458dcf015147eefdfd031d"
    FON_UNVAN_DEGISIKLIGI_BYF = "8aca490d51458dcf0151480122af0464"
    FONA_ILISKIN_BILGILER = "8aca490d51458dcf015147f7ca3a03b6"
    FONUN__MALI_YAPISI = "8aca490d51058254015105acab48014d"
    FONUN_IDARI_YAPISI_VE_ORGANIZASYONU = "8aca490d51058254015105ab2fc70139"
    FONUN_ISLEM_ESASLARI_VE_BIRIM_PAY_DEGERI = "8aca490d51058254015105aa434b012f"
    FONUN_PORTFOY_YAPISI_VE_YONETIM_STRATEJISI = "8aca490d51058254015105ad6d550157"
    FONUN_SONA_ERMESI_DEVRI_DONUSTURULMESI_BIRLESTIRILMESI_KURUCUSUNUN_DEGISTIRILMESI = "8aca490d51058254015105ae28740161"
    FONUN_TAKIP_ETTIGI_ENDEKSE_ILISKIN_ACIKLAMA = "8aca490d51058254015105aef2c8016b"
    GENEL_ACIKLAMA = "8aca490d502dd03b01502de6916c009a"
    GERCEKLESEN_TAKIP_FARKI_VE_HATASI = "4028328d537aad0a015383d991db458e"
    HERHANGI_BIR_OTORITEYE_MALI_TABLO_VERILMESI = "8aca490d51458dcf0151480237510479"
    HIZMET_SAGLAYICININ_FAALIYETLERI_VE_FON_VARLIKLARININ_MEVCUDIYETINE_ILISKIN_RAPOR = "8aca490d51458dcf015147fd29720414"
    IC_TUZUK = "8aca490d51458dcf015147f57fea039c"
    IC_TUZUK_DEGISIKLIK = "8aca490d51458dcf015147f6a7e303ac"
    IHRAC_BELGESI = "8aca490d51458dcf015147feae1f0432"
    IZAHNAME = "8aca490d502dd03b01502deb982000e2"
    IZAHNAME_DEGISIKLIK_ = "8aca490d51153da601511548b25900fb"
    KESINLESEN_PORTFOY_BILGILERI = "4028328d537aad0a015383dac84945a2"
    KREDI_DERECELENDIRME_NOTU = "8aca490d51458dcf015147fa9e6903fc"
    KREDI_KULLANIMI = "8aca490d51458dcf015147f49732037e"
    OZEL_DURUM_ACIKLAMASI = "8aca490d51458dcf01514802e9ac0490"
    PERFORMANS_SUNUM_RAPORU = "8aca490d502e18ef01502e2efff6006c"
    PORTFOY_DAGILIM_RAPORU = "8aca490d502e34b801502e380044002b"
    SON_BIR_YILLIK_DONEM_ICIN_ONGORULEN_TAHMINI_TAKIP_HATASI = "4028328d537aad0a015383d6c89a457a"
    SEMSIYE_FON_IC_TUZUGU = "8aca490d51153da60151154412830097"
    SEMSIYE_FON_IC_TUZUGU_DEGISIKLIK = "8aca490d51153da601511547a1b000ed"
    TANITIM_FORMU = "4028328d537aad0a015383d60baf4570"
    TASARRUF_SAHIPLERI_SIRKULERI = "8aca490d51458dcf015147fe02bd0425"
    TERTIP_IHRAC_BELGESI = "8aca490d51458dcf015147ff8784043f"
    TUREV_ARAC_ISLEMLERINE_ILISKIN_ILKELER = "8aca490d502e34b801502e375fac0021"
    VARLIK_VEYA_IHRACCI_DERECELENDIRME_NOTU = "8aca490d51153da6015115464c9d00da"
    YAPILANDIRILMIS_YATIRIM_ARACLARI_IKRAZ_ISTIRAK_SENETLERI = "8aca490d51458dcf015147f0b0af0345"
    YATIRIM_FONU_BILGI_FORMU = "8aca490d51458dcf015147f333b60361"
    YATIRIMCI_BILGI_FORMU = "8aca490d51153da6015115455c5f00b9"
    YATIRIMCI_RAPORU = "8aca490d51458dcf015147fb9add0406"
    YILLIK_RAPOR = "4028328d537aad0a015383d56e204566"
    YF_IC_TUZUK = "8aca490d502dd03b01502deab28500bc"

    
