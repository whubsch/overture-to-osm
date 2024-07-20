from collections import Counter
import json
from overture_to_osm.process import process_place_props

# from ..src.overture_to_osm.process import process_place_props
# from ..src.overture_to_osm.resources import tags

with open("test_in.geojson", "r", encoding="utf-8") as f:
    contents: dict = json.load(f)
    count = []

    for each in contents["features"]:
        each["properties"] = process_place_props(each["properties"], confidence=0.8)
        # try:
        #     prim = tags.get(each["properties"]["categories"]["main"])
        #     if not prim:
        #         # print(each["properties"]["categories"]["main"])
        #         count.append(each["properties"]["categories"]["main"])

        # except KeyError:
        #     pass

    contents["features"] = [each for each in contents["features"] if each["properties"]]

    with open("test_out.geojson", "w+", encoding="utf-8") as f:
        json.dump(contents, f, indent=4)

    # print(len(count), len(contents["features"]))
    # print(Counter(count))