from typing import Dict, TYPE_CHECKING, NamedTuple, Optional

if TYPE_CHECKING:
    from . import Crash2World

class LocData(NamedTuple):
    ap_code: Optional[int]
    region: Optional[str]
    addr: Optional[int]
    bit: Optional[int]
    # Used for multiple address checking
    sub_addr: Optional[int]
    sub_bit: Optional[int]
    match_type: Optional[str]

def get_total_locations(world) -> int:
    locations = [ l for l in world.multiworld.get_locations() if l.player == world.player ]
    return len(locations)

def get_location_names() -> Dict[str, int]:
    names = {name: data.ap_code for name, data in location_table.items()}
    return names

def get_regions() -> list:
    regions = [data.region for _, data in location_table.items()]
    return regions

def get_ap_code(location_name) -> list:
    ap_code = [data.ap_code for name, data in location_table.items() if location_name == name]
    return ap_code

class stageType():
    stage=0
    boss=1

# ap_code = 50_XX_YY_ZZ:
#   XX: 00 == stage, 01 == boss
#   YY: stage(01~27), if boss, set 00
#   ZZ: item_number(starts 1)
#
# 『全パワーアップ取得』
#  800695C8 1F
#
# # 『完全クリア』
# Power stone
# 8006957C FC00
# 8006957E 7FFF
# 80069580 001D
# White Gems
# 80069400 FFFE
# 80069402 FFFF
# 80069404 00FF
#
# Color Gems(+ 3x White Dummy?)
# 80069406 FC00
#   04: Red
#   08: Green
#   10: Purple
#   20: Blue
#   40: Yellow
#   Others: White
#
# Relic ?
# 80069604 FC00
# 80069606 FFFF
# 80069608 00FF
# 8006960C FC00
# 8006960E FFFF
# 80069610 00FF
# Boss flag?
# 800693B4 00F8
#
# Power stone
# 0x6957C ~ 69583 (0x8 byte)
# 0x6957C: OK (0xFF == dummy)
# 0x6957D: OK (0x03 == dummy)
# 0x6957E: OK (0x00 == dummy)
# 0x6957F: OK (0x80 == dummy)
# 0x69580: OK (0x00 == dummy)
# 0x69581: OK (0xFF == dummy)
# 0x69582: OK (0xFF == dummy)
# 0x69583: OK (0xFF == dummy)
# Stage_dict = {location_name: address_bit}
powerstone_dict = {
    "Stage01: Power Stone": 0, # 0x6957D 0x08
    "Stage02: Power Stone": 0, # 0x6957D 0x40
    "Stage03: Power Stone": 0, # 0x6957D 0x04
    "Stage04: Power Stone": 0, # 0x6957D 0x10
    "Stage05: Power Stone": 0, # 0x6957F 0x02
    "Stage06: Power Stone": 0, # 0x6957D 0x80   
    "Stage07: Power Stone": 0, # 0x6957E 0x40
    "Stage08: Power Stone": 0, # 0x6957E 0x20
    "Stage09: Power Stone": 0, # 0x6957E 0x04
    "Stage10: Power Stone": 0, # 0x6957E 0x02
    "Stage11: Power Stone": 0, # 0x6957E 0x01
    "Stage12: Power Stone": 0, # 0x6957F 0x10
    "Stage13: Power Stone": 0, # 0x6957F 0x04
    "Stage14: Power Stone": 0, # 0x6957E 0x10
    "Stage15: Power Stone": 0, # 0x6957F 0x20
    "Stage16: Power Stone": 0, # 0x6957F 0x40
    "Stage17: Power Stone": 0, # 0x6957E 0x08
    "Stage18: Power Stone": 0, # 0x6957D 0x20
    "Stage19: Power Stone": 0, # 0x6957F 0x08
    "Stage20: Power Stone": 0, # 0x6957F 0x01
    "Stage21: Power Stone": 0, # 0x69580 0x08
    "Stage22: Power Stone": 0, # 0x69580 0x01
    "Stage23: Power Stone": 0, # 0x69580 0x04
    "Stage24: Power Stone": 0, # 0x6957E 0x80
    "Stage25: Power Stone": 0, # 0x69580 0x10
}
stage_order = [
    6, 2, 18, 
]
# White Gems
# 0x69400: 
# 0x69401: 
# 0x69402: 
# 0x69403: 
# 0x69404: 
# 0x69405: Dummy
# 0x69406: Dummy
# 0x69407: Color
#
# Color Gems(+ 3x White Dummy?)
# 80069406 FC00
#   04: Red
#   08: Green
#   10: Purple
#   20: Blue
#   40: Yellow
#   Others: White

