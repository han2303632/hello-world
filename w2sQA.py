import json
from collections import OrderedDict


def JsonConvert(InputFile,OutputFile):
    root = {}
    data = []
    id_count = 0
    me_train = json.load(open(InputFile))
    
    for f_key in me_train.keys():
        question = me_train[f_key]["question"]
        for s_key in me_train[f_key]['evidences'].keys():
            qas = list(OrderedDict() for i in range(1))
            paragraphs = list(OrderedDict() for i in range(1))
            article = OrderedDict()
            id_count += 1
            evidence = me_train[f_key]['evidences'][s_key]['evidence']
            answer = me_train[f_key]['evidences'][s_key]['answer'][0]

            if('train' in OutputFile):
                answers = answers4train(evidence,answer)
            else:
                answers = answers4test(evidence,answer)

            qas[0]["answers"] = answers
            qas[0]["question"] = question
            qas[0]["id"] = ("%024d")%id_count

            paragraphs[0]["context"] = evidence 
            paragraphs[0]["qas"] = qas

            article["title"] = " "
            article["paragraphs"] = paragraphs

            data.append(article)



    root["data"] = data
    json.dump(root,open(OutputFile,'w'))



def answers4train(context,text):
    answers = []
    answer = OrderedDict()
    if(text != 'no_answer'):
        try:
            answer_start = context.index(text)
            answer["answer_start"] = answer_start
            answer["text"] = text
            answers.append(answer)
        except ValueError:
            answers = []
    return answers

def answers4test(context,text):
    answers = []

    if(text != 'no_answer'):
        answers = list(OrderedDict() for i in range(3))
        answers[0]["text"] = answers[1]["text"] = answers[2]["text"] = text
        try:
            answer_start = context.index(text)
            answers[0]["answer_start"]=answers[1]["answer_start"]=answers[2]["answer_start"]=answer_start
            for i in range(1,3):
                answer_start = context.find(text,answer_start+1)
                if(answer_start != -1):
                    answers[i]["answer_start"] = answer_start
                else:
                    break
        except ValueError:
            answers = []

    return answers









            

JsonConvert('me_test.ann.json','out_test.json')
