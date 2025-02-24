from telegram.ext import Updater, CommandHandler
from telegram.ext.dispatcher import run_async
import json
import requests
from datetime import datetime, timedelta
from time import sleep
import pytz

IST = pytz.timezone('Asia/Kolkata')

TOKEN = "2105638884:AAEKPoWvEACxplXeCTFyp8B3NbjxjTS8ycA"  # Bot Token

TIME_GAP = 60  # 1 Minutes

data = {'nicobar': 3, 'north and middle andaman': 1, 'south andaman': 2, 'anantapur': 9, 'chittoor': 10, 'east godavari': 11, 'guntur': 5, 'krishna': 4, 'kurnool': 7, 'prakasam': 12, 'sri potti sriramulu nellore': 13, 'srikakulam': 14, 'visakhapatnam': 8, 'vizianagaram': 15, 'west godavari': 16, 'ysr district, kadapa (cuddapah)': 6, 'anjaw': 22, 'changlang': 20, 'dibang valley': 25, 'east kameng': 23, 'east siang': 42, 'itanagar capital complex': 17, 'kamle': 24, 'kra daadi': 27, 'kurung kumey': 21, 'lepa rada': 33, 'lohit': 29, 'longding': 40, 'lower dibang valley': 31, 'lower siang': 18, 'lower subansiri': 32, 'namsai': 36, 'pakke kessang': 19, 'papum pare': 39, 'shi yomi': 35, 'siang': 37, 'tawang': 30, 'tirap': 26, 'upper siang': 34, 'upper subansiri': 41, 'west kameng': 28, 'west siang': 38, 'baksa': 46, 'barpeta': 47, 'biswanath': 765, 'bongaigaon': 57, 'cachar': 66, 'charaideo': 766, 'chirang': 58, 'darrang': 48, 'dhemaji': 62, 'dhubri': 59, 'dibrugarh': 43, 'dima hasao': 67, 'goalpara': 60, 'golaghat': 53, 'hailakandi': 68, 'hojai': 764, 'jorhat': 54, 'kamrup metropolitan': 49, 'kamrup rural': 50, 'karbi-anglong': 51, 'karimganj': 69, 'kokrajhar': 61, 'lakhimpur': 63, 'majuli': 767, 'morigaon': 55, 'nagaon': 56, 'nalbari': 52, 'sivasagar': 44, 'sonitpur': 64, 'south salmara mankachar': 768, 'tinsukia': 45, 'udalguri': 65, 'west karbi anglong': 769, 'araria': 74, 'arwal': 78, 'aurangabad': 77, 'banka': 83, 'begusarai': 98, 'bhagalpur': 82, 'bhojpur': 99, 'buxar': 100, 'darbhanga': 94, 'east champaran': 105, 'gaya': 79, 'gopalganj': 104, 'jamui': 107, 'jehanabad': 91, 'kaimur': 80, 'katihar': 75, 'khagaria': 101, 'kishanganj': 76, 'lakhisarai': 84, 'madhepura': 70, 'madhubani': 95, 'munger': 85, 'muzaffarpur': 86, 'nalanda': 90, 'nawada': 92, 'patna': 97, 'purnia': 73, 'rohtas': 81, 'saharsa': 71, 'samastipur': 96, 'saran': 102, 'sheikhpura': 93, 'sheohar': 87, 'sitamarhi': 88, 'siwan': 103, 'supaul': 72, 'vaishali': 89, 'west champaran': 106, 'chandigarh': 108, 'balod': 110, 'baloda bazar': 111, 'balrampur': 112, 'bastar': 113, 'bemetara': 114, 'bijapur': 115, 'bilaspur': 219, 'dantewada': 117, 'dhamtari': 118, 'durg': 119, 'gariaband': 120, 'gaurela pendra marwahi ': 136, 'janjgir-champa': 121, 'jashpur': 122, 'kanker': 123, 'kawardha': 135, 'kondagaon': 124, 'korba': 125, 'koriya': 126, 'mahasamund': 127, 'mungeli': 128, 'narayanpur': 129, 'raigarh': 130, 'raipur': 109, 'rajnandgaon': 131, 'sukma': 132, 'surajpur': 133, 'surguja': 134, 'dadra and nagar haveli': 137, 'central delhi': 141, 'east delhi': 145, 'new delhi': 140, 'north delhi': 146, 'north east delhi': 147, 'north west delhi': 143, 'shahdara': 148, 'south delhi': 149, 'south east delhi': 144, 'south west delhi': 150, 'west delhi': 142, 'north goa': 151, 'south goa': 152, 'ahmedabad': 154, 'ahmedabad corporation': 770, 'amreli': 174, 'anand': 179, 'aravalli': 158, 'banaskantha': 159, 'bharuch': 180, 'bhavnagar': 175, 'bhavnagar corporation': 771, 'botad': 176, 'chhotaudepur': 181, 'dahod': 182, 'dang': 163, 'devbhumi dwaraka': 168, 'gandhinagar': 153, 'gandhinagar corporation': 772, 'gir somnath': 177, 'jamnagar': 169, 'jamnagar corporation': 773, 'junagadh': 178, 'junagadh corporation': 774, 'kheda': 156, 'kutch': 170, 'mahisagar': 183, 'mehsana': 160, 'morbi': 171, 'narmada': 184, 'navsari': 164, 'panchmahal': 185, 'patan': 161, 'porbandar': 172, 'rajkot': 173, 'rajkot corporation': 775, 'sabarkantha': 162, 'surat': 165, 'surat corporation': 776, 'surendranagar': 157, 'tapi': 166, 'vadodara': 155, 'vadodara corporation': 777, 'valsad': 167, 'ambala': 193, 'bhiwani': 200, 'charkhi dadri': 201, 'faridabad': 199, 'fatehabad': 196, 'gurgaon': 188, 'hisar': 191, 'jhajjar': 189, 'jind': 204, 'kaithal': 190, 'karnal': 203, 'kurukshetra': 186, 'mahendragarh': 206, 'nuh': 205, 'palwal': 207, 'panchkula': 187, 'panipat': 195, 'rewari': 202, 'rohtak': 192, 'sirsa': 194, 'sonipat': 198, 'yamunanagar': 197, 'chamba': 214, 'hamirpur': 655, 'kangra': 213, 'kinnaur': 216, 'kullu': 211, 'lahaul spiti': 210, 'mandi': 215, 'shimla': 208, 'sirmaur': 212, 'solan': 209, 'una': 218, 'anantnag': 224, 'bandipore': 223, 'baramulla': 225, 'budgam': 229, 'doda': 232, 'ganderbal': 228, 'jammu': 230, 'kathua': 234, 'kishtwar': 231, 'kulgam': 221, 'kupwara': 226, 'poonch': 238, 'pulwama': 227, 'rajouri': 237, 'ramban': 235, 'reasi': 239, 'samba': 236, 'shopian': 222, 'srinagar': 220, 'udhampur': 233, 'bokaro': 242, 'chatra': 245, 'deoghar': 253, 'dhanbad': 257, 'dumka': 258, 'east singhbhum': 247, 'garhwa': 243, 'giridih': 256, 'godda': 262, 'gumla': 251, 'hazaribagh': 255, 'jamtara': 259, 'khunti': 252, 'koderma': 241, 'latehar': 244, 'lohardaga': 250, 'pakur': 261, 'palamu': 246, 'ramgarh': 254, 'ranchi': 240, 'sahebganj': 260, 'seraikela kharsawan': 248, 'simdega': 249, 'west singhbhum': 263, 'bagalkot': 270, 'bangalore rural': 276, 'bangalore urban': 265, 'bbmp': 294, 'belgaum': 264, 'bellary': 274, 'bidar': 272, 'chamarajanagar': 271, 'chikamagalur': 273, 'chikkaballapur': 291, 'chitradurga': 268, 'dakshina kannada': 269, 'davanagere': 275, 'dharwad': 278, 'gadag': 280, 'gulbarga': 267, 'hassan': 289, 'haveri': 279, 'kodagu': 283, 'kolar': 277, 'koppal': 282, 'mandya': 290, 'mysore': 266, 'raichur': 284, 'ramanagara': 292, 'shimoga': 287, 'tumkur': 288, 'udupi': 286, 'uttar kannada': 281, 'vijayapura': 293, 'yadgir': 285, 'alappuzha': 301, 'ernakulam': 307, 'idukki': 306, 'kannur': 297, 'kasaragod': 295, 'kollam': 298, 'kottayam': 304, 'kozhikode': 305, 'malappuram': 302, 'palakkad': 308, 'pathanamthitta': 300, 'thiruvananthapuram': 296, 'thrissur': 303, 'wayanad': 299, 'kargil': 309, 'leh': 310, 'agatti island': 796, 'lakshadweep': 311, 'agar': 320, 'alirajpur': 357, 'anuppur': 334, 'ashoknagar': 354, 'balaghat': 338, 'barwani': 343, 'betul': 362, 'bhind': 351, 'bhopal': 312, 'burhanpur': 342, 'chhatarpur': 328, 'chhindwara': 337, 'damoh': 327, 'datia': 350, 'dewas': 324, 'dhar': 341, 'dindori': 336, 'guna': 348, 'gwalior': 313, 'harda': 361, 'hoshangabad': 360, 'indore': 314, 'jabalpur': 315, 'jhabua': 340, 'katni': 353, 'khandwa': 339, 'khargone': 344, 'mandla': 335, 'mandsaur': 319, 'morena': 347, 'narsinghpur': 352, 'neemuch': 323, 'panna': 326, 'raisen': 359, 'rajgarh': 358, 'ratlam': 322, 'rewa': 316, 'sagar': 317, 'satna': 333, 'sehore': 356, 'seoni': 349, 'shahdol': 332, 'shajapur': 321, 'sheopur': 346, 'shivpuri': 345, 'sidhi': 331, 'singrauli': 330, 'tikamgarh': 325, 'ujjain': 318, 'umaria': 329, 'vidisha': 355, 'ahmednagar': 391, 'akola': 364, 'amravati': 366, 'aurangabad ': 397, 'beed': 384, 'bhandara': 370, 'buldhana': 367, 'chandrapur': 380, 'dhule': 388, 'gadchiroli': 379, 'gondia': 378, 'hingoli': 386,
        'jalgaon': 390, 'jalna': 396, 'kolhapur': 371, 'latur': 383, 'mumbai': 395, 'nagpur': 365, 'nanded': 382, 'nandurbar': 387, 'nashik': 389, 'osmanabad': 381, 'palghar': 394, 'parbhani': 385, 'pune': 363, 'raigad': 393, 'ratnagiri': 372, 'sangli': 373, 'satara': 376, 'sindhudurg': 374, 'solapur': 375, 'thane': 392, 'wardha': 377, 'washim': 369, 'yavatmal': 368, 'bishnupur': 398, 'chandel': 399, 'churachandpur': 400, 'imphal east': 401, 'imphal west': 402, 'jiribam': 410, 'kakching': 413, 'kamjong': 409, 'kangpokpi': 408, 'noney': 412, 'pherzawl': 411, 'senapati': 403, 'tamenglong': 404, 'tengnoupal': 407, 'thoubal': 405, 'ukhrul': 406, 'east garo hills': 424, 'east jaintia hills': 418, 'east khasi hills': 414, 'north garo hills': 423, 'ri-bhoi': 417, 'south garo hills': 421, 'south west garo hills': 422, 'south west khasi hills': 415, 'west garo hills': 420, 'west jaintia hills': 416, 'west khasi hills': 419, 'aizawl east': 425, 'aizawl west': 426, 'champhai': 429, 'kolasib': 428, 'lawngtlai': 432, 'lunglei': 431, 'mamit': 427, 'serchhip': 430, 'siaha': 433, 'dimapur': 434, 'kiphire': 444, 'kohima': 441, 'longleng': 438, 'mokokchung': 437, 'mon': 439, 'peren': 435, 'phek': 443, 'tuensang': 440, 'wokha': 436, 'zunheboto': 442, 'angul': 445, 'balangir': 448, 'balasore': 447, 'bargarh': 472, 'bhadrak': 454, 'boudh': 468, 'cuttack': 457, 'deogarh': 473, 'dhenkanal': 458, 'gajapati': 467, 'ganjam': 449, 'jagatsinghpur': 459, 'jajpur': 460, 'jharsuguda': 474, 'kalahandi': 464, 'kandhamal': 450, 'kendrapara': 461, 'kendujhar': 455, 'khurda': 446, 'koraput': 451, 'malkangiri': 469, 'mayurbhanj': 456, 'nabarangpur': 470, 'nayagarh': 462, 'nuapada': 465, 'puri': 463, 'rayagada': 471, 'sambalpur': 452, 'subarnapur': 466, 'sundargarh': 453, 'karaikal': 476, 'mahe': 477, 'puducherry': 475, 'yanam': 478, 'amritsar': 485, 'barnala': 483, 'bathinda': 493, 'faridkot': 499, 'fatehgarh sahib': 484, 'fazilka': 487, 'ferozpur': 480, 'gurdaspur': 489, 'hoshiarpur': 481, 'jalandhar': 492, 'kapurthala': 479, 'ludhiana': 488, 'mansa': 482, 'moga': 491, 'pathankot': 486, 'patiala': 494, 'rup nagar': 497, 'sangrur': 498, 'sas nagar': 496, 'sbs nagar': 500, 'sri muktsar sahib': 490, 'tarn taran': 495, 'ajmer': 507, 'alwar': 512, 'banswara': 519, 'baran': 516, 'barmer': 528, 'bharatpur': 508, 'bhilwara': 523, 'bikaner': 501, 'bundi': 514, 'chittorgarh': 521, 'churu': 530, 'dausa': 511, 'dholpur': 524, 'dungarpur': 520, 'hanumangarh': 517, 'jaipur i': 505, 'jaipur ii': 506, 'jaisalmer': 527, 'jalore': 533, 'jhalawar': 515, 'jhunjhunu': 510, 'jodhpur': 502, 'karauli': 525, 'kota': 503, 'nagaur': 532, 'pali': 529, 'pratapgarh': 682, 'rajsamand': 518, 'sawai madhopur': 534, 'sikar': 513, 'sirohi': 531, 'sri ganganagar': 509, 'tonk': 526, 'udaipur': 504, 'east sikkim': 535, 'north sikkim': 537, 'south sikkim': 538, 'west sikkim': 536, 'aranthangi': 779, 'ariyalur': 555, 'attur': 578, 'chengalpet': 565, 'chennai': 571, 'cheyyar': 778, 'coimbatore': 539, 'cuddalore': 547, 'dharmapuri': 566, 'dindigul': 556, 'erode': 563, 'kallakurichi': 552, 'kanchipuram': 557, 'kanyakumari': 544, 'karur': 559, 'kovilpatti': 780, 'krishnagiri': 562, 'madurai': 540, 'nagapattinam': 576, 'namakkal': 558, 'nilgiris': 577, 'palani': 564, 'paramakudi': 573, 'perambalur': 570, 'poonamallee': 575, 'pudukkottai': 546, 'ramanathapuram': 567, 'ranipet': 781, 'salem': 545, 'sivaganga': 561, 'sivakasi': 580, 'tenkasi': 551, 'thanjavur': 541, 'theni': 569, 'thoothukudi (tuticorin)': 554, 'tiruchirappalli': 560, 'tirunelveli': 548, 'tirupattur': 550, 'tiruppur': 568, 'tiruvallur': 572, 'tiruvannamalai': 553, 'tiruvarur': 574, 'vellore': 543, 'viluppuram': 542, 'virudhunagar': 549, 'adilabad': 582, 'bhadradri kothagudem': 583, 'hyderabad': 581, 'jagtial': 584, 'jangaon': 585, 'jayashankar bhupalpally': 586, 'jogulamba gadwal': 587, 'kamareddy': 588, 'karimnagar': 589, 'khammam': 590, 'kumuram bheem': 591, 'mahabubabad': 592, 'mahabubnagar': 593, 'mancherial': 594, 'medak': 595, 'medchal': 596, 'mulugu': 612, 'nagarkurnool': 597, 'nalgonda': 598, 'narayanpet': 613, 'nirmal': 599, 'nizamabad': 600, 'peddapalli': 601, 'rajanna sircilla': 602, 'rangareddy': 603, 'sangareddy': 604, 'siddipet': 605, 'suryapet': 606, 'vikarabad': 607, 'wanaparthy': 608, 'warangal(rural)': 609, 'warangal(urban)': 610, 'yadadri bhuvanagiri': 611, 'dhalai': 614, 'gomati': 615, 'khowai': 616, 'north tripura': 617, 'sepahijala': 618, 'south tripura': 619, 'unakoti': 620, 'west tripura': 621, 'agra': 622, 'aligarh': 623, 'ambedkar nagar': 625, 'amethi': 626, 'amroha': 627, 'auraiya': 628, 'ayodhya': 646, 'azamgarh': 629, 'badaun': 630, 'baghpat': 631, 'bahraich': 632, 'balarampur': 633, 'ballia': 634, 'banda': 635, 'barabanki': 636, 'bareilly': 637, 'basti': 638, 'bhadohi': 687, 'bijnour': 639, 'bulandshahr': 640, 'chandauli': 641, 'chitrakoot': 642, 'deoria': 643, 'etah': 644, 'etawah': 645, 'farrukhabad': 647, 'fatehpur': 648, 'firozabad': 649, 'gautam buddha nagar': 650, 'ghaziabad': 651, 'ghazipur': 652, 'gonda': 653, 'gorakhpur': 654, 'hapur': 656, 'hardoi': 657, 'hathras': 658, 'jalaun': 659, 'jaunpur': 660, 'jhansi': 661, 'kannauj': 662, 'kanpur dehat': 663, 'kanpur nagar': 664, 'kasganj': 665, 'kaushambi': 666, 'kushinagar': 667, 'lakhimpur kheri': 668, 'lalitpur': 669, 'lucknow': 670, 'maharajganj': 671, 'mahoba': 672, 'mainpuri': 673, 'mathura': 674, 'mau': 675, 'meerut': 676, 'mirzapur': 677, 'moradabad': 678, 'muzaffarnagar': 679, 'pilibhit': 680, 'prayagraj': 624, 'raebareli': 681, 'rampur': 683, 'saharanpur': 684, 'sambhal': 685, 'sant kabir nagar': 686, 'shahjahanpur': 688, 'shamli': 689, 'shravasti': 690, 'siddharthnagar': 691, 'sitapur': 692, 'sonbhadra': 693, 'sultanpur': 694, 'unnao': 695, 'varanasi': 696, 'almora': 704, 'bageshwar': 707, 'chamoli': 699, 'champawat': 708, 'dehradun': 697, 'haridwar': 702, 'nainital': 709, 'pauri garhwal': 698, 'pithoragarh': 706, 'rudraprayag': 700, 'tehri garhwal': 701, 'udham singh nagar': 705, 'uttarkashi': 703, 'alipurduar district': 710, 'bankura': 711, 'basirhat hd (north 24 parganas)': 712, 'birbhum': 713, 'bishnupur hd (bankura)': 714, 'cooch behar': 715, 'coochbehar': 783, 'dakshin dinajpur': 716, 'darjeeling': 717, 'diamond harbor hd (s 24 parganas)': 718, 'east bardhaman': 719, 'hoogly': 720, 'howrah': 721, 'jalpaiguri': 722, 'jhargram': 723, 'kalimpong': 724, 'kolkata': 725, 'malda': 726, 'murshidabad': 727, 'nadia': 728, 'nandigram hd (east medinipore)': 729, 'north 24 parganas': 730, 'paschim medinipore': 731, 'purba medinipore': 732, 'purulia': 733, 'rampurhat hd (birbhum)': 734, 'south 24 parganas': 735, 'uttar dinajpur': 736, 'west bardhaman': 737, 'daman': 138, 'diu': 139}

