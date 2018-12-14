const fs = require("fs");
const { shell } = require('electron');

Process = () => {
    shell.openItem('run.bat');
    setTimeout(() => {
        var data = fs.readFileSync('../data.txt');
        document.getElementById('text').innerHTML = data.toString();
    }, 5000);
}