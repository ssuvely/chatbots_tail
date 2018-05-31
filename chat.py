# -*- coding: utf-8 -*-

#---------------------------------
# pangpang2.py
#---------------------------------

import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/keyboard')
def Keyboard():
    dataSend = {
        "type" : "buttons",
        "buttons" : ["도움말","끝말잇기 게임"]
        }
    return jsonify(dataSend)

@app.route('/message', methods=['POST'])
def Message():
    dataReceive = request.get_json()
    content = dataReceive['content']
    if content == u"도움말":
        dataSend = {
            "message": {
                "text": "꼬리봇은 기본적으로 사용자의 말을 따라합니다\n끝말잇기 게임은 꼬리봇과 끝말잇기 게임을 하는 기능입니다."
        },
        "/keyboard":{
                "type" : "buttons",
                "buttons" : ["도움말","끝말잇기 게임"]
            }
        }
    elif u"안녕" in content:
        dataSend = {
            "message": {
                "text": "안녕~ 인사는 따라하지 않을거야! :("
            }
    }
    elif u"그만" in content:
        dataSend = {
            "message": {
                "text": "어떻게 그만이라고 할 수 있어..? ㅜㅜ"
            }
    }
    elif content == u"끝말잇기 게임":
        dataSend = {
            "message":{
                "text": "끝말잇기 시작! 먼저 시작해! 그만하고 싶으면 뒤로가기 라고 말해줘\n아직 정식 서비스 준비중이라 게임이 원활하진 않을거에요ㅜㅜ"
            }
        }
            elif u"무" == content[len(content-1)]:
                dataSend = {
                    "message": {
                        "text": content[len(content-1)] + "기질"
                    }
                }
            elif u"기" == content[len(content-1)]:
                dataSend = {
                    "message": {
                        "text": content[len(content-1)] + "러기"
                    }
                }
            elif u"바" == content[len(content-1)]:
                dataSend = {
                    "message": {
                        "text": content[len(content-1)] + "보"
                    }
                }
            elif u"회" == content[len(content-1)]:
                dataSend = {
                    "message": {
                        "text": content[len(content-1)] + "의실"
                    }
                }
            elif u"경" == content[len(content-1)]:
                dataSend = {
                    "message": {
                        "text": content[len(content-1)] + "찰"
                    }
                }
            elif u"영" == content[len(content-1)]:
                dataSend = {
                    "message": {
                        "text": content[len(content-1)] + "화관"
                    }
                }
            elif u"사" == content[len(content-1)]:
                dataSend = {
                    "message": {
                        "text": content[len(content-1)] + "기꾼"
                    }
                }
            elif u"아" == content[len(content-1)]:
                dataSend = {
                    "message": {
                        "text": content[len(content-1)] + "기사자"
                    }
                }
            elif u"자" == content[len(content-1)]:
                dataSend = {
                    "message": {
                        "text": content[len(content-1)] + "소서 극혐"
                    }
                }
            elif u"신" == content[len(content-1)]:
                dataSend = {
                    "message": {
                        "text": content[len(content-1)] + "서유기"
                    }
                }
            elif u"대" == content[len(content-1)]:
                dataSend = {
                    "message": {
                        "text": content[len(content-1)] + "로변"
                    }
                }
            elif u"다" == content[len(content-1)]:
                dataSend = {
                    "message": {
                        "text": content[len(content-1)] + "한증"
                    }
                }
            elif u"전" == content[len(content-1)]:
                dataSend = {
                    "message": {
                        "text": content[len(content-1)] + "자렌지"
                    }
                }
            elif u"지" == content[len(content-1)]:
                dataSend = {
                    "message": {
                        "text": content[len(content-1)] + "구본"
                    }
                }
            elif u"강" == content[len(content-1)]:
                dataSend = {
                    "message": {
                        "text": content[len(content-1)] + "아지"
                    }
                }
            elif u"고" == content[len(content-1)]:
                dataSend = {
                    "message": {
                        "text": content[len(content-1)] + "양이"
                    }
                }
            elif u"공" == content[len(content-1)]:
                dataSend = {
                    "message": {
                        "text": content[len(content-1)] + "부하기 싫다"
                    }
                }
            elif u"시" == content[len(content-1)]:
                dataSend = {
                    "message": {
                        "text": content[len(content-1)] + "험기간"
                    }
                }
            elif u"술" == content[len(content-1)]:
                dataSend = {
                    "message": {
                        "text": content[len(content-1)] + "쟁이"
                    }
                }
            elif u"한" == content[len(content-1)]:
                dataSend = {
                    "message": {
                        "text": content[len(content-1)] + "강 가고싶다"
                    }
                }
            elif u"트" == content[len(content-1)]:
                dataSend = {
                    "message": {
                        "text": content[len(content-1)] + "외이스"
                    }
                }
            elif u"레" == content[len(content-1)]:
                dataSend = {
                    "message": {
                        "text": content[len(content-1)] + "드벨벳"
                    }
                }
            elif u"엑" == content[len(content-1)]:
                dataSend = {
                    "message": {
                        "text": content[len(content-1)] + "소"
                    }
                }
            elif u"샤" == content[len(content-1)]:
                dataSend = {
                    "message": {
                        "text": content[len(content-1)] + "방샤방"
                    }
                }
            elif u"인" == content[len(content-1)]:
                dataSend = {
                    "message": {
                        "text": content[len(content-1)] + "강"
                    }
                }
            else:
                dataSend = {
                    "message": {
                        "text": "이건 아직 뭐라 대답해야할지 모르겠어 :( 네가 이겼어~"
                    }
                }
    return jsonify(dataSend)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 6000)
