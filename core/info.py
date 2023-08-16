from enum import Enum

options = {
    "Retail services": {
        "Financing services": {
            "Auto & Trucks": [
                "Automobile",
                "Trucks"
            ],
            "consumer": ["consumer_finance"],
            "Education & Clubs memberships": ["Education", "Club_membership"],
            "Weddings and Events": ["weddings_and_events_finance"],
            "Home interior & Furniture": ["home_interior", "furniture"],
            "Mortgage": ["home_equity", "home"],
            "maintenance": ["maintenance"],
            "Green Finance": ["green"]
        },
        "Insurance services": ["Insurance_brokerage"],
        "Electronic payments": ["electronic_payments"],
        "Customer programs": ["Rewards_program", "Contact_homes", "Referral_program"]
    },
    "Corporate & Medical centers": {
        "Leasing": ["leasing"],
        "Factoring": ["factoring"],
        "Insurance Brokerage": ["Insurance_brokerage"]
    },
    "Branches": ["branches"],
    "Complaints and suggestions": ["Complaints_and_suggestions"],
    "Evaluation and feedback": ["Evaluation_and_feedback"],
    "Reward points": ["reward_points"],
    "Credit limit": ["credit_limit"],
    "Check & pay installments": ["check_or_pay_installments"],
}

outputs = {
    "Automobile": """
        If you need to buy a new or used car, Contact will provide you with distinguished financing solutions for
    all brands and models with flexibility in procedures and a big variety of installment plans tailored to suit
    your needs. \n
    Benefits: \n
    • Down-payments starting from 20% \n
    • Financing up to 5 million EGP \n
    • Payment plans up to 5 years \n
    • Simple and fast procedures \n
    • Full service, starting from car licensing, insurance to installments \n
    • Insurance is optional \n
    """,
    "Trucks": """
        Whether you need heavy or light truck, with Contact, you can finance all types of new, used and
    imported trucks with easy and flexible procedures. \n
    Benefits: \n
    • Down-payments starting from 20% \n
    • Financing up to 5 million EGP \n
    • Payment plans up to 5 years \n
    • Simple and fast procedures \n
    """,
    "consumer_finance": """
        Buy what you need, and Contact will facilitate it through hassle-free shopping experience with the
    easiest and fastest approval and the widest merchant network, covering all your needs from products
    and services. \n
    Benefits: \n
    • No down-payment \n
    • Financing up to 1 million EGP \n
    • Payment plans up from 1 to 5 years \n
    • Easy and fast transactions, only with your National ID and mobile number \n
    • A wide network of retail outlets, merchants, and megastores \n
    """,
    "Education": """
        Looking for a brighter future for you and your children, Contact will finance the journey through all
    stages of local and international educational programs. \n
    Benefits: \n
    • No down-payment \n
    • Financing up to 1 million EGP \n
    • Payment plans up to 12 months for schools, universities, and courses \n
    • Payment plans up to 3 years for masters’ programs and 5 years for PHD \n
    • Simple and fast procedures \n
    """,
    "Club_membership": """
        Develop your children’s talents and help them practice their favorite sport, with Contact you can finance
    the membership of your aspired club in Egypt with the easiest and fastest procedures, and convenient
    payment plans. \n
    Benefits:\n
    • No down-payment \n
    
    • Financing up to 1 million EGP \n
    • Payment plans up to 5 years \n
    • Simple and fast procedures \n
    • Instant activation for membership \n
        """,
    "weddings_and_events_finance": """
        Enjoy a memorable and hassle-free celebration with Contact either a wedding, engagement, graduation,
    or birthday, Contact will finance your event through the simplest procedures and convenient
    installments. \n
    Benefits: \n
    • No down-payment \n
    • Financing up to 1 million EGP \n
    • Payment plans up to 3 years \n
    • Simple and fast procedures \n
        """,
    "home_interior": """
        Take your home to another level through the best interior design companies in Egypt, and Contact will
    finance you to design and finish your home with the largest financing value and convenient installment
    plans. \n
    Benefits: \n
    • No down-payment \n
    • Financing up to 2 million EGP \n
    • Payment plans up to 5 years \n
    • Simple and fast procedures\n
        """,
    "furniture": """
        Furnish your home with a new and unique design, and Contact will finance you through the widest and
    most diversified suppliers and showrooms to suit all styles and budgets.\n
    Benefits: \n
    • No down-payments \n
    • Financing up to 2 million EGP \n
    • Payment plans up to 5 years \n
    • Simple and fast procedures \n
    • The ability of combining different quotations in same request \n
        """,
    "home_equity": """
        Make the right step to your new home and Contact will finance you with the easiest and fastest
    procedures through the Home Finance program. \n
    Benefits: \n
    • 25% down-payment \n
    • Financing up to 6 million EGP \n
    • Payment plans up to 10 years. \n
    • Financing all types of Residential units (standalone and compound units) \n
        """,
    "home": """
        Get financed up to 50% against your home value with the Home Equity program from Contact. \n
    Benefits: \n
    • No down-payment \n
    • Financing up to 6 million EGP \n
    • Payment plans up to 5 years\n
    • Financing all types of Residential units (standalone and compound units) \n
        """,
    "maintenance": """
        Your home, Car or property needs maintenance, Contact made it easy and will finance your
    maintenance with the easiest procedures and convenient payment plans. \n
    Benefits: \n
    • No down-payment \n
    • Financing up to 1.5 million EGP \n
    • Payment plans up to 24 months \n
    • Simple and fast procedures \n
        """,
    "green": """
        If you need to develop your agricultural investment, Contact believes that agriculture development is
    the main pillar for economic growth, food security, and a cornerstone for a bright future. Contact will
    finance your agriculture investments to achieve environmental sustainability. \n
    Benefits \n
    • No down-payment \n
    • Financing up to 1.5 million EGP \n
    • Payment plans up to 5 years \n
    • Fastest and easiest procedures \n
        """,
    "Insurance_brokerage": """
    [Insurance Brokerage output (not supplied)]
    """,
    "electronic_payments": """
        Now with Contact Pay, you can easily and securely pay your mobile, electricity, gas, water bills and many
    other services at one place, through ContactNow mobile application or Contact branches all over Egypt. \n
    Payment services: \n
    • Electricity, gas, and water bills \n
    • Landline, mobile, internet and TV subscription \n
    • Transportation tickets \n
    • Insurance installments \n
    • Donations and NGOs \n
    • Clubs, schools, and university fees \n
        """,
    "Rewards_program": """
        With the Rewards Program enjoy a world of unlimited benefits that covers all your shopping needs.
    Collect Points with each Purchase and redeem them simply through a unique selected Partners network
    from the biggest brands in the Egyptian Market or pay Contact’s installments and administrative fees
    using your points credit. \n
        """,
    "Contact_homes": """""",
    "Referral_program": """
        For Contact customers now you can nominate your friends and receive free points and exclusive
    discounts to purchase from Rewards Program partners or pay your installments and administrative fees.
    The partnership between Contact and Coldwell Banker, grants you advantage of an endless world of
    benefits and offers. Providing you with a great deal of discounts and special prices. It is a new beginning
    for a perfect life. \n
        """,
    "leasing": """
        If you’re looking to develop your business, Contact will help you with the best financing services and
    easiest solutions that guarantee the speed and success to reach your goals. \n
    Benefits \n
    • Down payment starting from 10% according to the asset type \n
    • Payment plans up to 5 years \n
    • Comprehensive and wide suppliers’ network and world-class manufacturers \n
    • Different plans customized to suit your needs \n
    • Efficient and fast process \n
    • Medical devices and equipment financing for hospitals, clinics, medical centers, and
    ambulance services. \n
    • Transportation financing from passenger vehicles to commercial vehicles (light, medium,
    heavy trucks) in addition to busses and vans. \n
        """,
    "factoring": """
        If you need to increase your business cash flow, Contact will ensure empowering your business and
    boosting your working capital long before collecting bills and extended payment terms, with less
    burdens, flexibility, innovative and specialized solutions. \n
    Benefits \n
    • Immediate access for cash \n
    • Easier and faster approval process than traditional bank lending \n
    • Covering a diversity of industries \n
        """,
    "branches": """
        Opening hours from 9 am to 5:30 pm (opening hours may vary during Ramadan and public holidays) \n
    Misr El-Gedida (Press 1)
    
    Heliopolis (Press 2)
    Nasr City (Press 3)
    New Cairo (Press 4)
    Maadi (Press 5)
    Zamalek (Press 6)
    Dokki (Press 7)
    Giza (Press 8)
    Alexandria (Press 9)
    Alexandria Roshdy (Press 10)
    Damanhur (Press 11)
    Mansoura (Press 12)
    Zagazig (Press 13)
    Tanta (Press 14)
    Benha (Press 15)
    Al Minufya (Press 16)
    Port Said (Press 17)
    Damietta (Press 18)
    Kafr el Sheikh (Press 19)
    Ismailia (Press 20)
    Suez (Press 21)
    Sharm El Sheikh (Press 22)
    Hurghada (Press 23)
    Beni Suef (Press 24)
    Faiyum (Press 25)
    Minya (Press 26)
    Asyut (Press 27)
    Sohag (Press 28)
    Qena (Press 29)
    Luxor (Press 30)
    
    Aswan (Press 31)
    Mini-Abu Kibir (Press 32)
    Shubra (Press 33)
    Faisal Branch (Press 34)
    El Sadat City (Press 35)
    Mini-El-Alamein (Press 36)
    El-Abaseya (Press 37)
    Mini-Kafr El-Dawar (Press 38)
    Rehab (Press 39)
    Alexandria Corniche (Press 40)
    Mini-Beni Mazar (Press 41)
    El Gouna (Press 42)
    El-Mahalla El-Kubra (Press 43)
    Mini-Mallawi (Press 44)
    Mini-Biba (Press 45)
    Mini-Mit Ghamr (Press 46)
    Mini-Damietta (Press 47)
    Mini-Badrshein (Press 48)
    October (Press 49)
    Haram (Press 50)
    Obour (Press 51)
    Mini-Qus (Press 52)
    El-Bahr El-Aazam (Press 53)
    El Mokattam (Press 54)
    Shubra Al-Khaymah (Press 55)
    El-Agamy(Press56)
        """,
    "Complaints_and_suggestions": """
    For complaints, please fill the following form: [link]
    """,
    "Evaluation_and_feedback": """
    For complaints, please fill the following form: [link]
    """,
    "reward_points": """
    [Reward points bot]
    """,
    "credit_limit": """
    Left to use: 50000 EGP \n
    Total Limit: 100000 EGP \n
    """,
    "check_or_pay_installments": """
    Due payments 2000 EGP \n
    To pay your due installments, visit (https://contacteg.page.link/app) \n
    """
}

