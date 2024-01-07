from types import SimpleNamespace


class Popup:
    def __init__(self) -> None:
        self.TYPE = SimpleNamespace(**{
            "COMMON_POPUP": "COMMON_POPUP",
            "TOST_POPUP": 'TostPopUp',
            "TOP_TOAST_POPUP": 'topToastPopup',
            "MIDDLE_TOAST_POPUP": 'middleToastPopup',
            "COMMON_TOAST_POPUP": 'commonToastPopup',
        })
        self.BUTTON_COLOR = SimpleNamespace(**{
            "RED": 'red',
            "GREEN": 'green',
            "YELLOW": 'yellow',
            "BLUE": 'blue',
        })
        self.BUTTON_TEXT = SimpleNamespace(** {
            "OK": 'Okay',
            "YES": 'Yes',
            "NO": 'No',
            "EXIT": 'Exit',
        })
        self.BUTTON_METHOD = SimpleNamespace(**{
            "OK": 'OkBtn',
            "YES": 'PlayAgainYes',
            "NO": 'PlayAgainNo',
            "FTUESkipYes": 'FTUESkipYes',
            "FTUESkipNo": 'FTUESkipNo',
            "EXIT": 'ExitBtnClick',
        })

        self.POPUP_TITLE = 'Alert'
        self.POPUP_TYPE = 'AcknowledgeEvent'

        self.REJOIN_POPUP_TYPE = 'Acknowledge Event'
        self.REJOIN_POPUP_MESSAGE = 'success'
        self.REJOIN_POPUP_TITLE = 'Alert'
