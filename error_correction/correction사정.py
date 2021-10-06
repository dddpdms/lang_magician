from gensim.models import FastText
from gensim.models.fasttext import FastText, load_facebook_vectors

target_word = "사정.07"

# 코렉스 구축 사전
fin = open("write", 'r', encoding='utf-8', newline='\n', errors='ignore')
data = dict()
for line in fin:
    tokens = line.rstrip().split(' ')
    data[tokens[0]] = tokens[1]

# 그래프 임베딩 벡터 사전
f1 = open("C:/Users/ai/Desktop/word.embeddings", 'r')
a = dict()
candidate_word = f1.readline()
for k in range(1, 82116):
    candidate_word = f1.readline()
    blank_split = candidate_word.split(".n.") # 어깨번호 고려해서 여기서 자름
    a[blank_split[0]] = blank_split[1]

def graph_vec_dic_search(aa, bb):
    len_num = 0
    aa_vec = ""
    bb_vec = ""

    try:
        aa_ = data[aa]
        aa_sp = aa_.split(".n.")
        aa_vec = a[aa_sp[0]]
        if aa_sp[0] in a:
            len_num = 1128
    except KeyError:
        aa_ = ""

    try:
        bb_ = data[bb]
        bb_sp = bb_.split(".n.")
        bb_vec = a[bb_sp[0]]
        if bb_sp[0] in a:
            if len_num == 1128:
                len_num += 1000
            else:
                len_num = 2128
    except KeyError:
        bb_ = ""

    return aa_vec, bb_vec, len_num

model = load_facebook_vectors('C:/Users/ai/Desktop/sg300_ceo1_shoulder.bin')
f = open("C:/Users/ai/Desktop/data/교정실험_after_어깨번호/붙힌것/사정_세종1.txt", 'r', encoding='utf-8', newline='\n', errors='ignore')

cnt = 0
correct_cnt = 0
correct_limit = 0
while True:
    line = f.readline()
    if not line: break

    split_list = line.split(' ')
    sum1 = 0
    sum2 = 0
    for i in split_list:
        if target_word in i:
            cnt += 1
            cut_num = split_list.index(i)

            temp_str = split_list[cut_num].replace("사정.07", "사장.10")

            vec_len = 0
            if (cut_num - 5) > 0:
                aa, bb, vec_len = graph_vec_dic_search(split_list[cut_num], split_list[cut_num - 5])
                sum1 += model.similarity(split_list[cut_num], split_list[cut_num - 5], aa, bb, vec_len)
                aa, bb, vec_len = graph_vec_dic_search(temp_str, split_list[cut_num - 5])
                sum2 += model.similarity(temp_str, split_list[cut_num - 5], aa, bb, vec_len)
                vec_len = 0
            if (cut_num - 4) > 0:
                aa, bb, vec_len = graph_vec_dic_search(split_list[cut_num], split_list[cut_num - 4])
                sum1 += model.similarity(split_list[cut_num], split_list[cut_num - 4], aa, bb, vec_len)
                aa, bb, vec_len = graph_vec_dic_search(temp_str, split_list[cut_num - 4])
                sum2 += model.similarity(temp_str, split_list[cut_num - 4], aa, bb, vec_len)
                vec_len = 0
            if (cut_num - 3) > 0:
                aa, bb, vec_len = graph_vec_dic_search(split_list[cut_num], split_list[cut_num - 3])
                sum1 += model.similarity(split_list[cut_num], split_list[cut_num - 3], aa, bb, vec_len)
                aa, bb, vec_len = graph_vec_dic_search(temp_str, split_list[cut_num - 3])
                sum2 += model.similarity(temp_str, split_list[cut_num - 3], aa, bb, vec_len)
                vec_len = 0
            if (cut_num - 2) > 0:
                aa, bb, vec_len = graph_vec_dic_search(split_list[cut_num], split_list[cut_num - 2])
                sum1 += model.similarity(split_list[cut_num], split_list[cut_num - 2], aa, bb, vec_len)
                aa, bb, vec_len = graph_vec_dic_search(temp_str, split_list[cut_num - 2])
                sum2 += model.similarity(temp_str, split_list[cut_num - 2], aa, bb, vec_len)
                vec_len = 0
            if (cut_num - 1) > 0:
                aa, bb, vec_len = graph_vec_dic_search(split_list[cut_num], split_list[cut_num - 1])
                sum1 += model.similarity(split_list[cut_num], split_list[cut_num - 1], aa, bb, vec_len)
                aa, bb, vec_len = graph_vec_dic_search(temp_str, split_list[cut_num - 1])
                sum2 += model.similarity(temp_str, split_list[cut_num - 1], aa, bb, vec_len)
                vec_len = 0

            if (cut_num + 1) < len(split_list):
                aa, bb, vec_len = graph_vec_dic_search(split_list[cut_num], split_list[cut_num + 1])
                sum1 += model.similarity(split_list[cut_num], split_list[cut_num + 1], aa, bb, vec_len)
                aa, bb, vec_len = graph_vec_dic_search(temp_str, split_list[cut_num + 1])
                sum2 += model.similarity(temp_str, split_list[cut_num + 1], aa, bb, vec_len)
                vec_len = 0
            if (cut_num + 2) < len(split_list):
                aa, bb, vec_len = graph_vec_dic_search(split_list[cut_num], split_list[cut_num + 2])
                sum1 += model.similarity(split_list[cut_num], split_list[cut_num + 2], aa, bb, vec_len)
                aa, bb, vec_len = graph_vec_dic_search(temp_str, split_list[cut_num + 2])
                sum2 += model.similarity(temp_str, split_list[cut_num + 2], aa, bb, vec_len)
                vec_len = 0
            if (cut_num + 3) < len(split_list):
                aa, bb, vec_len = graph_vec_dic_search(split_list[cut_num], split_list[cut_num + 3])
                sum1 += model.similarity(split_list[cut_num], split_list[cut_num + 3], aa, bb, vec_len)
                aa, bb, vec_len = graph_vec_dic_search(temp_str, split_list[cut_num + 3])
                sum2 += model.similarity(temp_str, split_list[cut_num + 3], aa, bb, vec_len)
                vec_len = 0
            if (cut_num + 4) < len(split_list):
                aa, bb, vec_len = graph_vec_dic_search(split_list[cut_num], split_list[cut_num + 4])
                sum1 += model.similarity(split_list[cut_num], split_list[cut_num + 4], aa, bb, vec_len)
                aa, bb, vec_len = graph_vec_dic_search(temp_str, split_list[cut_num + 4])
                sum2 += model.similarity(temp_str, split_list[cut_num + 4], aa, bb, vec_len)
                vec_len = 0
            if (cut_num + 5) < len(split_list):
                aa, bb, vec_len = graph_vec_dic_search(split_list[cut_num], split_list[cut_num + 5])
                sum1 += model.similarity(split_list[cut_num], split_list[cut_num + 5], aa, bb, vec_len)
                aa, bb, vec_len = graph_vec_dic_search(temp_str, split_list[cut_num + 5])
                sum2 += model.similarity(temp_str, split_list[cut_num + 5], aa, bb, vec_len)
                vec_len = 0

            if cnt % 2 == 0: #에러 단어 sum1 원글 / sum2 변환글
                if sum1 > sum2:
                    correct_cnt += 1
                else:
                    correct_limit += 1
            elif cnt % 2 == 1:
                if sum1 > sum2:
                    correct_cnt += 1

print("precision : " + str(correct_cnt/(correct_cnt+correct_limit)))
print("recall : " + str(correct_cnt/cnt))
f.close()
fin.close()
f1.close()