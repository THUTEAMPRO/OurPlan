var share_util={
    getTaskList:function(){
        return _.map($("label.tasklabel"),function(tasklabel){
            return $(tasklabel).attr("data-id");
        });
    },
    submit:function(){
        var form={
            tasklist:share_util.getTaskList().join(","),
        }
        _.each(form,function(v,k){
            $("form#shareform input[name="+k+"]").val(v);
        });
        return true;
    }
}
