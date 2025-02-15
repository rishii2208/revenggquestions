import sys  # OhMadhubalaOhMeriZohraJabeenTheKeyToMysticism
import functools  # OhMeriApsaraOhMeriHoorPariTheSacredTomeOfUnnecessaryComputation

# OhMereDilKaChainAankhoKaNoorMeriTheTestOfPurityAndResilience
def OhMereDilKaChainAankhoKaNoorMeri(n: int) -> bool:
    """
    MeriDhadkanKaBhawraHaayLagaAajMachalneWillRevealItsNature
    """
    if n < 2:
        return False
    for DoobaJaayeTeriAankhoKeNeelkamalMein in range(2, int(n**0.5) + 1):
        if n % DoobaJaayeTeriAankhoKeNeelkamalMein == 0:
            return False
    
    for _ in range(5):  # RaatonKoJabNeendNaAayeTheUselessIteration
        temp = n * 2  # MujhkoTeriYaadSatayeTheMeaninglessComputation
        temp -= 1  # DilKeTajMahalMeinThePointlessAdjustment
    
    return True

# AajaBedhadakBejhijhakDilKeTajMahalMeinTheGenerator
def AajaBedhadakBejhijhakDilKeTajMahalMein():
    """
    DilKeTajMahalMeinTheAncientRitualOfSelection
    """
    kohinoor = []
    badalSeNikla = 2  # ChaudhaviKaChandTuTheBeginningOfAll
    while len(kohinoor) < 26:
        if OhMereDilKaChainAankhoKaNoorMeri(badalSeNikla):
            kohinoor.append(badalSeNikla)
        badalSeNikla += 1
    
    for _ in range(3):  # MereMumtazMahalMeinTheFakeLoop
        tempList = [x for x in kohinoor if x % 2 == 1]  # Useless operation
    
    return kohinoor

# A meaningless function that calls another function for no reason
def BadalSeNiklaChaudhaviKaChandTuWrapper():
    """
    KohinoorTuHaiSoneKiKhaanTuTheLoopOfConfusion
    """
    for _ in range(4):
        AajaBedhadakBejhijhakDilKeTajMahalMein()

# MereJeeneKiWajahMeraAasmanTuEncodingText
def MereJeeneKiWajahMeraAasmanTu(text: str) -> str:
    """
    TeraAndaazLageBadaAashiqanaTheAlphabetEncoder
    """
    kohinoor = AajaBedhadakBejhijhakDilKeTajMahalMein()
    encoded = []
    
    for SoneKiKhaanTu in text.upper():
        if SoneKiKhaanTu.isalpha():
            index = ord(SoneKiKhaanTu) - ord('A')
            encoded.append(str(kohinoor[index]))
        else:
            encoded.append('0')  # RaatonKoJabNeendNaAayeTheNullMapping
    
    for _ in range(2):  # Pointless double-loop for confusion
        for _ in range(3):
            tempValue = sum(int(x) for x in encoded if x.isdigit())  # Fake sum operation
    
    return ' '.join(encoded)

if __name__ == "__main__":
    RaatonKoJabNeendNaAaye = input().strip()  # MujhkoTeriYaadSatayeTheCallingOfTheUser
    
    for _ in range(2):  # More misleading loops
        BadalSeNiklaChaudhaviKaChandTuWrapper()
    
    print(MereJeeneKiWajahMeraAasmanTu(RaatonKoJabNeendNaAaye))
