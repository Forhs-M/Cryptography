import math
from collections import Counter

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# seq_search : Finds every 3 letter sequence in a given message.
# mess : Message whose sequences will be found.
# Returns a list containing every 3 letter sequence found.

def seq_search(mess):
    seq_list = []
    for i in range(len(mess)-2):
        seq = mess[i:i+3]
        for j in range(i+1, len(mess)- 2):
            poss_seq = mess[j:j+3]
            if seq == poss_seq:
                seq_list.append(seq)
                break
    return seq_list

# factor : Computes the factors of a given number.
# num : Given number.
# Returns a list that contais every factor of given number.

def factor(num):
    fact_list = []
    for i in range(2, (num//2)+1):
        if num % i == 0:
            fact_list.append(i)
    fact_list.append(num)
    return fact_list        

# kasiski: Implementation of Kasiski test on a given encrypted message.
# mess: Given encrypted message.
# Returns a list containg possible key lengths and their frequency.

def kasiski(mess):
    seq_list = seq_search(mess)
    factor_counts = Counter()
    for i in range(len(seq_list)):
        seq_poss = []
        seq_dist = []
        seq = seq_list[i]
        for j in range(len(mess)-2):
            coll_seq = mess[j:j+3]
            if seq == coll_seq:
                seq_poss.append(j)
        for j in range(len(seq_poss)-1):
            seq_dist.append(seq_poss[j+1]-seq_poss[j])
        for j in range(len(seq_dist)):
            fact_list = factor(seq_dist[j])
            factor_counts.update(fact_list)
    return factor_counts.most_common()

# letter_freq : Frequency of every letter in English alphabet.

letter_freq = {
    'A': 8.167,  'B': 1.492,  'C': 2.782,  'D': 4.253,
    'E': 12.702, 'F': 2.228,  'G': 2.015,  'H': 6.094,
    'I': 6.966,  'J': 0.153,  'K': 0.772,  'L': 4.025,
    'M': 2.406,  'N': 6.749,  'O': 7.507,  'P': 1.929,
    'Q': 0.095,  'R': 5.987,  'S': 6.327,  'T': 9.056,
    'U': 2.758,  'V': 0.978,  'W': 2.360,  'X': 0.150,
    'Y': 1.974,  'Z': 0.074
}

# chi_squared : Computes the chi-squared statistic for a given message.
# mess : Message whose letter frequency will be analyzed.
# Returns a chi-squared value.

def chi_squared(mess):
    n = len(mess)
    count = Counter(mess)
    chi2 = 0.0
    for letter in alphabet:
        observed = count.get(letter, 0)
        expected = letter_freq[letter] * n / 100.0
        chi2 += ((observed - expected) ** 2) / expected
    return chi2

# key_finder : Finds the key used for encryption of a message,
# that was encrypted with Vigenere, using statistical analysis.
# mess : Encrypted message.
# key_length : Length of the key.
# Returns the key used for encryption.

def key_finder(mess, key_length):
    columns = []
    for i in range(key_length):
        col = ""
        for j in range(i, len(mess), key_length):
            col += mess[j]
        columns.append(col)
    key = ""
    for col in columns:
        best_score = float('inf')
        best_shift = 0
        for shift in range(26):
            decoded = ""
            for char in col:
                decoded += alphabet[(alphabet.index(char) - shift) % 26]
            score = chi_squared(decoded)
            if score < best_score:
                best_score = score
                best_shift = shift
        key += alphabet[best_shift]
    return key

# decryption : Decrypts a message that was encrypted with Vigenere.
# mess : Encrypted message.
# Returns the decrypted message.

def decryption(mess):
    poss_key_lengths = kasiski(mess)
    assumed_key_length = poss_key_lengths[0][0]
    key = key_finder(mess, assumed_key_length)
    print("The key is :", key)
    dec_mess = ""
    for i, char in enumerate(mess):
        dec_mess += alphabet[(alphabet.index(char) - alphabet.index(key[i % assumed_key_length])) % 26]
    return dec_mess

mess = "SCEELGZSSLCRFPWUTNTSBXAHRCCCMSAGVCAHYOQHQRKAHRTFRSAEFGDEGWOEGWBFVFGUSVEWOEGOALPDRNGGZPSVFOXAUTBNBVVLACESFWUTRQPLSUEATZVKOMNGVREHTVPWNFAUEVBTLOAGGVRZBMNAPESPNVFGBELTUVBTDPKRNDVWJEBSIESUIHZHUWOUZNBOJHIAVTVLPSORZBOAHRPFVLPCNYZNHHNQLCHKOOBGCAWUEHGFBFPNGBWGSKDVGWBFHLZBFROVUYQPRHYOQHQRVIYVZDNUAIGYSNVZTBNBRPARRZSYQLXCYCFACEBSHUWPSFHSVFJRRNGRLOEFVNRGMTURIESUIHZHHJPNTFOLKAHVFWFKVMRGVVFNLVXSVVLAFVBGZLHHZOATYAVAHUWYENESFGTECRCCDLISLCHKOOBGCAWPDRNWALVTURPESPNLBIJASLTRHNZHLSNBVVLABHHGZLRRNFRGAHREDRGWLRJVBSYEORMBFKTUVGCGPNGNHJZPCUGVRQWRBQIPWAWBVRRSZFBESNUOIQROFWUTVAHUGZENESGZLPRBDYWIELBBQLOEXASRGMTURQHJCEVQCALDAAGHBKVUAQSTGAIFGWPSSHRESVVVNGGVVFRTUNHVSTBRLCAVAHRXBRWVFGUWFUBRIROAVPDBAHXFVWNAMBFLWUBWFAKOXACJKVMRCSBHSEGUOGOLRRVHUAUKSBFRPHMCYSGZHTNAMBFLWVYZNYYERGVNLPSNNQAWDTBAKBMSDORKRDSOAGVRLVPBSHUAZCHEJROOEALCHLOIAXHUSAAGGVRSNEBSHJWUTLSWIWOEUNRCJVDHPSQWUOHTVFUPEAPSCZFSVPGNFKMNGVREHTVPGGGTAXRHRFVRGJSALFMRATNEVUFUSCJVDHPSQTPNBZWNDAHRBFREKISSSEWUTVNZNFKIAGSTJHLPNZPMSUFYOJKVFTEOIAAAGVCADHWFBTZGAIBARRUVMCBGVLPOABTJZPTRYWTZAAAQGBGUNBJKUSAIFVHGZHTFUCBLZOARICLVTUVGCSYTBSHUWJUEISJZHTNESGZLBNFWPJLQHVFRELNGFWGZPNXJSPGBLQFSGVVWAGVEWLTUVBTKAHNGOEWMAVEZLFLCRFGNJFFBEGPALNGVTVUYEFROEUOOESCESUYFBFGGMIAISALPNTBFZSAHRZOGAJSBEDUQZIPFCESUYGUWAYHLBAUGZHTYVBRAKOAGHUAUKNCSEKVNPNBTWAAYBBTOPTUBIGSUYBASBXAHRFSGZYERGVRXPRFGCAWPSBOJVGBSGEOVFPNTNBQWEPREWRFJELBIQGUTRKDRUAAYNKLWYHBJSIWYBEVUULOEZNMOWAOTVJRQVUNASJLOEBEMBXWHLFWPKAHRFSQSFSBEANLOEZNHVUZOERBTAUEREWAYAHRFSPGUDGUWAYPSNPSELHIANABMUTBSWALLLYVURFJEBEHNDLNGVBBLOEEJCEVZYBHVNNLTBUOIWHNVDHUSAIFSOVJSYUVUULVDBTCBVYEFROEUOWBEYVVVNGGVVFRTUNHGZLRRVGNFFGBBRRFNIARSEGYSPVSALPSGGVNLJAATSGSSOATCASUIDBTJZPCUVGGZLAIRFNYLFBEVHEHNORWAYZIABHUWYWBERFZLHNFHBZHVRNBVIOITUSELOAAGVNLLVREMBFLIAGVVKYOBZWFUVNFVRRJHBYLOOGCEGUOGLOIFJSZANHGFOLAZAZNHGWYOSRBIAYOAZSALPNGRZYANEAPSVKHMNGHRJVFURFRVPTLGVBKLTJBWQGUTGUWACHRRFISXPCVRBGAAHVAYGZLRRVGNLOIEQQBFZTVGIRFAHRESNLOIEQQBEWOARBGOOIPUWFLOEBASGZHTZNYRKHNRVBFLLIABFNFPSNNQAWDTBATBJDAAGCSSIEGGSEOVRQJSJASLPNZYAAMBGWISAIBAWAGAHREKBJKSLBIUSCEGBVNNLSBZSXAUDBSOQJPVRFCZWRIAQCSSKEFVFRLVFVARBMATUROAKDEENRRKPRRGCSAUDBHHJZHTZNYRKAHVAUFLPCXVTLGBDBAHUSCEGUOGQVUZNMUSCENYZGZLTENWAAUGNARVFAEYYWTWUCRVBGZLWBEZQQVUQBBGZHVRDIRKAIBAGNFKYBHKBFAJHFHSAUDNAGJWYSGUWFAZAUNFQLOIATHBHBTLBIEXPNTRFBFPTVFOZSATRECSLLMCRFNELNGCFBTHBYLHUSAIFNANLAEEBTCJVBNOZLWHRYLHESPNVAURSYLLPVVDKHBBRRPWEEVSAULSJUSGZLRLBIJASLZBHVNHTRVBGZLDVESPLPOABTFUPEAGWSAJRRFSNJJHVGVVFRTUNHNLHSHCSEXPCVNZYWCEYVHVKILRARRVBSRBTFWCEENZGZPNTFHUAZIFACGSUYNGHREWTNGOQWLPNAOYQZIFNHNDSBHGALXLEYVBTAZTUNHNYVOQFQVWUTVFHUSZATESNLKENYCSOOAGJSPSUCNYZPMYIBFWGQPWBAHTGHNLQSRHLRVAHBAATUNBGZHTURKNFASGBYAGDTUROAKDEEFVRKQUFGQHJPOHFVBOAHVAUFLPCXNBQZLWNAHFLVKABKGZLAAFKRJZTBDIRKAIBAGNFKISUSFWLSGUWACZHRJOALZTBEOVKLQHRGGAVNFNBQZLWNAHFLVKABKGZLAAFKRJZTBGVBKLTURBGZLRRFHUWPDRNCSVPSFNHVKMAPGWBFIYGUWFAKOAGARSUACRGFATIFGWPVPSFNHVKMAPGWBFVFGUSJGYLQJSQGUTYVYRLOEJNMGZPNTFOEWPMRNBNUVNFGFHUAIIRRVKZAGVGSSJTVBBGZLIQROPGBLQOSRPWRRFGRVPNGUSJGYDFGVVKPSBXPHLPTUVBXLOIATGPGBLQOSQGUEORHGWYIGUWACAHRESVKHNRNHRJDALGCQGAHVFWGZPNXGVVFNSPBIYVIEVZDEGCEQNZVLALRVBBLOEEJCEVZTURFRAZCBAHVFBAYYMNKSITUHVJYIGNHVGUWURBGZPNTFRBFALBBYDMPTREWTZAAAQWGZPNXGVNLKIFFOGAZFNPHVGUIACFRKLNGQOLKPSNXSLVYIIVBTXVRPRWAYVOQFQVWUTVFHF"

print("The decrypted message is :", decryption(mess))
