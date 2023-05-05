import json as json_api
import sys

#file read 
json_org_file = open('.\sample2.json')
words_to_search = ['num', 'Num']

def find_search_word(target_sentence): 
    #print('debug : find_search_word() called : (target_sentence : '+target_sentence+')')
    found_words = []
    for target_word in words_to_search:
        if(target_sentence.find(target_word) >= 0):
            #print('debug : found_word : '+target_word)
            found_words.append(target_word)
    return found_words

def json_search(current_json_dict, current_path, hierarchy): 
    #print('debug : json_search called : (current_path : ' + current_path + '), (hierarchy : '+str(hierarchy)+')')
    for next_path in current_json_dict.keys():
        #print('debug : (current_path : '+current_path+'), (next_path : '+next_path+'), (hierarchy : '+str(hierarchy)+')')
        found_words = find_search_word(next_path)
        for j in range(len(found_words)): 
            dict_value = ''
            dict_next_path_type = type(current_json_dict[next_path])
            if dict_next_path_type == dict: 
                dict_value = '[dict]'
            elif dict_next_path_type == list:
                dict_value = '[list]'
            elif dict_next_path_type == str:
                dict_value = current_json_dict[next_path]
            else: 
                dict_value = '[not string value]'
            print('json_search() : (path : '+current_path+'[' + found_words[j] + ']), (value : '+dict_value+'), (found_word : '+found_words[j]+'), (hierarchy : '+str(hierarchy)+')')

        if type(current_json_dict[next_path]) == dict: 
            json_search(current_json_dict[next_path], current_path + '[' + next_path + ']', hierarchy + 1)
        elif type(current_json_dict[next_path]) == list:
            for i in range(len(current_json_dict[next_path])):
                json_search(current_json_dict[next_path][i], current_path + '[' + next_path + ']array['+str(i)+']', hierarchy + 1)

    return

#jsonを辞書型に読み込み
json_org_dict = json_api.load(json_org_file)

#各関数呼び出し(※先頭が配列の場合の対応)
if type(json_org_dict) == list: 
    for i in range(len(json_org_dict)):
        print('json_list number : ' + str(i))
        json_search(json_org_dict[i], 'root' + str(i), 0)
elif type(json_org_dict) == dict: 
    json_search(json_org_dict, 'root', 0)
else: 
    print('ERROR: json file is not formated as json.')
    sys.exit(1)

sys.exit(0)
