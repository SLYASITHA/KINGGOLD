/* Codded by @YASITH OFFICAL

Telegram: t.me/YASITHAOFFICAL

Licensed under the  GPL-3.0 License;
you may not use this file except in compliance with the License.

Whats bot - YASITHA OFFICAL


*/
var config = require('./config');
var Commands = [];

function newcmdaddtosew(info, func) {
   
    var types = ['photo', 'image', 'text', 'message'];

    var infos = {
        fromMe: info['fromMe'] === undefined ? true : info['fromMe'], // Or Sudo
        onlyGrpSew: info['onlyGrpSew'] === undefined ? false : info['onlyGrpKing'],
        onlyPinned: info['onlyPinned'] === undefined ? false : info['onlyPinned'],
        onlyPm: info['onlyPm'] === undefined ? false : info['onlyPm'],
        delownsewcmd: info['delownsewcmd'] === undefined ? true : info['delownkingcmd'],
        desc: info['desc'] === undefined ? '' : info['desc'],
        usage: info['usage'] === undefined ? '' : info['usage'],
        dontAdCommandList: info['dontAdCommandList'] === undefined ? false : info['dontAdCommandList'],
        warn: info['warn'] === undefined ? '' : info['warn'],
        function: func
    };

    if (info['on'] === undefined && info['pattern'] === undefined) {
        infos.on = 'message';
        infos.fromMe = false;
    } else if (info['on'] !== undefined && types.includes(info['on'])) {
        infos.on = info['on'];

        if (info['pattern'] !== undefined) {
            infos.pattern = new RegExp((info['handler'] === undefined || info['handler'] === true ? config.HANDLERS : '') + info.pattern, (info['flags'] !== undefined ? info['flags'] : ''));
        }
    } else {
        infos.pattern = new RegExp((info['handler'] === undefined || info['handler'] === true ? config.HANDLERS : '') + info.pattern, (info['flags'] !== undefined ? info['flags'] : ''));
    }

    Commands.push(infos);
    return infos;
}

module.exports = {
    newcmdaddtoking: newcmdaddtoking,
    commands: Commands
}