gem_dict = {
    "Stage01: All boxes Gem": 0,
    "Stage02: All boxes Gem": 0,
    "Stage03: All boxes Gem": 0,
    "Stage04: All boxes Gem": 0,
    "Stage04: Secret Gem(Red Gem Course)": 0,
    "Stage05: All boxes Gem": 0,
    "Stage06: All boxes Gem": 0,
    "Stage07: All boxes Gem": 0,
    "Stage07: Yellow Gem(Enter from Stage27)": 0,
    "Stage08: All boxes Gem": 0,
    "Stage09: All boxes Gem(Need Purple Gem)": 0,
    "Stage09: Secret Gem(Purple Gem Course)": 0,
    "Stage10: All boxes Gem": 0,
    "Stage11: All boxes Gem(Need Yellow Gem)": 0,
    "Stage11: Secret Gem(Yellow Gem Course)": 0,
    "Stage12: All boxes Gem": 0,
    "Stage12: Red Gem(Secret Path)": 0,
    "Stage13: All boxes Gem": 0,
    "Stage13: Purple Gem(Dokuro course)": 0,
    "Stage14: All boxes Gem": 0,
    "Stage15: All boxes Gem": 0,
    "Stage16: All boxes Gem": 0,
    "Stage16: Secret Gem(Blue Gem Course)": 0,
    "Stage17: All boxes Gem": 0,
    "Stage18: All boxes Gem": 0,
    "Stage19: All boxes Gem(Enter from Stage29)": 0,
    "Stage19: Secret Gem(Enter from Stage29)": 0,
    "Stage20: All boxes Gem": 0,
    "Stage20: Blue Gem(Dokuro course)": 0,
    "Stage21: All boxes Gem(Need Green Gem)": 0,
    "Stage21: Secret boxes Gem(Need Green Gem)": 0,
    "Stage22: All boxes Gem": 0,
    "Stage23: All boxes Gem(Need Fruit bazooka)": 0,
    "Stage23: Green Gem(Dokuro course)": 0,
    "Stage24: All boxes Gem": 0,
    "Stage25: All boxes Gem": 0,
    "Stage25: Secret Gem(Need All Color Gems)": 0,
    "Stage26: All boxes Gem": 0,
    "Stage28: All boxes Gem": 0,
    "Stage28: Secret Gem(Win the race)": 0,
    "Stage30: All boxes Gem": 0,
    "Stage30: Secret Gem(Win the race)": 0,
    "Stage31: All boxes Gem": 0,
    "Stage32: All boxes Gem": 0,
}
# Relic ?
## sapphire
# 80069604 00
# 80069605 FC
# 80069606 FF
# 80069607 FF
# 80069608 FF
# 80069609 00
## Gold
# 8006960C 00
# 8006960D FC
# 8006960E FF
# 8006960F FF
# 80069610 FF
# 80069611 00
## Platinum : Gold & Spphire Flag
# if Sapphire relic: addr=a and bit=b, 
#    Gold relic:     addr = a + 0x08, bit=b
#    Platinum relic: spphire relic and gold reric flag
relic_dict = {
# Normal room
    "Stage01: Relic": 0, # 0x69605 0x08
    "Stage02: Relic": 0, 
    "Stage03: Relic": 0, 
    "Stage04: Relic": 0, 
    "Stage05: Relic": 0, 
    "Stage06: Relic": 0, 
    "Stage07: Relic": 0, 
    "Stage08: Relic": 0, 
    "Stage09: Relic": 0, 
    "Stage10: Relic": 0, 
    "Stage11: Relic": 0, 
    "Stage12: Relic": 0, 
    "Stage13: Relic": 0, 
    "Stage14: Relic": 0, 
    "Stage15: Relic": 0, 
    "Stage16: Relic": 0, 
    "Stage17: Relic": 0, 
    "Stage18: Relic": 0, 
    "Stage19: Relic": 0, 
    "Stage20: Relic": 0, 
    "Stage21: Relic": 0, 
    "Stage22: Relic": 0, 
    "Stage23: Relic": 0, 
    "Stage24: Relic": 0, 
    "Stage25: Relic": 0, 
# Room 6(Secret Room)
    "Stage26: Relic": 0, 
    # Stage27 is another entrance of stage07
    "Stage28: Relic": 0, 
    # Stage29 is another entrance of stage19
    "Stage30: Relic": 0, 
# Room 7(Secret Course)
    # boat stage
    "Stage31: Relic": 0, 
    # Baby-T stage
    "Stage32: Relic": 0, 
}

