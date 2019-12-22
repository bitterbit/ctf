
console.log("Script loaded successfully ");

var key = "F00Bar?!F00Bar?!"

Java.perform(function(){
    var Base64 = Java.use("android.util.Base64");
    var Thread = Java.use('java.lang.Thread');
    var thread = Thread.$new();
 
    console.log("Inside java perform function");

    var acaai = Java.use("a.c.a.a.i");

    acaai.$init.implementation = function(activity) {
        console.log("acaai activity");
        return this.$init(activity);
    }

    acaai.a.implementation = function(s){
        console.log("f24d", this.d.value);
        var rval = this.a(s);
        return rval;
    }

    var Cipher = Java.use("javax.crypto.Cipher");
    var IvParameterSpec = Java.use("javax.crypto.spec.IvParameterSpec");
    var SecretKeySpec = Java.use("javax.crypto.spec.SecretKeySpec");

    Cipher.getInstance.overload("java.lang.String").implementation = function(s){
        var rval = this.getInstance(s);
        console.log("Cipher", s);
        return rval;
    }

    // Cipher.init.overload("int", , ).implementation = function(flags, keySpec, ivSpec){
    Cipher.init.overload('int', 'java.security.Key', 'java.security.spec.AlgorithmParameterSpec').implementation = function(flags, keySpec, ivSpec){
        var iv = Java.cast(ivSpec, IvParameterSpec).getIV();
        var key = Java.cast(keySpec, SecretKeySpec).getEncoded();
        printByteArr(iv);
        printByteArr(key);

        console.log("init cipher", flags);
        return this.init(flags, keySpec, ivSpec);
    }


    Base64.decode.overload("java.lang.String", 'int').implementation = function(s, flags) {
        console.log("base64!", s)
        var d = this.decode(s, flags)
        // printByteArr(d);
        // console.log(d[0], d[1],d[2],d[3],d.length)
        console.log(d.length)
        return d
    }


});


function printByteArr(bytearr) {
    var p = Memory.alloc(bytearr.length)
    for (var i=0; i<bytearr.length; i++) {
        Memory.writeS8(p.add(i), bytearr[i]);
    }
    console.log(">>>",hexdump(p, {length: bytearr.length}));
}
