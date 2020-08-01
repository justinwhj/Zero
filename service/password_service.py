import os
from collections import Counter

root_path = os.path.join(os.path.dirname(__file__) , os.path.pardir)

def pass_type(pass_str):
    if len(pass_str)>4:
        return "strong"
    else:
        return "weak"

def analyze_single_dict(pass_txt="../data/passwords/test.txt"):
    pass_txt = root_path + pass_txt

    length_dict = {}
    char_dict = {}
    type_dict = {}

    with open(pass_txt, "r",encoding="UTF-8") as f:
        passwords = f.read().splitlines()
    pass_counter = Counter(passwords)
    pass_set = set(passwords)
    most_common_pass = pass_counter.most_common(10)

    for k,v in pass_counter.most_common():
        # 统计口令的长度分布
        if str(len(k)) not in length_dict.keys():
            length_dict[str(len(k))] = 1
        else :
            length_dict[str(len(k))] += 1
        # 统计口令的类别分布
        if str(pass_type(k)) not in type_dict.keys():
            type_dict[str(pass_type(k))] = 1
        else:
            type_dict[str(pass_type(k))] += 1
        # 统计口令的字符频率
        for s in k:
            if s not in char_dict.keys():
                char_dict[s] = 1
            else :
                char_dict[s] += 1

    result = {
        "most":dict(most_common_pass),
        "len_dict":length_dict,
        "char_dict":char_dict,
        "type_dict":type_dict
    }

    return result

def compare_two_dicts(txt_1,txt_2):
    result1 = analyze_single_dict(txt_1)
    result2 = analyze_single_dict(txt_2)


if __name__ == "__main__":
    result= analyze_single_dict()
    print(result)
