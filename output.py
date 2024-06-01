import json

data = {
    "pools": [
        {
            "rolls": {
                "min": 1,
                "max": 3
            },
            "bonus_rolls": 1,
            "entries": [

            ]
        }
    ]
}

tools = open("objects/含耐久物品.alt", 'r', encoding="utf-8").read().splitlines()
tools_widget = 2
stuff = open("objects/一般性物品.alt", 'r', encoding="utf-8").read().splitlines()
stuff_widget = 3
cheap = open("objects/廉价性物品.alt", 'r', encoding="utf-8").read().splitlines()
cheap_widget = 6
special = open("objects/稀有性物品.alt", 'r', encoding="utf-8").read().splitlines()
special_widget = 2
potion = open("objects/药水物品.alt", 'r', encoding="utf-8").read().splitlines()
potion_widget = 1
effects = open(".\\especial\\药水效果", "r", encoding="utf-8").read().splitlines()

all_fit = len(tools) * tools_widget + len(stuff) * stuff_widget + len(special) * special_widget + len(potion) * len(
    effects) * potion_widget + cheap_widget * len(cheap)


print(f"Added {len(cheap)} cheap stuff \t\t {len(cheap) * cheap_widget / all_fit * 100}%")

for x in tools:
    data["pools"][0]["entries"].append(
        {
            "type": "minecraft:item",
            "name": f"minecraft:{x}",
            "weight": tools_widget,
            "functions": [
                {
                    "function": "minecraft:set_damage",
                    "damage": {
                        "type": "minecraft:uniform",
                        "min": 0,
                        "max": 1
                    }
                }
            ]
        }
    )

print(f"Added {len(tools)} tools \t\t\t\t {len(tools) * tools_widget / all_fit * 100}%")

for x in stuff:
    data["pools"][0]["entries"].append(
        {
            "type": "minecraft:item",
            "name": f"minecraft:{x}",
            "weight": stuff_widget,
            "functions": [
                {
                    "function": "minecraft:set_count",
                    "count": {
                        "min": 0,
                        "max": 4
                    }
                }
            ]
        }
    )

print(f"Added {len(stuff)} stuff \t\t\t {len(stuff) * stuff_widget / all_fit * 100}%")

for x in special:
    data["pools"][0]["entries"].append(
        {
            "type": "minecraft:item",
            "name": f"minecraft:{x}",
            "weight": special_widget,
        }
    )

print(f"Added {len(special)} special stuff \t\t {len(special) * special_widget / all_fit * 100}%")

for x in potion:
    for eff in effects:
        data["pools"][0]["entries"].append(
            {
                "type": "minecraft:item",
                "name": f"minecraft:{x}",
                "weight": potion_widget,
                "functions": [
                    {
                        "function": "minecraft:set_potion",
                        "id": eff
                    }
                ]
            }
        )

print(
    f"Added {len(potion) * len(effects)} potions \t\t\t {len(potion) * len(effects) * potion_widget / all_fit * 100}%")

a = json.dumps(data)
f = open("loot_table.json", 'w', encoding='utf-8')
f.write(a)
