from tornado import ioloop
from tornado import httpserver
from tornado.web import Application
from controllers.sysvaldo_controller import Index, Cadastrar, Deletar, Atualizar


class RunApp(Application):

    def __init__(self):
        handlers = [
            ('/', Index),
            ('/sysvaldo/cadastro', Cadastrar),
            (r'/sysvaldo/deletar/(\d+)', Deletar),
            (r'/sysvaldo/atualizar/(\d+)', Atualizar)
        ]

        settings = dict(
            debug=True,
            template_path='views',
            static_path='static',
        )

        Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    http_server = httpserver.HTTPServer(RunApp())
    http_server.listen(8000)
    ioloop.IOLoop.instance().start()
