from constant.massages.index import MESSAGES


def common_popup_formate(message: str,  buttonCounts: int = 0, button_text: list = [], button_color: list = [], button_methods: list = [], title: str = None, showLoader: bool = False):

    data = {
        "isPopup": True,
        "popupType": MESSAGES.POPUP.TYPE.COMMON_POPUP,
        "message": message,
        "title": "Alert",
        "buttonCounts": buttonCounts if buttonCounts else 0,
        "button_text": button_text if button_text else [],
        "button_color": button_color if button_color else [],
        "button_methods": button_methods if button_methods else [],
    }

    if showLoader:
        data["showLoader"] = True

    return {
        "en": "POPUP",
        "data": data
    }
