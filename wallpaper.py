import math


def wallpaper(room_width, room_length, room_height, wallpaper_width, wallpaper_length, wallpaper_repeat):
    """
    >>> wallpaper(5, 6, 2.75, 1.06, 10, 0.64)
    11
    """

    room_perimeter = 2 * (room_width + room_length)

    panel_number_all = room_perimeter / wallpaper_width
    panel_number_all = math.ceil(panel_number_all)

    panel_number_wallpaper = wallpaper_length // (room_height + wallpaper_repeat)

    wallpaper_number = panel_number_all / panel_number_wallpaper
    wallpaper_number = math.ceil(wallpaper_number)
    return wallpaper_number


print("Для комнаты указанных размеров вам потребуется минимум",
      wallpaper(room_width=5, room_length=6, room_height=2.75, wallpaper_width=1.06,
                wallpaper_length=10, wallpaper_repeat=0.64),
      "рулонов.\n"
      "Но мы рекомендуем Вам дополнительно приобрести еще"
      " 1-2 рулона на случай возможного повреждения обоев, например, во время ремонта")

