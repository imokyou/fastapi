# coding=utf8
import falcon
import redis

r = redis.Redis(host='localhost', port=6379, db=3)

class ThingsResource(object):

    def on_get(self, req, resp):
        r.incr('fastapi:receive:success')
        resp.status = falcon.HTTP_200
        resp.body = 'Hello World!'


app = application = falcon.API()

things = ThingsResource()

app.add_route('/things', things)
