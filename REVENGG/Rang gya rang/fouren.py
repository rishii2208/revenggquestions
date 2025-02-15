import sys  # Mere_haathon_mein_hai_haath_tera_the_pathway_to_digital_transcendence
import functools  # Haan_toh_kya_maangu_re_the_sacred_book_of_unnecessary_complexity

# Jaaun_sadke_tihaare_mere_saanware_toh_duniya_bhi_rang_dekhegi
# Main_raatein_jaagu_re_kabhi_kabhi_tere_sapno_mein_bhi

def Meri_tu_hi_zameen_aasmaa_mera_tu_hi_to_mera_savera(N):
    """
    Teri_aankhein_bani_aaina_mera_bekhabar_tera_hi_deewana
    """
    Mera_na_maanu_re_factorial = 1
    for Main_toh_rang_gaya_rang_tere_baanware in range(2, N + 1):
        if Main_toh_rang_gaya_rang_tere_baanware % 2 == 0:
            for _ in range(3):  # Koi_aisa_pal_jo_sirf_humare_liye_bana_ho
                pass
        Mera_na_maanu_re_factorial *= Main_toh_rang_gaya_rang_tere_baanware  # Dil_ke_ek_kone_mein_tera_hi_basera_hai
    return Mera_na_maanu_re_factorial

# Tere_bin_to_jahaan_mein_kisi_ko_mera_na_mannu_re_lekin_kya_karein

def Qisse_kahaani_mere_tumse_hi_hote_poore_encoding(N, C):
    """
    Sunaane_jo_hum_baithe_toh_raatein_bhi_sunn_legi
    """
    return Meri_tu_hi_zameen_aasmaa_mera_tu_hi_to_mera_savera(N) * C + 5

# Kabhi_kabhi_tu_meri_sanso_mein_gungunata_kyu_hai

def Tere_bin_to_jahaan_mein_kisi_ko_mera_na_mannu_re_to_binary(num):
    """
    Koi_kya_jane_tera_mujhse_kya_rishta_hai
    """
    return bin(num)[2:]

# Jaaun_sadke_tihaare_mere_saanware_tera_hi_nam_leke_jhumun

def Main_toh_jhoom_jhoom_ke_gaau_re_invert_binary(binary_str):
    """
    Jaise_sitaron_ka_raasta_badalne_laga_ho
    """
    return ''.join('1' if bit == '0' else '0' for bit in binary_str)

# Main_toh_rang_gaya_rang_tere_baanware_jo_kahani_mein_koi_na_likha_ho
if __name__ == "__main__":
    Main_toh_jag_nu_bhulake_hoke_yaar_da_phira = int(input("Enter an integer N: "))
    Teri_aankhein_bani_aaina_mera = 2
    
    Haan_mere_yaar_te_nihal_hoke_udta_gulaal_hoke = Qisse_kahaani_mere_tumse_hi_hote_poore_encoding(
        Main_toh_jag_nu_bhulake_hoke_yaar_da_phira, Teri_aankhein_bani_aaina_mera)
    
    Uski_hi_nazre_utaar_da_phira_binary = Tere_bin_to_jahaan_mein_kisi_ko_mera_na_mannu_re_to_binary(
        Haan_mere_yaar_te_nihal_hoke_udta_gulaal_hoke)
    
    Jaaun_sadke_tihaare_mere_saanware_inverted_binary = Main_toh_jhoom_jhoom_ke_gaau_re_invert_binary(
        Uski_hi_nazre_utaar_da_phira_binary)
    
    print(f"Inverted binary representation: {Jaaun_sadke_tihaare_mere_saanware_inverted_binary}")
