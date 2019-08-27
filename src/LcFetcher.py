# nice repo to take a look https://github.com/skygragon/leetcode-cli

import requests
import json


class Lcfetcher(object):
    def __init__(self):
        pass

    def getProblems(self):
        req = {}
        req['url'] = "https://leetcode.com/graphql"
        req['headers'] = {}
        req['headers']['Origin'] = "https://leetcode.com"
        req['headers']['Referer'] = "https://leetcode.com/problems/two-sum/description/"
        req['json'] = True
        req['body'] = {
            'query': "\n".join([
                'query getQuestionDetail($titleSlug: String!) {',
                '  question(titleSlug: two-sum) {',
                '    content',
                '    stats',
                '    codeDefinition',
                '    sampleTestCase',
                '    enableRunCode',
                '    metaData',
                '    translatedContent',
                '  }',
                '}'
            ]),
            'variables': {'titleSlug': 'two-sum'},
            'operationName': 'getQuestionDetail'
        }
        query = "\n".join([
            'query getQuestionDetail($titleSlug: String!) {',
            '  question(titleSlug: two-sum) {',
            '    content',
            '    stats',
            '    codeDefinition',
            '    sampleTestCase',
            '    enableRunCode',
            '    metaData',
            '    translatedContent',
            '  }',
            '}'
        ])

        content = requests.post("https://leetcode.com/graphql", json={'query': query}, hooks={'response': print_url}, timeout=300)
        #content = requests.post('https://leetcode.com/problems/two-sum/description/', data=req, timeout=10)
        #print(content)
        #rint(content.content)
        #print(json.loads(content))


def print_url(r, *args, **kwargs):
    print(r)


if __name__ == "__main__":
    l = Lcfetcher()
    l.getProblems()
