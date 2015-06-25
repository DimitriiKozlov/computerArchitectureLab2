from bottle import *
import bottle


n = 100
finished = []
start_time = 0
finish_time = 0
a = -1000
b = -900
n_count = 500
n_inc = 100
n_all = 1000
n_total = 0
total_worker = 0
pause_server = False
I = []


# Returns static file. Used for getting JavaScript files from /scripts folder
@bottle.get('/scripts/:filename#.*#')
def send_static(filename):
    return static_file(filename, root='./scripts/')


# Returns worker page
@bottle.get('/')
def worker():
    return static_file('worker.html', root='./')


# Returns server page
@bottle.get('/server')
def server():
    return static_file('server.html', root='./')


# Returns data for server: number of clients, percents
# of done work and if work finished results with working time
@get('/serverData')
def worker_get():
    _s = ''
    for i in I:
        _s += str(i) + '\n'

    if n_all == n_total:
        return {'number_of_clients': total_worker,
                'percents': 100, 'results': _s,
                'time': finish_time - start_time}
    else:
        return {'number_of_clients': total_worker,
                'percents': n_total / n_all * 100, 'results': _s,
                'time': finish_time - start_time}


# Processes data we got from worker: his id and founded integral
@post('/serverData')
def server_post():
    data = request.forms.get('data')
    global pause_server, start_time, n_total
    if data == 'pause':
        pause_server = True
    elif data == 'resume':
        pause_server = False
    elif data == 'restart':
        pause_server = False
        n_total = -1
        start_time = 0


# Returns data for worker: his id and text
@get('/workerData')
def worker_get():
    global total_worker
    global n_total
    if pause_server:
        return {'state': 'pause', 'a': 0, 'b': 0, 'n': 0, 'worker_number': -1}

    global start_time
    if start_time == 0:
        start_time = time.time()

    if n_total < n_all:
        total_worker += 1
        return {'state': 'work', 'a': a + n_total * n_inc, 'b': b + n_total * n_inc, 'n': n_count,
                'worker_number': total_worker}

    # Message that worker needs to stop
    return {'state': 'stop', 'a': 0, 'b': 0, 'n': 0, 'worker_number': 0}


# Processes data we got from worker: his id and founded palindromes
@post('/workerData')
def worker_post():
    global total_worker
    global n_total
    global finish_time
    n_total += 1
    total_worker -= 1
    if n_total == n_all:
        finish_time = time.time()
    integral = request.forms.get('integral')
    I.append(integral)

    # For debugging
    print('Part #%s finished' % n_total)


run(host='0.0.0.0', port=8084, debug=True)
