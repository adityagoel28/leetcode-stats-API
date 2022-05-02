from django.shortcuts import render
from django.http import JsonResponse
import requests
import json

# Create your views here.

def home(request):
    return render(request, 'index.html')

def getUsername(request, username):
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
    return JsonResponse(json_data, status=201, safe=False)

def svg(request, username):
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
    return render(request, 'svg.html', context)