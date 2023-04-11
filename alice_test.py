from requests import post

json_request = {
    "request": {
        "command": "не хочу",
        "original_utterance": "ну ладно"
    },
    "session": {
        "new": True,
        "message_id": 4,
        "session_id": "2eac4854-fce721f3-b845abba-20d60",
        "skill_id": "3ad36498-f5rd-4079-a14b-788652932056",
        "user_id": "AC9WC3DF6FCE052E45A4566A48E6B7193774B84814CE49A922E163B8B29881DC"
    },
    "version": "1.0"
}

print(post('http://localhost:5000/post', json=json_request).json())
