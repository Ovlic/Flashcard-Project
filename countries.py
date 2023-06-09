import random, datetime

# Get seed, so questions are the same for one day and change the next day
# x = datetime.datetime.today().strftime("%Y:%m:%d")
# random.seed(x)


countries = [
    {'country': 'Afghanistan', 'capital': 'Kabul'},
    {'country': 'Albania', 'capital': 'Tirana'},
    {'country': 'Algeria', 'capital': 'Algiers'},
    {'country': 'American Samoa (USA)', 'capital': 'Pago Pago'},
    {'country': 'Andorra', 'capital': 'Andorra La Vella'},
    {'country': 'Angola', 'capital': 'Luanda'},
    {'country': 'Antigua and Barbuda', 'capital': 'Saint Johns'},
    {'country': 'Argentina', 'capital': 'Buenos Aires'},
    {'country': 'Armenia', 'capital': 'Yerevan'},
    {'country': 'Australia', 'capital': 'Canberra'},
    {'country': 'Austria', 'capital': 'Vienna'},
    {'country': 'Azerbaijan', 'capital': 'Baku'},
    {'country': 'Bahamas', 'capital': 'Nassau'},
    {'country': 'Bahrain', 'capital': 'Manama'},
    {'country': 'Bangladesh', 'capital': 'Dhaka'},
    {'country': 'Barbados', 'capital': 'Bridgetown'},
    {'country': 'Belarus', 'capital': 'Minsk'},
    {'country': 'Belgium', 'capital': 'Brussels'},
    {'country': 'Belize', 'capital': 'Belmopan'},
    {'country': 'Benin', 'capital': 'Porto-Novo'},
    {'country': 'Bhutan', 'capital': 'Thimphu'},
    {'country': 'Bolivia', 'capital': 'Sucre'},
    {'country': 'Bosnia and Herzegovina', 'capital': 'Sarajevo'},
    {'country': 'Botswana', 'capital': 'Gaborone'},
    {'country': 'Brazil', 'capital': 'Brasilia'},
    {'country': 'Brunei', 'capital': 'Bandar Seri Begawan'},
    {'country': 'Bulgaria', 'capital': 'Sofia'},
    {'country': 'Burkina Faso', 'capital': 'Ouagadougou'},
    {'country': 'Burundi', 'capital': 'Bujumbura'},
    {'country': 'Cambodia', 'capital': 'Phnom Penh'},
    {'country': 'Cameroon', 'capital': 'Yaoundé'},
    {'country': 'Canada', 'capital': 'Ottawa'},
    {'country': 'Cape Verde', 'capital': 'Praia'},
    {'country': 'Central African Republic', 'capital': 'Bangui'},
    {'country': 'Chad', 'capital': "N'Djamena"},
    {'country': 'Chile', 'capital': 'Santiago'},
    {'country': 'China', 'capital': 'Beijing'},
    {'country': 'Colombia', 'capital': 'Bogotá'},
    {'country': 'Comoros', 'capital': 'Moroni'},
    {'country': 'Cook Islands (New Zealand)', 'capital': 'Avarua'},
    {'country': 'Costa Rica', 'capital': 'San Jose'},
    {'country': 'Croatia', 'capital': 'Zagreb'},
    {'country': 'Cuba', 'capital': 'Havana'},
    {'country': 'Cyprus', 'capital': 'Nicosia'},
    {'country': 'Czech Republic', 'capital': 'Prague'},
    {'country': 'D.R Congo', 'capital': 'Kinshasa'},
    {'country': 'Denmark', 'capital': 'Copenhagen'},
    {'country': 'Djibouti', 'capital': 'Djibouti-city'},
    {'country': 'Dominica', 'capital': 'Roseau'},
    {'country': 'Dominican Republic', 'capital': 'Santo Domingo'},
    {'country': 'Ecuador', 'capital': 'Quito'},
    {'country': 'Egypt', 'capital': 'Cairo'},
    {'country': 'El Salvador', 'capital': 'San Salvador'},
    {'country': 'Equatorial Guinea', 'capital': 'Malabo'},
    {'country': 'Eritrea', 'capital': 'Asmara'},
    {'country': 'Estonia', 'capital': 'Tallinn'},
    {'country': 'Ethiopia', 'capital': 'Addis Ababa'},
    {'country': 'Fiji', 'capital': 'Suva'},
    {'country': 'Finland', 'capital': 'Helsinki'},
    {'country': 'France', 'capital': 'Paris'},
    {'country': 'French Guiana (France)', 'capital': 'Cayenne'},
    {'country': 'Gabon', 'capital': 'Libreville'},
    {'country': 'Gambia', 'capital': 'Banjul'},
    {'country': 'Georgia', 'capital': 'Tbilisi'},
    {'country': 'Germany', 'capital': 'Berlin'},
    {'country': 'Ghana', 'capital': 'Accra'},
    {'country': 'Greece', 'capital': 'Athens'},
    {'country': 'Greenland (Denmark)', 'capital': 'Nuuk'},
    {'country': 'Grenada', 'capital': "St. George's"},
    {'country': 'Guatemala', 'capital': 'Guatemala City'},
    {'country': 'Guinea', 'capital': 'Conakry'},
    {'country': 'Guinea-Bissau', 'capital': 'Bissau'},
    {'country': 'Guyana', 'capital': 'Georgetown'},
    {'country': 'Haiti', 'capital': 'Port-au-prince'},
    {'country': 'Honduras', 'capital': 'Tegucigalpa'},
    {'country': 'Hungary', 'capital': 'Budapest'},
    {'country': 'Iceland', 'capital': 'Reykjavik'},
    {'country': 'India', 'capital': 'New Delhi'},
    {'country': 'Indonesia', 'capital': 'Jakarta'},
    {'country': 'Iran', 'capital': 'Tehran'},
    {'country': 'Iraq', 'capital': 'Baghdad'},
    {'country': 'Ireland', 'capital': 'Dublin'},
    {'country': 'Isle of Man (UK)', 'capital': 'Douglas'},
    {'country': 'Israel', 'capital': 'Jerusalem'},
    {'country': 'Italy', 'capital': 'Rome'},
    {'country': 'Ivory Coast', 'capital': 'Yamoussoukro'},
    {'country': 'Jamaica', 'capital': 'Kingston'},
    {'country': 'Japan', 'capital': 'Tokyo'},
    {'country': 'Jordan', 'capital': 'Amman'},
    {'country': 'Kazakhstan', 'capital': 'Astana'},
    {'country': 'Kenya', 'capital': 'Nairobi'},
    {'country': 'Kiribati', 'capital': 'Tarawa'},
    {'country': 'Kosovo', 'capital': 'Pristina'},
    {'country': 'Kuwait', 'capital': 'Kuwait City'},
    {'country': 'Kyrgyzstan', 'capital': 'Bishkek'},
    {'country': 'Laos', 'capital': 'Vientiane'},
    {'country': 'Latvia', 'capital': 'Riga'},
    {'country': 'Lebanon', 'capital': 'Beirut'},
    {'country': 'Lesotho', 'capital': 'Maseru'},
    {'country': 'Liberia', 'capital': 'Monrovia'},
    {'country': 'Libya', 'capital': 'Tripoli'},
    {'country': 'Liechtenstein', 'capital': 'Vaduz'},
    {'country': 'Lithuania', 'capital': 'Vilnius'},
    {'country': 'Luxembourg', 'capital': 'Luxembourg'},
    {'country': 'Macedonia', 'capital': 'Skopje'},
    {'country': 'Madagascar', 'capital': 'Antananarivo'},
    {'country': 'Malawi', 'capital': 'Lilongwe'},
    {'country': 'Malaysia', 'capital': 'Kuala Lumpur'},
    {'country': 'Maldives', 'capital': 'Malé'},
    {'country': 'Mali', 'capital': 'Bamako'},
    {'country': 'Malta', 'capital': 'Valletta'},
    {'country': 'Marshall Islands', 'capital': 'Majuro'},
    {'country': 'Mauritania', 'capital': 'Nouakchott'},
    {'country': 'Mauritius', 'capital': 'Port Louis'},
    {'country': 'Mexico', 'capital': 'Mexico City'},
    {'country': 'Micronesia', 'capital': 'Palikir'},
    {'country': 'Moldova', 'capital': 'Chisinau'},
    {'country': 'Monaco', 'capital': 'Monaco'},
    {'country': 'Mongolia', 'capital': 'Ulan Bator'},
    {'country': 'Montenegro', 'capital': 'Podgorica'},
    {'country': 'Montserrat (UK)', 'capital': 'Brades, Plymouth'},
    {'country': 'Morocco', 'capital': 'Rabat'},
    {'country': 'Mozambique', 'capital': 'Maputo'},
    {'country': 'Myanmar', 'capital': 'Naypyidaw'},
    {'country': 'Namibia', 'capital': 'Windhoek'},
    {'country': 'Nauru', 'capital': 'Yaren'},
    {'country': 'Nepal', 'capital': 'Kathmandu'},
    {'country': 'Netherlands', 'capital': 'Amsterdam'},
    {'country': 'New Zealand', 'capital': 'Wellington'},
    {'country': 'Nicaragua', 'capital': 'Managua'},
    {'country': 'Niger', 'capital': 'Niamey'},
    {'country': 'Nigeria', 'capital': 'Abuja'},
    {'country': 'Norfolk Island (Australia)', 'capital': 'Kingston'},
    {'country': 'North Korea', 'capital': 'Pyongyang'},
    {'country': 'Norway', 'capital': 'Oslo'},
    {'country': 'Oman', 'capital': 'Muscat'},
    {'country': 'Pakistan', 'capital': 'Islamabad'},
    {'country': 'Palau', 'capital': 'Ngerulmud'},
    {'country': 'Palestine', 'capital': 'Ramallah and Gaza'},
    {'country': 'Panama', 'capital': 'Panama City'},
    {'country': 'Papua New Guinea', 'capital': 'Port Moresby'},
    {'country': 'Paraguay', 'capital': 'Asunción'},
    {'country': 'Peru', 'capital': 'Lima'},
    {'country': 'Philippines', 'capital': 'Manila'},
    {'country': 'Poland', 'capital': 'Warsaw'},
    {'country': 'Portugal', 'capital': 'Lisbon'},
    {'country': 'Puerto Rico', 'capital': 'San Juan'},
    {'country': 'Qatar', 'capital': 'Doha'},
    {'country': 'Republic of the Congo', 'capital': 'Brazzaville'},
    {'country': 'Romania', 'capital': 'Bucharest'},
    {'country': 'Russia', 'capital': 'Moscow'},
    {'country': 'Rwanda', 'capital': 'Kigali'},
    {'country': 'Saint Kitts and Nevis', 'capital': 'Basseterre'},
    {'country': 'Saint Lucia', 'capital': 'Castries'},
    {'country': 'Saint Vincent and the Grenadines', 'capital': 'Kingstown'},
    {'country': 'Samoa', 'capital': 'Apia'},
    {'country': 'San Marino', 'capital': 'San Marino'},
    {'country': 'Sao Tome and Principe', 'capital': 'São Tomé'},
    {'country': 'Saudi Arabia', 'capital': 'Riyadh'},
    {'country': 'Senegal', 'capital': 'Dakar'},
    {'country': 'Serbia', 'capital': 'Belgrade'},
    {'country': 'Seychelles', 'capital': 'Victoria'},
    {'country': 'Sierra Leone', 'capital': 'Freetown'},
    {'country': 'Singapore', 'capital': 'Singapore'},
    {'country': 'Sint Maarten (Netherlands)', 'capital': 'Philipsburg'},
    {'country': 'Slovakia', 'capital': 'Bratislava'},
    {'country': 'Slovenia', 'capital': 'Ljubljana'},
    {'country': 'Solomon Islands', 'capital': 'Honiara'},
    {'country': 'Somalia', 'capital': 'Mogadishu'},
    {'country': 'South Africa', 'capital': 'Cape Town'},
    {'country': 'South Korea', 'capital': 'Seoul'},
    {'country': 'South Sudan', 'capital': 'Juba'},
    {'country': 'Spain', 'capital': 'Madrid'},
    {'country': 'Sri Lanka', 'capital': 'Sri Jayawardenapura-kotte'},
    {'country': 'Sudan', 'capital': 'Khartoum'},
    {'country': 'Suriname', 'capital': 'Paramaribo'},
    {'country': 'Swaziland', 'capital': 'Mata-utu'},
    {'country': 'Sweden', 'capital': 'Stockholm'},
    {'country': 'Switzerland', 'capital': 'Bern'},
    {'country': 'Syria', 'capital': 'Damascus'},
    {'country': 'Taiwan', 'capital': 'Taipei'},
    {'country': 'Tajikistan', 'capital': 'Dushanbe'},
    {'country': 'Tanzania', 'capital': 'Dodoma'},
    {'country': 'Thailand', 'capital': 'Bangkok'},
    {'country': 'Togo', 'capital': 'Lome'},
    {'country': 'Tokelau (New Zealand)', 'capital': 'Nukunonu, Atafu,Tokelau'},
    {'country': 'Tonga', 'capital': 'Nukuʻalofa'},
    {'country': 'Transnistria', 'capital': 'Tiraspol'},
    {'country': 'Trinidad and Tobago', 'capital': 'Port Of Spain'},
    {'country': 'Tunisia', 'capital': 'Tunis'},
    {'country': 'Turkey', 'capital': 'Ankara'},
    {'country': 'Turkmenistan', 'capital': 'Ashgabat'},
    {'country': 'Tuvalu', 'capital': 'Funafuti'},
    {'country': 'Uganda', 'capital': 'Kampala'},
    {'country': 'Ukraine', 'capital': 'Kiev'},
    {'country': 'United Arab Emirates', 'capital': 'Abu Dhabi'},
    {'country': 'United Kingdom', 'capital': 'London'},
    {'country': 'United States', 'capital': 'Washington D.C.'},
    {'country': 'Uruguay', 'capital': 'Montevideo'},
    {'country': 'Uzbekistan', 'capital': 'Tashkent'},
    {'country': 'Vanuatu', 'capital': 'Port Vila'},
    {'country': 'Vatican City', 'capital': 'Vatican City'},
    {'country': 'Venezuela', 'capital': 'Caracas'},
    {'country': 'Vietnam', 'capital': 'Hanoi'},
    {'country': 'Yemen', 'capital': "Sana'a"},
    {'country': 'Zambia', 'capital': 'Lusaka'},
    {'country': 'Zimbabwe', 'capital': 'Harare'},
]

def update_seed():
    x = datetime.datetime.today().strftime("%Y:%m:%d")
    random.seed(x)
    return None

def get_random_country():
    return random.choice(countries)

def get_random_capital() -> str:
    return random.choice(countries)['capital']

def get_three_capitals() -> list:
    """Return a list of three random capitals in flask wtforms format
    [("TextLabel", "value"), ...])]"""
    return [(c['capital'], c['capital']) for c in random.sample(countries, 3)]