from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import json
import pandas as pd
from django.utils.html import format_html

# Create your views here.

def home(request):
    return render(request, 'index.html')

def getUsername(request, username):
    print('wwww')

    query = '''
    query getUserProfile($username: String!) {
        allQuestionsCount {
        difficulty
        count
        }
        matchedUser(username: $username) {
        username
        submitStats {
            acSubmissionNum {
            difficulty
            count
            }
        }
        }
    }
    '''

    username = username
    variables = {'username': username}

    url = 'https://leetcode.com/graphql/'
    r = requests.post(url, json={'query': query, 'variables': variables})
    json_data = json.loads(r.text)

    # df_data = json_data['data']['matchedUser']
    # df = pd.DataFrame(df_data)
    # print(df)
    print('AA', json_data)
    data = json.dumps(json_data, indent=3)

    print(json.dumps(json_data, indent=4))
    
    usernameHandle = json_data['data']['matchedUser']['username']
    total = json_data['data']['matchedUser']['submitStats']['acSubmissionNum'][0]['count']
    easy = json_data['data']['matchedUser']['submitStats']['acSubmissionNum'][1]['count']
    med = json_data['data']['matchedUser']['submitStats']['acSubmissionNum'][2]['count']
    hard = json_data['data']['matchedUser']['submitStats']['acSubmissionNum'][3]['count']
    
    print(usernameHandle)
    print(total)
    print(easy)
    print(med)
    print(hard)
    return JsonResponse(json_data, status=201, safe=False)

def svg(request, username):
    print('ssss')

    query = '''
    query getUserProfile($username: String!) {
        allQuestionsCount {
        difficulty
        count
        }
        matchedUser(username: $username) {
        username
        submitStats {
            acSubmissionNum {
            difficulty
            count
            submissions
            }
        }
        }
    }
    '''
    
    username = username
    variables = {'username': username}

    url = 'https://leetcode.com/graphql/'
    r = requests.post(url, json={'query': query, 'variables': variables})
    json_data = json.loads(r.text)
    print(json.dumps(json_data, indent=4))
    
    usernameHandle = json_data['data']['matchedUser']['username']
    total = json_data['data']['matchedUser']['submitStats']['acSubmissionNum'][0]['count']
    easy = json_data['data']['matchedUser']['submitStats']['acSubmissionNum'][1]['count']
    med = json_data['data']['matchedUser']['submitStats']['acSubmissionNum'][2]['count']
    hard = json_data['data']['matchedUser']['submitStats']['acSubmissionNum'][3]['count']
    
    print(usernameHandle)
    print(total)
    print(easy)
    print(med)
    print(hard)

    context = {'usernameHandle': usernameHandle, 'total': total, 'easy': easy, 'med':med, 'hard': hard}
    # return HttpResponse('a', content_type="image/svg+xml")
    return render(request, 'svg.html', context)