for_more_info = """
For more information visit our website: www.contact.eg \n
Download Contact Brochure: bit.ly/3YpRsnV \n
Download Contact mobile app: https://contacteg.page.link/app \n
Visit our social media pages: https://www.facebook.com/ContactEg \n
Or call 16177 \n
"""

products = ['Automobile', 'Trucks', 'consumer_finance', 'Education', 'Club_membership', 'weddings_and_events_finance',
            'home_interior', 'furniture', 'home_equity', 'home', 'maintenance', 'green', 'Insurance_brokerage',
            'electronic_payments', 'Contact_homes', 'leasing', 'factoring']
know_more = ['Rewards_program', 'Referral_program']
others = ['branches', 'Complaints_and_suggestions', 'Evaluation_and_feedback', 'reward_points']


class States(Enum):
    main = 'main'
    product = 'product'
    know_more = 'know_more'
    others = 'others'


def get_question(state):
    if state == States.main:
        return ""
    if state == States.product:
        return "Are you interested in that product?"
    if state == States.know_more:
        return "Do you want to know more about that program?"
    if state == States.others:
        return ""
    return ""


def get_state(key):
    """
    Get the type of key and returns the program state
    :param key:
    :return:
    """
    if key in products:
        return States.product
    elif key in know_more:
        return States.know_more
    elif key in others:
        return States.others
    return States.main


def get_key(phrase):
    """
    checks which key is related to this phrase
    :param phrase:
    :return:
    """
    for key in outputs.keys():
        if key in phrase:
            return key
    for key in options.keys():
        if key in phrase and type(options[key]) is list and len(options[key]) == 1:
            return options[key][0]
    return None