# FixMe: To adjust for Crash3
def gen_stage_locations(stage_dict: Dict[str, int]):
    location_dict = {}
    item_counter = 1
    prev_stage_num = 0
    for name, data in stage_dict.items():
        stage_num = int(name.split(":")[0].replace("Stage",""), 10) -1 # 1~5 -> 0~4
        floor_num = stage_num // 5 + 1
        if stage_num == prev_stage_num:
            item_counter += 1
        else:
            item_counter = 1
        prev_stage_num = stage_num
        # AP code
        ap_code = 50000000 + stage_num*100 + item_counter
        # Region
        region = f"{floor_num}F"
        if floor_num > 5: # Secret stage case
            region = f"{name.split(':')[0]}"
        # Address
        if "Gem" in name:
            addr = 0x69400 + (data//8)
        elif "Relic" in name:
            addr = 0x69604 + (data//8)
        else: # Power Stone
            addr = 0x6957C + (data//8)
        # Bit
        bit =  (data % 8)

        # Generate locations
        if "Relic" in name: # Generate 3 type of location
            location_dict[f"{name} Sapphire"] = LocData(ap_code   , region, addr, bit, addr+0x08, match_type="or")
            location_dict[f"{name} Gold"]     = LocData(ap_code+10, region, addr+0x08, bit)
            location_dict[f"{name} Platinum"] = LocData(ap_code+20, region, addr, bit, addr+0x08, bit, match_type="and")
        else:
            location_dict[name] = LocData(ap_code, region, addr, bit)
    return location_dict

stage_dict = {
    **powerstone_dict,
    **gem_dict,
    **relic_dict,
}

stage_locations = gen_stage_locations(stage_dict)
boss_locations = {
    "Boss01": LocData(50010001, "2F", 0x0006D9D8, 6),
    "Boss02": LocData(50010002, "3F", 0x0006D9D9, 0),
    "Boss03": LocData(50010003, "4F", 0x0006D9D8, 3),
    "Boss04": LocData(50010004, "5F", 0x0006D9D9, 1),
    "Boss05": LocData(50010005, "6F", 0x0006D9D8, 7),
}

location_table = {
    **stage_locations,
    **boss_locations,
}

#class EventData(NamedTuple):
#    name:       str
#    ap_code:    Optional[int] = None
#class LocData(NamedTuple):
#    ap_code: Optional[int]
#    region: Optional[str]
def get_level_locations(region):
    return map(lambda l: l[0], get_level_location_data(region))

def get_level_location_data(region):
    return filter(lambda l: l[1].region == (region), location_table.items())

