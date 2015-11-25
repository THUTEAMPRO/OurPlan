var sth=$;
var vote_util={
    optionHTML:'<a id="option<%=i%>" href="#" class="list-group-item">'+
        '<div id="datetime<%=i%>" class="input-group date">'+
              '<span class="input-group-addon"><%=i%>.</span>'+
              '<input class="form-control" size="10" type="text" value="" readonly>'+
              '<span class="input-group-addon"><span class="glyphicon glyphicon-remove"></span></span>'+
			  '<span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span>'+
        '</div>'+'</a>',
    bind_group:function(){
        $("input.groupselect").click(function(e){
            var $label=$(e.target).closest("label");
            var groupid=$label.attr("data-groupid");
            var groupname=$label.attr("data-groupname");
            selected_data.groupid=groupid;
            // TODO
            console.log(groupname);
        });
    },
    bind:function(){
        vote_util.bind_group();
        $("#optionlist");
    }
}
$(document).ready(function(){
    vote_util.bind();
});
