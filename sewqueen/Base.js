/* Coded By YASITHA OFFICAL.

Licensed under the  GPL-3.0 License;
you may not use this file except in compliance with the License.

Whats bot - YASITHA OFFICAL

*/

'sew';

class Base {
    constructor(client) {
        Object.defineProperty(this, 'client', { value: client });
    }

    _clone() {
        return Object.assign(Object.create(this), this);
    }
    
    _patch(data) { return data; }
}

sew.exports = Base;
