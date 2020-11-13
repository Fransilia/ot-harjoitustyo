class LoginView:
    def __init__(self, root, handle_login, handle_show_create_user_view):
        self.root = root
        self.handle_login = handle_login
        self.handle_show_create_user_view = handle_show_create_user_view
        self.frame = None

        self.initialize()

    def login_handler(self):
        username = self.username_entry.get()