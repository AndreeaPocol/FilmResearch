fileNames = ["first_omdb_movies.json", "second_omdb_movies.json"]
filter = False # filter out movies less than 75 minutes long
includeAllCountries = True
releasedInCountryOfInterest = []
write = True # write data to a CSV

# https://www.sheffield.ac.uk/international/english-speaking-countries
englishSpeakingCountries = [
    "Antigua and Barbuda",
    "Australia",
    "Bahamas",
    "Barbados",
    "Belize",
    "Canada",
    "Dominica",
    "Grenada",
    "Guyana",
    "Ireland",
    "Jamaica",
    "Malta",
    "New Zealand",
    "St Kitts and Nevis",
    "St Lucia",
    "St Vincent And The Grenadines",
    "Trinidad and Tobago",
    "UK",
    "USA",
]

china = ["China"]

india = ["India"]

# https://www.worldometers.info/geography/how-many-countries-in-europe/
europeanCountries = [
    "Russia",
    "West Germany",
    "East Germany",
    "UK",
    "France",
    "Italy",
    "Spain",
    "Ukraine",
    "Poland",
    "Romania",
    "Netherlands",
    "Belgium",
    "Czech Republic",
    "Greece",
    "Portugal",
    "Sweden",
    "Hungary",
    "Belarus",
    "Austria",
    "Serbia",
    "Switzerland",
    "Bulgaria",
    "Denmark",
    "Finland",
    "Slovakia",
    "Norway",
    "Ireland",
    "Croatia",
    "Moldova",
    "Bosnia and Herzegovina",
    "Albania",
    "Lithuania",
    "North Macedonia",
    "Slovenia",
    "Latvia",
    "Estonia",
    "Montenegro",
    "Luxembourg",
    "Malta",
    "Iceland",
    "Andorra",
    "Monaco",
    "Liechtenstein",
    "San Marino",
    "Holy See",
]

# https://www.worldometers.info/geography/how-many-countries-in-asia/
asianCountries = [
    "China",
    "India",
    "Indonesia",
    "Pakistan",
    "Bangladesh",
    "Japan",
    "Philippines",
    "Vietnam",
    "Turkey",
    "Iran",
    "Thailand",
    "Myanmar",
    "South Korea",
    "Iraq",
    "Afghanistan",
    "Saudi Arabia",
    "Uzbekistan",
    "Malaysia",
    "Yemen",
    "Nepal",
    "North Korea",
    "Sri Lanka",
    "Kazakhstan",
    "Syria",
    "Cambodia",
    "Jordan",
    "Azerbaijan",
    "United Arab Emirates",
    "Tajikistan",
    "Israel",
    "Laos",
    "Lebanon",
    "Kyrgyzstan",
    "Turkmenistan",
    "Singapore",
    "Oman",
    "Palestine",
    "Kuwait",
    "Georgia",
    "Mongolia",
    "Armenia",
    "Qatar",
    "Bahrain",
    "Timor-Leste",
    "Cyprus",
    "Bhutan",
    "Maldives",
    "Brunei",
]

asianCountriesMinusChina = [
    "India",
    "Indonesia",
    "Pakistan",
    "Bangladesh",
    "Japan",
    "Philippines",
    "Vietnam",
    "Turkey",
    "Iran",
    "Thailand",
    "Myanmar",
    "South Korea",
    "Iraq",
    "Afghanistan",
    "Saudi Arabia",
    "Uzbekistan",
    "Malaysia",
    "Yemen",
    "Nepal",
    "North Korea",
    "Sri Lanka",
    "Kazakhstan",
    "Syria",
    "Cambodia",
    "Jordan",
    "Azerbaijan",
    "United Arab Emirates",
    "Tajikistan",
    "Israel",
    "Laos",
    "Lebanon",
    "Kyrgyzstan",
    "Turkmenistan",
    "Singapore",
    "Oman",
    "Palestine",
    "Kuwait",
    "Georgia",
    "Mongolia",
    "Armenia",
    "Qatar",
    "Bahrain",
    "Timor-Leste",
    "Cyprus",
    "Bhutan",
    "Maldives",
    "Brunei",
]

countriesOfInterest = englishSpeakingCountries
# countriesOfInterest = china
# countriesOfInterest = india
# countriesOfInterest = europeanCountries
# countriesOfInterest = asianCountries
# countriesOfInterest = asianCountriesMinusChina

genresToConsider = {
    "Horror": [],
    "Romance": [],
    "Comedy": [],
    "Action": [],
    "Adventure": [],
    "Animation": [],
    "Crime": [],
    "Drama": [],
}

numericGenresToConsider = {
    "Horror": 1,
    "Romance": 2,
    "Comedy": 3,
    "Action": 4,
    "Adventure": 5,
    "Animation": 6,
    "Crime": 7,
    "Drama": 8,
}


def releasedInCountryOfInterest(countries):
    for country in countries:
        if country in countriesOfInterest:
            return True
    return False
