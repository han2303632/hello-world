jq '.data' train-v1.1.json
jq '.data' out_train.json

jq '.data[1]' train-v1.1.json
jq '.data[1]' out_train.json

jq '.data[1]["paragraphs"][0]' train-v1.1.json
jq '.data[1]["paragraphs"][0]' out_train.json


jq '.data[1]["paragraphs"][0]["qas"][0]' train-v1.1.json
jq '.data[1]["paragraphs"][0]["qas"][0]' out_train.json



jq '.data' dev-v1.1.json
jq '.data' out_test.json

jq '.data[1]' dev-v1.1.json
jq '.data[1]' out_test.json

jq '.data[1]["paragraphs"][0]' dev-v1.1.json
jq '.data[1]["paragraphs"][0]' out_test.json


jq '.data[1]["paragraphs"][0]["qas"][0]' dev-v1.1.json
jq '.data[1]["paragraphs"][0]["qas"][0]' out_test.json
