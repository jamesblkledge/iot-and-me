const {app, BrowserWindow, Menu} = require('electron');
  
let win;

function createWindow () {
    win = new BrowserWindow({frame: false, alwaysOnTop: false});
    win.setFullScreen(true);

    win.loadFile('src/index.html');

    win.on('closed', () => {
        win = null;
    });
}

app.on('ready', createWindow);

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

app.on('activate', () => {
    if (win === null) {
        createWindow();
    }
});