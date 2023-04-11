def handle_dialog(req, res, session_storage):
    user_id = req['session']['user_id']

    if req['session']['new']:
        session_storage[user_id] = {
            'suggests': [
                "Не хочу.",
                "Не буду.",
                "Отстань!",
            ]
        }
        res['response']['text'] = 'Привет! Купи слона!'
        res['response']['buttons'] = get_suggests(user_id, session_storage)
        return

    if any(word in req['request']['original_utterance'].lower() for word in ['ладно', 'куплю', 'покупаю', 'хорошо']) \
            and 'не' not in req['request']['original_utterance'].lower():
        res['response']['text'] = 'Слона можно найти на Яндекс.Маркете!'
        res['response']['end_session'] = True
        return

    res['response']['text'] = \
        f"Все говорят '{req['request']['original_utterance']}', а ты купи слона!"
    res['response']['buttons'] = get_suggests(user_id, session_storage)


# Функция возвращает две подсказки для ответа.
def get_suggests(user_id, session_storage):
    session = session_storage[user_id]
    suggests = [
        {'title': suggest, 'hide': True}
        for suggest in session['suggests'][:2]
    ]
    session['suggests'] = session['suggests'][1:]
    session_storage[user_id] = session
    if len(suggests) < 2:
        suggests.append({
            "title": "Ладно",
            "url": "https://market.yandex.ru/search?text=слон",
            "hide": True
        })

    return suggests
