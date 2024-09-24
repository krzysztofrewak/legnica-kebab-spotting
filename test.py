import json


def is_proper_coordinate(value):
    value = str(value)
    parts = value.split(".")

    if not len(parts) == 2:
        return False

    if parts[0].startswith("-"):
        if not parts[0][1:].isnumeric():
            return False
    else:
        if not parts[0].isnumeric():
            return False

    if parts[1].startswith("-"):
        if not parts[1][1:].isnumeric():
            return False
    else:
        if not parts[1].isnumeric():
            return False

    return True

with open("markers.json", encoding="utf-8") as file:
	markers = json.loads(file.read())
	i = 0

	for marker in markers:
		assert isinstance(marker["name"], str), "Element {}. of markers.json file name should be a string".format(i + 1)
		assert isinstance(marker["details"], str), "Element {}. of markers.json file details should be a string".format(i + 1)
		assert is_proper_coordinate(marker["location"]["coordinates"][0]), "Element {}. of markers.json file latitude should be a proper coordinate".format(i + 1)
		assert is_proper_coordinate(marker["location"]["coordinates"][1]), "Element {}. of markers.json file longitude should be a proper coordinate".format(i + 1)
		assert isinstance(marker["location"]["country"], str), "Element {}. of markers.json file country should be a string".format(i + 1)
		assert isinstance(marker["location"]["city"], str), "Element {}. of markers.json file city should be a string".format(i + 1)
		assert isinstance(marker["status"], str), "Element {}. of markers.json file city should be a string".format(i + 1)
		assert marker["status"] in ["placed", "removed"], "Element {}. of markers.json file status should have on of possible options".format(i + 1)
		i = i + 1
