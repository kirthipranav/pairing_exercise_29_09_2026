## 1 problem - user story
```
As a member of a group chat,
I want the chat's participants shown as a single readable line,
so that I can see at a glance who's in the conversation.

Acceptance criteria:

No participants: the line is empty.
[] => ""

One participant: just their name.
["Bart"] => "Bart"

Two participants: joined with an ampersand.
["Bart", "Lisa"] => "Bart & Lisa"

Three or more participants: commas between names, with an ampersand before the last one.
["Bart", "Lisa", "Maggie"] => "Bart, Lisa & Maggie"

Order is kept: names appear in the same order they were given.
```
## 2 function signature
```python
# Parameters:
# List of strings representing particpants in the group chat
# Return type:
# String of formatted participant list
# Side Effects:
# None
def format_names():
    pass
```

## 3 exampples
```python
# scenario 1
format_names([]) => ""
# scenario 2
format_names(["Bart"]) => "Bart"
# scenario 3
format_names(["Bart", "Lisa"]) => "Bart & Lisa"
# scenario 4
format_names(["Bart", "Lisa", "Maggie"]) => "Bart, Lisa & Maggie"
# scenario 5
format_names(["Bart", "Lisa", "Maggie", "Laurence"]) => "Bart, Lisa, Maggie & Laurence"
```