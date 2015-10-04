// dependency underscore
(function(env){
    var gUtil=gUtil||{};
    var Class=gUtil.Class=function(){
        this._id=_.uniqueId();
    }
    //copy from backbone.js
    var classExtend = function(protoProps, staticProps) {
        var parent = this;
        var cls;

        // The constructor function for the new subclass is either defined by you
        // (the "constructor" property in your `extend` definition), or defaulted
        // by us to simply call the parent's constructor.
        if (protoProps && _.has(protoProps, 'constructor')) {
            cls = protoProps.constructor;
        } else {
            cls = function(){ return parent.apply(this, arguments); };
        }

        // Add static properties to the constructor function, if supplied.
        _.extend(cls, parent, staticProps);

        // Set the prototype chain to inherit from `parent`, without calling
        // `parent`'s constructor function.
        var ClsProto = function(){ this.constructor = cls; };
        ClsProto.prototype = parent.prototype;
        cls.prototype = new ClsProto;

        // Add prototype properties (instance properties) to the subclass,
        // if supplied.
        if (protoProps) _.extend(cls.prototype, protoProps);

        // Set a convenience property in case the parent's prototype is needed
        // later.
        cls.__super__ = parent.prototype;

        return cls;
    };
    Class.extend=classExtend;
})()