def svg_icon(request, username):
    print('dddd')

    query = '''
    query getUserProfile($username: String!) {
        allQuestionsCount {
        difficulty
        count
        }
        matchedUser(username: $username) {
        username
        submitStats {
            acSubmissionNum {
            difficulty
            count
            submissions
            }
        }
        }
    }
    '''
    
    username = username
    variables = {'username': username}

    url = 'https://leetcode.com/graphql/'
    r = requests.post(url, json={'query': query, 'variables': variables})
    json_data = json.loads(r.text)
    print(json.dumps(json_data, indent=4))
    
    usernameHandle = json_data['data']['matchedUser']['username']
    total = json_data['data']['matchedUser']['submitStats']['acSubmissionNum'][0]['count']
    easy = json_data['data']['matchedUser']['submitStats']['acSubmissionNum'][1]['count']
    med = json_data['data']['matchedUser']['submitStats']['acSubmissionNum'][2]['count']
    hard = json_data['data']['matchedUser']['submitStats']['acSubmissionNum'][3]['count']
    

    svg_tag = format_html('<svg width="330" height="180" xmlns="http://www.w3.org/2000/svg">'
            # '<style>'
            #     'svg {'
            #         'font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif;'
            #         'font-size: 14px;'
            #         'line-height: 1.5;'
            #     '}'

            #     '.total-solved-container .total-count::before {'
            #         'content: "/";'
            #         'margin: 0 1px;'
            #     '}'

            #     '.total-solved-container .total-count {'
            #         'color: #8A8A8E;'
            #         'font-size: 12px;'
            #         'font-weight: 500;'
            #         'line-height: 14px;'
            #     '}'

            #     '.top {'
            #         'height: 108px;'
            #     '}'
            # '</style>'
            '<g>'
                '<rect x="5" y="5" id="background" style="width: calc(100% - 10px);height: 400px;fill: #FFF;rx: 8px;ry: 8px;"/>'
                '<g>'
                    '<foreignObject x="21" y="17" width="318" height="176" style="width: calc(100% - 10px - 32px); height: 400px;">'
                        '<div xmlns="http://www.w3.org/1999/xhtml">'
                            '<div style="margin-bottom:15px; font-size:18px;"><b style="color:#fc9905;">{0}</b> - LeetCode Stats</div>'
                            '<div class="row1" style="margin-top:10px;">'
                                '<div class="column" style="float: left;width: 35%;">'
                                '<div class="stat-wrapper top" size="108" style="display: flex; flex-direction: column;text-align: start; margin-top:40px;">'
                                    '<div class="problems-solved" style="color: #8A8A8E;font-size: 16px;line-height: 17px; margin-bottom: 2px;white-space: nowrap;font-weight: 500;">Problems Solved</div>'
                                    '<div class="total-solved-count" style="font-size: 22px;font-weight: 600;line-height: 100%;white-space: nowrap;color: #262626;">{1}</div>'
                                '</div>'
                            # '<div class="total-solved-container" style="display: -webkit-box;display: -ms-flexbox;display: flex;-webkit-box-pack: justify;-ms-flex-pack: justify;justify-content: space-between;color: #9e9e9e;height: 33px;">'
                            #     '<div class="stat-wrapper" data-difficulty="Easy" style="display: flex; flex-direction: column;text-align: start;">'
                            #         '<div class="difficulty-label easy" style="color: #43A047;font-size: 12px;font-weight: normal;line-height: 17px;margin-bottom: 2px;white-space: nowrap;">Easy</div>'
                            #         '<div class="solved" style="color: #262626;font-size: 14px;font-weight: 600;line-height: 100%;white-space: nowrap;">'
                            #             '{2}<span class="total-count">/568</span>'
                            #         '</div>'
                            #     '</div>'
                            #     '<div class="stat-wrapper" data-difficulty="Medium" style="display: flex; flex-direction: column;text-align: start;">'
                            #         '<div class="difficulty-label medium" style="color: #FB8C00;font-size: 12px;font-weight: normal;line-height: 17px;margin-bottom: 2px;white-space: nowrap;">Medium</div>'
                            #         '<div class="solved" style="color: #262626;font-size: 14px;font-weight: 600;line-height: 100%;white-space: nowrap;">'
                            #             '{3}<span class="total-count">/1203</span>'
                            #         '</div>'
                            #     '</div>'
                            #     '<div class="stat-wrapper" data-difficulty="Hard" style="display: flex; flex-direction: column;text-align: start;">'
                            #         '<div class="difficulty-label hard" style="color: #E91E63;font-size: 12px;font-weight: normal;line-height: 17px;margin-bottom: 2px;white-space: nowrap;">Hard</div>'
                            #         '<div class="solved" style="color: #262626;font-size: 14px;font-weight: 600;line-height: 100%;white-space: nowrap;">'
                            #             '{4}<span class="total-count">/491</span>'
                            #         '</div>'
                            #     '</div>'
                            # '</div>'
                            '</div>'
                                '<div class="column" style="float: left;width: 65%;">'
                                    '<div style="margin:20px; margin-bottom:2px; margin-top:0px;"><span style="color:#5db55f;">Easy:</span> <b style="color:#5db55f;">{2}</b>/568</div>'
                                    '<div style="background-color:#e4e4e4; border-radius:50px; margin:20px; margin-top:2px;">'
                                        '<div style="height:4px; width:calc(({2}/568) * 100%); background-color:#5db55f; border-radius:50px;"></div>'
                                    '</div>'
                                    '<div style="margin:20px; margin-bottom:2px;"><span style="color:#faab43;">Medium: </span> <b style="color:#faab43;">{3}</b>/1203</div>'
                                    '<div style="background-color:#e4e4e4; border-radius:50px; margin:20px; margin-top:2px;">'
                                        '<div style="height:4px; width:calc(({3}/1203) * 100%); background-color:#faab43; border-radius:50px;"></div>'
                                    '</div>'
                                    '<div style="margin:20px; margin-bottom:2px;"><span style="color:#d55951;">Hard: </span> <b style="color:#d55951;">{4}</b>/491</div>'
                                    '<div style="background-color:#e4e4e4; border-radius:50px; margin:20px; margin-top:2px;">'
                                        '<div style="height:4px; width:calc(({4}/491) * 100%); background-color:#d55951; border-radius:50px;"></div>'
                                    '</div>'
                                '</div>'
                            '</div>'
                        '</div>'
                    '</foreignObject>'
                '</g>'
            '</g>'
        '</svg>', username, total, easy, med, hard, )

    # return mark_safe(svg_tag)
    return HttpResponse(svg_tag, content_type="image/svg+xml")