var vote_util={
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
        $("")
    }
}
$(document).ready(function(){
    vote_util.bind();
})