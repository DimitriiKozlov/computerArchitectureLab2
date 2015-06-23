function f(x){
    return 3*x*x*x - 5*x*x - x*Math.cos(2*x) + Math.sin(-3*x)
}


function getValueOfIntegral(a, b, n){
    var dx = (b - a) / n;
    var I = 0;
    for (var i = a; i < b; i+=dx){
        I += (f(i) + f(i + dx)) / 2 * dx;
    }
    return I
}


var state = 'work', workerNumber, a, b, n, I = 0;

postMessage('Waiting for first data');
while (state != 'exit') {
    //postMessage('IN');
    var requestGET = new XMLHttpRequest();
    requestGET.open("GET", "/workerData", false);
    requestGET.send();

    var whatWeGot = JSON.parse(requestGET.responseText);
    a = whatWeGot['a'];
    b = whatWeGot['b'];
    n = whatWeGot['n'];
    state = whatWeGot['state'];
    workerNumber = whatWeGot['worker_number'];

    if (state == 'work') {
        I = getValueOfIntegral(a, b, n);
        //console.log(I);
        var requestPOST = new XMLHttpRequest();
        requestPOST.open("POST", "/workerData", true);
        requestPOST.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        requestPOST.send("worker_number=" + workerNumber + "&integral=" + I);

        postMessage('Working.<br>Last count integral: ' + I);
    }
    else if (state == 'pause')
        postMessage('Paused.<br>Last count integral: ' + I);
    else if (state == 'stop')
        postMessage('Finished.<br>Last count integral: ' + I);
    else
        postMessage('Waiting for task.');
}
