class Router:
    AVAILABLE_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']

    def __init__(self):
        self.storage = {}
        self.path_storage = set('')

    def __getattr__(self, attr):
        if attr.upper() in self.AVAILABLE_METHODS:
            return lambda path: self.request(attr.upper(), path)
        raise AttributeError(f"method {attr} is not defined for {self}")

    def add_path(self, path, method, func):
        self.path_storage.add(path)

        if (method, path) in self.storage.keys():
            if ((method, path), func) in self.storage.items():
                return f"path {path} already associated with method {method}"
            else:
                self.storage.update([((method, path), func)])
                return f"method {method} added  for path {path}"

        else:
            self.storage.update([((method, path), func)])

            return f"method {method} added  for path {path} "

    def request(self, method, path):
        if (method, path) not in self.storage.keys():
            if path not in self.path_storage:
                return f'Error 404, path {path} not found'
            else:
                return f'Error 405, Method {method}  not allowed'

        else:
            func = self.storage[(method, path)]
            return func(path, method)


def my_info(path, method):
    return 200, {"me": "lynxvf"}


def update_me(path, method):
    return 200, "OK"


def guest_info(path, method):
    guest_name = input('your name is: ')
    if guest_name:
        return 200, {"guest_name": guest_name}
    else:
        return 401, 'Unauthorized'







if __name__ == "__main__":

    router = Router()

    print(router.add_path('/me', 'GET', my_info))
    print(router.add_path('/me', 'GET', my_info))
    print(router.add_path('/me', 'PATCH', update_me))
    print(router.add_path('/guest', 'POST', guest_info))

    print(router.request('GET', '/me'))
    print(router.get('/me'))

    print(router.request('POST', '/me'))
    print(router.patch('/you'))

    print(router.request('POST', '/guest'))
    print(router.post('/guest'))

