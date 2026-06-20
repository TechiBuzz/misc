# ICONS


class Icons:
    CLOUDY = "icons/cloud.png"
    RAINY = "icons/rain.png"
    SNOWY = "icons/snow.png"
    SUNNY = "icons/sun.png"
    THUNDERSTORM = "icons/thunderstorm.png"

    LOCATION = "icons/location.png"

    desc_to_image = {
        "cloudy": CLOUDY,
        "rainy": RAINY,
        "snowy": SNOWY,
        "sunny": SUNNY,
        "thunderstorm": THUNDERSTORM,
    }


def get_weather_category(icon_number):
    sunny = [1, 2, 3, 5]
    cloudy = [4, 6, 7, 8, 11]
    rainy = [12, 13, 14, 18, 26]
    snowy = [19, 20, 21, 22, 23, 24, 25, 29]
    thunderstorm = [15, 16, 17]

    if icon_number in sunny:
        return Icons.SUNNY
    elif icon_number in cloudy:
        return Icons.CLOUDY
    elif icon_number in rainy:
        return Icons.RAINY
    elif icon_number in snowy:
        return Icons.SNOWY
    elif icon_number in thunderstorm:
        return Icons.THUNDERSTORM
    else:
        return Icons.SUNNY


class Fonts:
    WEATHER_HEADER = ("Source Code Pro", 25, "bold")
    WEATHER_LABELS = ("Liberation Mono", 13, "normal")

    INPUT_HEADER = ("Source Code Pro", 20, "bold")
    INPUT_DROPDOWN_SELECTED = ("Liberation Mono", 13, "bold")
    INPUT_DROPDOWN = ("Liberation Mono", 13, "normal")

    LOADING = ("Source Code Pro", 45, "bold")

    """ To use in case we gotta use windows for some bad reason"""
    # WEATHER_HEADER = ("Consolas", 25, "bold")
    # WEATHER_LABELS = ("Consolas", 13, "normal")
    # INPUT_HEADER = ("Consolas", 20, "bold")
    # INPUT_DROPDOWN_SELECTED = ("Consolas", 13, "bold")
    # INPUT_DROPDOWN = ("Consolas", 13, "normal")
    # LOADING = ("Consolas", 45, "bold")
