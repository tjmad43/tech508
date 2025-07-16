# Practice dictionaries - Hero Story

story_1 = {"start":"This is the start.",
           "middle":"This is the middle.",
           "end":"This is the end."
           }
print(story_1)
print(type(story_1))
print(story_1.keys())
print(story_1.values())

print(story_1["start"])
print(story_1["middle"])
print(story_1["end"])

story_1["character"] = "Character"
print(f'The end. I hope you enjoyed the story about {story_1["character"]}!')