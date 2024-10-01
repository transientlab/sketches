# broker.hivemq.com
import pytest
import requests

class TestHTTP():
    # urls with expected result
    httpstat_url = "https://httpstat.us/"
    # codes
    ok_code = 200
    notfound_code = 404
    unauth_code = 401
    teapot_code = 418
    # http connect function
    def connect_http(self, url, code):
        resp = requests.get(url + str(code))
        return resp.status_code
    
    # test connection OK status
    def test_ok(self):
        assert self.connect_http(self.httpstat_url, self.ok_code) == self.ok_code

    # test NOT FOUND status
    def test_notfound(self):
        assert self.connect_http(self.httpstat_url, self.notfound_code) == self.notfound_code

    # test UNAUTHORIZED
    def test_unauthorized(self):
        assert self.connect_http(self.httpstat_url, self.unauth_code) == self.unauth_code

    # test UNAUTHORIZED
    def test_teapot(self):
        assert self.connect_http(self.httpstat_url, self.teapot_code) == self.teapot_code

class TestMQTT():
    pass
# # mqtt poll
# def connect_mqtt(broker):
#     pass    

# # test mqtt broker response
# def test_mqtt():
#     assert connect_mqtt("http://broker.hivemq.com")


# import paho.mqtt.client as mqtt

# mqtt_ses = mqtt.Client("session1")

# print(mqtt_ses.connect("http://broker.hivemq.com", 1883))
