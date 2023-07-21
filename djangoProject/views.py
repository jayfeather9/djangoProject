from django.shortcuts import render

# Create your views here.


def index(request):
    test_question_list = [
        {"ID": 0, "Name": "Question One", "Time": "2022/1/2", "Diff": "Easy", "Uploader": "Red"},
        {"ID": 5271, "Name": "Simple question", "Time": "2022/1/4", "Diff": "Medium", "Uploader": "Silence"},
        {"ID": 2352, "Name": "Question Three", "Time": "2022/1/7", "Diff": "Hard", "Uploader": "Cute"},
        {"ID": 23, "Name": "Question Four", "Time": "2022/5/7", "Diff": "Expert", "Uploader": "Bunny"},
        {"ID": 721, "Name": "YES Five", "Time": "2022/3/7", "Diff": "Easy", "Uploader": "Red"},
        {"ID": 34, "Name": "Question Six", "Time": "2022/8/7", "Diff": "Medium", "Uploader": "Silence"},
        {"ID": 512, "Name": "NOOOOO Seven", "Time": "2023/5/7", "Diff": "Hard", "Uploader": "Cute"},
        {"ID": 634, "Name": "Question Eight", "Time": "2022/12/7", "Diff": "Expert", "Uploader": "Bunny"},
        {"ID": 23, "Name": "Red is handsome Nine", "Time": "2023/4/7", "Diff": "Master", "Uploader": "Red"},
        {"ID": 663, "Name": "Go Play Arknights NOW!!", "Time": "2022/3/7", "Diff": "Re:Master", "Uploader": "Silence"},
    ]
    trans_text_color = {"Easy": "text--darkest-gray", "Medium": "text--darkest-gray", "Hard": "text--white",
                        "Expert": "text--white", "Master": "text--white", "Re:Master": "text--white"}
    trans_bg_color = {"Easy": "bg--lightest-gray", "Medium": "bg--light-gray", "Hard": "bg--gray",
                      "Expert": "bg--dark-gray", "Master": "bg--darkest-gray", "Re:Master": "bg--tertiary-color"}
    for i in range(len(test_question_list)):
        test_question_list[i]["text_color"] = trans_text_color[test_question_list[i]["Diff"]]
        test_question_list[i]["bg_color"] = trans_bg_color[test_question_list[i]["Diff"]]
    return render(request, "index.html", {"test_question_list": test_question_list})
