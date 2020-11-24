from ui.frontpage_view import Frontpage
from ui.login_view import LoginView
from ui.settings_view import GameSettings
from ui.showcard_view import ShowCard
from ui.answerinput_view import GameAnswers
from ui.results_view import GameResults

class UI:
    def __init__(self,root):
        self.root = root
        self.current_view = None

    def show_frontpage_view(self):
        self.hide_current_view()
        self.current_view = Frontpage(
            self.root,
            self.show_login_view,
            self.show_settings_view
        )
        self.current_view.pack()

    def show_settings_view(self):
        self.hide_current_view()
        self.current_view = GameSettings(
            self.root,
            self.show_game_first_view
        )
        self.current_view.pack()


    def show_login_view(self):
       ##self.current_view = LoginView
       print("moi, login tulossa")

    def show_game_first_view(self,gamestate):
        self.hide_current_view()
        self.current_view = ShowCard(
            self.root,
            gamestate,
            self.show_answerinput_view
        )
        self.current_view.pack()

    def show_answerinput_view(self,gamestate):
        self.hide_current_view()
        self.current_view = GameAnswers(
            self.root,
            gamestate,
            self.show_result_view
        )
        self.current_view.pack()

    def show_result_view(self,gamestate):
        self.hide_current_view()
        self.current_view = GameResults(
            self.root,
            gamestate
        )
        self.current_view.pack()
    
    def hide_current_view(self):
        if self.current_view:
            self.current_view.destroy()

        self.current_view = None
    
    def start(self):
        self.show_frontpage_view()
