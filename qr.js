/* Codded by @YASITHA OFFICAL

Telegram: t.me/YASITHA OFFICAL

Licensed under the  GPL-3.0 License;
you may not use this file except in compliance with the License.

Whats bot - YASITHA OFFICAL
*/

const chalk = require('chalk');
const {WAConnection, MessageOptions, MessageType} = require('@adiwajshing/baileys');
const {StringSession} = require('./sewqueen/');
const fs = require('fs');

async function sewQueen () {
    const conn = new WAConnection();
    const Session = new StringSession();  
    conn.version = [2, 2126, 14]
    conn.logger.level = 'warn';
    conn.regenerateQRIntervalMs = 50000;
    
    conn.on('connecting', async () => {
        console.log(`${chalk.green.bold('KING')}${chalk.blue.bold('GOLD')}
${chalk.white.italic('QueenSewString')}

${chalk.blue.italic('ℹ️  Connecting to Whatsapp... Please Wait.')}`);
    });
    

    conn.on('open', async () => {
        var st = Session.createStringSession(conn.base64EncodedAuthInfo());
        console.log(
            chalk.green.bold('KING GOLD String: '), Session.createStringSession(conn.base64EncodedAuthInfo())
        );
        
        if (!fs.existsSync('config.env')) {
            fs.writeFileSync('config.env', `ASENA_SESSION="${st}"`);
        }
        if (conn.user.jid.startsWith('90')) {
            await conn.sendMessage(conn.user.jid,st, MessageType.text)
            await conn.sendMessage(conn.user.jid,'*KING*', MessageType.text)
            console.log(
                chalk.blue.bold('KING.')
            );
        }
        else {
            await conn.sendMessage(conn.user.jid,st, MessageType.text)
            await conn.sendMessage(conn.user.jid,'*Do Not Share This Code With Anyone!*', MessageType.text)
            console.log(
                chalk.blue.bold('If you are installing locale, you can start the bot with node king.js')
            );
        }
        
        process.exit(0);
    });

    await conn.connect();
}

kingGold()
