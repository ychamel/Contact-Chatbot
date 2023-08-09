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
            "Maintenance": ["maintenance"],
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
    your needs.
    Benefits:
    • Down-payments starting from 20%
    • Financing up to 5 million EGP
    • Payment plans up to 5 years
    • Simple and fast procedures
    • Full service, starting from car licensing, insurance to installments
    • Insurance is optional
    """,
    "Trucks": """
        Whether you need heavy or light truck, with Contact, you can finance all types of new, used and
    imported trucks with easy and flexible procedures.
    Benefits:
    • Down-payments starting from 20%
    • Financing up to 5 million EGP
    • Payment plans up to 5 years
    • Simple and fast procedures
    """,
    "consumer_finance": """
        Buy what you need, and Contact will facilitate it through hassle-free shopping experience with the
    easiest and fastest approval and the widest merchant network, covering all your needs from products
    and services.
    Benefits:
    • No down-payment
    • Financing up to 1 million EGP
    • Payment plans up from 1 to 5 years
    • Easy and fast transactions, only with your National ID and mobile number
    • A wide network of retail outlets, merchants, and megastores
    """,
    "Education": """
        Looking for a brighter future for you and your children, Contact will finance the journey through all
    stages of local and international educational programs.
    Benefits:
    • No down-payment
    • Financing up to 1 million EGP
    • Payment plans up to 12 months for schools, universities, and courses
    • Payment plans up to 3 years for masters’ programs and 5 years for PHD
    • Simple and fast procedures
    """,
    "Club_membership": """
        Develop your children’s talents and help them practice their favorite sport, with Contact you can finance
    the membership of your aspired club in Egypt with the easiest and fastest procedures, and convenient
    payment plans.
    Benefits:
    • No down-payment
    
    • Financing up to 1 million EGP
    • Payment plans up to 5 years
    • Simple and fast procedures
    • Instant activation for membership
        """,
    "weddings_and_events_finance": """
        Enjoy a memorable and hassle-free celebration with Contact either a wedding, engagement, graduation,
    or birthday, Contact will finance your event through the simplest procedures and convenient
    installments.
    Benefits:
    • No down-payment
    • Financing up to 1 million EGP
    • Payment plans up to 3 years
    • Simple and fast procedures
        """,
    "home_interior": """
        Take your home to another level through the best interior design companies in Egypt, and Contact will
    finance you to design and finish your home with the largest financing value and convenient installment
    plans.
    Benefits:
    • No down-payment
    • Financing up to 2 million EGP
    • Payment plans up to 5 years
    • Simple and fast procedures
        """,
    "furniture": """
        Furnish your home with a new and unique design, and Contact will finance you through the widest and
    most diversified suppliers and showrooms to suit all styles and budgets.
    Benefits:
    • No down-payments
    • Financing up to 2 million EGP
    • Payment plans up to 5 years
    • Simple and fast procedures
    • The ability of combining different quotations in same request
        """,
    "home_equity": """
        Make the right step to your new home and Contact will finance you with the easiest and fastest
    procedures through the Home Finance program.
    Benefits:
    • 25% down-payment
    • Financing up to 6 million EGP
    • Payment plans up to 10 years.
    • Financing all types of Residential units (standalone and compound units)
        """,
    "home": """
        Get financed up to 50% against your home value with the Home Equity program from Contact.
    Benefits:
    • No down-payment
    • Financing up to 6 million EGP
    • Payment plans up to 5 years
    • Financing all types of Residential units (standalone and compound units)
        """,
    "maintenance": """
        Your home, Car or property needs maintenance, Contact made it easy and will finance your
    maintenance with the easiest procedures and convenient payment plans.
    Benefits:
    • No down-payment
    • Financing up to 1.5 million EGP
    • Payment plans up to 24 months
    • Simple and fast procedures
        """,
    "green": """
        If you need to develop your agricultural investment, Contact believes that agriculture development is
    the main pillar for economic growth, food security, and a cornerstone for a bright future. Contact will
    finance your agriculture investments to achieve environmental sustainability.
    Benefits
    • No down-payment
    • Financing up to 1.5 million EGP
    • Payment plans up to 5 years
    • Fastest and easiest procedures
        """,
    "Insurance_brokerage": """
    [Insurance Brokerage output (not supplied)]
    """,
    "electronic_payments": """
        Now with Contact Pay, you can easily and securely pay your mobile, electricity, gas, water bills and many
    other services at one place, through ContactNow mobile application or Contact branches all over Egypt.
    Payment services:
    • Electricity, gas, and water bills
    • Landline, mobile, internet and TV subscription
    • Transportation tickets
    • Insurance installments
    • Donations and NGOs
    • Clubs, schools, and university fees
        """,
    "Rewards_program": """
        With the Rewards Program enjoy a world of unlimited benefits that covers all your shopping needs.
    Collect Points with each Purchase and redeem them simply through a unique selected Partners network
    from the biggest brands in the Egyptian Market or pay Contact’s installments and administrative fees
    using your points credit.
        """,
    "Contact_homes": """""",
    "Referral_program": """
        For Contact customers now you can nominate your friends and receive free points and exclusive
    discounts to purchase from Rewards Program partners or pay your installments and administrative fees.
    The partnership between Contact and Coldwell Banker, grants you advantage of an endless world of
    benefits and offers. Providing you with a great deal of discounts and special prices. It is a new beginning
    for a perfect life.
        """,
    "leasing": """
        If you’re looking to develop your business, Contact will help you with the best financing services and
    easiest solutions that guarantee the speed and success to reach your goals.
    Benefits
    • Down payment starting from 10% according to the asset type
    • Payment plans up to 5 years
    • Comprehensive and wide suppliers’ network and world-class manufacturers
    • Different plans customized to suit your needs
    • Efficient and fast process
    • Medical devices and equipment financing for hospitals, clinics, medical centers, and
    ambulance services.
    • Transportation financing from passenger vehicles to commercial vehicles (light, medium,
    heavy trucks) in addition to busses and vans.
        """,
    "factoring": """
        If you need to increase your business cash flow, Contact will ensure empowering your business and
    boosting your working capital long before collecting bills and extended payment terms, with less
    burdens, flexibility, innovative and specialized solutions.
    Benefits
    • Immediate access for cash
    • Easier and faster approval process than traditional bank lending
    • Covering a diversity of industries
        """,
    "branches": """
        Opening hours from 9 am to 5:30 pm (opening hours may vary during Ramadan and public holidays)
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
    Left to use: ….... EGP
    Total Limit: …….. EGP
    """,
    "check_or_pay_installments": """
    Due payments….
    To pay your due installments, visit (https://contacteg.page.link/app)
    """
}
