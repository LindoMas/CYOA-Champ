

import json


def read_world_json(story_file):
    with open(story_file, 'r') as f:
        story = json.load(f)
    return story


def decode_world_json():
    """
    Responsble for displaying it onto the terminal and more
    
    """
    newId = 0
    story = read_world_json("story/world.json")
    # print(story[0])
    while True:
        temp_dict = {}
        for i in story:
            if i["PageId"] == newId:
                print("Story: ",i["Story"])
                for j in i["Choices"]:
                    print(j["Text"])
                    temp_dict.update({j["Text"]: j["PageId"]})
        
        # print(temp_dict)
        
        choosen_option = input("Choose an option: ")
        newId = temp_dict.get(choosen_option)
        print(newId)
        temp_dict.clear()
        
if __name__=="__main__":
    decode_world_json()
    pass