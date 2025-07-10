from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6

def block_to_block_type(markdown_block):
    line_split = (markdown_block.strip().split("\n"))
    loop_track = True
    string_before_space = line_split[0].split(" ", 1)[0]
    for c in string_before_space:
        if c != ("#"):
            loop_track = False
            break

    if ((loop_track == True) and (len(string_before_space) <= 6) and (len(string_before_space) >= 1)):
        return BlockType.HEADING
    
    if (markdown_block.startswith("```") and markdown_block.endswith("```")):
        return BlockType.CODE
    
    loop_track = True
    for line in line_split:
        if not line.startswith(">"):
            loop_track = False
            break
    if loop_track == True:
        return BlockType.QUOTE
    
    loop_track = True

    for line in line_split:
        if not line.startswith("- "):
            loop_track = False
            break
    if loop_track == True:
        return BlockType.UNORDERED_LIST
    
    loop_track = True
    number_track = 1
    for line in line_split:
        if not line.startswith(f"{number_track}. "):
            loop_track = False
            break
        number_track += 1
    if loop_track == True:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH