from django.shortcuts import render
# from django.http import HttpResponse

#関数ベースビュー
#ビュー関数
def index(request):
    question_list =[
        "人間は好きですか？",
        "地球はすきですか？",
        "宇宙はすきですか？",
    ]
    context = {
        "question_list":question_list,
        "is_polled": True,
        "polled_msg":"投票ありがとうごさいました",
        "not_polled_msg":"投票してください",
    }
    return render(request,"main/index.html",context)
