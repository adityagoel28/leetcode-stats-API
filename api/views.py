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

                # '.problems-solved {'
                #     color: #8A8A8E;font-size: 12px;line-height: 17px; margin-bottom: 2px;white-space: nowrap;font-weight: 500;
                # '}'

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

            #     'foreignObject {'
            #         'width: calc(100% - 10px - 32px);'
            #         'height: calc(100% - 10px - 24px);'
            #     '}'
            # '</style>'
            '<g>'
                '<rect x="5" y="5" id="background" style="width: calc(100% - 10px);height: calc(100% - 10px);fill: #FFF;rx: 8px;ry: 8px;"/>'
                '<g>'
                    '<foreignObject x="21" y="17" width="318" height="176">'
                        '<div xmlns="http://www.w3.org/1999/xhtml">'
                            '<div class="stat-wrapper top" size="108" style="display: flex; flex-direction: column;text-align: start;">'
                                '<div class="problems-solved" style="color: #8A8A8E;font-size: 12px;line-height: 17px; margin-bottom: 2px;white-space: nowrap;font-weight: 500;">Problems Solved</div>'
                                '<div class="total-solved-count" style="font-size: 22px;font-weight: 600;line-height: 100%;white-space: nowrap;color: #262626;">{0}</div>'
                            '</div>'
                            '<div class="total-solved-container" style="display: -webkit-box;display: -ms-flexbox;display: flex;-webkit-box-pack: justify;-ms-flex-pack: justify;justify-content: space-between;color: #9e9e9e;height: 33px;">'
                                '<div class="stat-wrapper" data-difficulty="Easy" style="display: flex; flex-direction: column;text-align: start;">'
                                    '<div class="difficulty-label easy" style="color: #43A047;font-size: 12px;font-weight: normal;line-height: 17px;margin-bottom: 2px;white-space: nowrap;">Easy</div>'
                                    '<div class="solved" style="color: #262626;font-size: 14px;font-weight: 600;line-height: 100%;white-space: nowrap;">'
                                        '{0}<span class="total-count">/568</span>'
                                    '</div>'
                                '</div>'
                                '<div class="stat-wrapper" data-difficulty="Medium" style="display: flex; flex-direction: column;text-align: start;">'
                                    '<div class="difficulty-label medium" style="color: #FB8C00;font-size: 12px;font-weight: normal;line-height: 17px;margin-bottom: 2px;white-space: nowrap;">Medium</div>'
                                    '<div class="solved" style="color: #262626;font-size: 14px;font-weight: 600;line-height: 100%;white-space: nowrap;">'
                                        '{0}<span class="total-count">/1203</span>'
                                    '</div>'
                                '</div>'
                                '<div class="stat-wrapper" data-difficulty="Hard" style="display: flex; flex-direction: column;text-align: start;">'
                                    '<div class="difficulty-label hard" style="color: #E91E63;font-size: 12px;font-weight: normal;line-height: 17px;margin-bottom: 2px;white-space: nowrap;">Hard</div>'
                                    '<div class="solved" style="color: #262626;font-size: 14px;font-weight: 600;line-height: 100%;white-space: nowrap;">'
                                        '{0}<span class="total-count">/491</span>'
                                    '</div>'
                                '</div>'
                            '</div>'
                        '</div>'
                    '</foreignObject>'
                '</g>'
            '</g>'
        '</svg>',total, easy, med, hard)

    # return mark_safe(svg_tag)
    return HttpResponse(svg_tag, content_type="image/svg+xml")