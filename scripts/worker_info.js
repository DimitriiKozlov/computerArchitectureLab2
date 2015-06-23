function startWorker() {
    var worker = new Worker("scripts/worker.js");

    worker.onmessage = function (event) {
        document.getElementById('info').innerHTML = event.data;
    };
}
