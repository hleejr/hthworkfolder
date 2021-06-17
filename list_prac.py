'''
Change “Oakland” to “San Francisco”
Change “New York City” to “Brooklyn”
Change “Los Angeles” to “Hollywood”
Change “Miami” to “Tampa”


'''

US_cities = [ "Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "New Orleans" ]

fav_anime = [ "One Piece", "Bleach", "Fullmetal Alchemist", "Tokyo Ghoul", "The Disatrous Life of Saiki K." ]
fav_anime[0] = "YuYu Hakasho"

US_cities.append("New Jersey")
US_cities.extend(fav_anime)
US_cities.insert(7, "Washington, D.C.")

del US_cities[7]
US_cities.pop(0)
US_cities.remove("Boston")

