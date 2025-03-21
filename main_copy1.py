

def replace_new(text: str) -> str:
    text.replace(",", "***")
    return text.replace(", ", "*****")

print(replace_new("aaabbbb, aaaabbbb, aaaaabbbbb"))


def crasy(fanc, text: str) -> None:
    veriable = fanc(text)
    new_text = veriable + " Great"
    print(veriable, new_text)
    return None

crasy(replace_new, 'Hello, whot is this?')