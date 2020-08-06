import os
from collections import Counter

base_path = os.path.join(os.path.dirname(__file__) , os.path.pardir).split("service")[0]
base_path = os.path.join(base_path,"data/passwords/")

def evaluate(path1,path2):
    path1 = base_path + path1
    path2 = base_path + path2

    with open(path1, "r",encoding="UTF-8") as f:
        train_unique_set = f.read().splitlines()
    train_freq_unique_set = Counter(train_unique_set)
    train_keys_unique_set = set(train_unique_set)

    with open(path2, "r",encoding="UTF-8") as f:
        test_unique_set = f.read().splitlines()
    test_freq_unique_set = Counter(test_unique_set)
    test_keys_unique_set = set(test_unique_set)

    union_pswds = train_keys_unique_set | test_keys_unique_set

    match_data = 0
    match_only_in_train = []
    match_only_in_test = []
    matched_password = []

    for pswd in union_pswds:
        freq_in_train = 0 if not pswd in train_freq_unique_set else train_freq_unique_set[pswd]
        freq_in_test = 0 if not pswd in test_freq_unique_set else test_freq_unique_set[pswd]

        if freq_in_test > 0 and freq_in_train > 0:
            match_data += 1
            matched_password.append(pswd)
        elif freq_in_test > 0 :
            match_only_in_test.append(pswd)
        else:
            match_only_in_train.append(pswd)

    res = {
        "match_data":match_data,
        "train_size":len(train_keys_unique_set),
        "test_size":len(test_keys_unique_set),
        "matched":matched_password,
        "match_rate1":round(match_data/len(train_keys_unique_set),3),
        "match_rate2":round(match_data / len(test_keys_unique_set), 3),
        "match_only_in_train":match_only_in_train,
        "match_only_in_test":match_only_in_test
    }
    return res


def pass_type(pass_str):
    if len(pass_str)>4:
        return "strong"
    else:
        return "weak"

def analyze_single_dict(pass_txt="../data/passwords/test.txt"):
    pass_txt = base_path + pass_txt

    passwords = []

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
        "type_dict":type_dict,
        "passwords":passwords
    }

    return result

def compare_two_dicts(txt_1,txt_2):
    result1 = analyze_single_dict(txt_1)
    result2 = analyze_single_dict(txt_2)
    analyze = evaluate(txt_1,txt_2)
    return result1,result2,analyze


if __name__ == "__main__":
    # path = ""
    # paths = os.listdir(root_path + "\\data\\passwords\\" + path)
    # print(paths)

    print(base_path)

    # result= analyze_single_dict()
    # print(result)