headers = {"Accept": "application/json", "Accept-Language": "hi_IN",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}


def district(update, context):
    flag = 0
    da = str(' '.join(context.args[:])).lower()
    # print(da)
    for day in range(0, 5):
        d3 = (datetime.now(IST) + timedelta(days=day)).strftime("%d-%m-%Y")
        d4 = data.get(da)
        if(d4 == None):
            update.message.reply_text("[-]Wrong District!\n")
            return
        url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={d4}&date={d3}"
        print(url)
        try:
            response = requests.get(url, headers=headers)
        except:
            update.message.reply_text("API Error!\n")
            return
        if response.status_code == 200:
            json_data = json.loads(response.text)
            if len(json_data["sessions"]):
                for session in json_data["sessions"]:
                    if session["available_capacity"] > 0:
                        msg = f"{session['vaccine']} available for {session['available_capacity']} (Age-{session['min_age_limit']}+) people on {session['date']} at {session['name']},{session['address']}\n"
                        update.message.reply_text(msg)
                        flag = 1
    if flag == 0:
        update.message.reply_text("No Slots found check later!")


def pincode(update, context):
    flag = 0
    if(len(context.args) == 1):
        pin = str(context.args[0])
    else:
        update.message.reply_text(
            "Please provide pin or type Command properly!\n")
        return
    for day in range(0, 5):
        d3 = (datetime.now(IST) + timedelta(days=day)).strftime("%d-%m-%Y")
        url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pin}&date={d3}"
        print(url)
        try:
            response = requests.get(url, headers=headers)
        except:
            update.message.reply_text("API Error!\n")
            return
        if response.status_code == 200:
            json_data = json.loads(response.text)
            if len(json_data["sessions"]):
                for session in json_data["sessions"]:
                    # print(session)
                    if session["available_capacity"] > 0:
                        msg = f"{session['vaccine']} available for {session['available_capacity']} (Age-{session['min_age_limit']}+) people on {session['date']} at {session['name']},{session['address']}\n"
                        update.message.reply_text(msg)
                        flag = 1
    if flag == 0:
        update.message.reply_text("No slots found check later!")


