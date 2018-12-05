from flask import Flask, request, abort, render_template
from config import DevConfig
import numpy as np
import json

success_count = 0
error_count = 0

def is_correct_data_format(data):
    if 'x' not in data or 'y' not in data:
        print('[error] missing input args "x" or "y"')
        return False

    x, y = data['x'], data['y']
    if type(x) != type(list()) or type(y) != type(list()):
        print('[error] Wrong types of x or y')
        return False

    if len(x) != len(y):
        print('[error] innerproduct cannot not be done \
                with different lengths of x and y'.format(len(x)))
        return False

    if len(x) > 50 or len(x) < 1:
        print('[error] length of x not in range[1~50]: {}'.format(len(x)))
        return False
    if len(y) > 50 or len(y) < 1:
        print('[error] length of y not in range[1~50]: {}'.format(len(y)))
        return False

    return True


def innerproduct(x, y):
    try:
        vec_x = np.array(x)
        vec_y = np.array(y)
        ans = np.inner(vec_x, vec_y)
        return {
                "number_of_request": {"xTy": ans},
                }
    except:
        print('[error] something wrong with innerproduct')
        return False



# 初始化 Flask 類別成為 instance
app = Flask(__name__)
app.config.from_object(DevConfig)


@app.errorhandler(404)
def page_not_found(e):
    global error_count
    error_count += 1
    return render_template('404.html'), 404


# user -- 接收input
@app.route('/innerproduct/', methods=['POST'])
def get_client_input():
    if not request.is_json:
        print('[error] not in json format')
        return abort(404)

    data = request.get_json()

    if not is_correct_data_format(data):
        return abort(404)

    x, y = data['x'], data['y']
    ans = innerproduct(x, y)

    if not ans:
        return abort(404)

    global success_count
    success_count += 1

    return str(ans)


# admin -- check problems
@app.route('/info/', methods=['GET'])
def get_resp_statistics():
    global success_count, error_count
    resp = { "number_of_requests": { "innerproduct": success_count } ,
            "number_of_errors": {"innerproduct": error_count}
            }
    return str(resp)


# 判斷自己執行非被當做引入的模組，因為 __name__ 這變數若被當做模組引入使用就不會是 __main__
if __name__ == '__main__':
    app.run()