def botpincode(update, context):

    if(len(context.args) == 3):
        pin = str(context.args[0])
        dosec = str(context.args[2])
        dose = 'available_capacity_dose'+dosec
        age = int(context.args[1])
    else:
        update.message.reply_text("Invalid Example- /botpincode 800001 18")
        return
    update.message.reply_text("Bot Started\n")
    while True:
        for day in range(0, 5):
            d3 = (datetime.now(IST) + timedelta(days=day)).strftime("%d-%m-%Y")

            url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pin}&date={d3}"
            print(url)
            try:
                response = requests.get(url, headers=headers)
            except:
                update.message.reply_text("API Error!\n")
                return
            if response.status_code == 200:
                # print(response.text)
                json_data = json.loads(response.text)
                if len(json_data["sessions"]):
                    for session in json_data["sessions"]:
                        if session[dose] > 0 and session["min_age_limit"] <= age:
                            msg = f"{session['vaccine']} available for {session[dose]} people  for Dose {dosec}  on {session['date']} at {session['name']},{session['address']}\n"
                            update.message.reply_text(msg)
                            return
        update.message.reply_text(
            "We'll notify when further slots Available!\n")
        sleep(TIME_GAP)


def help(update, context):
    msg = ''' 
	
	Programmed by, 

	Mahankali Prathyusha Lahari,
	IV CSE-1,MGIT.
    

    Check Instructions to  get slot details!!\n
    ---------------------------------------------\n

    ->Checks For Slots in this PinCode\n
    /pincode pin\n
    Example:/pincode 800001\n
    
    ->Checks For Slots in this District \n
    /district name\n
    Example: /district khammam\n
    
    ->Starts a Bot that checks continously district-wise \n
    /botdistrict district_name age dose\n
    Example: /botdistrict 800001 18 1\n

    
    ---------------------------------------------\n

'''
    update.message.reply_text(msg)


def main():
    updater = Updater(token=TOKEN, use_context=True, workers=10)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("district", district, run_async=True))
    dp.add_handler(CommandHandler("pincode", pincode, run_async=True))
    dp.add_handler(CommandHandler("botpincode", botpincode, run_async=True))
    dp.add_handler(CommandHandler("help", help, run_async=True))
    dp.add_handler(CommandHandler("start", help, run_async=True))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
